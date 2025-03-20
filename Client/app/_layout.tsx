import React, { useState } from "react";
import { Stack } from "expo-router";
import { AuthProvider } from "../context/AuthContext";
import { PositionProvider } from "../context/PositionContext";
import { useEffect } from "react";
import { useAuth } from "../context/AuthContext";
import { Redirect } from "expo-router";
import * as Font from "expo-font";
import * as SplashScreen from "expo-splash-screen";
import { FONTS } from "@/constants/fonts";
import { ThemeProvider } from "@context/ThemeContext";

const loadFonts = () => {
  return Font.loadAsync({
    [FONTS.regular]: require("../assets/fonts/Regular.ttf"),
    [FONTS.medium]: require("../assets/fonts/Medium.ttf"),
    [FONTS.semibold]: require("../assets/fonts/SemiBold.ttf"),
    [FONTS.bold]: require("../assets/fonts/Bold.ttf"),
  });
};

function RootLayoutNav() {
  const { isAuthenticated } = useAuth();
  const [fontsLoaded, setFontsLoaded] = useState(false);
  useEffect(() => {
    async function prepare() {
      try {
        await loadFonts();
      } catch (e) {
        console.warn(e);
      } finally {
        setFontsLoaded(true);
        await SplashScreen.hideAsync();
      }
    }
    prepare();
  }, []);

  if (!fontsLoaded) return null;

  return (
    <ThemeProvider>
      <Stack screenOptions={{ headerShown: false }}>
        {!isAuthenticated ? (
          <>
            <Stack.Screen name="(auth)/login" />
            <Stack.Screen name="(auth)/register" />
          </>
        ) : (
          
            <>
            <Stack.Screen
              name="(tabs)"
              options={{
                headerShown: false,
              }}
            />
            <Stack.Screen 
              name="addPackage" 
              options={{
                headerShown: true,
                title: "Add Package",
              }}
            />
            <Stack.Screen 
              name="addTruck" 
              options={{
                headerShown: true,
                title: "Add Truck",
              }}
            />
          </>
        )}
      </Stack>
    </ThemeProvider>
  );
}

export default function RootLayout() {
  return (
    <AuthProvider>
      <PositionProvider>
        <RootLayoutNav />
      </PositionProvider>
    </AuthProvider>
  );
}

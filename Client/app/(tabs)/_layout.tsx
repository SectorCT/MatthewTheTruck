import { Tabs } from "expo-router";
import { MaterialIcons } from "@expo/vector-icons";
import { useTheme } from "@context/ThemeContext";
import Cubes from "@assets/icons/cubes.svg";
import House from "@assets/icons/house.svg";
import { View } from "react-native";

export default function TabLayout() {
  const { theme } = useTheme();
  const ICON_SIZE = 25;

  const backgroundColor = "#f2f3f5";

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: theme.color.darkPrimary,
        tabBarInactiveTintColor: "#8b8c90",
        tabBarActiveBackgroundColor: "#f2f3f5",
        tabBarInactiveBackgroundColor: "#f2f3f5",
        headerShown: false,
        tabBarStyle: {
          backgroundColor: backgroundColor,
        },
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: "Home",
          tabBarIcon: ({ color }) => (
            <House height={ICON_SIZE} width={ICON_SIZE} fill={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="packages"
        options={{
          title: "Packages",
          tabBarIcon: ({ color }) => (
            <Cubes height={ICON_SIZE} width={ICON_SIZE} fill={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="trucks"
        options={{
          title: "Trucks",
          tabBarIcon: ({ color }) => (
            <Cubes height={ICON_SIZE} width={ICON_SIZE} fill={color} />
          ),
        }}
      />

      <Tabs.Screen name="styles/homeStyles" options={{ href: null }} />
      <Tabs.Screen name="styles/packageStyles" options={{ href: null }} />
      <Tabs.Screen name="styles/trucksStyles" options={{ href: null }} />
    </Tabs>
  );
}

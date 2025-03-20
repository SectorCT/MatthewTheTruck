import { View, Text, TouchableOpacity } from "react-native";
import useStyles from "./styles";
import { useTheme } from "@context/ThemeContext";
import { MaterialIcons } from "@expo/vector-icons";
import Plus from "@assets/icons/plus.svg";

export default function AddButton({ onPress }: { onPress: () => void }) {
  const styles = useStyles();
  const { theme } = useTheme();

  return (
    <TouchableOpacity style={styles.container} onPress={onPress}>
      <Plus height={40} width={40} />
    </TouchableOpacity>
  );
}

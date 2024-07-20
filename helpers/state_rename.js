import { stateMap } from "@/constants/names";

// Helper function to get the full state name
export function getStateFullName(shortName) {
  return stateMap[shortName] || shortName;
}

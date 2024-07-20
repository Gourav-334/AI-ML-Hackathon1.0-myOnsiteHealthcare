"use server";

import fs from "fs/promises";

const areaEnum = [
  "Ahmedabad",
  "Amreli",
  "Anand",
  "Aravali",
  "Baruch",
  "Bhavnagar",
  "Dhahod",
  "Ghandinagar",
  "Gujarat",
];
export async function getData(area) {
  area = areaEnum.includes(area) ? area : "Gujarat";
  try {
    const data = await fs.readFile(`./data/${area}.json`, "utf8");
    const parsedData = JSON.parse(data);
    return parsedData;
  } catch (error) {
    return [];
  }
}

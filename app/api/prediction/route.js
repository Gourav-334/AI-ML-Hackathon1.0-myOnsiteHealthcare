import { getData } from "@/data/db";
import { NextRequest, NextResponse } from "next/server";

export async function GET(req) {
  const request = new NextRequest(req);
  const area = request.nextUrl.searchParams.get("area") || "Gujarat";
  try {
    const data = await getData(area);
    return NextResponse.json({ data: data });
  } catch (error) {
    return NextResponse.json({ error: error.message }, { status: 404 });
  }
}

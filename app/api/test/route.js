import { query } from "@/lib/db";

export async function GET(request) {
  const { rows } = await query("SELECT COUNT(*) FROM users");
  return NextResponse.json(rows);
}
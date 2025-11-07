import { query } from "@/lib/db";

export async function GET() {
  try {
    const result = await query("SELECT COUNT(*) FROM users;");
    return Response.json({ users: result.rows[0].count });
  } catch (error) {
    console.error(error);
    return Response.json({ error: "Database connection failed" }, { status: 500 });
  }
}

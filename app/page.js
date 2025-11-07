import Image from "next/image";
import pool from "@/lib/db";

export default function Home() {
  return (
    <main className="flex items-center justify-center h-dvh w-screen">
      <Image
        className="w-96 h-auto"
        src="/ekonverto-logo.svg"
        alt="EKONVERTO | Logo"
        width={175}
        height={20}
      />
    </main>
  );
}

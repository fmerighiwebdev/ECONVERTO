import Image from "next/image";

export default function Home() {
  return (
    <main className="flex items-center justify-center h-dvh w-screen">
      <Image className="w-96 h-auto" src="/econverto-logo.svg" alt="ECONVERTO | Logo" width={175} height={20} />
    </main>
  );
}

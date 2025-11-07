import Image from "next/image";

export default function Header() {
  return (
    <header className="w-full bg-white py-6 shadow-lg shadow-gray-100 fixed top-0 z-999">
      <div className="container">
        <Image
          src="/ekonverto-logo.svg"
          alt="EKONVERTO Logo"
          width={200}
          height={20}
        />
      </div>
    </header>
  );
}

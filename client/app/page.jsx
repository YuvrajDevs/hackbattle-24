// app/page.jsx
import Link from 'next/link';
import Navbar from './components/Navbar/page';
import Wordrecall from './components/Wordrecall/page';

export default function MainPage() {
  return (
    <>
      <Navbar />
      <div className="flex justify-center items-center min-h-[calc(100vh-64px)]">
        <Wordrecall/>
      </div>
    </>
  );
}

// app/page.jsx
import Link from 'next/link';
import Navbar from './components/Navbar/page';
import Page from './contructionalPraxis/page';
import WordRecall from './namingTask/page';
import Speaking from './speaking/page';
import Ideational from './ideationalpraxis/page';
// import Wordrecall from './components/Wordrecall/page';

export default function MainPage() {
  return (
    <>
      <div className="flex justify-center items-center min-h-[calc(100vh-64px)]">
        {/* <WordRecall/> */}
        <Ideational/>        
        
      </div>
    </>
  );
}

// app/page.jsx
// import Link from 'next/link';
import Navbar from './components/Navbar/page';
import Page from './contructionalPraxis/page';
import WordRecall from './namingTask/page';
import Speaking from './speaking/page';
import Ideational from './ideationalpraxis/page';
import Comprehension from './comprehension/page';
// import Wordrecall from './components/Wordrecall/page';
import Button from './components/Button/page';
import Link from 'next/link';

export default function MainPage() {
  return (
    <>
      <div className="flex-col justify-center items-center">
        {/* <WordRecall/> */}
        <Ideational/>        
        
      </div>
    </>
  );
}

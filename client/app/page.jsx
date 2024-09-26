// app/page.jsx
import Link from 'next/link';
import Navbar from './components/Navbar/page';
import Page from './constructionalpraxis/page';
import Speaking from './speaking/page';
import Ideational from './ideationalpraxis/page';
import Comprehension from './comprehension/page';
import TaskHeading from './components/TaskHeading/page';
import Subheading from './components/SubHeading/page';
import Button from './components/Button/page';
// import Wordrecall from './components/Wordrecall/page';

export default function MainPage() {
  return (
    <>
      <div className="flex flex-col justify-center items-center min-h-[calc(100vh-64px)]">
      <TaskHeading  heading="Alzheimer's Cognitive Assessment"/>
      <Subheading subHeading='Sub'/>

        <Button name="Start the test"/>
      </div>
    </>
  );
}

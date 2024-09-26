import React from 'react'
import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
import Link from 'next/link'
const WordRecall = () => {
  const instruction = 'We will ask you a few questions about general information, such as the day, date, and place. Please answer each question to the best of your ability'
  return (
    <section className='flex flex-col items-center justify-center mx-10'>
      <TaskHeading heading='Orientation'/>
      <SubHeading subHeading='Instructions' />
      <Paragraph para={instruction} />
      <Link href="/orientation/testorientation">
      <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default WordRecall

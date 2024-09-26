import React from 'react'
import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const WordRecall = () => {
  const instruction = 'Now we will show you some objects, one at a time. You should tell us what their names are, what are they called.'
  return (
    <section className='flex mx-10 flex-col  items-center justify-center mt-10'>
      <TaskHeading heading='Word Recall Task'/>
      <SubHeading subHeading='Instructions' />
      <Paragraph para={instruction} />
      <Link href='/wordRecall/recall-test'>
        <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default WordRecall

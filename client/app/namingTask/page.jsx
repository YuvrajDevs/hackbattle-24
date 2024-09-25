import React from 'react'
import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Paragraph from '../components/Paragraph/page'
import Button from '../components/Button/page'
const WordRecall = () => {
  const instruction = 'Now we will show you some objects, one at a time. You should tell us what their names are, what are they called.'
  return (
    <section className='flex flex-col items-center justify-center mt-10'>
      <TaskHeading heading='Naming Task'/>
      <SubHeading subHeading='Instructions' />
      <Paragraph para={instruction} />
      <Button name='Start Test'/>
    </section>
  )
}

export default WordRecall

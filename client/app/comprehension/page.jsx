import React from 'react'
import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const Comprehension = () => {
  return (
    <section className='flex flex-col mx-10 items-center justify-center mt-10'>
      <TaskHeading heading='Word-Finding Difficulty' />
      <SubHeading subHeading='Instruction for Instructor' />
      <ul className="list-disc mt-4">
        <li>Focus only on word-finding difficulty during spontaneous speech, not overall spoken language ability.</li>
        <li>Observe if the subject struggles to find the correct words and uses circumlocution (explanatory phrases or similar words) to compensate.</li>
        <li>Do not include finger and object naming tasks in this rating.</li>
        <li>Ensure that the rating reflects only the subject's ability to retrieve specific words during conversation, not their general communication abilities.</li>
      </ul>
      <Link href='comprehension/testcomp'>
       <Button name='Start Test'/>
      </Link>
    </section>
  )
}

export default Comprehension

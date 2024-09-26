import React from 'react'
import TaskHeading from '../components/TaskHeading/page'
import SubHeading from '../components/SubHeading/page'
import Button from '../components/Button/page'
import Link from 'next/link'

const Ideational = () => {
  return (
    <section className='flex flex-col items-center justify-center mt-10'>
      <TaskHeading heading='Ideational Praxis Task' />
      <SubHeading subHeading='Instruction for Instructor' />
      <ul className="list-disc mt-4">
        <li>Prepare an envelope, an 8.5" x 11" sheet of paper, and a pencil before starting.</li>
        <li>Verbally guide the subject to write themselves a letter, fold the paper, place it in the envelope, seal it, and address the envelope to themselves.</li>
        <li>If the subject forgets a step, give a single reminder for that component before moving on.</li>
        <li>Mark the subject's performance on each step using the provided worksheet.</li>
        <li>Ensure the task is conducted with minimal additional prompts, focusing on the subject's ability to follow the sequence.</li>
      </ul>
      <Link href='/ideationalpraxis/testideational'>
      <Button name='Submit'/>
      </Link>
      
    </section>
  )
}

export default Ideational

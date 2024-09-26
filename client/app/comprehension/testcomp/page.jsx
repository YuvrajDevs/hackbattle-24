import Button from '@/app/components/Button/page'
import Subheading from '@/app/components/SubHeading/page'
import TaskHeading from '@/app/components/TaskHeading/page'
import Link from 'next/link'
import React from 'react'

export default function Testcomp() {
  return (
    <section className='flex flex-col mx-10 items-center gap justify-center mt-10'>
      <TaskHeading heading='Word-Finding Difficulty' />
      <Subheading subHeading='Scoring' />
      <div className='flex flex-col '>
      <table className='w-full mt-2 text-left'>
        <tbody>
          <tr>
            <td className='pr-6'>0</td>
            <td>No evidence of word finding difficulty in spontaneous speech</td>
          </tr>
          <tr>
            <td className='pr-6'>1</td>
            <td>Very mild – 1 or 2 instances, not clinically significant</td>
          </tr>
          <tr>
            <td className='pr-6'>2</td>
            <td>Mild – noticeable circumlocution or synonym substitution</td>
          </tr>
          <tr>
            <td className='pr-6'>3</td>
            <td>Moderate – loss of words without comprehension on occasion</td>
          </tr>
          <tr>
            <td className='pr-6'>4</td>
            <td>Moderately severe – frequent loss of words without comprehension</td>
          </tr>
          <tr>
            <td className='pr-6'>5</td>
            <td>Severe – near total loss of content of words; speech sounds empty;1 – 2 word utterances</td>
          </tr>
        </tbody>
      </table>
      </div>
      <input type="text" placeholder='Enter the score'className='text-center border-2 border-black rounded-lg px-5 py-2 mt-5' />
      <Link href='/comprehension//testcomp'>
      <Button name='Submit'/>
      </Link>
    </section>
  )
}

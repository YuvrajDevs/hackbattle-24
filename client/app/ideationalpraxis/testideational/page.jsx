import Button from '@/app/components/Button/page'
import Subheading from '@/app/components/SubHeading/page'
import TaskHeading from '@/app/components/TaskHeading/page'
import Link from 'next/link'
import React from 'react'

export default function Testidea() {
  return (
    <section className='flex flex-col items-center gap justify-center mt-10'>
      <TaskHeading heading='Ideational praxis' />
      <Subheading subHeading='Scoring' />
      <div className='flex flex-col '>
      <table className='w-full mt-2 text-left'>
        <tbody>
          <tr>
            <td className='pr-6'>0</td>
            <td>All components performed correctly</td>
          </tr>
          <tr>
            <td className='pr-6'>1</td>
            <td>Failure to perform 1 component</td>
          </tr>
          <tr>
            <td className='pr-6'>2</td>
            <td>Failure to perform 2 components</td>
          </tr>
          <tr>
            <td className='pr-6'>3</td>
            <td>Failure to perform 3 components</td>
          </tr>
          <tr>
            <td className='pr-6'>4</td>
            <td>Failure to perform 4 components</td>
          </tr>
          <tr>
            <td className='pr-6'>5</td>
            <td>Failure to perform 5 components</td>
          </tr>
        </tbody>
      </table>
      </div>
      <input type="text" placeholder='Enter the score'className='text-center border-2 border-black rounded-lg px-5 py-2 mt-5' />
      <Link href='/speaking/testspeak'>
      <Button name='Start Test'/>
      </Link>
    </section>
  )
}

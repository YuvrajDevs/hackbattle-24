import Button from '@/app/components/Button/page'
import Subheading from '@/app/components/SubHeading/page'
import TaskHeading from '@/app/components/TaskHeading/page'
import Link from 'next/link'
import React from 'react'

export default function Testspeak() {
  return (
    <section className='flex flex-col items-center mx-10 gap justify-center mt-10'>
      <TaskHeading heading='Speaking ability' />
      <Subheading subHeading='Scoring' />
      <div className='flex flex-col '>
      <table className='w-full mt-2 text-left'>
        <tbody>
          <tr>
            <td className='pr-6'>0</td>
            <td>No instances when it is difficult to understand the subject</td>
          </tr>
          <tr>
            <td className='pr-6'>1</td>
            <td>Very mild – one instance of lack of understandability</td>
          </tr>
          <tr>
            <td className='pr-6'>2</td>
            <td>Mild – subject has difficulty less than 25% of the time</td>
          </tr>
          <tr>
            <td className='pr-6'>3</td>
            <td>Moderate – subject has difficulty 25-50% of the time</td>
          </tr>
          <tr>
            <td className='pr-6'>4</td>
            <td>Moderately severe – subject has difficulty 50% of the time</td>
          </tr>
          <tr>
            <td className='pr-6'>5</td>
            <td>Severe – one or two word utterance; fluent, but empty speech; mute</td>
          </tr>
        </tbody>
      </table>
      </div>
      <input type="text" placeholder='Enter the score'className='text-center border-2 border-black rounded-lg px-5 py-2 mt-5' />
      <Link href='/speaking/testspeak'>
      <Button name='Submit'/>
      </Link>
    </section>
  )
}

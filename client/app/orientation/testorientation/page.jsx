import Button from '@/app/components/Button/page'
import Subheading from '@/app/components/SubHeading/page'
import TaskHeading from '@/app/components/TaskHeading/page'
import Link from 'next/link'
import React from 'react'

export default function Testidea() {
  return (
    <section className='flex flex-col items-center mx-10 gap justify-center mt-10'>
      <TaskHeading heading='Orientation' />

      <div>
        <h1 className='text-2xl'>What is your name ma?</h1>
      </div>
      
      <Link href='/orientation'>
      <Button name='Record'/>
      </Link>
    </section>
  )
}

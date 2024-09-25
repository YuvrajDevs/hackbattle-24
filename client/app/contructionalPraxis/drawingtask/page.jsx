import React from 'react'
import TaskHeading from '../../components/TaskHeading/page'
import Image from 'next/image'
import shapeCirlce from '../../public/circle.png'
const page = () => {
  return (
    <div className='justify-center flex-col flex items-center'>
      <TaskHeading heading='Constructional Praxis'/>
      <Image src={shapeCirlce} height={150} width={150} className='object-contain flex justify-center items-center'/>
      <h3 className='my-3 font-bold text-2xl'>Circle</h3>

    </div>
  )
}

export default page

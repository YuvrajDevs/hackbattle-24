import React from 'react'
import Image from 'next/image'
import logo from '../../public/Alzybud.png'
export default function Navbar() {
  return (
    <nav className='test py-5 px-10 flex items-center justify-between'>
            <Image src={logo} className='object-contain'/>
            <button className='text-xl py-2 px-6 rounded-2xl border-solid border-2 border-black '>Exit</button>
    </nav>
)
}

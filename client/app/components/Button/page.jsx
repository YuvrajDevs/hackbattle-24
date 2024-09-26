import React from 'react'

const Button = ({ name }) => {
  return (
    <button className="mt-12 px-10 py-2 rounded-lg text-white font-bold bg-green-500 hover:bg-green-600 transition duration-300 ease-in-out">
        {name}
    </button>
  )
}

export default Button

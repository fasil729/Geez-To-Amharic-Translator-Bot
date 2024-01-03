import React from 'react'
import './button.css'
export const Button = ({type}) => {
  return (
   <button className={`btn ${
    (type ==='add' && 'add')||
    (type ==='remove' && 'remove')||
    (type ==='checkout' && 'checkout')
   }`}>{type}</button>
  )
}

import React from 'react';
import './home.css'

import { AiFillAudio } from "react-icons/ai";


import { FaRegShareFromSquare } from "react-icons/fa6";

import { MdContentCopy, MdOutlineStarBorder } from "react-icons/md";
import TextArea from "../components/textarea/textarea";
import { Button } from "../components/button/button";
import Container from "../components/container/container";
import { FaImage, FaLongArrowAltRight } from "react-icons/fa";
import SpeechToText from '../components/audio/audio';


const Home = () => {

  
  return (  <div className="App flex justify-center">
    
  <div className='flex flex-col gap-20 width justify-center m-10 h-screen'>
   {/* <CameraComponent/> */}
  <Container>
     <div className='flex justify-between  '>
    <div className='font-bold'>ግእዝ</div>
   <FaLongArrowAltRight size={30}/>
    <div className='font-bold'>አማርኛ</div>
     </div>

   </Container>

   <Container>
     <div className='flex flex-col gap-10'>
     <div className='flex justify-between '>
    <div className='font-bold'>ግእዝ</div>
    
    
     </div>

     <div>
       <TextArea/>

       <div className='flex justify-between mt-10'>
    <div>
     <div className="flex">
      <AiFillAudio size={30} />
     <div className="relative">
     <FaImage className="upload-icon" size={30}/>
     <input type="file" className='inputImage' />
     </div>
     {/* <SpeechToText/> */}
     </div>
    </div>
    
    <Button/>
     </div>
     </div>

     </div>

   </Container>



   <Container>
     <div className='flex flex-col gap-10'>
     <div className='flex justify-between'>
    <div className='font-bold'>አማርኛ</div>
    
    
     </div>

     <div>
      <p>
      The result of the query is true if the specified 
      media type matches the type of device the document 
      is being displayed on and all media features in the 
      media query are true. When a media query is true, the 
      corresponding style sheet or style rules are applied, 
      following the normal cascading rules.
      </p>

       <div className='flex justify-end mt-20'>
         <div className='flex justify-between mt-10'>

<MdContentCopy size={24}/>
<FaRegShareFromSquare size={24}/>
<MdOutlineStarBorder size={24}/>
         </div>
    
     </div>
     </div>

     </div>

   </Container>




 


  
  </div>


   </div>);
}
 
export default Home;
import React, {  useState } from 'react';
import './home.css'
import Tesseract from 'tesseract.js';
import { AiFillAudio } from "react-icons/ai";


import { FaRegShareFromSquare } from "react-icons/fa6";

import { MdContentCopy, MdOutlineStarBorder } from "react-icons/md";
import TextArea from "../components/textarea/textarea";

import Container from "../components/container/container";
import { FaImage} from "react-icons/fa";
import SpeechToText from '../components/audio/audio';
import Navbar from '../components/navbar/navbar';
import { useTheme } from '../hooks/useTheme';
import CameraComponent from '../camera/camera';




const Home = () => {
  const { language,data ,resetData,textChange} = useTheme();
  const [photo,setPhoto]=useState(null);

  const [Loading,setLoading]=useState(false);
  const [text,setText]=useState(data);
  console.log("text Data",text)


  const handleFileChange=(event) => {
    const file=event.target.files[0];
    if (file){
      const reader=new FileReader();
      reader.onload=() =>{
        setPhoto(reader.result);
      }
      reader.readAsDataURL(file);
    }
  }

// useEffect(()=>{
//   if(photo){
//     const convertImageToText =async () => {
//       setLoading(true);
//        Tesseract.recognize(
//        photo,
//         'amh',
//         { logger: (info) => console.log(info) }
//       ).then(({ data: { text } }) => {
//         setText(text);
//       }).finally(() => {
//         setLoading(false);
//       });
//     };
//     return convertImageToText();
//   }
// },[photo])

console.log("data:-",data);
const convertImageToText =async () => {
  setLoading(true);
   Tesseract.recognize(
   photo,
    'amh',
    { logger: (info) => console.log(info) }
  ).then(({ data: { text } }) => {
    // setText(text);
    textChange(text)
  }).finally(() => {
    setLoading(false);
  });
};






  return (<>  <div className="App flex justify-center">
   
  <div className='flex flex-col gap-20 width justify-center m-10 '>
   {/* <CameraComponent/> */}
  <Navbar/>

   <Container>
     <div className='flex flex-col gap-10'>
     <div className='flex justify-between '>
    <div className='font-bold'> {language==='amharic'? 'ግእዝ':'English'}</div>
    
    
     </div>

     <div>
      <div className="mt-10 relative ">
        {photo &&(data===" ")&& <img src={photo} alt="photo"  className='w-300 h-400'/>}
        {Loading&& <div className='photoLoading'>Loading...</div>}
      </div>
      <p>{language==='amharic'&&data}</p>
       <TextArea value={data}/>

       <div className='flex justify-between mt-10'>
    <div>
     <div className="flex">
      
     {!photo&&(data===" ")? (<><button className='btn btn-success' onClick={convertImageToText}> {language==='amharic'? 'ግወደ ጽሑፍ ቀይር':'convertTo Text'}</button>
     <div className=" flex ">
     <div className="relative mt-20">
     <FaImage className="upload-icon" size={30}/>

<input type="file" className='inputImage' onChange={handleFileChange}/>
     </div>
     <CameraComponent/>
     </div></>):(<button className='btn btn-light' onClick={resetData}>Reset</button>)}
     {language!=='amharic'&& (
      <>
      <AiFillAudio size={30} />
      <SpeechToText/>
      </>
     )}
     
     </div>
    </div>
    
    <button className='btn btn-primary'>{language==='amharic'? 'ተርጉም':'Translate'}</button>
     </div>
     </div>

     </div>

   </Container>



   <Container>
     <div className='flex flex-col gap-10'>
     <div className='flex justify-between'>
    <div className='font-bold'> አማርኛ</div>
    
    
     </div>

     <div>
      <p className='note'>
      ከተገለፀው የጥያቄው ውጤት እውነት ነው።
      የሚዲያ አይነት ከሰነዱ አይነት ጋር ይዛመዳል
      በ ላይ እና ሁሉም የሚዲያ ባህሪያት እየታዩ ነው።
      የሚዲያ ጥያቄ እውነት ነው። የሚዲያ ጥያቄ እውነት ሲሆን እ.ኤ.አ
      ተጓዳኝ የቅጥ ሉህ ወይም የቅጥ ህጎች ይተገበራሉ ፣
      መደበኛውን የማብሰያ ህጎችን በመከተል ።
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


   </div></>);
}
 
export default Home;
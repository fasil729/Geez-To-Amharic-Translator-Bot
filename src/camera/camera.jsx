import React, { useRef, useCallback, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import './camera.css'
import { FaCamera } from "react-icons/fa";



import Tesseract from 'tesseract.js';

import { useTheme } from '../hooks/useTheme';
import MyModal from '../components/modal';

const CameraComponent = () => {
  const webcamRef = useRef(null);

  const [capturedImage, setCapturedImage] = useState(null);
 
  const [photoLoading, setPhotoLoading] = useState(false);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setCapturedImage(imageSrc);
  }, [webcamRef]);

const emptyCapturedImage =() => {
  setCapturedImage(null);
};
const {textChange,data}=useTheme();
  // //conver photo to text
  const convertImageToText =async () => {
    setPhotoLoading(true);
     Tesseract.recognize(
    capturedImage,
      'amh',
      { logger: (info) => console.log(info) }
    ).then(({ data: { text } }) => {
      console.log("data",text)
      textChange(text)
    }).finally(() => {
      setPhotoLoading(false);
    });
  };
  console.log("Text",data)
  


  useEffect(()=>{
    if(data!==" "){
      
    }
  },[data]);
  
  return (
     <MyModal
     data={data}
     label={<FaCamera size={30}/>}
     title={"Camera"}
     children={<div  className=''>
     
     {capturedImage?  (
       <div className=' cameraPhoto'>
         <div className="photo ">
         <h2>Captured Photo:</h2>
         {<img src={capturedImage} alt="Captured" />}

         <div className="flex justify-around mt-20">
         <button className='btn mt-20' onClick={()=>emptyCapturedImage()}>Back</button>
         <button className='btn mt-20' onClick={()=>convertImageToText()}>Convert to Text</button>
         
         </div>
         {photoLoading && <div className="photoLoading">Loading...</div>}
         </div>

         {data &&<div className="text">
          <div>
           <p className='text-items'>{data}</p></div>
         </div>
         }
       </div>
     ):<div className="w-full">
     <Webcam
    className="w-full"
       audio={false}
       ref={webcamRef}
       screenshotFormat="image/jpeg"
     />
     <button className='btn mt-20' onClick={capture}>Capture Photo</button>
     </div>}


    
   </div>}
   />
 
      
   
  );
};

export default CameraComponent;

import React, { useRef, useCallback, useState } from 'react';
import Webcam from 'react-webcam';
import './camera.css'
import Tesseract from 'tesseract.js';
const CameraComponent = () => {
  const webcamRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [text, setText] = useState(null);
  const [photoLoading, setPhotoLoading] = useState(false);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setCapturedImage(imageSrc);
  }, [webcamRef]);

const emptyCapturedImage =() => {
  setCapturedImage(null);
};
  //conver photo to text
  const convertImageToText = () => {
    setPhotoLoading(true);
    Tesseract.recognize(
      capturedImage,
      'amh',
      { logger: (info) => console.log(info) }
    ).then(({ data: { text } }) => {
      setText(text);
    }).finally(() => {
      setPhotoLoading(false);
    });
  };
  

  return (
    <div  className=''>
      {capturedImage?  (
        <div className='flex cameraPhoto'>
          <div className="photo ">
          <h2>Captured Photo:</h2>
          <img src={capturedImage} alt="Captured" />

          <div className="flex justify-around mt-20">
          <button className='btn mt-20' onClick={emptyCapturedImage}>Back</button>
          <button className='btn mt-20' onClick={convertImageToText}>Convert to Text</button>
          
          </div>
          {photoLoading && <div className="photoLoading">Loading...</div>}
          </div>

          {text &&<div className="text">
           <div>
            <p className='text-items'>{text}</p></div>
          </div>}
        </div>
      ):<div className="">
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
      />
      <button className='btn mt-20' onClick={capture}>Capture Photo</button>
      </div>}


     
    </div>
  );
};

export default CameraComponent;

'use client'
import React, { useState, useRef } from "react";
import { Camera } from "react-camera-pro";

const Page = () => {
  const camera = useRef(null);
  const [image, setImage] = useState(null);

  const handleCapture = () => {
    const photo = camera.current.takePhoto();
    setImage(photo);
    
    // Convert the photo to base64 and log it
    fetch(photo)
      .then(res => res.blob())
      .then(blob => {
        const reader = new FileReader();
        reader.onloadend = () => {
          console.log("Base64 string:", reader.result);
        };
        reader.readAsDataURL(blob);
      });
  };

  return (
    <div className="max-w-md mx-auto p-4 bg-white rounded-lg shadow-md">
      <header className="flex justify-between align-right items-center mb-4">
      
        <button onClick={()=>{setImage(null)}} className="px-3 py-1 bg-gray-200 rounded">Reset</button>
      </header>

      <h2 className="text-2xl text-center font-bold  m-6">Commands test</h2>

      <div className="mb-4 rounded-lg overflow-hidden">
        {image ? (
          <img src={image} alt="Captured" className="w-full h-56 object-cover" />
        ) : (
          <Camera ref={camera} facingMode="user" aspectRatio={16 / 9} />
        )}
      </div>

      <p className="text-xl mb-4 text-center">Raise your hand</p>

      <button 
        onClick={handleCapture}
        className="w-full py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
      >
        Record
      </button>
    </div>
  );
};

export default Page;
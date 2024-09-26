'use client'
import React, { useRef, useState, useEffect } from 'react'
import TaskHeading from '../../components/TaskHeading/page'
import Image from 'next/image'
import shapeCirlce from '../../public/circle.png'
import { ReactSketchCanvas } from 'react-sketch-canvas'

const styles = {
  border: '0.0625rem solid #9c9c9c',
  borderRadius: '0.25rem',
};

const Page = () => {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [timeLeft, setTimeLeft] = useState(10); // 3 minutes in seconds

  useEffect(() => {
    let timer;
    if (isDrawing && timeLeft > 0) {
      timer = setInterval(() => {
        setTimeLeft((prevTime) => prevTime - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      handleDownload();
    }
    return () => clearInterval(timer);
  }, [isDrawing, timeLeft]);

  const handleStartDrawing = () => {
    canvasRef.current.clearCanvas();
    setIsDrawing(true);
    setTimeLeft(10);
  };

  

  const handleReset = () => {
    setIsDrawing(false);
    setTimeLeft(180);
    canvasRef.current.clearCanvas();
  };

  const handleDownload = () => {
    canvasRef.current
      .exportImage("jpeg")
      .then(data => {
        // Log the base64 string representation of the image
        console.log("Base64 image data:", data);
        
        // Convert base64 to Blob (keeping this part for reference)
        const base64Data = data.split(',')[1];
        const blob = b64toBlob(base64Data, 'image/jpeg');
        
        // Create a FileReader to read the Blob as ArrayBuffer
        const reader = new FileReader();
        reader.onloadend = function() {
          // Convert ArrayBuffer to Uint8Array
          const uint8Array = new Uint8Array(reader.result);
          console.log("JPEG image data (Uint8Array):", uint8Array);
        }
        reader.readAsArrayBuffer(blob);

        setIsDrawing(false);
      })
      .catch(e => {
        console.error("Error exporting image:", e);
      });
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  return (
    <div className='justify-center flex-col flex items-center'>
      <TaskHeading heading='Constructional Praxis'/>
      <Image src={shapeCirlce} height={150} width={150} className='object-contain flex justify-center items-center'/>
      <h3 className='my-3 font-bold text-2xl'>Circle</h3>
      
      <div className='mt-4 w-[600px]'>
        <div className='mb-4 flex justify-between items-center'>
          <div className='text-xl font-bold'>
            {isDrawing && `Time left: ${formatTime(timeLeft)}`}
          </div>
          <div className='flex gap-4'>
            <button 
              onClick={handleStartDrawing} 
              className='bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded transition duration-300 ease-in-out'
              disabled={isDrawing}
            >
              Start Drawing
            </button>
            <button 
              onClick={handleReset} 
              className='bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded transition duration-300 ease-in-out'
              disabled={!isDrawing}
            >
              Reset
            </button>
          </div>
        </div>
        <ReactSketchCanvas
          ref={canvasRef}
          strokeWidth={12}
          strokeColor="red"
          style={styles}
          width="600px"
          height="400px"
          canvasColor={isDrawing ? "white" : "lightgray"}
          disabled={!isDrawing}
          className='mb-5'
        />
      </div>
    </div>
  )
}

export default Page

// Helper function to convert base64 to Blob
const b64toBlob = (b64Data, contentType = '', sliceSize = 512) => {
  const byteCharacters = atob(b64Data);
  const byteArrays = [];

  for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
    const slice = byteCharacters.slice(offset, offset + sliceSize);
    const byteNumbers = new Array(slice.length);
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    byteArrays.push(byteArray);
  }

  const blob = new Blob(byteArrays, { type: contentType });
  return blob;
};
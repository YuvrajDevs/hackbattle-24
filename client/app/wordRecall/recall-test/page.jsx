'use client'
import React, { useState, useEffect } from 'react';
// import styles from './RecallTest.module.css'; // You'll need to create this CSS module

const RecallTest = () => {
  const [words] = useState(['Flower', /* ... add 9 more words ... */]);
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [showRecordButton, setShowRecordButton] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [timeLeft, setTimeLeft] = useState(60);

  useEffect(() => {
    if (currentWordIndex < words.length) {
      const timer = setInterval(() => {
        setTimeLeft((prevTime) => {
          if (prevTime <= 1) {
            clearInterval(timer);
            setCurrentWordIndex(prevIndex => prevIndex + 1);
            return 60;
          }
          return prevTime - 1;
        });
      }, 1000);

      return () => clearInterval(timer);
    } else {
      setShowRecordButton(true);
    }
  }, [currentWordIndex, words.length]);

  const startRecording = async () => {
    setIsRecording(true);
    // Implement audio recording logic here
  };

  const stopRecording = () => {
    setIsRecording(false);
    // Implement logic to save the recorded audio as WAV
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100 p-4">
      <main className="flex-1 flex flex-col items-center">
        <h2 className="text-3xl font-bold mb-4">Word recall test</h2>
        <p className="text-xl mb-8">Trial: {currentWordIndex + 1}</p>
        {currentWordIndex < words.length ? (
          <>
            <div className="relative mb-8">
              <span className="absolute -left-8 -top-8 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center">
                {currentWordIndex + 1}
              </span>
              <div className="border-2 border-black rounded-lg p-6 text-4xl font-bold">
                {words[currentWordIndex]}
              </div>
            </div>
            <p className="text-lg mb-8">Read it out loud and try to remember it</p>
            <div className="text-2xl font-bold text-green-500">
              {timeLeft} seconds
            </div>
          </>
        ) : showRecordButton ? (
          <button
            className="px-8 py-3 bg-green-500 text-white rounded-full text-xl"
            onClick={isRecording ? stopRecording : startRecording}
          >
            {isRecording ? 'Stop Recording' : 'Start Recording'}
          </button>
        ) : null}
      </main>
    </div>
  );
};

export default RecallTest;
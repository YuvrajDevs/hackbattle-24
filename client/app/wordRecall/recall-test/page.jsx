'use client'
import React, { useState, useEffect } from 'react';
import Link from 'next/link';

const RecallTest = () => {
  const [words] = useState([
    "apple",
    "",
    "mountain",
    "book",
    "house",
    "car",
    "flower",
    "chair",
    "dog",
    "sun",
    "river",
    "tree",
    "bird",
    "fish",
    "water",
    "sky",
    "cloud",
    "rain",
    "wind",
    
]);
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [showRecordButton, setShowRecordButton] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [timeLeft, setTimeLeft] = useState(2);
  const [trialCount, setTrialCount] = useState(1);
  const [isTestComplete, setIsTestComplete] = useState(false);

  useEffect(() => {
    if (currentWordIndex < words.length && !isTestComplete) {
      const timer = setInterval(() => {
        setTimeLeft((prevTime) => {
          if (prevTime <= 1) {
            clearInterval(timer);
            setCurrentWordIndex(prevIndex => prevIndex + 1);
            return 2; // Reset to 2 seconds for each word
          }
          return prevTime - 1;
        });
      }, 1000);

      return () => clearInterval(timer);
    } else if (currentWordIndex >= words.length) {
      setShowRecordButton(true);
    }
  }, [currentWordIndex, words.length, isTestComplete]);

  const startRecording = async () => {
    setIsRecording(true);
    // Implement audio recording logic here
  };

  const stopRecording = () => {
    setIsRecording(false);
    // Implement logic to save the recorded audio as WAV
    if (trialCount < 3) {
      setTrialCount(prevTrial => prevTrial + 1);
      setCurrentWordIndex(0);
      setShowRecordButton(false);
      setTimeLeft(2);
    } else {
      setIsTestComplete(true);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-100 p-4">
      <main className="flex-1 flex flex-col items-center">
        <h2 className="text-3xl font-bold mb-4">Word recall test</h2>
        <p className="text-xl mb-8">Trial: {trialCount}</p> {/* Update this line */}
        {isTestComplete ? (
          <>
            <p className="text-2xl font-bold mb-8">Test Complete!</p>
            <Link href="/contructionalPraxis">
              <button className="px-8 py-3 bg-blue-500 text-white rounded-full text-xl">
                Move to Next Test
              </button>
            </Link>
          </>
        ) : currentWordIndex < words.length ? (
          <>
            <div className="relative mb-8">
              {/* <span className="absolute -left-8 -top-8 bg-green-500 text-white rounded-full w-10 h-10 flex items-center justify-center">
                {currentWordIndex + 1}
              </span> */}
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
# import os
# import google.generativeai as genai
# import dotenv
# import ast
# import speech_recognition as sr
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv

# def record_user_audio():
#     # Sampling frequency
#     freq = 44100

#     # Recording duration in seconds
#     duration = 20

#     # Start recorder with the given values 
#     recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

#     # Record audio for the given number of seconds
#     print("Recording started...")
#     sd.wait()  # Wait for the recording to finish
#     print("Recording finished.")

#     # Save the recorded audio as WAV file
#     audio_filename = "patient_recording.wav"
#     write(audio_filename, freq, recording)

#     # Optionally, also save using wavio for wider compatibility
#     wv.write(audio_filename, recording, freq, sampwidth=1)
    
#     return audio_filename

# def recognize_speech_from_file(audio_file):
#     recognizer = sr.Recognizer()

#     # Load the audio file for speech recognition
#     with sr.AudioFile(audio_file) as source:
#         print(f"Recognizing speech from {audio_file}...")
#         audio_data = recognizer.record(source)  # Read the entire audio file
#         try:
#             recognized_text = recognizer.recognize_google(audio_data)
#             print(f"{recognized_text}")
#             return recognized_text
#         except sr.UnknownValueError:
#             print("Speech recognition could not understand the audio.")
#             return ""
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#             return ""

# dotenv.load_dotenv()
# genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# # Generate high-imagery noun list using Google Gemini AI
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(
#     '''Generate a list of 10 High Imagery Nouns. Give me the words in a python list. 
#     The list of words is to be given to an Alzheimer's patient for ADAS COG Word Recall Task. 
#     Do not give anything else in the output.'''
# )

# # Extract the text output from the API response
# generated_text = response.text

# # Parse the string to a list
# try:
#     parsed_list = ast.literal_eval(generated_text)
#     print(f"Generated Word List: {parsed_list}")
# except (SyntaxError, ValueError) as e:
#     print(f"Error parsing the generated list: {e}")
#     parsed_list = []

# def process_recognized(lst, recognized_text):
#     lst_patient = recognized_text.split()  # Split recognized text into words
#     lst_patient = sorted([s.lower() for s in lst_patient])  # Convert to lowercase and sort
#     lst_patient = list(set(lst_patient))  # Remove duplicates by converting to set and back to list
    
#     lst = sorted([s.lower() for s in lst])  # Ensure the target list is sorted and lowercase

#     print("Recognized Words (After Removing Duplicates):")
#     for i in lst_patient:
#         print(i, end=" ")
    
#     print("\nTarget Word List:")
#     for i in lst:
#         print(i, end=" ")

    
    
    

# # Record user audio
# audio_file = record_user_audio()
# # audio_file = './patient_recording.wav'
# # Recognize speech from the recorded file
# recognized_text = recognize_speech_from_file(audio_file)

# # Process recognized words
# if recognized_text:
#     process_recognized(parsed_list, recognized_text)

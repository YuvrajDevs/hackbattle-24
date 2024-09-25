# from fastapi import FastAPI, UploadFile
# from fastapi.responses import StreamingResponse
# from fastapi.middleware.cors import CORSMiddleware

# from dotenv import load_dotenv


# # import openai
# from transformers import pipeline
# from groq import Groq

# import os
# import json
# import requests

# load_dotenv()

# # openai.api_key = os.getenv("OPEN_AI_KEY")
# # openai.organization = os.getenv("OPEN_AI_ORG")
# elevenlabs_key = os.getenv("ELEVENLABS_KEY")

# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small.en")

# app = FastAPI()

# origins = [
#     "http://localhost:5174",
#     "http://localhost:5173",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/talk")
# async def post_audio(file: UploadFile):
#     user_message = transcribe_audio(file)
#     chat_response = get_chat_response(user_message)
#     audio_output = text_to_speech(chat_response)

#     def iterfile():
#         yield audio_output

#     return StreamingResponse(iterfile(), media_type="application/octet-stream")

# @app.get("/clear")
# async def clear_history():
#     file = 'database.json'
#     open(file, 'w')
#     return {"message": "Chat history has been cleared"}

# # Functions
# def transcribe_audio(file):
#     # Save the blob first
#     with open(file.filename, 'wb') as buffer:
#         buffer.write(file.file.read())
#     audio_file = open(file.filename, "rb")
#     # transcript = openai.Audio.transcribe("whisper-1", audio_file)
#     result = pipe(audio_file)
#     transcript = result['text']
#     print(transcript)
#     return transcript

# def get_chat_response(user_message):
#     messages = load_messages()
#     messages.append({"role": "user", "content": user_message['text']})
#     # 

#     client = Groq(
#         api_key=os.environ.get("GROQ_API_KEY"),
#     )

#     chat_completion = client.chat.completions.create(
#         messages=messages,
#         model="mixtral-8x7b-32768",
#     )

#     # 

#     # Send to ChatGpt/OpenAi
#     # gpt_response = gpt_response = openai.ChatCompletion.create(
#     #     model="gpt-3.5-turbo",
#     #     messages=messages
#     # )

#     parsed_chat_response = chat_completion.choices[0].message.content

#     # Save messages
#     save_messages(user_message['text'], parsed_chat_response)

#     return parsed_chat_response

# def load_messages():
#     messages = []
#     file = 'database.json'

#     empty = os.stat(file).st_size == 0

#     if not empty:
#         with open(file) as db_file:
#             data = json.load(db_file)
#             for item in data:
#                 messages.append(item)
#     else:
#         messages.append(
#             {"role": "system", "content": "You are interviewing the user for a front-end React developer position. Ask short questions that are relevant to a junior level developer. Your name is Greg. The user is Travis. Keep responses under 30 words and be funny sometimes."}
#         )
#     return messages

# def save_messages(user_message, chat_response):
#     file = 'database.json'
#     messages = load_messages()
#     messages.append({"role": "user", "content": user_message})
#     messages.append({"role": "assistant", "content": chat_response})
#     with open(file, 'w') as f:
#         json.dump(messages, f)

# def text_to_speech(text):
#     voice_id = 'pNInz6obpgDQGcFmaJgB'
    
#     body = {
#         "text": text,
#         "model_id": "eleven_monolingual_v1",
#         "voice_settings": {
#             "stability": 0,
#             "similarity_boost": 0,
#             "style": 0.5,
#             "use_speaker_boost": True
#         }
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "accept": "audio/mpeg",
#         "xi-api-key": elevenlabs_key
#     }

#     url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

#     try:
#         response = requests.post(url, json=body, headers=headers)
#         if response.status_code == 200:
#             return response.content
#         else:
#             print('something went wrong')
#     except Exception as e:
#         print(e)


# #1. Send in audio, and have it transcribed
# #2. We want to send it to chatgpt and get a response
# #3. We want to save the chat history to send back and forth for context.
from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

def load_messages():
    messages = []
    file = 'database.json'

    if os.path.exists(file) and os.stat(file).st_size != 0:
        with open(file) as db_file:
            data = json.load(db_file)
            messages.extend(data)
    else:
        messages.append(
            {"role": "system", "content": "You are interviewing the user for a front-end React developer position. Ask short questions that are relevant to a junior level developer, one question at a time. Your name is Greg. Welcome the candidate first, ask them for their name and brief introduction, then dive into the interview. Keep responses under 30 words and be funny sometimes."}
        )
    return messages

def save_messages(messages):
    with open('database.json', 'w') as f:
        json.dump(messages, f)

def get_chat_response(user_message):
    messages = load_messages()
    messages.append({"role": "user", "content": user_message})

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="mixtral-8x7b-32768",
    )

    assistant_response = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})
    
    save_messages(messages)
    return assistant_response

def get_candidate_score():
    messages = load_messages()
    
    evaluation_prompt = (
        "Based on the interview conversation so far, provide a score for the candidate "
        "on a scale of 1-10, where 1 is poor and 10 is excellent. Also provide a brief "
        "explanation for the score. Format your response as JSON with 'score' and 'explanation' keys."
    )
    
    messages.append({"role": "user", "content": evaluation_prompt})

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="mixtral-8x7b-32768",
    )

    evaluation_response = chat_completion.choices[0].message.content
    
    try:
        evaluation_data = json.loads(evaluation_response)
        return evaluation_data
    except json.JSONDecodeError:
        return {"score": 0, "explanation": "Error in processing the evaluation."}



def main():
    print("Welcome to the conversation! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            get_candidate_score()
            break
        
        response = get_chat_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
import random
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from transformers import pipeline
import re
from metaphone import doublemetaphone
from Levenshtein import distance as levenshtein_distance

from vocablist import vocab_list
# Initialize Whisper pipeline
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small.en")

def record_user_audio(duration=20, freq=44100):
    print("Recording started...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()
    print("Recording finished.")
    
    audio_filename = "patient_recording.wav"
    write(audio_filename, freq, recording)
    wv.write(audio_filename, recording, freq, sampwidth=1)
    
    return audio_filename

def recognize_speech_from_file(audio_file):
    print(f"Recognizing speech from {audio_file} using Whisper model...")
    
    try:
        result = pipe(audio_file)
        recognized_text = result['text']
        print(f"Recognized text: {recognized_text}")
        return recognized_text
    except Exception as e:
        print(f"Error during speech recognition: {e}")
        return ""

selected_indices=[]
def generate_word_list(vocablist):
    random_indices = []
    selected_words = []

    while len(selected_words) < 10:
        rand_index = random.randint(0, len(vocablist) - 1)
        if rand_index not in selected_indices:
            selected_indices.append(rand_index)
            selected_words.append(vocab_list[rand_index])

    return selected_words

def compare_words(target_word, spoken_word, threshold=0.66):
    # Convert to lowercase
    target_word = target_word.lower()
    spoken_word = spoken_word.lower()

    # Direct comparison
    if target_word == spoken_word:
        return True

    # Phonetic comparison using Metaphone
    target_phonetic = doublemetaphone(target_word)[0]
    spoken_phonetic = doublemetaphone(spoken_word)[0]
    
    if target_phonetic == spoken_phonetic:
        return True

    # Strict edit distance comparison on phonetic codes
    max_distance = max(len(target_phonetic), len(spoken_phonetic))
    similarity = 1 - (levenshtein_distance(target_phonetic, spoken_phonetic) / max_distance)
    
    if similarity >= threshold:
        return True

    # Strict regular expression for pronunciation variations
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    pattern = '^'
    for c in target_word:
        if c in vowels:
            pattern += f'[{vowels}]'
        elif c in consonants:
            pattern += c
        else:
            pattern += c
    pattern += '$'

    if re.match(pattern, spoken_word) and len(target_word) == len(spoken_word):
        return True

    return False

def process_recognized(target_list, recognized_text):
    count_not_recalled = len(target_list)
    recognized_words = recognized_text.lower().split()
    target_words = [word.lower() for word in target_list]

    print("Recognized Words:")
    print(" ".join(recognized_words))

    print("\nTarget Word List:")
    print(" ".join(target_words))

    # Track which target words have been matched
    matched_words = set()

    for recognized_word in recognized_words:
        for target_word in target_words:
            if compare_words(target_word, recognized_word) and target_word not in matched_words:
                print(f"Matched: {recognized_word} -> {target_word}")
                matched_words.add(target_word)  # Mark the target word as matched
                count_not_recalled -= 1
                break  # Move to the next recognized word after a match

    print(f"\nNumber of words not recalled: {count_not_recalled}")

def main():
    word_list = generate_word_list(vocab_list)
    if not word_list:
        print("Failed to generate word list. Exiting.")
        return
    print(word_list)
    audio_file = record_user_audio()
    recognized_text = recognize_speech_from_file(audio_file)
    
    if recognized_text:
        process_recognized(word_list, recognized_text)
    else:
        print("No text was recognized. Please try again.")

if __name__ == "__main__":
    main()

# import os
# import random
# import time
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv
# from transformers import pipeline
# import re
# from metaphone import doublemetaphone
# from Levenshtein import distance as levenshtein_distance
# from vocablist import vocab_list

# # Initialize Whisper pipeline
# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small.en")

# # Function to record audio from the user
# def record_user_audio(duration=20, freq=44100):
#     print("Recording started...")
#     recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
#     sd.wait()
#     print("Recording finished.")
    
#     audio_filename = "patient_recording.wav"
#     write(audio_filename, freq, recording)
#     wv.write(audio_filename, recording, freq, sampwidth=1)
    
#     return audio_filename

# # Function to recognize speech from the recorded file using Whisper
# def recognize_speech_from_file(audio_file):
#     print(f"Recognizing speech from {audio_file} using Whisper model...")
    
#     try:
#         result = pipe(audio_file)
#         recognized_text = result['text']
#         print(f"Recognized text: {recognized_text}")
#         return recognized_text
#     except Exception as e:
#         print(f"Error during speech recognition: {e}")
#         return ""

# selected_indices = []

# # Function to generate a word list while ensuring no duplicates are selected
# def generate_word_list(vocablist):
#     selected_words = []

#     while len(selected_words) < 10:
#         rand_index = random.randint(0, len(vocablist) - 1)
#         if rand_index not in selected_indices:
#             selected_indices.append(rand_index)
#             selected_words.append(vocablist[rand_index])

#     return selected_words

# # Function to compare target and spoken words, ensuring no partial matches
# def compare_words(target_word, spoken_word):
#     target_word = target_word.lower()
#     spoken_word = spoken_word.lower()

#     # Exact match only
#     return target_word == spoken_word

# # Function to process recognized text and count unrecalled words
# def process_recognized(target_list, recognized_text):
#     count_not_recalled = len(target_list)
#     recognized_words = recognized_text.lower().split()
#     target_words = [word.lower() for word in target_list]

#     print("Recognized Words:")
#     print(" ".join(recognized_words))

#     print("\nTarget Word List:")
#     print(" ".join(target_words))

#     matched_words = set()

#     for recognized_word in recognized_words:
#         for target_word in target_words:
#             if compare_words(target_word, recognized_word) and target_word not in matched_words:
#                 print(f"Matched: {recognized_word} -> {target_word}")
#                 matched_words.add(target_word)
#                 count_not_recalled -= 1
#                 break

#     print(f"\nNumber of words not recalled: {count_not_recalled}")
#     return count_not_recalled

# # Function to display words with a time interval gap
# def display_words_with_intervals(word_list, interval=2):
#     print("Please listen carefully to the following words:")
#     for word in word_list:
#         print(f"Word: {word}")
#         time.sleep(interval)

# # Function to display instructions for the patient
# def instructions_for_patient():
#     print("""
#     Welcome to the word recall task. In this task, you will be presented with a list of 10 words.
#     After you hear the words, you will need to recall as many as possible.
#     This task will be repeated for three rounds. At the end of each round, your score will be shown.
#     The final score will be the average of all three rounds.
    
#     Please make sure you are in a quiet environment, and try to remember as many words as possible.
#     Let's get started!
#     """)

# # Function to clear the screen (cross-platform)
# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # Main function to handle the three iterations and score calculation
# def main(vocab_list, iterations=3):
#     instructions_for_patient()
    
#     total_score = 0
    
#     for round_num in range(1, iterations + 1):
#         print(f"\nStarting round {round_num}...\n")
        
#         # Generate the word list for the current round
#         word_list = generate_word_list(vocab_list)
#         display_words_with_intervals(word_list)
        
#         time.sleep(5)  # Pause before clearing the screen
        
#         # Clear the screen before starting the recording
#         clear_screen()

#         print("\nNow, please recall the words you remember.")
#         audio_file = record_user_audio()
#         recognized_text = recognize_speech_from_file(audio_file)
        
#         if recognized_text:
#             round_score = process_recognized(word_list, recognized_text)
#             print(f"\nRound {round_num} score: {round_score} words not recalled.")
#             total_score += round_score
#         else:
#             print("No text was recognized. Please try again.")
    
#     final_score = total_score / iterations
#     print(f"\nFinal score (average of all rounds): {final_score} words not recalled.")
#     print("Thank you for participating in the task!")

# if __name__ == "__main__":
#     # vocab_list = ["Apple", "Sunset", "Chair", "Dog", "Book", "Ocean", "Pencil", "House", "Tree", "Music"]
#     main(vocab_list)

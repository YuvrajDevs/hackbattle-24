import time

from vocablist import vocab_list
# Initialize Whisper pipeline
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small.en")

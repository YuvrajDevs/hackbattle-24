# # from thefuzz import fuzz


# # print(fuzz.partial_ratio("ukulele", "ookelele"))

# # import re
# # from metaphone import doublemetaphone
# # from Levenshtein import distance as levenshtein_distance

# # def compare_words(target_word, spoken_word, threshold=0.8):
# #     # Convert to lowercase
# #     target_word = target_word.lower()
# #     spoken_word = spoken_word.lower()

# #     # Direct comparison
# #     if target_word == spoken_word:
# #         return True

# #     # Phonetic comparison using Metaphone
# #     target_phonetic = doublemetaphone(target_word)[0]
# #     spoken_phonetic = doublemetaphone(spoken_word)[0]
    
# #     if target_phonetic == spoken_phonetic:
# #         return True

# #     # Edit distance comparison
# #     max_distance = max(len(target_phonetic), len(spoken_phonetic))
# #     similarity = 1 - (levenshtein_distance(target_phonetic, spoken_phonetic) / max_distance)
    
# #     if similarity >= threshold:
# #         return True

# #     # More precise regular expression for common pronunciation variations
# #     vowel_map = {
# #         'a': '[aə]',  # 'a' or schwa
# #         'e': '[eɛ]',  # 'e' or open e
# #         'i': '[iɪ]',  # 'i' or near-close near-front unrounded vowel
# #         'o': '[oɔ]',  # 'o' or open-mid back rounded vowel
# #         'u': '[uʊ]'   # 'u' or near-close near-back rounded vowel
# #     }
# #     consonant_map = {
# #         'b': '[b]', 'c': '[ck]', 'd': '[d]', 'f': '[f]', 'g': '[g]',
# #         'h': '[h]', 'j': '[dʒ]', 'k': '[k]', 'l': '[l]', 'm': '[m]',
# #         'n': '[n]', 'p': '[p]', 'q': '[k]', 'r': '[r]', 's': '[s]',
# #         't': '[t]', 'v': '[v]', 'w': '[w]', 'x': '[ks]', 'y': '[j]',
# #         'z': '[z]'
# #     }

# #     pattern = '^'
# #     for c in target_word:
# #         if c in vowel_map:
# #             pattern += vowel_map[c]
# #         elif c in consonant_map:
# #             pattern += consonant_map[c]
# #         else:
# #             pattern += c
# #     pattern += '$'

# #     if re.match(pattern, spoken_word):
# #         return True

# #     return False

# # # Example usage
# # target_words = ["ukulele", "guitar", "piano"]
# # spoken_words = ["ookelele", "gitar", "peeano"]

# # for target, spoken in zip(target_words, spoken_words):
# #     result = compare_words(target, spoken)
# #     print(f"Target: {target}, Spoken: {spoken}, Match: {result}")


# import re
# from metaphone import doublemetaphone
# from Levenshtein import distance as levenshtein_distance

# def compare_words(target_word, spoken_word, threshold=0.66):
#     # Convert to lowercase
#     target_word = target_word.lower()
#     spoken_word = spoken_word.lower()

#     # Direct comparison
#     if target_word == spoken_word:
#         return True

#     # Phonetic comparison using Metaphone
#     target_phonetic = doublemetaphone(target_word)[0]
#     spoken_phonetic = doublemetaphone(spoken_word)[0]
    
#     if target_phonetic == spoken_phonetic:
#         return True

#     # Strict edit distance comparison on phonetic codes
#     max_distance = max(len(target_phonetic), len(spoken_phonetic))
#     similarity = 1 - (levenshtein_distance(target_phonetic, spoken_phonetic) / max_distance)
    
#     if similarity >= threshold:
#         return True

#     # Strict regular expression for pronunciation variations
#     vowels = 'aeiou'
#     consonants = 'bcdfghjklmnpqrstvwxyz'
    
#     pattern = '^'
#     for c in target_word:
#         if c in vowels:
#             pattern += f'[{vowels}]'
#         elif c in consonants:
#             pattern += c
#         else:
#             pattern += c
#     pattern += '$'

#     if re.match(pattern, spoken_word) and len(target_word) == len(spoken_word):
#         return True

#     return False

# # Example usage
# target_words = ["ukulele", "guitar", "piano"]
# spoken_words = ["ookelele", "gitar", "peeano"]

# for target, spoken in zip(target_words, spoken_words):
#     result = compare_words(target, spoken)
#     print(f"Target: {target}, Spoken: {spoken}, Match: {result}")




# def compare_words(target_word, spoken_word, threshold=0.66):
#     # Convert to lowercase
#     target_word = target_word.lower()
#     spoken_word = spoken_word.lower()

#     # Direct comparison
#     if target_word == spoken_word:
#         return True

#     # Phonetic comparison using Metaphone
#     target_phonetic = doublemetaphone(target_word)[0]
#     spoken_phonetic = doublemetaphone(spoken_word)[0]
    
#     if target_phonetic == spoken_phonetic:
#         return True

#     # Strict edit distance comparison on phonetic codes
#     max_distance = max(len(target_phonetic), len(spoken_phonetic))
#     similarity = 1 - (levenshtein_distance(target_phonetic, spoken_phonetic) / max_distance)
    
#     if similarity >= threshold:
#         return True

#     # Strict regular expression for pronunciation variations
#     vowels = 'aeiou'
#     consonants = 'bcdfghjklmnpqrstvwxyz'
    
#     pattern = '^'
#     for c in target_word:
#         if c in vowels:
#             pattern += f'[{vowels}]'
#         elif c in consonants:
#             pattern += c
#         else:
#             pattern += c
#     pattern += '$'

#     if re.match(pattern, spoken_word) and len(target_word) == len(spoken_word):
#         return True

#     return False

# Use a pipeline as a high-level helper
from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="google/gemma-2-2b-it")
pipe(messages)
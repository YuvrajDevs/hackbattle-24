# import os
# import google.generativeai as genai
# import dotenv
# import ast
# import sounddevice as sd
# from scipy.io.wavfile import write
# import wavio as wv
# from thefuzz import fuzz
# from transformers import pipeline


# from groq import Groq

# # Initialize Whisper pipeline
# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small.en")
# # pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# def record_user_audio(duration=20, freq=44100):
#     print("Recording started...")
#     recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
#     sd.wait()
#     print("Recording finished.")
    
#     audio_filename = "patient_recording.wav"
#     write(audio_filename, freq, recording)
#     wv.write(audio_filename, recording, freq, sampwidth=1)
    
#     return audio_filename

# def recognize_speech_from_file(audio_file):
#     print(f"Recognizing speech from {audio_file} using Whisper model...")
    
#     try:
#         # Whisper expects a file path to the audio
#         result = pipe(audio_file)
#         recognized_text = result['text']
#         print(f"Recognized text: {recognized_text}")
#         return recognized_text
#     except Exception as e:
#         print(f"Error during speech recognition: {e}")
#         return ""

# def generate_word_list():
#     dotenv.load_dotenv()
#     # genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

#     client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
#     # model = genai.GenerativeModel("gemini-1.5-flash")
    # prompt = '''Generate a list of 10 High Imagery Nouns. Give me the words in a python list.
    # The list of words is to be given to an Alzheimer's patient for ADAS COG Word Recall Task.
    # Do not give anything else in the output.
    # This is how the output should look like:
    #     [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10]

    # You can select 10 words at random from the following list, or generate similar words

    # Word List that can be used for reference:
    # [
    # "abagment", "abyss", "acrobat", "action", "actor", "admiration", "affection", "anarchy", 
    # "animal", "antelope", "anxiety", "appk", "asparaps", "attribute", "baby", "badger", 
    # "banana", "bath", "beauty", "beetle", "boat", "box", "bronze", "brotherhood", "brugt", 
    # "buffalo", "bullet", "butter", "butterfly", "cabbage", "cake", "campus", "candy", 
    # "cannon", "canyon", "captive", "curot", "cashmere", "charm", "cherry", "child", 
    # "Chile", "chisel", "church", "cider", "city", "clemency", "cloak", "club", "coat", 
    # "committee", "controversy", "course", "coyote", "crater", "cracker", "daisy", "danger", 
    # "day", "debate", "decay", "delerium", "demon", "depth", "devotion", "dignity", "disease", 
    # "doctor", "donkey", "door", "dress", "eagle", "elephant", "emotion", "faith", "fame", 
    # "farmer", "fear", "figment", "fig", "fog", "foot", "frune", "fraud", "freedom", "fruit", 
    # "furnace", "garden", "gardenia", "gove", "goat", "gorilla", "government", "grasshopper", 
    # "grief", "guns", "hair", "hammer", "hand", "harness", "harp", "hat", "hate", "health", 
    # "height", "hill", "hunt", "hog", "hope", "horse", "hunger", "ignorance", "income", 
    # "India", "infection", "jacket", "jealousy", "joy", "judgment", "juggler", "justice", 
    # "king", "knee", "knife", "knuckle", "lake", "lamb", "lamp", "larceny", "lawyer", 
    # "length", "lettuce", "liberty", "life", "link", "lion", "liquor", "lock", "love", 
    # "loyalty", "marriage", "martyr", "maturity", "mechanic", "memory", "method", "Mexico", 
    # "milk", "mind", "miner", "minister", "minute", "monkey", "moon", "moth", "motion", 
    # "music", "muskrat", "nation", "need", "nurg", "nuts", "ocean", "oil", "ounce", "oven", 
    # "owl", "panther", "pants", "paper", "patriot", "peace", "pen", "philosopher", "piano", 
    # "picture", "pistol", "pity", "pliers", "poet", "politician", "popularity", "position", 
    # "prayer", "preview", "proxy", "queen", "rabbit", "religion", "repentance", "roar", 
    # "robbery", "scissors", "scout", "shame", "shape", "sheep", "silk", "skin", "sleep", 
    # "sofa", "soldier", "soul", "sound", "spider", "stream", "strife", "stomach", "stool", 
    # "stove", "success", "sweater", "sword", "symphony", "theory", "thirst", "thought", 
    # "thumb", "time", "tin", "train", "trout", "trumpet", "truth", "tunnel", "turnip", 
    # "uniform", "unit", "ukulele", "valley", "vase", "violin", "want", "warning", "wasp", 
    # "water", "weight", "whiskey", "whistle", "width", "window", "wolf", "zebra", "abbess", 
    # "abdication", "abdomen", "abduction", "aberration", "ability", "abode", "accordion", 
    # "adage", "admiral", "advantage", "adversity", "advice", "afterlife", "agility", "agony", 
    # "agreement", "air", "alcohol", "algebra", "alimony", "allegory", "alligator", "ambulance", 
    # "amount", "amour", "amplifier", "anecdote", "anger", "angle", "animosity", "ankle", 
    # "answer", "antitoxin", "appearance", "apple", "appliance", "aptitude", "arbiter", "arm", 
    # "armadillo", "army", "array", "arrow", "artist", "assault", "athletics", "atmosphere", 
    # "atrocity", "attendant", "attitude", "author", "automobile", "avalanche", "avenue", 
    # "background", "bacteria", "bagpipe", "banality", "bandit", "banker", "banner", "bar", 
    # "bard", "baron", "barrel", "basement", "beast", "beaver", "beggar", "belfry", "belief", 
    # "belongings", "bereavement", "betrayal", "beverage", "bivouac", "blacksmith", "blandness", 
    # "blasphemy", "blessing", "blister", "blood", "bloom", "blossom", "blunderbuss", "board", 
    # "body", "book", "boredom", "bosom", "boss", "bottle", "boulder", "bouquet", "bowl", 
    # "boy", "brain", "brassiere", "bravery", "breast", "breeze", "brutality", "brute", 
    # "buffoon", "builder", "building", "bungalow", "busybody", "butcher", "cabin", 
    # "camouflage", "camp", "candidate", "cane", "capacity", "car", "caravan", "cash", "cat", 
    # "caterpillar", "cattle", "causality", "cell", "cellar", "centennial", "cerebrum", 
    # "ceremony", "chair", "chance", "chaos", "charlatan", "charter", "chasm", "chief", "chin", 
    # "chloride", "Christmas", "cigar", "circle", "circuit", "citation", "claw", "cleanness", 
    # "clock", "cobblestone", "code", "coffee", "coin", "college", "colony", "combustion", 
    # "comedy", "comforter", "comparison", "competence", "competition", "comrade", "comradeship", 
    # "concept", "confidence", "connoisseur", "conquest", "contents", "context", "contract", 
    # "contribution", "convention", "cooperation", "copybook", "cord", "core", "corn", "corner", 
    # "corpse", "cost", "costume", "cottage", "cotton", "courtship", "cowhide", "cradle", 
    # "crag", "cranium", "creator", "creature", "crime", "crisis", "criterion", "cuisine", 
    # "custom", "daffodil", "dalliance", "damsel", "dawn", "daybreak", "daylight", "death", 
    # "debacle", "deceit", "decoration", "decree", "deduction", "deed", "dell", "deluge", 
    # "democracy", "destruction", "determination", "detonation", "development", "devil", 
    # "diamond", "direction", "dirt", "disaster", "discipline", "disclosure", "disconnection", 
    # "discovery", "discretion", "disparity", "disposition", "distinction", "distraction", 
    # "disturber", "doll", "dollar", "domicile", "doorman", "dove", "drama", "dream", "dreamer", 
    # "dummy", "dust", "duty", "dweller", "dynasty", "earth", "eccentricity", "economy", 
    # "edifice", "edition", "effort", "ego", "elaboration", "elbow", "emancipation", 
    # "embezzlement", "emergency", "emporium", "encephalon", "encore", "engagement", "engine", 
    # "ensemble", "enterprise", "episode", "epistle", "equity", "errand", "evangelist", "event", 
    # "evidence", "exactitude", "examination", "exclusion", "excuse", "exertion", "exhaust", 
    # "exhaustion", "explanation", "expression", "extermination", "fabric", "facility", "fact", 
    # "factory", "falconer", "fallacy", "fantasy", "fate", "fatigue", "fault", "feline", 
    # "festivity", "feudalism", "fiord", "fire", "fireplace", "firmament", "fisherman", "flag", 
    # "flesh", "flexibility", "flood", "flower", "foam", "foible", "folly", "footwear", 
    # "forehead", "forest", "forethought", "fork", "form", "formation", "fortune", "fowl", 
    # "fox", "franchise", "friction", "friend", "frog", "frontage", "fun", "functionary", 
    # "fur", "furniture", "gadfly", "gaiety", "galaxy", "gallery", "garments", "garret", 
    # "geese", "gem", "gender", "genius", "ghost", "gift", "gilt", "gingham", "girl", "gist", 
    # "glacier", "glory", "glutton", "goblet", "goddess", "gold", "golf", "gore", "graduation", 
    # "grandmother", "grass", "gravity", "greed", "green", "guardhouse", "gymnastics", 
    # "habitation", "hairpin", "hall", "hamlet", "hankering", "happiness", "hardship", 
    # "hardwood", "hatred", "headlight", "headquarters", "hearing", "heaven", "henchman", 
    # "heredity", "heroism", "hide", "hierarchy", "hillside", "hindrance", "hint", "history", 
    # "home", "homicide", "honeycomb", "honor", "hoof", "horsehair", "hospital", "hostage", 
    # "hostility", "hotel", "hound", "hour", "house", "humor", "hurdle", "hurricane", 
    # "hypothesis", "icebox", "idea", "idiom", "illusion", "immunity", "impact", "impotency", 
    # "impropriety", "impulse", "inanity", "incident", "inclemency", "increment", "inducement", 
    # "industry", "inebriety", "infant", "infirmary", "ingratitude", "inhabitant", "injury", 
    # "ink", "inn", "insect", "insolence", "instance", "institute", "instructor", "instrument", 
    # "intellect", "interest", "interim", "interview", "intimate", "investigation", "invoice", 
    # "iron", "irony", "islander", "item", "jail", "jelly", "jeopardy", "joke", "journal", 
    # "judge", "jury", "keg", "kerchief", "kerosene", "kettle", "kindness", "kine", "kiss", 
    # "knowledge", "labyrinth", "lad", "landscape", "lark", "law", "lawn", "leaflet", "lecture", 
    # "lecturer", "leggings", "legislation", "lemon", "lemonade", "leopard", "letter", 
    # "letterhead", "library", "lice", "limb", "lime", "limelight", "lip", "lobster", "locker", 
    # "loquacity", "lord", "lubricant", "lump", "macaroni", "machine", "madness", "magazine", 
    # "magnitude", "maiden", "majority", "maker", "malady", "malaria", "malice", "mammal", 
    # "management", "mantle", "market", "mast", "master", "mastery", "material", "mathematics", 
    # "meadow", "meat", "medallion", "meeting", "menace", "mercy", "metal", "metropolis", 
    # "microscope", "mileage", "miracle", "mirage", "mischief", "misconception", "misery", 
    # "missile", "molecule", "moment", "monarch", "money", "monk", "month", "mood", "moral", 
    # "morgue", "mosquito", "moss", "mother", "mountain", "mucus", "mule", "multiplication", 
    # "murder", "musician", "nail", "namesake", "necessity", "nectar", "nephew", "newspaper", 
    # "nightfall", "nonsense", "noose", "northwest", "nun", "nursery", "nutmeg", "nymph", 
    # "oats", "obedience", "obsession", "occasion", "odor", "officer", "offshoot", "onslaught", 
    # "opinion", "opium", "orchestra", "origin", "originator", "osculation", "outcome", 
    # "outsider", "owner", "ownership", "oxygen", "pacifism", "pact", "painter", "palace", 
    # "panic", "panorama", "party", "parity", "passageway", "passion", "patent", "peacemaker", 
    # "peach", "pelt", "pencil", "pep", "pepper", "perception", "performer", "periodical", 
    # "perjury", "permission", "person", "phantom", "photograph", "physician", "pianist", 
    # "pipe", "piston", "plain", "plank", "plant", "pleasure", "pledge", "pole", "policeman", 
    # "pollution", "portal", "portrait", "poster", "potato", "poverty", "power", "prairie", 
    # "present", "pressure", "prestige", "priest", "prison", "prisoner", "procession", 
    # "product", "profession", "professor", "profile", "promotion", "property", "proprietor", 
    # "prosecutor", "prosperity", "pudding", "pupil", "python", "quality", "quantity", "quest", 
    # "railroad", "rating", "rattle", "reaction", "recital", "recognition", "reflection", 
    # "reflex", "refrigerator", "reminder", "rendezvous", "replacement", "reptile", "research", 
    # "residue", "restaurant", "retailer", "revolt", "revolver", "rhapsody", "rheumatism", 
    # "ritual", "river", "rock", "rod", "rosin", "rubble", "sadness", "safety", "salad", 
    # "salary", "saloon", "salutation", "salute", "satire", "sauce", "savant", "scarlet", 
    # "science", "scorpion", "sea", "season", "seat", "sensation", "sentiment", "serf", 
    # "series", "session", "settlement", "settler", "shadow", "sheepskin", "ship", "shock", 
    # "shore", "shotgun", "shriek", "sickness", "silence", "simile", "situation", "skillet", 
    # "sky", "slave", "slipper", "slush", "snake", "sobriety", "socialist", "soil", "sonata", 
    # "sovereign", "speakeasy", "speaker", "speech", "spire", "spirit", "spray", "spree", 
    # "square", "stagecoach", "stain", "star", "steam", "steamer", "steerage", "stone", 
    # "storeroom", "storm", "strawberry", "street", "strength", "string", "stub", "student", 
    # "style", "substitute", "subtraction", "suds", "sugar", "sulphur", "sultan", "sunburn", 
    # "sunset", "supplication", "suppression", "surtax", "swamp", "table", "tablespoon", 
    # "tank", "teacher", "temerity", "tempest", "temple", "tendency", "theologian", "thicket", 
    # "thief", "thistledown", "thorn", "ticket", "tidbit", "timepiece", "toast", "tobacco", 
    # "tomahawk", "tomb", "tool", "tower", "toy", "traction", "tragedy", "tree", "trellis", 
    # "tribute", "tripod", "troops", "trouble", "truce", "truck"]
    # '''
    
#     client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"))

#     model = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         model="mixtral-8x7b-32768",
#     )

#     response = model.choices[0].message.content
#     print(response)

#     try:
#         # parsed_list = response.strip().split()
#         parsed_list = ast.literal_eval(response)
#         print(f"Generated Word List: {parsed_list}")

#         return parsed_list
#         # return parsed_list
#     except (SyntaxError, ValueError) as e:
#         print(f"Error parsing the generated list: {e}")
#         return []

# def process_recognized(target_list, recognized_text):
#     count_not_recalled = len(target_list)
#     recognized_words = set(recognized_text.lower().split())  # Convert to set to remove duplicates
#     target_words = set(word.lower() for word in target_list)

#     print("Recognized Words (After Removing Duplicates):")
#     print(" ".join(sorted(recognized_words)))

#     print("\nTarget Word List:")
#     print(" ".join(sorted(target_words)))

#     # Track which target words have been matched
#     matched_words = set()

#     for recognized_word in recognized_words:
#         for target_word in target_words:
#             if fuzz.ratio(recognized_word, target_word) >= 70 and target_word not in matched_words:
#                 print(f"Matched: {recognized_word} -> {target_word}")
#                 matched_words.add(target_word)  # Mark the target word as matched
#                 count_not_recalled -= 1
#                 break  # Move to the next recognized word after a match

#     print(f"\nNumber of words not recalled: {count_not_recalled}")

# def main():
#     word_list = generate_word_list()
#     if not word_list:
#         print("Failed to generate word list. Exiting.")
#         return

#     audio_file = record_user_audio()
#     # audio_file = './patient_recording.wav'
#     recognized_text = recognize_speech_from_file(audio_file)
    
#     if recognized_text:
#         process_recognized(word_list, recognized_text)
#     else:
#         print("No text was recognized. Please try again.")

# if __name__ == "__main__":
#     main()


import os
import google.generativeai as genai
import dotenv
import ast
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from transformers import pipeline
from groq import Groq
import re
from metaphone import doublemetaphone
from Levenshtein import distance as levenshtein_distance

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

def generate_word_list():
    dotenv.load_dotenv()
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = '''Generate a list of 10 High Imagery Nouns. Give me the words in a python list.
    The list of words is to be given to an Alzheimer's patient for ADAS COG Word Recall Task.
    Do not give anything else in the output.
    This is how the output should look like:
        [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10]

    You can select 10 words at random from the following list, or generate similar words

    Word List that can be used for reference:
    [
    "abagment", "abyss", "acrobat", "action", "actor", "admiration", "affection", "anarchy", 
    "animal", "antelope", "anxiety", "appk", "asparaps", "attribute", "baby", "badger", 
    "banana", "bath", "beauty", "beetle", "boat", "box", "bronze", "brotherhood", "brugt", 
    "buffalo", "bullet", "butter", "butterfly", "cabbage", "cake", "campus", "candy", 
    "cannon", "canyon", "captive", "curot", "cashmere", "charm", "cherry", "child", 
    "Chile", "chisel", "church", "cider", "city", "clemency", "cloak", "club", "coat", 
    "committee", "controversy", "course", "coyote", "crater", "cracker", "daisy", "danger", 
    "day", "debate", "decay", "delerium", "demon", "depth", "devotion", "dignity", "disease", 
    "doctor", "donkey", "door", "dress", "eagle", "elephant", "emotion", "faith", "fame", 
    "farmer", "fear", "figment", "fig", "fog", "foot", "frune", "fraud", "freedom", "fruit", 
    "furnace", "garden", "gardenia", "gove", "goat", "gorilla", "government", "grasshopper", 
    "grief", "guns", "hair", "hammer", "hand", "harness", "harp", "hat", "hate", "health", 
    "height", "hill", "hunt", "hog", "hope", "horse", "hunger", "ignorance", "income", 
    "India", "infection", "jacket", "jealousy", "joy", "judgment", "juggler", "justice", 
    "king", "knee", "knife", "knuckle", "lake", "lamb", "lamp", "larceny", "lawyer", 
    "length", "lettuce", "liberty", "life", "link", "lion", "liquor", "lock", "love", 
    "loyalty", "marriage", "martyr", "maturity", "mechanic", "memory", "method", "Mexico", 
    "milk", "mind", "miner", "minister", "minute", "monkey", "moon", "moth", "motion", 
    "music", "muskrat", "nation", "need", "nurg", "nuts", "ocean", "oil", "ounce", "oven", 
    "owl", "panther", "pants", "paper", "patriot", "peace", "pen", "philosopher", "piano", 
    "picture", "pistol", "pity", "pliers", "poet", "politician", "popularity", "position", 
    "prayer", "preview", "proxy", "queen", "rabbit", "religion", "repentance", "roar", 
    "robbery", "scissors", "scout", "shame", "shape", "sheep", "silk", "skin", "sleep", 
    "sofa", "soldier", "soul", "sound", "spider", "stream", "strife", "stomach", "stool", 
    "stove", "success", "sweater", "sword", "symphony", "theory", "thirst", "thought", 
    "thumb", "time", "tin", "train", "trout", "trumpet", "truth", "tunnel", "turnip", 
    "uniform", "unit", "ukulele", "valley", "vase", "violin", "want", "warning", "wasp", 
    "water", "weight", "whiskey", "whistle", "width", "window", "wolf", "zebra", "abbess", 
    "abdication", "abdomen", "abduction", "aberration", "ability", "abode", "accordion", 
    "adage", "admiral", "advantage", "adversity", "advice", "afterlife", "agility", "agony", 
    "agreement", "air", "alcohol", "algebra", "alimony", "allegory", "alligator", "ambulance", 
    "amount", "amour", "amplifier", "anecdote", "anger", "angle", "animosity", "ankle", 
    "answer", "antitoxin", "appearance", "apple", "appliance", "aptitude", "arbiter", "arm", 
    "armadillo", "army", "array", "arrow", "artist", "assault", "athletics", "atmosphere", 
    "atrocity", "attendant", "attitude", "author", "automobile", "avalanche", "avenue", 
    "background", "bacteria", "bagpipe", "banality", "bandit", "banker", "banner", "bar", 
    "bard", "baron", "barrel", "basement", "beast", "beaver", "beggar", "belfry", "belief", 
    "belongings", "bereavement", "betrayal", "beverage", "bivouac", "blacksmith", "blandness", 
    "blasphemy", "blessing", "blister", "blood", "bloom", "blossom", "blunderbuss", "board", 
    "body", "book", "boredom", "bosom", "boss", "bottle", "boulder", "bouquet", "bowl", 
    "boy", "brain", "brassiere", "bravery", "breast", "breeze", "brutality", "brute", 
    "buffoon", "builder", "building", "bungalow", "busybody", "butcher", "cabin", 
    "camouflage", "camp", "candidate", "cane", "capacity", "car", "caravan", "cash", "cat", 
    "caterpillar", "cattle", "causality", "cell", "cellar", "centennial", "cerebrum", 
    "ceremony", "chair", "chance", "chaos", "charlatan", "charter", "chasm", "chief", "chin", 
    "chloride", "Christmas", "cigar", "circle", "circuit", "citation", "claw", "cleanness", 
    "clock", "cobblestone", "code", "coffee", "coin", "college", "colony", "combustion", 
    "comedy", "comforter", "comparison", "competence", "competition", "comrade", "comradeship", 
    "concept", "confidence", "connoisseur", "conquest", "contents", "context", "contract", 
    "contribution", "convention", "cooperation", "copybook", "cord", "core", "corn", "corner", 
    "corpse", "cost", "costume", "cottage", "cotton", "courtship", "cowhide", "cradle", 
    "crag", "cranium", "creator", "creature", "crime", "crisis", "criterion", "cuisine", 
    "custom", "daffodil", "dalliance", "damsel", "dawn", "daybreak", "daylight", "death", 
    "debacle", "deceit", "decoration", "decree", "deduction", "deed", "dell", "deluge", 
    "democracy", "destruction", "determination", "detonation", "development", "devil", 
    "diamond", "direction", "dirt", "disaster", "discipline", "disclosure", "disconnection", 
    "discovery", "discretion", "disparity", "disposition", "distinction", "distraction", 
    "disturber", "doll", "dollar", "domicile", "doorman", "dove", "drama", "dream", "dreamer", 
    "dummy", "dust", "duty", "dweller", "dynasty", "earth", "eccentricity", "economy", 
    "edifice", "edition", "effort", "ego", "elaboration", "elbow", "emancipation", 
    "embezzlement", "emergency", "emporium", "encephalon", "encore", "engagement", "engine", 
    "ensemble", "enterprise", "episode", "epistle", "equity", "errand", "evangelist", "event", 
    "evidence", "exactitude", "examination", "exclusion", "excuse", "exertion", "exhaust", 
    "exhaustion", "explanation", "expression", "extermination", "fabric", "facility", "fact", 
    "factory", "falconer", "fallacy", "fantasy", "fate", "fatigue", "fault", "feline", 
    "festivity", "feudalism", "fiord", "fire", "fireplace", "firmament", "fisherman", "flag", 
    "flesh", "flexibility", "flood", "flower", "foam", "foible", "folly", "footwear", 
    "forehead", "forest", "forethought", "fork", "form", "formation", "fortune", "fowl", 
    "fox", "franchise", "friction", "friend", "frog", "frontage", "fun", "functionary", 
    "fur", "furniture", "gadfly", "gaiety", "galaxy", "gallery", "garments", "garret", 
    "geese", "gem", "gender", "genius", "ghost", "gift", "gilt", "gingham", "girl", "gist", 
    "glacier", "glory", "glutton", "goblet", "goddess", "gold", "golf", "gore", "graduation", 
    "grandmother", "grass", "gravity", "greed", "green", "guardhouse", "gymnastics", 
    "habitation", "hairpin", "hall", "hamlet", "hankering", "happiness", "hardship", 
    "hardwood", "hatred", "headlight", "headquarters", "hearing", "heaven", "henchman", 
    "heredity", "heroism", "hide", "hierarchy", "hillside", "hindrance", "hint", "history", 
    "home", "homicide", "honeycomb", "honor", "hoof", "horsehair", "hospital", "hostage", 
    "hostility", "hotel", "hound", "hour", "house", "humor", "hurdle", "hurricane", 
    "hypothesis", "icebox", "idea", "idiom", "illusion", "immunity", "impact", "impotency", 
    "impropriety", "impulse", "inanity", "incident", "inclemency", "increment", "inducement", 
    "industry", "inebriety", "infant", "infirmary", "ingratitude", "inhabitant", "injury", 
    "ink", "inn", "insect", "insolence", "instance", "institute", "instructor", "instrument", 
    "intellect", "interest", "interim", "interview", "intimate", "investigation", "invoice", 
    "iron", "irony", "islander", "item", "jail", "jelly", "jeopardy", "joke", "journal", 
    "judge", "jury", "keg", "kerchief", "kerosene", "kettle", "kindness", "kine", "kiss", 
    "knowledge", "labyrinth", "lad", "landscape", "lark", "law", "lawn", "leaflet", "lecture", 
    "lecturer", "leggings", "legislation", "lemon", "lemonade", "leopard", "letter", 
    "letterhead", "library", "lice", "limb", "lime", "limelight", "lip", "lobster", "locker", 
    "loquacity", "lord", "lubricant", "lump", "macaroni", "machine", "madness", "magazine", 
    "magnitude", "maiden", "majority", "maker", "malady", "malaria", "malice", "mammal", 
    "management", "mantle", "market", "mast", "master", "mastery", "material", "mathematics", 
    "meadow", "meat", "medallion", "meeting", "menace", "mercy", "metal", "metropolis", 
    "microscope", "mileage", "miracle", "mirage", "mischief", "misconception", "misery", 
    "missile", "molecule", "moment", "monarch", "money", "monk", "month", "mood", "moral", 
    "morgue", "mosquito", "moss", "mother", "mountain", "mucus", "mule", "multiplication", 
    "murder", "musician", "nail", "namesake", "necessity", "nectar", "nephew", "newspaper", 
    "nightfall", "nonsense", "noose", "northwest", "nun", "nursery", "nutmeg", "nymph", 
    "oats", "obedience", "obsession", "occasion", "odor", "officer", "offshoot", "onslaught", 
    "opinion", "opium", "orchestra", "origin", "originator", "osculation", "outcome", 
    "outsider", "owner", "ownership", "oxygen", "pacifism", "pact", "painter", "palace", 
    "panic", "panorama", "party", "parity", "passageway", "passion", "patent", "peacemaker", 
    "peach", "pelt", "pencil", "pep", "pepper", "perception", "performer", "periodical", 
    "perjury", "permission", "person", "phantom", "photograph", "physician", "pianist", 
    "pipe", "piston", "plain", "plank", "plant", "pleasure", "pledge", "pole", "policeman", 
    "pollution", "portal", "portrait", "poster", "potato", "poverty", "power", "prairie", 
    "present", "pressure", "prestige", "priest", "prison", "prisoner", "procession", 
    "product", "profession", "professor", "profile", "promotion", "property", "proprietor", 
    "prosecutor", "prosperity", "pudding", "pupil", "python", "quality", "quantity", "quest", 
    "railroad", "rating", "rattle", "reaction", "recital", "recognition", "reflection", 
    "reflex", "refrigerator", "reminder", "rendezvous", "replacement", "reptile", "research", 
    "residue", "restaurant", "retailer", "revolt", "revolver", "rhapsody", "rheumatism", 
    "ritual", "river", "rock", "rod", "rosin", "rubble", "sadness", "safety", "salad", 
    "salary", "saloon", "salutation", "salute", "satire", "sauce", "savant", "scarlet", 
    "science", "scorpion", "sea", "season", "seat", "sensation", "sentiment", "serf", 
    "series", "session", "settlement", "settler", "shadow", "sheepskin", "ship", "shock", 
    "shore", "shotgun", "shriek", "sickness", "silence", "simile", "situation", "skillet", 
    "sky", "slave", "slipper", "slush", "snake", "sobriety", "socialist", "soil", "sonata", 
    "sovereign", "speakeasy", "speaker", "speech", "spire", "spirit", "spray", "spree", 
    "square", "stagecoach", "stain", "star", "steam", "steamer", "steerage", "stone", 
    "storeroom", "storm", "strawberry", "street", "strength", "string", "stub", "student", 
    "style", "substitute", "subtraction", "suds", "sugar", "sulphur", "sultan", "sunburn", 
    "sunset", "supplication", "suppression", "surtax", "swamp", "table", "tablespoon", 
    "tank", "teacher", "temerity", "tempest", "temple", "tendency", "theologian", "thicket", 
    "thief", "thistledown", "thorn", "ticket", "tidbit", "timepiece", "toast", "tobacco", 
    "tomahawk", "tomb", "tool", "tower", "toy", "traction", "tragedy", "tree", "trellis", 
    "tribute", "tripod", "troops", "trouble", "truce", "truck"]
    '''
    
    model = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",
    )

    response = model.choices[0].message.content
    print(response)

    try:
        parsed_list = ast.literal_eval(response)
        if len(parsed_list)>10:
            parsed_list=parsed_list[:10]
        print(f"Generated Word List: {parsed_list}")
        return parsed_list
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing the generated list: {e}")
        return []

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
    word_list = generate_word_list()
    if not word_list:
        print("Failed to generate word list. Exiting.")
        return

    audio_file = record_user_audio()
    recognized_text = recognize_speech_from_file(audio_file)
    
    if recognized_text:
        process_recognized(word_list, recognized_text)
    else:
        print("No text was recognized. Please try again.")

if __name__ == "__main__":
    main()
# import datetime

# def get_input(prompt):
#     return input(prompt).strip()

# def check_date(answer):
#     today = datetime.date.today()
#     try:
#         answer_date = datetime.datetime.strptime(answer, "%Y-%m-%d").date()
#         return abs((answer_date - today).days) <= 1
#     except ValueError:
#         return False

# def check_time(answer):
#     now = datetime.datetime.now()
#     try:
#         answer_time = datetime.datetime.strptime(answer, "%H:%M").time()
#         diff = datetime.timedelta(hours=abs(now.hour - answer_time.hour), 
#                                   minutes=abs(now.minute - answer_time.minute))
#         return diff <= datetime.timedelta(hours=1)
#     except ValueError:
#         return False

# def check_season(answer):
#     today = datetime.date.today()
#     month = today.month
#     day = today.day
    
#     seasons = {
#         "spring": (3, 20, 6, 20),
#         "summer": (6, 21, 9, 22),
#         "fall": (9, 23, 12, 20),
#         "autumn": (9, 23, 12, 20),
#         "winter": (12, 21, 3, 19)
#     }
    
#     current_season = None
#     for season, (start_month, start_day, end_month, end_day) in seasons.items():
#         if (month > start_month or (month == start_month and day >= start_day)) and \
#            (month < end_month or (month == end_month and day <= end_day)):
#             current_season = season
#             break
    
#     if current_season in ["fall", "autumn"] and answer.lower() in ["fall", "autumn"]:
#         return True
    
#     return answer.lower() == current_season

# def run_orientation_test():
#     questions = [
#         ("What is your full name?", lambda x: True),  # Always correct as we can't verify
#         ("What day of the week is it?", lambda x: x.lower() == datetime.datetime.now().strftime("%A").lower()),
#         ("What is today's date? (YYYY-MM-DD)", check_date),
#         ("What month is it?", lambda x: x.lower() == datetime.datetime.now().strftime("%B").lower()),
#         ("What year is it?", lambda x: x == str(datetime.datetime.now().year)),
#         ("What season is it?", check_season),
#         ("What time is it now? (HH:MM in 24-hour format)", check_time),
#         ("Where are we now? (Name of hospital, clinic, or professional building)", lambda x: True)  # Always correct as we can't verify
#     ]

#     score = 0
#     for question, validator in questions:
#         answer = get_input(f"{question} ")
#         if not validator(answer):
#             score += 1
#             print("Incorrect.")
#         else:
#             print("Correct.")

#     print(f"\nTest completed. Score: {score} (lower is better, maximum incorrect = 8)")

# if __name__ == "__main__":
#     print("ADAS Cog Orientation Task")
#     print("-------------------------")
#     run_orientation_test()

import datetime
import speech_recognition as sr

def get_speech_input(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.strip()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return get_speech_input(prompt)
        except sr.RequestError:
            print("There was an error with the speech recognition service. Please type your answer.")
            return input("Your answer: ").strip()

def check_date(answer):
    today = datetime.date.today()
    try:
        answer_date = datetime.datetime.strptime(answer, "%Y-%m-%d").date()
        return abs((answer_date - today).days) <= 1
    except ValueError:
        return False

def check_time(answer):
    now = datetime.datetime.now()
    try:
        answer_time = datetime.datetime.strptime(answer, "%H:%M").time()
        diff = datetime.timedelta(hours=abs(now.hour - answer_time.hour), 
                                  minutes=abs(now.minute - answer_time.minute))
        return diff <= datetime.timedelta(hours=1)
    except ValueError:
        return False

def check_season(answer):
    today = datetime.date.today()
    month = today.month
    day = today.day
    
    seasons = {
        "spring": (3, 20, 6, 20),
        "summer": (6, 21, 9, 22),
        "fall": (9, 23, 12, 20),
        "autumn": (9, 23, 12, 20),
        "winter": (12, 21, 3, 19)
    }
    
    current_season = None
    for season, (start_month, start_day, end_month, end_day) in seasons.items():
        if (month > start_month or (month == start_month and day >= start_day)) and \
           (month < end_month or (month == end_month and day <= end_day)):
            current_season = season
            break
    
    if current_season in ["fall", "autumn"] and answer.lower() in ["fall", "autumn"]:
        return True
    
    return answer.lower() == current_season

def run_orientation_test():
    questions = [
        ("Please state your full name.", lambda x: True, "Speak your first and last name clearly."),
        ("What day of the week is it?", lambda x: x.lower() == datetime.datetime.now().strftime("%A").lower(), "Say the full name of the day, like 'Monday' or 'Tuesday'."),
        ("What is today's date?", check_date, "Say the date in the format: year, month, day. For example, '2024, September, 23'."),
        ("What month is it?", lambda x: x.lower() == datetime.datetime.now().strftime("%B").lower(), "Say the full name of the month, like 'September' or 'October'."),
        ("What year is it?", lambda x: str(datetime.datetime.now().year) in x, "Say the full year, like '2024'."),
        ("What season is it?", check_season, "Say either 'Spring', 'Summer', 'Fall' (or 'Autumn'), or 'Winter'."),
        ("What time is it now?", check_time, "Say the time in hours and minutes, like '2:30' or '14:30'."),
        ("Where are we now?", lambda x: True, "Say the name of the hospital, clinic, or professional building you're in.")
    ]

    print("\nWelcome to the ADAS Cog Orientation Task.")
    print("I will ask you a series of questions about time and place.")
    print("Please answer each question to the best of your ability.")
    print("If you need me to repeat a question, just say 'repeat'.")
    print("Let's begin!\n")

    score = 0
    for question, validator, instruction in questions:
        while True:
            answer = get_speech_input(f"{question}\n{instruction}")
            if answer.lower() == 'repeat':
                continue
            if not validator(answer):
                score += 1
                print("I'm afraid that's not correct.")
            else:
                print("That's correct.")
            break

    print(f"\nTest completed. Score: {score} (lower is better, maximum incorrect = 8)")

if __name__ == "__main__":
    print("ADAS Cog Orientation Task")
    print("-------------------------")
    run_orientation_test()
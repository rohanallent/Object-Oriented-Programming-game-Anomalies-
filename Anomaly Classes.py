import time
import random

questions = {1: "Where have you come from?",
             2: "Why should I let you in?",
             3: "Have you noticed anything unusual about yourself lately?",
             4: "Where were you when the first outbreak occurred?",
             5: "Is there anyone waiting for you inside?"}

#_____________________________________________________________
# Individual parent class
#_____________________________________________________________

class Individual:
    # All anomaly definitions.
    ANOMALIES = {1: "Delayed Speech",
        2: "Unusual Pallor",
        3: "Irregular Breathing",
        4: "Irregular Tremors",
        5: "Speech Impediment",
        6: "Inappropriate Responses"}

    # Initializing code for each subclass/object
    def __init__(self,
        name,
        backstory,
        appearance,
        dialogues,
        anomaly_id=None):
        self.name = name
        self.backstory = backstory
        self.appearance = appearance
        self.dialogues = dialogues
        self.anomaly_id = anomaly_id

        self.asked_questions = set()
        self.is_inspected = False

#_____________________________________________________________
# Characters. Define each subclass of individual as each character
#_____________________________________________________________

class Pandemic_Survivor_1(Individual):
    def __init__(self, anomaly_id=None):
        super().__init__(name="Pandemic Survivor 1",
            backstory="A doctor who tried and failed to find a cure.",
            appearance="A traveller who appears to have been travelling for years. They are wearing a worn-out backpack, and have dark circles under their eyes.",
            dialogues={1: "I come from the east, I've been moving from place to place since I left my home. I hope I can finally find a place to stay.",
                2: "I don't have a lot to offer, I just need a shelter to stay in.",
                3: "I've been feeling tired lately, but I guess that's normal when you've been walking for days.",
                4: " In my hometown, everybody was living so peacefully, it was a rather quiet place in the countryside, but everything just fell apart so quickly.",
                5: "Not that I know of, but hopefully I can find somebody I know in there"
            }, anomaly_id=anomaly_id)

class Walang_Pagkain_Buseng(Individual):
    pass

class Doctor(Individual):
    pass

#_____________________________________________________________
# Functions / Methods para sa individuals (Sila Ten n dito)
#_____________________________________________________________

START_SANITY = 100
ACTION_COST = 5
WRONG_GUESS_COST = 20

def answer_question(self, question_id):
    if question_id not in self.dialogues:
        return "Invalid question."

    if question_id in self.asked_questions:
        return "You have already asked this question."

    self.asked_questions.add(question_id)
    response = self.dialogues[question_id]

    # Apply a dialogue anomaly when appropriate.
    if self.anomaly_id == 1:
        time.sleep(3)

    elif self.anomaly_id == 3:
        pass

    elif self.anomaly_id == 4:
        pass

    elif self.anomaly_id == 5:
        pass

    elif self.anomaly_id == 6:
        pass

    return response

def inspect_appearance(self):
    self.is_inspected = True
    description = self.appearance

    # Apply physical anomaly descriptions when appropriate.
    if self.anomaly_id == 2:
        description += " Their skin is unusually pale."

    elif self.anomaly_id == 4:
        pass

    return description

def get_anomaly_name(self):
    if self.anomaly_id is None:
        return "No anomaly"

    return self.ANOMALIES.get(self.anomaly_id, "Unknown anomaly")

def generate_level_characters():
    return random.sample(range(1, 21), 10)

def talk_to_character(char):
    for number, question in questions.items(): 
        print(f"{number}. {question}")

    choice = input("Ask which question? ")

    if choice.isdigit():
        print(answer_question(char, int(choice)))
    else:
        print("Invalid question.")

def guess_anomaly(person, sanity):
    if (input("Is the character an anomaly? (y/n)") == "y") == (person.anomaly_id is not None):
        print("Correct.")
        return sanity

    print("Wrong guess!") # if wrong guess
    return sanity - WRONG_GUESS_COST

def character_encounter(self):
    print("\nAN ANOMALY APPROACHES YOU")
    print(self.appearance)

    while sanity > 0:
        print(f"\nSanity: {sanity}")
        print("1. Inspect their body")
        print("2. Talk to them")
        print("3. Make your decision")
        choice = input("> ")

        if choice == "1":
            print(inspect_appearance(person))
            sanity -= ACTION_COST

        elif choice == "2":
            talk_to_character(person)
            sanity -= ACTION_COST

        elif choice == "3":
            return guess_anomaly(person, sanity)

        else:
            print("Invalid choice.")

def play_game(characters):
    sanity = START_SANITY

    for level, person in enumerate(characters, start=1):
        print(f"Level {level}")  # level 1-10
        sanity = character_encounter(person, sanity)

        if sanity <= 0:
            print("You lose (No sanity left).")
            return

    print(f"You win!")

# Test dito:
question = questions[1]
person = Pandemic_Survivor_1(anomaly_id=1)

print(question)
print("\nPandemic Survivor 1:")
print(person.answer_question(1))
print("\nAnomly type:")
print(person.get_anomaly_name())
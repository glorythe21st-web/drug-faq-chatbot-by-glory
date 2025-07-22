import json
from fuzzywuzzy import fuzz, process

def load_intents(file_path="intents.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def load_drug_list(file_path="drug_list.txt"):
    with open(file_path, "r") as file:
        return [line.strip().lower() for line in file.readlines()]

def extract_drug(user_input, drug_list, threshold=80):
    match, score = process.extractOne(user_input.lower(), drug_list, scorer=fuzz.partial_ratio)
    return match if score >= threshold else None

def detect_intent(user_input):
    input_lower = user_input.lower()
    if any(word in input_lower for word in ["dose", "dosage", "how much", "take"]):
        return "dosage"
    elif any(word in input_lower for word in ["side effect", "reaction", "adverse"]):
        return "side_effects"
    elif any(word in input_lower for word in ["interaction", "combine", "mix"]):
        return "interactions"
    else:
        return "unknown"

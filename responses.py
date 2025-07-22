import random

def fallback_response():
    responses = [
        "Sorry, I didn't understand. Could you rephrase that?",
        "I'm not sure how to answer. Try asking differently.",
        "Hmm, I don't have that info yet. Try again?"
    ]
    return random.choice(responses)

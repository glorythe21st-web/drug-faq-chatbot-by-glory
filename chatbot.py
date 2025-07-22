import random
from utils import load_intents, load_drug_list, detect_intent, extract_drug

def main():
    print("💊 Drug FAQ Chatbot (CLI) by Glory 💊")
    print("Type 'exit' to quit.\n")

    intents = load_intents()
    drug_list = load_drug_list()

    while True:
        user_input = input("👤 You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye! Stay safe.")
            break

        intent_tag = detect_intent(user_input)
        drug = extract_drug(user_input, drug_list)

        intent_data = next((i for i in intents["intents"] if i["tag"] == intent_tag), None)

        if intent_data:
            response_template = random.choice(intent_data["responses"])
            if "{drug}" in response_template:
                if drug:
                    response = response_template.format(drug=drug.title())
                else:
                    response = "Please specify the drug name you're referring to."
            else:
                response = response_template
        else:
            response = "Sorry, I don't understand that yet."

        print("🤖 Bot:", response)

if __name__ == "__main__":
    main()

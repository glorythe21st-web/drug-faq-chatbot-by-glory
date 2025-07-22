```markdown
 💊 Drug FAQ Chatbot (CLI Version) by Glory

An intelligent command-line chatbot that answers drug-related questions using real-time logic and natural language processing (NLP). Built with Python and designed to assist users with basic drug FAQs such as dosage, use cases, and side effects.

 🚀 Features

- ✅ Command-line interface (CLI)
- ✅ Real-time question parsing using keyword detection
- ✅ Automatic drug name extraction (NLP-based)
- ✅ Smart fallback responses for unmatched queries
- ✅ Logs conversation history (`chat_log.txt`)
- ✅ Tracks usage analytics (`analytics.csv`)
- ✅ Easy-to-extend intents and responses via `intents.json`

 🛠️ Technologies Used

- Python 3.11+
- FuzzyWuzzy
- JSON-based intent handling
- Python logging module

 📂 Project Structure

```

drug-faq-chatbot/
├── chatbot.py
├── intents.json
├── drug\_list.txt
├── utils.py
├── responses.py
├── logger.py
├── chat\_log.txt
├── analytics.csv
├── requirements.txt
└── README.md

````

 🧪 How to Run

1. Clone the repo
   ```bash
   git clone https://github.com/glorythe21st-web/drug-faq-chatbot-by-glory.git
   cd drug-faq-chatbot-by-glory
````

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. *Run the chatbot*

   ```bash
   python chatbot.py
   ```

# 🔍 Sample Usage

```
💊 Drug FAQ Chatbot (CLI) by Glory 💊
Type 'exit' to quit.

👤 You: What is the dose of paracetamol for adults?
🤖 Bot: Searching...
🤖 Bot: The recommended dose of paracetamol for adults is 500mg to 1000mg every 4-6 hours.
```

# 📈 Logging & Analytics

* `chat_log.txt` – Full conversations
* `analytics.csv` – Structured usage tracking

# 🏷️ Release Info

* **Version:** 1.0.0
* **Release Date:** July 2025
* **Status:** Initial CLI version released

# 🔄 Future Plans

* 🌐 API integration (RxNav, OpenFDA)
* 🖼️ GUI (Tkinter)
* 🤖 Memory and context
* 🌍 Multilingual support
* 🧠 Enhanced NLP with spaCy or LLMs

# 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

# 📄 License

MIT License

# 👩‍💻 Author

**Joseph Glory Mamani**
[https://github.com/glorythe21st-web](https://github.com/glorythe21st-web)


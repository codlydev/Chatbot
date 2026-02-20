# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import logging

# # Enable logging for better debugging
# logging.basicConfig(level=logging.INFO)

# # Create and configure chatbot
# chatbot = ChatBot(
#     "AI Assistant",
#     storage_adapter="chatterbot.storage.SQLStorageAdapter",
#     database_uri="sqlite:///chatbot.sqlite3",
#     logic_adapters=[
#         {
#             "import_path": "chatterbot.logic.BestMatch",
#             "default_response": "Sorry, I don't understand that. Can you rephrase?",
#             "maximum_similarity_threshold": 0.8
#         }
#     ]
# )

# # Train the chatbot using English language corpus
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.english")

# print("🤖 Chatbot is ready! Type 'exit' to stop.\n")

# # Chat loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye! 👋")
#         break
#     response = chatbot.get_response(user_input)
#     print(f"Chatbot: {response}")


from transformers import pipeline

# Load pre-trained chatbot model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

print("🤖 AI Chatbot is ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    # Generate response
    response = chatbot(user_input, max_length=10000, do_sample=True)
    bot_reply = response[0]['generated_text']

    print(f"Chatbot: {bot_reply}")

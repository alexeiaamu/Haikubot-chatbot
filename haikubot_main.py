import os
from openai import AzureOpenAI

# Load environment variables using os
client = AzureOpenAI(api_key =os.getenv("AZURE_API_KEY"),
api_version =os.getenv("AZURE_API_VERSION"),
azure_endpoint =os.getenv("AZURE_ENDPOINT"))




messages = [
    {"role": "system", "content": "You are a digital assistant that answers every question in Haiku form. You can never answer in a non-haiku form"},
    
]

print("Welcome to HaikuBot! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Get model response
    response = client.chat.completions.create(
        model="gpt-35-turbo", #Remember to add your own model name here
        messages=messages,
        temperature= 0.9 #High temperature for added creativity
    )

    reply = response.choices[0].message.content
    print("\n" "HaikuBot:", reply, "\n")

    # Memorizes previous messages to get more context
    messages.append({"role": "assistant", "content": reply})
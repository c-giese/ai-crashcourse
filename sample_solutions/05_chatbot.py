import json

import requests

# Initialize the conversation with a greeting message
greeting_message = "Hi how can i help you today? To stop the chat, type /bye"
# Store all messages in a list to maintain conversation history
messages = [{"role": "assistant", "content": greeting_message}]
print(greeting_message)

# Main chat loop - continues until user types /bye
while True:
    # Get user input
    user_query = input("You: ")
    # Check if user wants to exit
    if user_query == "/bye":
        print("Assistant: Goodbye!")
        break
    # Add user's message to conversation history
    messages.append({"role": "user", "content": user_query})

    # Configure the API request to the local Ollama server
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "phi3:latest",
        "messages": messages,  # Send entire conversation history for context
        "stream": True,
    }
    # Send POST request with stream=True to receive response in chunks
    response = requests.post(url, json=payload, stream=True)
    if response.status_code == 200:
        fullText = ""  # Accumulate the complete response
        print("Assistant: ", end="", flush=True)
        # Process each line of the streaming response
        for line in response.iter_lines(decode_unicode=True):
            if line:  # Skip empty lines
                # Parse the JSON response
                data = json.loads(line)
                # Extract the content chunk from the message
                chunk = data["message"]["content"]
                # Accumulate chunks to build the full response
                fullText += chunk
                # Print chunk immediately for real-time streaming effect
                print(chunk, end="", flush=True)
                # Add assistant's response to conversation history
                messages.append({"role": "assistant", "content": fullText})
        print()  # Newline after completion
    else:
        print(f"Error: {response.status_code}")

# Build a basic Chat-Application

We want to rebuild the functionality of the command `ollama run` with python. We will implement the features incrementally

1. Send a simple POST-request to your local ollama-server via the `/api/chat`-Route ([API-Definition](https://docs.ollama.com/api#generate-a-chat-completion)). Do not stream the response yet, w.e. stream = false.
2. Make the response look more familiar by activating `stream = True` in the request and the payload. Adapt your print to the new stream.
3. Incorporate basic interactivity by prompting the user for a question that will be answered by the llm. (Use input and a greeting message) Also add a possibility to end the chat.
4. Make this a multi turn conversation, so that the user can ask multiple questions after another.
5. Implement real multi turn interactivity by keeping the context of the conversation. (have a look at the payload, it gives you a hint, where to start.)
6. Implement the same functionality with the ollama module. [Module-Documentation](https://ollama.com/blog/python-javascript-libraries)

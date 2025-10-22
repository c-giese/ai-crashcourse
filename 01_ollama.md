# What is ollama?

Local LLM Runner: Its primary function is to make it easy to download, run, and interact with various open-source large language models directly on your machine, rather than relying solely on cloud-based services. Simplified Setup: Ollama simplifies the often complex process of getting LLMs running locally. It handles tasks like downloading model weights, setting up the necessary environment, and optimizing the models for your hardware.

Model Library: It provides access to a library of popular open-source models that you can easily pull (download) and run with simple commands. Examples include models like Llama 2, Mistral, Gemma, Cohere, and many others.

API and Command Line Interface: Ollama offers both a command-line interface for direct interaction and scripting, and a local API that developers can use to integrate LLMs into their own applications.

Hardware Acceleration: It's designed to leverage hardware acceleration (like GPUs) if available on your system to improve performance, though it can also run models on the CPU.

Customization: It allows users to create, customize, and share their own models using Modelfiles.

In essence, Ollama acts like a server or runtime specifically for running LLMs locally. It democratizes access to powerful AI models, allowing developers and users to experiment, build applications, and run models privately and offline without needing external API calls or complex configurations.

## Steps to use ollama

1. Install ollama from https://ollama.com/
2. Download an run an local model in the terminal with `ollama run <MODEL_NAME>`, e.g. Gemma3:1B. You can chat with the model in the Terminal.
3. Download an run another model, e.g. Phi3:latest
4. Use `ollama list` to see the installed LLMs. You will see, that the sizes differ, does this have any impact on performance or speed?
5. Create your own model! Follow these steps:
   1. Create a file called Modelfile (no filetype!)
   2. Fill the data below into the Modelfile and save it. You can write any system prompt, which defines the character of the model.
   3. In the directory of the Modelfile, run `ollama create <NEW_MODEL_NAME> -f ./Modelfile`
   4. You can now use the Model like any other with `ollama run <NEW_MODEL_NAME>`
   5. Have fun with it 🥳

```
FROM gemma3:1b

PARAMETER temperature 1

SYSTEM """
Your are Master Yoda from Star Wars. Answer like he would.
"""
```

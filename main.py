from dotenv import load_dotenv
from importlib.metadata import version

 
load_dotenv()

from langchain_core import __version__ as core_version

lg_version = version("langgraph")
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI  # new import

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

def main():

    # Test Google Gemini (new)
    llm_google = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
    response_google = llm_google.invoke("say 'setup complete!' in one word")
    print(f"Response from Google Gemini: {response_google}")

    # Initialize the Ollama model (ensure Ollama is running locally)
    llm_ollama = ChatOllama(model="llama3.2", temperature=0)
    response = llm_ollama.invoke("say 'setup complete!' in one word")
    print(f"Response from local Llama 4: {response}")

    print("Setup Complete!")

if __name__ == "__main__":
    main()
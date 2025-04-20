# gem-wrapper
# Gemini Wrapper - Starting with a command line interface, eventually writing a WebUI.
# Study by Ethan P.

import os
from google import genai

def main():

    #Greets user on startup
    print("\n<(^.^)> This is a command line interface for the AI, Gemini. <(^.^)> ")
    print("(Type 'exit' to exit.) ")

    #Store API key,model name, and AI client for future use
    API_KEY = os.environ.get("GEMINI_API_KEY_v2")
    if not API_KEY:
        raise EnvironmentError("GEMINI_API_KEY_v2 environment variable not set. Please set it in your system's environment variables.")
    MODEL_NAME = "gemini-2.0-flash"
    genai_client = genai.Client(api_key=API_KEY)

    first_execution = True

    #Main loop, loops after returning a response or exits the loop to end the program.
    while True:

        if first_execution == True:
            prompt_text = input("\nEnter your prompt: ")
            first_execution = False
        else:
            prompt_text = input("\nIs there anything else you'd like to prompt? ")

        if prompt_text.lower() == "exit":
            print("\nOh... Okay, bye.")
            break

        print(f"\nYou said: \n\"{prompt_text}\"")

        #Interacting with the API


        try: #Error handling

            #Variable 'response' is the AI's response because it is set to a function which evaluates using our supplied data.
            response = genai_client.models.generate_content(
                model = MODEL_NAME,
                contents = prompt_text
                )

            ai_response = response.text

        except Exception as e:
            ai_response = f"Error generating response (f to pay respects): \"{e}\""

        print(f"\nGemini responded: \n\"{ai_response}\" \n")

if __name__ == "__main__":
    main()

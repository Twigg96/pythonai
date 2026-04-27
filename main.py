import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from system_prompt import system_prompt

def main():
    parser = argparse.ArgumentParser(description='Clanker')
    parser.add_argument("user_prompt", type=str, help="Type your shit")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if not api_key:
        raise RuntimeError("Clanker isn't working")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents= messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt),
            )
    if not response.usage_metadata:
        raise RuntimeError("Tokens no work")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:")
        print(response.text)
    else:
        print("Response:")
        print(response.text)





if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from system_prompt import system_prompt
from call_function import available_functions,call_function

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
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt,)
            )
    if not response.usage_metadata:
        raise RuntimeError("Tokens no work")

    function_call_list = []

    if response.function_calls is not None:
        for fc in response.function_calls:
            result = call_function(fc, verbose=args.verbose)

            if not result.parts:
                raise Exception("No parts list")

            if not result.parts[0].function_response:
                raise Exception("There is no function response")

            if not result.parts[0].function_response.response:
                raise Exception("There is no response")
            function_call_list.append(result.parts[0])

            if args.verbose:
                print(f"-> {result.parts[0].function_response.response}")
    else:
        print(response.text)



for i in range(20):
    main()

#if __name__ == "__main__":
#    main()


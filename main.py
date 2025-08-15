import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function, available_functions

from prompts import system_prompt

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("no prompt provided")
        print("usage: python main.py \"your proompt here\"")
        exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt="".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    for i in range(0,20):
      try:
          response = generate_content(client, messages, verbose)
          if response and response.text:
              print(response.text)
              break
      except Exception as e:
          print(f"Caught exception: {e}")

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions]
            )
    )

    for candidate in response.candidates:
        model_message = types.Content(
            role="model",
            parts=candidate.content.parts
        )
        messages.append(model_message)

    if not response.function_calls:
        return response

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    user_message = types.Content(
    role="user",
    parts=function_responses
    )
    messages.append(user_message)

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    return None

if __name__ == "__main__":
    main()

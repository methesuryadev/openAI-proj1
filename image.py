import os
import openai
openai.api_key = "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"
while True:
    # Set up the model and prompt
    model_engine = "text-davinci-003"

    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Generate a response
    completion = openai.Image.create(
        prompt=prompt,
        n=4,
        size="512x512"
    )

    # extracting useful part of response
    # response = completion.choices[0].text
    # printing response
    print(completion["data"][0]["url"])
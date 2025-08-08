import openai

openai.api_key = 'YOUR_API_KEY'

def chat_with_agent(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = chat_with_agent(user_input)
    print("Agent:", response)
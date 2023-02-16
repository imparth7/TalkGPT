import openai # pip install openai
import config

# Add config.py file and write Api = "Your_API_Key"
openai.api_key = config.Api
print("\t\033[44m", "TalkGPT", "\033[0m")

while True:
    print("\t\033[31m")
    ask = input('Question: \n\t')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=1,
        max_tokens=256,
        top_p=1,
        best_of=20,
        frequency_penalty=0.6,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    data = response['choices'][0]['text']
    print("\t\033[32m")
    print(f"Answer: {data}")

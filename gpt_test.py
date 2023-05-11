import openai

openai.api_key = "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"

def ans_ChatGPT(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",#モデル選択
        messages=[{
            "role":"user",
            "content":question,
        }]
    )

    response = completion.choices[0].message.content

    return response

print("chatgotへの質問内容は？")

question = input()

answer = ans_ChatGPT(question)

print(answer)
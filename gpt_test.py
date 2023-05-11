import openai

openai.api_key = "API Keyを入力してください"

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
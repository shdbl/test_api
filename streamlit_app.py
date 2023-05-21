import openai
import os

# 设置 API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,  # 调整此数值以生成不同长度的文本
        n=1,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

prompt = "Translate the following English text to French: '"
generated_text = generate_text(prompt)
print(generated_text)

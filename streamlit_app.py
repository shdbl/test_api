import openai
import os
import streamlit as st

# 设置 API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")
st.write("wait")
def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1000,  # 调整此数值以生成不同长度的文本
        n=1,
        temperature=1,
    )
    return response.choices[0].text.strip()

prompt = st.text_input("请输入一句话:")
generated_text = generate_text(prompt)
st.write(generated_text)

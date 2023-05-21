import openai
import os
import streamlit as st

# 设置 API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_text(prompt, chats):
    # 根据chats构造上下文
    model_engine = "text-davinci-002" # 使用GPT-3.5-turbo模型
    context = f"{''.join(chats)}User: {prompt}"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=context,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    text = response.choices[0].text.strip()
    return text

st.title("GPT3.5上下文对话应用")

user_input = st.text_input("请输入你的问题：")
history = st.session_state.get("history", [])

if st.button("生成回答"):
    if user_input:
        chat_input = f"User: {user_input}\n"
        history.append(chat_input)
        answer = generate_text(user_input, history)
        chat_output = f"GPT-3.5: {answer}\n"
        history.append(chat_output)
        st.session_state.history = history

st.write("聊天记录：")
st.write("".join(history))

# import openai
# import os
import streamlit as st

# # 设置 API 密钥
# openai.api_key = os.getenv("OPENAI_API_KEY")
# st.write("wait")
# def generate_text(prompt):
#     response = openai.Completion.create(
#         model= "gpt-3.5-turbo",
#         prompt=prompt,
#         max_tokens=1000,  # 调整此数值以生成不同长度的文本
#         n=1,
#         temperature=1,
#     )
#     return response.choices[0].text.strip()

# prompt = st.text_input("请输入一句话:")
# generated_text = generate_text(prompt)
# st.write(generated_text)

from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_story(keywords):
    # 加载预训练GPT-2模型
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # 加载GPT-2 tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # 将关键词转化成字符串
    input_text = " ".join(keywords)

    # 对输入文本进行编码
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # 生成提示为给定关键词的样本
    generated_outputs = model.generate(input_ids, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    # 对生成的输出进行解码
    generated_text = tokenizer.decode(generated_outputs[0], skip_special_tokens=True)
    generated_sentences = generated_text.split(". ")

    # 从生成的文本中提取故事
    story = ". ".join(generated_sentences[1:])

    return story


# 使用关键词生成故事：
keywords = ["beach", "sunset", "romance", "adventure", "treasure"]
st.write(generate_story(keywords))

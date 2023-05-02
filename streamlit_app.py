import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('D:/处理后的聊天记录.txt', sep='\t', header=None, names=['sender', 'message'])

from sklearn.feature_extraction.text import CountVectorizer
import jieba

def jieba_tokenizer(text):
    return jieba.lcut(text)

vectorizer = CountVectorizer(tokenizer=jieba_tokenizer)
X=df['message']
X=X.fillna('')
X = vectorizer.fit_transform(X)
y = df['sender']
unique_speakers = list(set(y.values))
speaker_labels = [unique_speakers.index(speaker) for speaker in y.values]

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, speaker_labels, test_size=0.2, random_state=2)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(score)

import re

def remove_bracket_characters(s):
    # 使用正则表达式替换s中的[]和其中的内容
    result = re.sub(r'\[.*?\]', '', s)
    # punctuation='[!@#$%^&*()_+-={}|:"\';<>,，。？！“”：.?/\\\[\]]'
    # result=re.sub(punctuation,'',result)
    return result

def shibie(s):
    new_message = [remove_bracket_characters(s)]
    new_message_transformed = vectorizer.transform(new_message)
    probability = clf.predict_proba(new_message_transformed)[0]
    for i in range(len(unique_speakers)):
        print(unique_speakers[i] + ':'+'{:.2f}%'.format(100*probability[i]))


st.title("发言者检测")

user_input = st.text_input("请输入一句话:")

prob=shibie(user_input)

st.write("发言者概率:")
st.write(prob)

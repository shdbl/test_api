import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 展示文本；文本直接使用Markdown语法
st.markdown("# Streamlit示例")
st.markdown("""
            - 这是
            - 一个
            - 无序列表
            """)

# 展示pandas数据框
if st.checkbox('Show raw data'):
    st.dataframe(pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"]))


# 加入交互控件，如输入框
number = st.number_input("Insert a number", 1)
st.write("输入的数字是：", number)

# 展示matplotlib绘图
fig=plt.figure(figsize=(5,number))
arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
plt.title("matplotlib plot")
st.pyplot(fig)
st.title("Streamlit 手动刷新示例")

if st.button("刷新"):
    st.experimental_rerun()

#
st.title('Streamlit 数学公式示例')

st.markdown(
    r'''
MathJax 可以帮助我们渲染数学公式。 下面是一个公式的例子:

$$
f(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi i \xi x} \,d\xi
$$

你还可以使用行内公式，例如当 $a \ne 0$ 时，二次方程 $ax^2 + bx + c = 0$ 的解为：

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
'''
)

st.title("文件上传示例")

uploaded_file=st.file_uploader("选择一个 CSV 文件",type="csv")

if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.write(data)

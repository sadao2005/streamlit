import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteratin = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteratin.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('問い合わせ内容を書く１')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ内容を書く２')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ内容を書く３')
expander4 = st.expander('問い合わせ４')
expander4.write('問い合わせ内容を書く４')

#img = Image.open('sample.jpg')

# option = st.text_input(
#   'あなたの趣味を教えてください。'
# )
# 'あなたの趣味は、', option, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション', condition



# if st.checkbox('Show Image'):
# st.image(img, caption='Kohei Imanighi', use_column_width=True)


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('Display Image')

st.write('Interactive Widgets')

#st.text_input→動的なテキスト入力ボックスが出る。
text = st.text_input('あなたの趣味を教えてください。')
 
'あなたの趣味は、', text, 'です'
#st.slider→スライダーが出る。 (最小値,最大値,初期値)
Condition = st.slider('あなたの今の調子は!?',0,100,50)
'コンディション:',Condition

#selectbox→プルダウンメニューができる...list(range(1,10))...初期値1で10個の数字を選べる

""" option = st.selectbox(
'あなたが好きな数字を教えてください、',
list(range(1,10))
)
'あなたの好きな数字は、', option, 'です' """

#checkbox→チェックボックスが作られる。 
""" if st.checkbox('Show Image'):
img = Image.open('キャプチャ.PNG')
st.image(img, caption= 'Vanpire Survivers', use_column_width = True) """
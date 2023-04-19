import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

#プログレスバー 0からどんどん増えていく、time0.1秒スリープさせつつ徐々に増える
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done'

#2カラム表示
left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

#押して出てくるやつ
expander1 =  st.expander('問い合わせ1')
expander1.write('問い合わせの回答')

expander2 =  st.expander('問い合わせ2')
expander2.write('問い合わせ内容の回答')

expander3 =  st.expander('問い合わせ3')
expander3.write('問い合わせ内容の回答')




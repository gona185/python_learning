import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('DataFrame') #データフレームと表示させる(pandas)

#df = pd.DataFrame({
#    '1列目': [1, 2, 3, 4],
 
#   '2列目': [10, 20, 30, 40]
#}) #4×4の表を用意する

#用意したデータフレームを格納し表示...width,height指定可能+.style.highlightでハイライトを付ける
#st.dataframe(df.style.highlight_max(axis=0)) 

#staticなテーブルを作成→table インタラクティブなテーブルを作成→dataframe
#st.table(df)

#マジックコマンド 
#""""　マークダウン記法

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
#(20 , 3)の行列を作成し、正規分布の乱数
#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#折れ線グラフ
#st.line_chart(df)

#棒グラフ
#st.bar_chart(df)

#折れ線塗グラフ
#st.area_chart(df)

#lat,lon→緯度経度
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#    columns=['lat', 'lon']
#)
#新宿付近でランダムにマッピング
#st.map(df)

st.write('Display Image')

img = Image.open('キャプチャ.PNG')

st.image(img, caption= 'Vanpire Survivers', use_column_width = True)
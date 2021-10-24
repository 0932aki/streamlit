#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:54:16 2021

@author: OguraMitsuaki
"""

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
# streamlit run main.py で最初の実行

st.title('Streamlit 基礎')
st.write('Display Image')

text = st.text_input('あなたの名前を教えてください')
'あなたの名前は，',text,'です'
condition = st.slider('あなたの今の調子は？',0, 100, 50)#最小値，最大値，スタート位置
'コンディション：',condition
option = st.selectbox(
    '好きな数字を教えてください',
    list(['生活場面','学校場面','地域場面','社会場面'])
)

'あなたが選択したのは，',option,'です'

st.sidebar.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty() #空コンテンツと一緒に変数を作成
bar = st.progress(0)#プログレスを作る　値は０

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')#空のIterationにテキストを入れていく
    bar.progress(i +1)#barの中身をぐいぐい増やしていく
    time.sleep(0.1)

'Done!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

#画像を開く
img = Image.open('room.jpg')
st.image(img, caption='生活場面', use_column_width=True)#use_colum_width実際のwebサイトの横幅に合わせて表示

#表に緯度と経度を入れる
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon',]#lat lon 緯度と経度
)

#緯度と経度から地図に書き込む
st.map(df)

#表にランダムにデータを入れ込む
df = pd.DataFrame(
    np.random.rand(20,3), #２０行３列
    columns = ['a','b','c']
)
#表として表示する
st.table(df.style.highlight_max(axis=0))
#表からグラフ化　bar line area
st.bar_chart(df)


#"""

# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```

#"""
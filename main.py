import streamlit as st
import time


st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'
# st.write('Display Image')

#プログレシバーの表示
latest_iteration = st.empty()  #文字を受ける変数を作成
bar = st.progress(0)  #bar(プログレスバー変数の作成)

for i in range(100): #1から100まで順番にiに格納される
    latest_iteration.text(f'Iteration {i + 1}') 
    bar.progress(i+1)
    time.sleep(0.1)   #0.1秒ごとに処理をする
    
'Done!!'
#プログレスバーが完了したら次の処理に進む

#ツーカラムレイアウトの作成
left_column, right_column = st.columns(2)  #2は「2カラムで」と言う意味
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

#エキスパンダーの作成
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ2')
expander3.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ3')
expander2.write('問い合わせ内容を書く')


#サイドバーの追加方法
# text = st.sidebar.text_input('あなたの趣味は何ですか')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,5)

# 'あなたの趣味:',text,
# 'コンディション:',condition

#セレクトボックスの作成
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

#'あなたが好きな数字は、',option,'です'

#チェックボックスの作成
# if st.checkbox('Show Image'):
#       img = Image.open('IMG_0788.JPG')
#       st.image(img, caption = 'サスケ', use_column_width=True)
    

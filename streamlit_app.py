import streamlit
streamlit.title('Sherlocks Daily routine')
streamlit.header('Morning routine')
streamlit.text('Wake up at 6:00 AM')
streamlit.text('Going to gym')
streamlit.text('Make avocado,banana smoothie')
import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick your fruits:",list(my_fruit_list.index),['Avacado','Kiwifruit','Lemon'])
streamlit.dataframe(my_fruit_list)

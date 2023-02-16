import streamlit
import pandas

streamlit.title("Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥑 menu item 1")
streamlit.text("🐔 menu item 2")
streamlit.text("🥗 menu item 3")

streamlit.header("Build your own fruit smoothie")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


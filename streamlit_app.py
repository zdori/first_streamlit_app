import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥑 menu item 1")
streamlit.text("🐔 menu item 2")
streamlit.text("🥗 menu item 3")

streamlit.header("Build your own fruit smoothie")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(fruit):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information!")
  else:
    res = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(res)
except URLError as e:
  streamlit.error()
    
streamlit.write('The user entered ', fruit_choice)

streamlit.stop()


def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit load list")
    return my_cur.fetchall()

streamlit.header("The fruit load list contains:")
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()  
  streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + add_fruit + "')")
streamlit.write('The user entered ', add_fruit)

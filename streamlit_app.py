# Import python packages
import streamlit as st

# Write directly to the app
st.title(f"My Parents New Healthy Diner")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)
 
from snowflake.snowpark.functions import col
 
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    my_dataframe
)

# if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)

ingredients_string = ''

for fruit_chosen in ingredients_list:
    ingredients_string += fruit_chosen + ' '

st.write(ingredients_string)
name_on_order = "reacher"
my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """', '""" + name_on_order + """')"""

st.write(my_insert_stmt)



time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
  
st.success(f'You {name_on_order} Your Smoothie is ordered!', icon="✅")
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
# st.text(smoothiefroot_response.json())
sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
    

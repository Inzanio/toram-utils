import streamlit as st
from toram_utils.prices_list import SPECIALS_ITEMS, PricesList, add_price,format_price
import datetime


st.title("Add Special Items prices")

date = st.date_input("Day of price", max_value=datetime.date.today())
col1,  col2 = st.columns(2)
selected_item_name = col1.selectbox("Select the Special Item you wich you wanna add price", options=SPECIALS_ITEMS)
price = col2.number_input("Price of the Special Item in Spina", min_value=0, step=100000)
col2.write(f"{format_price(price)}S")
if st.button("Save") :

    item_prices = st.session_state.special_items_prices.get(selected_item_name)
    if (item_prices):
        
        item_prices = PricesList.from_dict(item_prices.to_dict())
    else :
        item_prices = PricesList(selected_item_name)   
    item_prices.prices[date.strftime("%d/%m/%Y")] = price
    add_price(item_prices)
    st.success(f"{selected_item_name} for {format_price(price)}S at {date.strftime("%d/%m/%Y")} has been added successfully !")
    #date_creee = datetime.datetime.strptime("31/12/2024", "%d/%m/%Y")
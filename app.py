import streamlit as st
# setting up page config, like name and logo
st.set_page_config(
    layout="wide",
    page_title="toram_utils",
    page_icon="./img/toram-utils.png",
       
)

# -------------------- init ---------------------------#
from helpers.session import persist_session_data,load_crytas
from toram_utils.consommables import load_consommables
from toram_utils.regislet import load_registlets
from toram_utils.food_buff import load_food_buffs
from toram_utils.prices_list import load_special_items_prices
persist_session_data()

load_registlets()
load_crytas()
load_consommables()
load_food_buffs()
load_special_items_prices()


#st.session_state.ontest = st.radio("On Test",[False,True], horizontal=True)

build = st.Page("simulator/build.py",title="Build", icon="⚒️")
inventory = st.Page("simulator/inventory.py", title="Inventory",icon="🎒")

hit = st.Page("tools/hit.py",title="Hit", icon="🎯")
weapon = st.Page("tools/weapon.py", title = "Weapon", icon="⚔️")

addCrysta = st.Page("contribute/crystas.py", title="Add Crysta", icon="💎")
addConso = st.Page("contribute/consommables.py", title="Add Consommable", icon="🧪")
addFood_buff =st.Page("contribute/food_buff.py", title="Add Food Buff", icon="🥗")

addItem_price = st.Page("contribute/add_item_price.py", title="Add Special Item Price", icon="🌟")

food_buff_finder = st.Page("tools/food_buff_finder.py",title="Find Food Buff", icon="🥗",default=True)
items_prices = st.Page("tools/special_items_prices.py",title="Find Special Items Prices", icon="🌟")

test_dmg = st.Page("tools/test_dmg.py",title="Test DMG", icon="💥")

st.logo("./img/logo.png",size="large")

#if (st.session_state.ontest):
pages = {
    
    "Simulator":[build,inventory],
    "Tools" : [test_dmg,food_buff_finder,items_prices],
    "Contribute": [addFood_buff,addCrysta,addConso,addItem_price]
}
# else :
#     pages = {
        
#         #"Simulator":[build,inventory],
#         "Tools" : [food_buff_finder,items_prices],
#         "Contribute": [addFood_buff,addItem_price]
#     }
# setting up app navigation
app = st.navigation(pages)
app.run()
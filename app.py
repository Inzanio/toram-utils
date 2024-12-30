import streamlit as st
# setting up page config, like name and logo
st.set_page_config(
    layout="wide",
    page_title="toram_utils",
    page_icon="🌟",
       
)

# -------------------- init ---------------------------#
from helpers.session import persist_session_data,load_crytas
from toram_utils.consommables import load_consommables
from toram_utils.regislet import load_registlets
from toram_utils.food_buff import load_food_buffs
persist_session_data()

load_registlets()
load_crytas()
load_consommables()
load_food_buffs()
#print("Im running")
#st.logo("./static/img/logoCSP.png")
# List of pages of our 
# st.Page("./pages/home.py",title="🏠 Home"),
#     st.Page("./pages/hit.py",title="🎯 Hit"),
#     st.Page("./pages/spina.py", title = "💸 Spina"),
#     st.Page("./pages/weapon.py", title = "⚔️ Weapon"),
#     st.Page("./pages/build.py",title="⚒️ Build")
build = st.Page("simulator/build.py",title="Build", icon="⚒️")
inventory = st.Page("simulator/inventory.py", title="Inventory",icon="🎒")

hit = st.Page("tools/hit.py",title="Hit", icon="🎯")
weapon = st.Page("tools/weapon.py", title = "Weapon", icon="⚔️")

addCrysta = st.Page("contribute/crystas.py", title="Add Crysta", icon="💎")
addConso = st.Page("contribute/consommables.py", title="Add Consommable", icon="🧪")
addFood_buff =st.Page("contribute/food_buff.py", title="Add Food Buff", icon="🥗")
#addReg = st.Page("contribute/registlets.py", title="Add Registlet", icon="💎")
#magic = st.Page("contribute/magic.py", title="Current Session Data", icon="✨")
food_buff_finder = st.Page("tools/food_buff_finder.py",title="Find Food Buff", icon="🥗",default=True)

pages = {
    
    "Simulator":[build,inventory],
    "Tools" : [food_buff_finder,hit,weapon],
    "Contribute": [addCrysta, addConso, addFood_buff]
}
# setting up app navigation
app = st.navigation(pages)
app.run()

# Spina 
# Damage calculator
# Buid Section
# Database
# ChatBot
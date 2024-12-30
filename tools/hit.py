import streamlit as st
from toram_utils import get_hit_chance

from helpers.session import persist_session_data
persist_session_data()

# toram online utils
# st.title("Toram online utils")

# st.write("Toram online Fill Stat Price Estimators")

# st.write("Nothing for the moment xD")

st.subheader("(Nub) Hit chance calculator 🎯")

player_accuracy = st.number_input("🏹 Your nub Accuracy ",value=st.session_state.playerLevel, placeholder="Type your accuracy...")
monster_dodge = st.number_input("🏃🏽‍♂️ Damn Boss Dodge ",value=174, placeholder="Type that damn boss dodge...")

skill_mpcost = st.slider("⚡ Skill MP cost ", value = 0, step=100, max_value =2000)

hit_chance,message = get_hit_chance(monster_dodge=monster_dodge,player_accuracy=player_accuracy,skill_mpcost=skill_mpcost)
st.write(message)
st.write("🎯 Hit chance : "+ str(hit_chance) + " %")
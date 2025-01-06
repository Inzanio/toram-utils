import streamlit as st
from toram_utils.equipment import FOOD_BUFF_STAT
from helpers.session import persist_session_data
persist_session_data()

col1,col2 = st.columns([7,4],vertical_alignment="top")
col1.title("🍽️ Looking for a food buff ? 😋")
col2.image("./img/toram-utils.png",width=150)
food_stat = st.selectbox("📝Select the food buff the food buff you need", options=FOOD_BUFF_STAT)
#st.session_state.food_buffs[0].stat_names
food_buffs = [ fb for fb in  st.session_state.food_buffs if (food_stat in fb.stat_names and fb.levels[fb.stat_names.index(food_stat)] is not None )]
food_buffs.sort(key=lambda fb: fb.levels[fb.stat_names.index(food_stat)], reverse=True)
if (len(food_buffs)>0): 
    st.write(f" 🌟 List of land's code for :blue[{food_stat}]") 
    cols = st.columns(3)
    for i, food_buff in enumerate(food_buffs):
        with cols[i % 3]:  # Répartir les expanders sur les colonnes
            
            c = st.container(border=True)
            c.write(f"🏡 {food_buff.owner_name if food_buff.owner_name != '' else 'an OP player'} ⚡Level {food_buff.levels[food_buff.stat_names.index(food_stat)]}")
            c.code(food_buff.code,language=None)
else:
    st.write(f"💔 Sad, no land's code for :blue[{food_stat}] has been registered yet 😭") 
    st.write(f"If you know some please register 🥺")


    
import streamlit as st
from toram_utils.equipment import FOOD_BUFF_STAT
from helpers.session import persist_session_data
from toram_utils.food_buff import add_food_buff,FoodBuff
persist_session_data()

owner_name = st.text_input("Owner Name (IGN)")

col1, col2 = st.columns(2)

food_stat_1 = col1.selectbox("What Buff The owner cooks ?", options=FOOD_BUFF_STAT)
level_1 = col2.slider("Level ?", max_value=10, min_value=1, value=10)

food_stat_2 = col1.selectbox("What is second Buff The owner cooks ?", options=[None]+[fb for fb in FOOD_BUFF_STAT if fb!=food_stat_1])
if (food_stat_2 is not None):
    level_2 = col2.slider("second buff Level ?", max_value=10, min_value=1, value=10)

code = st.text_input("What is the code of the land ?")
code = code.replace(" ","")
if st.button("Save"):
    code_already_exist = code in [fb.code for fb in st.session_state.food_buffs ]

    if (not code_already_exist):
        food_buff = FoodBuff([food_stat_1,food_stat_2],code, owner_name=owner_name, levels=[level_1,None if food_stat_2 is None else level_2])
        add_food_buff(food_buff)
        st.success("The food buff has been successfully added !")
        

    else:
        st.error("Failed to save because A land with this code is already registered !")
    

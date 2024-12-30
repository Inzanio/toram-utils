import streamlit as st
from toram_utils import max_WATK,anvils,anvil_of_weapon,anvils_message
from helpers.session import persist_session_data
persist_session_data()


tabs = ["✨Weapon Anvil Finder","❓Something else upcoming..."]

tab_anvil_finder, tab = st.tabs(tabs)

with tab_anvil_finder :
    baseWATK = st.number_input("Base weapon ATK", min_value=0,value=220)
    WATK = st.number_input("Weapon ATK",min_value=0,value=220)
    
    maxATK = max_WATK(baseWATK)
    index_anvil = anvil_of_weapon(baseWATK,WATK)
    
    if (index_anvil >=0):
        st.slider("Opness Range", min_value=baseWATK , step=1, max_value =maxATK,disabled=True, value= WATK)
        
        st.info(anvils_message[index_anvil])
    else :
        if (index_anvil == -1):
            st.error("💀 Bro, your weapon atk is too high so that it breaks toram\'s rules 😭")
        if (index_anvil == -2) :
            st.warning("💀 Failed Weapon Bro, don't use that... 😭")
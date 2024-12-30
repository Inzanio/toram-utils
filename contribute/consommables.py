import streamlit as st
from toram_utils import STATS_ARMOR, print_stat
from toram_utils.consommables import ConsommableType, add_consommable, Consommable
from helpers.session import persist_session_data

persist_session_data()
#load_crytas()
col_name , col_target = st.columns(2)


name = col_name.text_input("Consommable Name")
type_conso = col_target.selectbox("Type of Consommable",ConsommableType.list())
stat_container = st.container(border=True)

col_stat , col_value , col_condition = st.columns(3)
statLabel = col_stat.selectbox("Stat Name", STATS_ARMOR)
statValue = col_value.number_input("Stat Value",value=0)

if st.button("Add Stat") :
    if (statValue != 0):
            st.session_state.currentConsoStat[statLabel] = statValue 
    else :
        st.warning("Sorry we won't add a stat with 0 as value")

print_stat(stats=st.session_state.currentConsoStat, container=stat_container)
# st.write("we printed the stat --2--",st.session_state.currentConsoStat)
# print("we printed the stat --2--",st.session_state.currentConsoStat)
if st.button("Save",type="primary"):
    if(st.session_state.currentConsoStat == {}):
        st.warning("Bro add at least one stat !")
    
    else :
        if not any(c.name == name for c in st.session_state.consommables):
            conso = Consommable(name=name, stats=st.session_state.currentConsoStat, type=type_conso)
            st.session_state.consommables.append(conso)
            add_consommable (conso)
            
            st.session_state.currentConsoStat = {}
            st.rerun()
        else:
            st.error("Oh, Sorry A Consommable With that Name already Exist !")

st.write("Current Consommables :")
cols = st.columns(3)
for i, conso in enumerate(st.session_state.consommables):       
    with cols[i % 3]: 
        a = st.expander(f"{conso.name}")
        print_stat(stats=conso.stats, container=a)
    

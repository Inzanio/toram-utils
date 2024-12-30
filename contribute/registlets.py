import streamlit as st
from toram_utils.printer import print_stat
from toram_utils.regislet import Registlet, add_registlet, RegisletNames,REGISTLET_STAT
from helpers.session import persist_session_data

persist_session_data()



col_maxlvl,col_stat_perlvl  = st.columns(2)
name = col_maxlvl.selectbox("Registlet Name",RegisletNames)
statLabel = col_stat_perlvl.selectbox("Stat Name", REGISTLET_STAT)

maxlevel = col_maxlvl.number_input("Max level", min_value=0, max_value=100, step=1)
stat_per_level = col_stat_perlvl.number_input("Stat per Level", min_value=0, step=1) 


col_stat , col_value , col_condition = st.columns(3)    
 
# st.write("we printed the stat --2--",st.session_state.currentConsoStat)
# print("we printed the stat --2--",st.session_state.currentConsoStat)
if st.button("Save",type="primary"):
    st.session_state.currentRegistletStat[statLabel] = 0
    if(st.session_state.currentRegistletStat == {}):
        st.warning("Bro add at least one stat !")
    
    else :
        if not any(r.name == name for r in st.session_state.regisltets):
            regs = Registlet(name=name, stats=st.session_state.currentRegistletStat, maxlevel=maxlevel,  stat_per_level=stat_per_level)
            st.session_state.regisltets.append(regs)
            add_registlet (regs)
            
            st.session_state.currentRegistletStat = {}
            st.rerun()
        else:
            st.error("Oh, Sorry A Registlet With that Name already Exist !")

st.write("Current Registlets :")
cols = st.columns(3)
for i, r in enumerate(st.session_state.regisltets):       
    with cols[i % 3]: 
        a = st.expander(f"{r.name}")
        print_stat(stats=r.stats, container=a)
    

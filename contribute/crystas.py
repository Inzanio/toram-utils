import streamlit as st
from toram_utils import STATS_ARMOR,XTALL_TARGET,Crysta,STAT_CONDITIONS, print_stat
from helpers.session import persist_session_data,load_crytas,add_crysta

persist_session_data()
#load_crytas()
col_name , col_target = st.columns(2)


name = col_name.text_input("Crysta Name")
target = col_target.selectbox("Crystas For",XTALL_TARGET)
stat_container = st.container(border=True)
col_stat , col_value , col_condition = st.columns(3)
statLabel = col_stat.selectbox("Stat Name", STATS_ARMOR)
statValue = col_value.number_input("Stat Value",value=0)
condition = col_condition.selectbox("Condition",STAT_CONDITIONS, index=0 ,help="Condition in game like 'With Ninjustsu Scroll :'")


# st.write("we printed the stat --1--",st.session_state.currentCrystaStat)
# print("we printed the stat --1--",st.session_state.currentCrystaStat)
if st.button("Add Stat") :
    if (statValue != 0):
        if (condition == None):
            st.session_state.currentCrystaStat[statLabel] = statValue
            st.write("Added non conditionnal stat")
            print("Added non conditionnal stat")
        else :
            index = next((i for i, cond in enumerate(st.session_state.currentCrystaConditionnalStat) if condition in cond), None)
            if index is not None:
                st.session_state.currentCrystaConditionnalStat[index][condition][statLabel] = statValue
            else:
                st.session_state.currentCrystaConditionnalStat.append({
                    condition : {
                        statLabel : statValue
                    }
                })
    else :
        st.warning("Sorry we won't add a stat with 0 as value")

print_stat(stats=st.session_state.currentCrystaStat, conditionnal_stats=st.session_state.currentCrystaConditionnalStat, container=stat_container)
# st.write("we printed the stat --2--",st.session_state.currentCrystaStat)
# print("we printed the stat --2--",st.session_state.currentCrystaStat)
if st.button("Save",type="primary"):
    if(st.session_state.currentCrystaStat == {}):
        st.warning("Bro add at least one stat !")
    
    else :
        if not any(xtall.name == name for xtall in st.session_state.crystas):
            crysta = Crysta(name=name, stats=st.session_state.currentCrystaStat, conditionnal_stats=st.session_state.currentCrystaConditionnalStat , target=target)
            st.session_state.crystas.append(crysta)
            add_crysta(crysta)
            
            st.session_state.currentCrystaStat = {}
            st.session_state.currentCrystaConditionnalStat = []
            st.rerun()
        else:
            st.error("Oh, Sorry A Crysta With that Name already Exist !")

st.write("Current Crystas :")
cols = st.columns(3)
for i, crysta in enumerate(st.session_state.crystas):       
    with cols[i % 3]: 
        a = st.expander(f"{crysta.name}")
        print_stat(stats=crysta.stats, conditionnal_stats=crysta.conditionnal_stats, container=a)
        
# with st.expander("Delete a crysta"):
#     name_to_delete = st.text_input("Crysta Name to Delete")
#     for crysta in st.session_state.crystas:
#         if crysta.name == name_to_delete:
#             st.session_state.crystas.remove(crysta)
#             save_crystas()
#             st.write(f"The crysta '{name_to_delete}' Has been removed successfully")
#             break
        
#     else:
#         st.write(f"No crysta with name : '{name_to_delete}' found !")
    

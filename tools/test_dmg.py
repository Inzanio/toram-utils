import streamlit as st

from toram_utils.skills.dmg_calculation import *

st.write("Test DMG :red[UNDER DEVELOPMENT]")

#ATK , player_level, target_level, target_resistance
#target_DEF , total_pierce

#base_dmg, effective_defense , skill_constant = 0 , skill_multiplier = 100 , 
# is_unsheathe = False, total_unsheathe_percent = 0, total_unsheathe_flat =0 , 
# is_critical = True , total_critical_damage = 150, total_dte = 100, 
# physical_prorate = 250, stability = 80, is_magic_stability = True

# tab player and target
player_stat_tab, target_stat_tab = st.tabs(["Player","Target"])
# Player
with player_stat_tab :
    col1,col2 = st.columns(2)
    player_level = col1.number_input("Player Level")
    stability = col2.number_input("Stability")
    
    tabs_physical, tabs_magical = st.tabs(["Physical Attribute","Magic Attribute"])
    
    with tabs_physical :
        col1,col2 = st.columns(2)
        ATK = col1.number_input("ATK")
        physical_pierce = col2.number_input("Physical Pierce")
    with tabs_magical :
        col1,col2 = st.columns(2)
        MATK = col1.number_input("MATK")
        magic_pierce = col2.number_input("Magic Pierce")
    

with target_stat_tab :
    target_difficulty =  "Normal"
    
    target_level = st.number_input("Target Level")
    col1,col2 = st.columns(2)
    target_DEF = col1.number_input("DEF")
    target_MDEF = col2.number_input("MDEF")
    
    target_PRES = col1.number_input("Physical Resistance")
    target_MRES = col2.number_input("Magic Resistance")
    
base_physical_dmg = base_dmg(ATK,player_level,target_level,target_resistance=target_PRES)
base_magic_dmg = base_dmg(MATK,player_level,target_level,target_resistance=target_MRES)

st.write(f"Base Physical DMG : :red[{base_physical_dmg}]")
st.write(f"Effective Physical DMG : :red[{base_physical_dmg}]")

st.write(f"Base Magic DMG : :blue[{base_magic_dmg}]")
st.write(f"Effective Magic DMG : :blue[{base_magic_dmg}]")


# target

# skill dmg
col1,col2 = st.columns(2)
skill_constant = col1.number_input("Skill Constant")
skill_multi = col1.number_input("Skill Multiplier")
# hits
hit = {
    "count": 1,
    "constant" : 0,
    "multi" : 0,
    "base_dmg":0,
    "is_magic": False,
    "extra_stats":{}
}
hit_count = st.number_input("Hit Count")
hit_constant = st.number_input("Hit Constant")
hit_multi = st.number_input("Hit Multi")


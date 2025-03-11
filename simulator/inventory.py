import streamlit as st
from helpers.session import persist_session_data,load_crytas
from toram_utils import STATS,WEAPON_TYPE,BODY_ARMOR_TYPE, Weapon,REFINE_LABELS,STATS_ARMOR, BodyArmor,Additionnal,Ring, EQUIPMENT_TYPE, STAT_CONDITIONS,POSSIBLE_SUB,SubWeapon,PURE_SUB_WEAPON,REFINABLE_SUB
from toram_utils.printer import print_ring, print_additionnal, print_body_armor, print_stat,print_weapon,print_subweapon
persist_session_data()

st.write(":red[UNDER DEVELOPMENT]")

@st.dialog("Create Equipment", width="large")
def create_equipment(equipment_type):
    
    st.write(f"Create your {equipment_type}")

    if (equipment_type == EQUIPMENT_TYPE[0]):
        
        coltype, colbaseWATK = st.columns(2)
        weaponType = coltype.selectbox("Weapon Type",WEAPON_TYPE)
        baseWATK = colbaseWATK.number_input("Base Weapon ATK",min_value=1)
        
        colWATK , col_RefStab = st.columns(2)
        watk = colWATK.number_input("Weapon ATK", min_value=1, key="main_WATK")  
        with col_RefStab:
            colRefine , colStab = st.columns(2)
            refine = colRefine.selectbox("Refine Value",REFINE_LABELS,index=15)
            baseStability = colStab.number_input("base stability", min_value=0, max_value=100, step=5, value=80)
    
    # Body armor
    if (equipment_type == EQUIPMENT_TYPE[1]):
        colbaseDEF,colRefine,coltype   = st.columns(3)
        baseDEF = colbaseDEF.number_input("DEF",min_value=0)
        refine = colRefine.selectbox("Refine Value",REFINE_LABELS,index=15)
        armorType = coltype.selectbox("Armor Type",BODY_ARMOR_TYPE)
        
    # Additionnal
    if (equipment_type == EQUIPMENT_TYPE[2]):
        name = st.text_input("Name")
        colbaseDEF,colRefine = st.columns(2)
        baseDEF = colbaseDEF.number_input("DEF",min_value=0)
        refine = colRefine.selectbox("Refine Value",REFINE_LABELS,index=15)
        
    
    # Ring
    if (equipment_type == EQUIPMENT_TYPE[3]):
        name = st.text_input("Name")
        baseDEF = st.number_input("DEF",min_value=0)
        
        #refine = colRefine.selectbox("Refine Value",REFINE_LABELS,index=15)
    if (equipment_type == "subweapon"):
        name = st.text_input("Name")
        colSubType,colATK  = st.columns(2)
        subType = colSubType.selectbox("Subweapon",POSSIBLE_SUB)
        colBATK, colStab = colATK.columns(2)
        if (subType in REFINABLE_SUB) :
            refine = colStab.selectbox("Refine Value",REFINE_LABELS,index=15)
        if (subType == PURE_SUB_WEAPON[-1]): # shield
            baseDEF = colBATK.number_input("DEF",min_value=0)
            
        else :
            
            subWATK = colBATK.number_input("ATK",min_value=0)
            if(subType==PURE_SUB_WEAPON[0]): # scroll
                colMPred , colCastTimeRed = st.columns(2)
                scrollMPRed = colMPred.number_input("Scroll MP Reduction", min_value=0, max_value=3)
                scrollCastTimeRed = colCastTimeRed.number_input("Ninjustsu Cast Time Reduction", min_value=0.0, max_value=1.2)
            else :
                baseStability = colStab.number_input("base stability", min_value=0, max_value=100, step=1, value=0)
        
            
    stat_container = st.container(border=True)
    col_stat , col_value,col_condition = st.columns(3)
    statLabel = col_stat.selectbox("Stat Name", STATS_ARMOR if equipment_type != EQUIPMENT_TYPE[0] else STATS)
    statValue = col_value.number_input("Stat Value",value=0)
    condition = col_condition.selectbox("Condition",STAT_CONDITIONS, index=0 ,help="Condition in game like 'With Ninjustsu Scroll :'")
    # Add Stat
    if st.button("Add Stat") :
        if (statValue != 0):
            if condition==None :
                st.session_state.currentEquipmentStat[statLabel] = statValue
            else :
                index = next((i for i, cond in enumerate(st.session_state.currentEquipmentConditonnalStat) if condition in cond), None)
                if index is not None:
                    st.session_state.currentEquipmentConditonnalStat[index][condition][statLabel] = statValue
                else:
                    st.session_state.currentEquipmentConditonnalStat.append({
                        condition : {
                            statLabel : statValue
                        }
                    })
        else :
            st.warning("Sorry we won't add a stat with 0 as value")
     
     # show added stat
        
    print_stat(stats=st.session_state.currentEquipmentStat, conditionnal_stats=st.session_state.currentEquipmentConditonnalStat, container=stat_container)
        
    # add crysta
    #st.write("If the equipment has not slot, add nothing here")
    if (equipment_type != "subweapon"):
        col_slot1 , col_slot2 = st.columns(2)

        available_crystas =[None] + [crysta for crysta in st.session_state.crystas 
                            if crysta.target == "ALL" or crysta.target == equipment_type]
        # if 'xtal_1' not in st.session_state:
        #     st.session_state.xtal_1 = None
        # if 'xtal_2' not in st.session_state:
        #     st.session_state.xtal_2 = None

        # xtal_1_options =[None] + [crysta for crysta in available_crystas if crysta != st.session_state.xtal_2]
        # xtal_2_options = [None] + [crysta for crysta in available_crystas if crysta != st.session_state.xtal_1]
        # xtal_1_options
        # xtal_2_options
        xtal_1 = col_slot1.selectbox("Crysta on Slot 1", available_crystas, index=0,format_func=lambda x: None if x == None else x.name)
        xtal_2 = col_slot2.selectbox("Crysta on slot 2", available_crystas, index=0,format_func=lambda x: None if x == None else x.name)
       

    if st.button("Save",type="primary"):
        if(st.session_state.currentEquipmentStat == {} and st.session_state.currentEquipmentConditonnalStat== [] ):
            st.warning("Bro add at least one stat !")
        
        else :
            
            if (equipment_type == EQUIPMENT_TYPE[0]):
                weapon  = Weapon(type=weaponType,baseWATK=baseWATK, WATK=watk,stats=st.session_state.currentEquipmentStat, stability=baseStability, refine=REFINE_LABELS.index(refine),
                                 slots=[xtal_1,xtal_2], conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                st.session_state.weapons.append(weapon)
            elif (equipment_type == EQUIPMENT_TYPE[1] ):
                bodyArmor = BodyArmor( type=armorType, stats=st.session_state.currentEquipmentStat,refine=REFINE_LABELS.index(refine),DEF=baseDEF,
                                      slots=[xtal_1,xtal_2], conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                st.session_state.bodyArmors.append(bodyArmor)
            elif (equipment_type == EQUIPMENT_TYPE[2]) :
                add =  Additionnal(stats=st.session_state.currentEquipmentStat,refine=REFINE_LABELS.index(refine),DEF=baseDEF,name=name,slots=[xtal_1,xtal_2], conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                st.session_state.additionnals.append(add)
            elif (equipment_type==EQUIPMENT_TYPE[3]):
                ring = Ring(stats=st.session_state.currentEquipmentStat,DEF=baseDEF,name=name,slots=[xtal_1,xtal_2], conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                st.session_state.rings.append(ring)
                
            elif(equipment_type == "subweapon"):
                
                if (subType == PURE_SUB_WEAPON[-1]): # shield
                    subWeapon = SubWeapon(name=name,type=subType,refine= refine, baseDEF= baseDEF, stats=st.session_state.currentEquipmentStat,conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                elif (subType == PURE_SUB_WEAPON[0]) :  # scroll
                    subWeapon = SubWeapon(name=name,type=subType,baseWATK= subWATK, scrollMPRed= scrollMPRed, scrollCastTimeRed=scrollCastTimeRed , stats=st.session_state.currentEquipmentStat,conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                else : # all other
                    subWeapon = SubWeapon(name=name,type=subType,baseWATK= subWATK, baseStability=baseStability , stats=st.session_state.currentEquipmentStat,conditionnal_stats=st.session_state.currentEquipmentConditonnalStat)
                st.session_state.subWeapons.append(subWeapon)
            st.rerun()

weapons_container = st.container(border=True)

with weapons_container :
    st.write("⚔️ Weapons")
    cols = st.columns(3)
    
    for i, weapon in enumerate(filter(None, st.session_state.weapons)):
        with cols[i % 3]:  # Répartir les expanders sur les colonnes
            w = st.expander(print_weapon(weapon))
            print_stat(stats=weapon.stats,conditionnal_stats=weapon.conditionnal_stats,container=w)
        
   
    if st.button("Add a weapon") :
        create_equipment(EQUIPMENT_TYPE[0])


subweapons_container = st.container(border=True)

with subweapons_container :
    st.write("➕ Sub Weapons")
    cols = st.columns(3)
    
    for i, subWeapon  in enumerate(filter(None, st.session_state.subWeapons)):
        with cols[i % 3]:  # Répartir les expanders sur les colonnes
            w = st.expander(print_subweapon(subWeapon))
            print_stat(stats=subWeapon.stats,conditionnal_stats=subWeapon.conditionnal_stats,container=w)
        
   
    if st.button("Add a subweapon") :
        create_equipment("subweapon")

armors_container = st.container(border=True)

with armors_container :
    st.write("🦺 Armors")
    cols = st.columns(3)
    for i, barmor in enumerate(filter (None,st.session_state.bodyArmors)):
        with cols[i % 3]: # Répartir les expanders sur les colonnes
            ba = st.expander(print_body_armor(barmor))
            print_stat(stats=barmor.stats,conditionnal_stats=barmor.conditionnal_stats,container=ba)
    
    if st.button("Add a BodyArmor") :
        create_equipment(EQUIPMENT_TYPE[1])

additionnal_container = st.container(border=True)

with additionnal_container :
    st.write("🪖 Additionnals")
    cols = st.columns(3)
    for i, add in enumerate(filter(None, st.session_state.additionnals)):   
        with cols[i % 3]: 
            for stat, value in add.stats.items():
                a = st.expander(print_additionnal(add))
                print_stat(stats=add.stats,conditionnal_stats=add.conditionnal_stats,container=a)
   
    if st.button("Add a Additionnal") :
            create_equipment(EQUIPMENT_TYPE[2])
        
rings_container = st.container(border=True)

with rings_container :
    st.write("💍 Rings")
    cols = st.columns(3)
    for i, ring in enumerate(filter(None, st.session_state.rings)):        
        with cols[i % 3]: 
            r = st.expander(print_ring(ring))
            print_stat(stats=ring.stats,conditionnal_stats=ring.conditionnal_stats,container=r)
   
    if st.button("Add a Ring") :
        create_equipment(EQUIPMENT_TYPE[3])
    

# with st.popover("Create Equipment"):
#         #st.markdown("Hello World 👋")
#         type_weapon = st.selectbox("Weapon:",["OHS","THS"])
#         name = st.text_input("Name")
#         baseWATK = st.number_input("WATK",min_value=1,step=1)
#         st.button("Add Equipment")
#         slot_1 = st.checkbox("First Slot")
        
#         if (slot_1):
#             slot_2 = st.checkbox("Second Slot")
            
#         stat_options = ["physical_resistance", "magic_resistance", "max_hp", "max_mp", "ATK%"]
#         stat_selected = st.selectbox("Stat:", stat_options)
#         stat_value = st.number_input("Valeur de la stat", min_value=1, step=1)
#         stats = {
            
#         }
#         # Ajouter la stat au dictionnaire
#         if st.button("Add Stat"):
#             stats[stat_selected] = stat_value
#             #st.write("Stat ajoutée avec succès !")
        
#         st.write(stats)
    
    
   
#     equipment = {
#         "name":"9th anniv Armor",
#         "DEF": 350,
#         "type":"Armor",
#         "stats":{
#             "physical_resistance":20,
#             "magic_resistance":20,
#             "max_hp":20,
#             "max_mp":200
#         },
#         "slot_1": None,
#         "slot_2": None
#     }
#     weapon = {
#         "name":"9th anniv sword",
#         "WATK": 550,
#         "type": "OHS",
#         "stats":{
#             "ATK%":14,
#             "STR%":10,
#             "CD%":20,
#             "CD":200
#         },
#         "slot_1":None,
#         "slot_2":None
        
#     }
#     #toramStats = 
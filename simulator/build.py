import streamlit as st
from helpers.session import persist_session_data, under_developement
from toram_utils import FOOD_BUFF_STAT,Ring,BodyArmor,Weapon,Additionnal,SubWeapon
from toram_utils.printer import print_body_armor, print_ring, print_additionnal, print_weapon,print_subweapon,show_percent, print_stat, print_conso,print_regisltet,print_skill, print_active_skill, print_passive_skill, print_dps_skill
from toram_utils.stat_calculations import Build
from toram_utils.skills import SKILLS,SkillTypes
persist_session_data()

under_developement()


tabs = ["🎛️ Resume ","🙋🏻‍♂️ Base Stat ","🪖 Equipment ","🌟 Skill ","🥗 Food Buff ","💎 Regislet ","🧪 Consommables "]

resume_tab, base_stat_tab , equipment_tab , skill_tab, food_buff_tab, regislet_tab, conso_tab,  = st.tabs(tabs)

with base_stat_tab :
    # st.title("")
    #col_baseStat, col_totalStat , col_totalStat2 = st.columns(3)
    #with col_baseStat :
    st.number_input("Level",min_value=1,key="playerLevel")
    st.number_input("STR",min_value=1,key="baseSTR")
    st.number_input("INT",min_value=1,key="baseINT")
    st.number_input("VIT",min_value=1,key="baseVIT")
    st.number_input("AGI",min_value=1,key="baseAGI")
    st.number_input("DEX",min_value=1,key="baseDEX")
    st.radio("Personnal Stat",["None","TEC","MTL","LUK","CRT"],horizontal=True,key="PersonnalSTAT_Label")
    
    if ( st.session_state.PersonnalSTAT_Label != "None"):
        personnalSTAT = st.number_input(st.session_state.PersonnalSTAT_Label,min_value=1, key="personnalSTAT_Value")
        
    basicStats = {
        "playerLevel": st.session_state.playerLevel,
        "baseSTR": st.session_state.baseSTR,
        "baseINT": st.session_state.baseINT,
        "baseVIT": st.session_state.baseVIT,
        "baseAGI": st.session_state.baseAGI,
        "baseDEX": st.session_state.baseDEX,
        "PersonnalSTAT_Label": st.session_state.PersonnalSTAT_Label,
        "personnalSTAT_Value": st.session_state.personnalSTAT_Value if st.session_state.PersonnalSTAT_Label != "None" else 0
    }
    build = Build("Build 1")
    build.set_basic_stat(basicStats)
        
        
def handleChange(obj,attr):
    st.session_state[attr] = obj 
    #st.rerun()
with equipment_tab :
    col1, col2 = st.columns(2)
    with col1 :
        main_weapon_expander = st.expander("⚔️ Main Weapon")
        with main_weapon_expander :
            
            main_weapon_options = [None] +[weapon.to_dict() for weapon in st.session_state.weapons if weapon != None]
            main_weapon = st.selectbox("weapon", main_weapon_options, format_func=lambda weapon: print_weapon(Weapon.from_dict(weapon)), on_change= lambda  : handleChange(main_weapon,"currentMainWeapon") , index=main_weapon_options.index(st.session_state.currentMainWeapon))
            
            build.main_weapon = Weapon.from_dict(main_weapon)
        sub_weapon_expander = st.expander("➕ Sub Weapon")
        with sub_weapon_expander :
            sub_weapon_options = [None] +[sub_weapon.to_dict() for sub_weapon in st.session_state.subWeapons if sub_weapon != None]
            sub_weapon = st.selectbox("sub", sub_weapon_options, format_func=lambda sub_weapon: print_subweapon(SubWeapon.from_dict(sub_weapon)), index=sub_weapon_options.index(st.session_state.currentSubWeapon))
            st.session_state.currentSubWeapon = sub_weapon
            build.sub_weapon = SubWeapon.from_dict(sub_weapon)
   
        body_armor_expander = st.expander("🦺 Body Armor")
        with body_armor_expander :
            body_armor_options = [None] +[body_armor.to_dict() for body_armor in st.session_state.bodyArmors if body_armor != None]
            body_armor = st.selectbox("body armor", body_armor_options, format_func=lambda body_armor: print_body_armor(BodyArmor.from_dict(body_armor)), index=body_armor_options.index(st.session_state.currentBodyArmor))
            st.session_state.currentBodyArmor = body_armor
            build.body_armor = BodyArmor.from_dict(body_armor)
        additionnal_expander = st.expander("🪖 Additionnal")
        with additionnal_expander :
            additionnal_options = [None]+[additionnal.to_dict() for additionnal in st.session_state.additionnals if additionnal != None]
            additionnal = st.selectbox("add", additionnal_options, format_func=lambda additionnal: print_additionnal(Additionnal.from_dict(additionnal)), index=additionnal_options.index(st.session_state.currentAdditionnal))
            st.session_state.currentAdditionnal = additionnal
            build.additional = Additionnal.from_dict(additionnal)
        ring_expander = st.expander("💍 Ring")
        with ring_expander :
            ring_options =[None] + [ring.to_dict() for ring in st.session_state.rings if ring != None]
            ring = st.selectbox("ring", ring_options , format_func= lambda ring :print_ring(Ring.from_dict(ring)),index=ring_options.index(st.session_state.currentRing))
            st.session_state.currentRing = ring
            build.ring = Ring.from_dict(st.session_state.currentRing)
            
# add skills to build
with skill_tab : 
    passive_tab, active_tab, dps_tab = st.tabs(["Passive Skill","Active Buff","DPS Skill"])
    
    
    with passive_tab :
        
        col_passive_skill = st.columns(3)
        
        
        options = [s for s in SKILLS if SkillTypes.PASSIVE in s.type]
        
        selected_passive_skills_names = {s["skillClass"].name for s in st.session_state.selected_passive_skills}
        options = [skill for skill in options if skill.name not in selected_passive_skills_names]
        
        st.divider()
        col_skill , col_lvl = st.columns(2)
        selected_passive_skill = col_skill.selectbox("Select The Passive skill to add",options, format_func= lambda skill: skill.name)
        skill_lvl = col_lvl.number_input("Level", min_value=1,max_value=10, value=10, key="passive_slvl")
        
        
        if st.button("Add Passive Skill") :
            st.session_state.selected_passive_skills.append({"skillClass": selected_passive_skill, "level":skill_lvl})
            st.rerun()
        for i, skill_info in enumerate(st.session_state.selected_passive_skills): 
            skill_class = skill_info["skillClass"]
            
            
            lvl = skill_info["level"]
            ## ----------- Extremely Important ----------------- ##
            skill = skill_class(lvl,build)
            #print(skill)
            #st.write(print_skill(skill))
            with col_passive_skill[i % 3]:  # Répartir les expanders sur les colonnes
                w = st.expander(print_skill(skill))
                print_passive_skill(skill, container=w)
        build.passive_skills = st.session_state.selected_passive_skills
        
    with active_tab :
        
        col_active_skill = st.columns(3)
        
        
        options = [s for s in SKILLS if SkillTypes.ACTIVE in s.type]
        selected_active_skills_names = {s["skillClass"].name for s in st.session_state.selected_active_skills}
        options = [skill for skill in options if skill.name not in selected_active_skills_names]
        
        st.divider()
        col_skill , col_lvl = st.columns(2)
        selected_active_skill = col_skill.selectbox("Select The Active skill to add",options, format_func= lambda skill: skill.name)
        skill_lvl = col_lvl.number_input("Level", min_value=1,max_value=10, value=10,key="active_slvl")
        
        
        if st.button("Add Active Skill") :
            st.session_state.selected_active_skills.append({"skillClass": selected_active_skill, "level":skill_lvl})
            st.rerun()
        for i, skill_info in enumerate(st.session_state.selected_active_skills):
            skill_class = skill_info["skillClass"]
            lvl = skill_info["level"]
            ## ----------- Extremely Important ----------------- ##
            skill = skill_class(lvl,build)
            #print(skill)
            #st.write(print_skill(skill))
            with col_active_skill[i % 3]:  # Répartir les expanders sur les colonnes
                w = st.expander(print_skill(skill))
                print_active_skill(skill,container=w)
        
        build.active_skills = st.session_state.selected_active_skills
        
    with dps_tab :
        
        col_dps_skill = st.columns(3)
        
        
        options = [s for s in SKILLS if SkillTypes.ATTACKING in s.type]
        selected_dps_skills_names = {s["skillClass"].name for s in st.session_state.selected_dps_skills}
        options = [skill for skill in options if skill.name not in selected_dps_skills_names]
        
        st.divider()
        col_skill , col_lvl = st.columns(2)
        selected_dps_skill = col_skill.selectbox("Select The DPS skill to add",options, format_func= lambda skill: skill.name)
        skill_lvl = col_lvl.number_input("Level", min_value=1,max_value=10, value=10,key="dps_slvl")
        
        
        if st.button("Add DPS Skill") :
            st.session_state.selected_dps_skills.append({"skillClass": selected_dps_skill, "level":skill_lvl})
            st.rerun()
        for i, skill_info in enumerate(st.session_state.selected_dps_skills):
            skill_class = skill_info["skillClass"]
            lvl = skill_info["level"]
            ## ----------- Extremely Important ----------------- ##
            skill = skill_class(lvl,build)
            #print(skill)
            #st.write(print_skill(skill))
            with col_dps_skill[i % 3]:  # Répartir les expanders sur les colonnes
                w = st.expander(print_skill(skill))
                print_dps_skill(skill,container=w)
        
        build.dps_skills = st.session_state.selected_dps_skills
    #build.registlets = st.session_state.selected_regisltets
with food_buff_tab :
    
    colFood1, colValue1 = st.columns(2)
    food1 = colFood1.selectbox("F1", FOOD_BUFF_STAT, index=FOOD_BUFF_STAT.index(next((stat for stat in st.session_state.foodBuffStat if stat in FOOD_BUFF_STAT), FOOD_BUFF_STAT[0])), key="food_stat_1",label_visibility="hidden")
    value1 = colValue1.number_input("V1", min_value=0, value=st.session_state.foodBuffStat.get(food1, 0), key="food_value_1",label_visibility="hidden")
    st.session_state.foodBuffStat["food_stat_1"] = food1
    st.session_state.foodBuffStat["food_value_1"] = value1

    colFood2, colValue2 = st.columns(2)
    food2 = colFood2.selectbox("F2", FOOD_BUFF_STAT, index=FOOD_BUFF_STAT.index(next((stat for stat in st.session_state.foodBuffStat if stat in FOOD_BUFF_STAT and stat != food1), FOOD_BUFF_STAT[1])), key="food_stat_2",label_visibility="hidden")
    value2 = colValue2.number_input("V2", min_value=0, value=st.session_state.foodBuffStat.get(food2, 0), key="food_value_2",label_visibility="hidden")
    st.session_state.foodBuffStat["food_stat_2"] = food2
    st.session_state.foodBuffStat["food_value_2"] = value2

    colFood3, colValue3 = st.columns(2)
    food3 = colFood3.selectbox("F3", FOOD_BUFF_STAT, index=FOOD_BUFF_STAT.index(next((stat for stat in st.session_state.foodBuffStat if stat in FOOD_BUFF_STAT and stat not in (food1, food2)), FOOD_BUFF_STAT[2])), key="food_stat_3",label_visibility="hidden")
    value3 = colValue3.number_input("V3", min_value=0, value=st.session_state.foodBuffStat.get(food3, 0), key="food_value_3",label_visibility="hidden")
    st.session_state.foodBuffStat["food_stat_3"] = food3
    st.session_state.foodBuffStat["food_value_3"] = value3

    colFood4, colValue4 = st.columns(2)
    food4 = colFood4.selectbox("F4", FOOD_BUFF_STAT, index=FOOD_BUFF_STAT.index(next((stat for stat in st.session_state.foodBuffStat if stat in FOOD_BUFF_STAT and stat not in (food1, food2, food3)), FOOD_BUFF_STAT[3])), key="food_stat_4",label_visibility="hidden")
    value4 = colValue4.number_input("V4", min_value=0, value=st.session_state.foodBuffStat.get(food4, 0), key="food_value_4",label_visibility="hidden")
    st.session_state.foodBuffStat["food_stat_4"] = food4
    st.session_state.foodBuffStat["food_value_4"] = value4

    colFood5, colValue5 = st.columns(2)
    food5 = colFood5.selectbox("F5", FOOD_BUFF_STAT, index=FOOD_BUFF_STAT.index(next((stat for stat in st.session_state.foodBuffStat if stat in FOOD_BUFF_STAT and stat not in (food1, food2, food3, food4)), FOOD_BUFF_STAT[4])), key="food_stat_5",label_visibility="hidden")
    value5 = colValue5.number_input("V5", min_value=0, value=st.session_state.foodBuffStat.get(food5, 0), key="food_value_5",label_visibility="hidden")
    st.session_state.foodBuffStat["food_stat_5"] = food5
    st.session_state.foodBuffStat["food_value_5"] = value5
    
    build.set_food_buff(st.session_state.foodBuffStat)
# build.__dict__
# if build.main_weapon is not None:
#     st.write(build.main_weapon.__dict__)
# st.write("Total STR %",build.calculate_augmentation("STR %"))
# build.totalSTR
# update des visuels

# add registlet to build
with regislet_tab :
    if len(st.session_state.selected_regisltets) ==0 :
        st.write("No Registlet used yet, Add some !")
    else :
        st.write("Current Regisltet")
        
    cols = st.columns(3)
    
    #col_slct, col_add = st.columns(2)    
    st.divider()
    col_reg, col_lvl = st.columns(2)
    
    selected_reg = col_reg.selectbox("List of available Registlets",st.session_state.regisltets, format_func= lambda  reg : print_regisltet(reg))
    registlet_lvl = col_lvl.number_input("Level", min_value=1,max_value=selected_reg.maxlevel)
    selected_reg.level = registlet_lvl
    #st.write(selected_reg)
    
    if st.button("Add Regisltet") :
        if selected_reg.name in [reg.name for reg in st.session_state.selected_regisltets]:
            st.session_state.selected_regisltets = [r for r in st.session_state.selected_regisltets if r.name != selected_conso.name] + [selected_reg]
        else:
            st.session_state.selected_regisltets.append(selected_reg)

    for i, reg in enumerate(st.session_state.selected_regisltets):
        with cols[i % 3]:  # Répartir les expanders sur les colonnes
            w = st.expander(print_regisltet(reg, showLevel = True))
            print_stat(stats=reg.stats,container=w)
    build.registlets = st.session_state.selected_regisltets

# add conso to build

with conso_tab :
    
    if len(st.session_state.selected_consommables) ==0 :
        st.write("No consommables used yet, Add some !")
    else :
        st.write("Current Consommables")
        
    cols = st.columns(3)
    
    #col_slct, col_add = st.columns(2)    
    st.divider()
    selected_conso = st.selectbox("List of available Consommables",st.session_state.consommables, format_func= lambda  conso : print_conso(conso))
    if st.button("Add") :
        if selected_conso.type in [conso.type for conso in st.session_state.selected_consommables]:
            st.session_state.selected_consommables = [c for c in st.session_state.selected_consommables if c.type != selected_conso.type] + [selected_conso]
        else:
            st.session_state.selected_consommables.append(selected_conso)

    for i, conso in enumerate(st.session_state.selected_consommables):
        with cols[i % 3]:  # Répartir les expanders sur les colonnes
            w = st.expander(print_conso(conso))
            print_stat(stats=conso.stats,container=w)
    build.consommables = st.session_state.selected_consommables

with resume_tab :
    part1, part2 = st.columns(2)
    with part1 :
        general_tab , total_stat = st.tabs(["General","Total Stat"])
        
        with general_tab :
            col_hp , col_mp = st.columns(2)
            
            col_hp.metric("Max HP", build.totalHP)
            col_mp.metric("Max MP", build.totalMP)
            
            col_hp.metric("Short Range Damage", show_percent(build.totalSRD))
            col_mp.metric("Long Range Damage", show_percent(build.totalLRD))
            
            col_hp.metric("Motion", show_percent(build.totalMotion))
            col_mp.metric("Dodge", build.totalDodge)
        
        with total_stat :
            col1, col2, col3, col4 = st.columns(4)
            

            col1.metric("Total STR", build.totalSTR)
            col1.metric("Total INT", build.totalINT)
            
            col2.metric("Total VIT", build.totalVIT)
            col2.metric("Total AGI", build.totalAGI)
            
            col3.metric("Total DEX", build.totalDEX)
        
    with part2:    
        physical_tab,magic_tab,Element_tab = st.tabs(["Physical","Magic","Element"])
    
        with physical_tab :
            col_cr , col_cd = st.columns(2)
            
            col_cr.metric("ATK", build.totalATK)
            col_cd.metric("Physical Pierce", show_percent(build.totalPhysicalPierce))
            
            col_cr.metric("Critical Rate", build.totalCriticalRate)
            col_cd.metric("Critical Damage", build.totalCriticalDamage)
            
            col_cr.metric("ASPD", build.totalASPD)
            col_cd.metric("Accuracy", build.totalAccuracy)
            
            
            col_cr.metric("AMPR", build.totalAMPR)
            col_cd.metric("Stability", show_percent(build.totalStability))
            
            col_cr.metric("Unsheathe Attack %", show_percent(build.totalUnsheathe_attack_percent))
            col_cd.metric("Unsheathe Attack ", build.totalUnsheathe_attack_flat)
        

        with magic_tab :
            col_mcr , col_mcd = st.columns(2)

            col_mcr.metric("MATK", build.totalMATK)
            col_mcd.metric("Magic Pierce", show_percent(build.totalMagicPierce))

            col_mcr.metric("Magic Critical Rate", build.totalMagicCriticalRate)
            col_mcd.metric("Magic Critical Damage", build.totalMagicCriticalDamage)

            col_mcr.metric("CSPD", build.totalCSPD)
            col_mcd.metric("CSPD Reduction", show_percent(build.totalCSPD_Reduction))

            col_mcr.metric("INT DTE", show_percent(build.totalINT_DTE))
            col_mcd.metric("Magic Stability", show_percent(build.totalStability))
            
            
        with Element_tab :
            col_dte1 , col_dte2 = st.columns(2)

            col_dte1.metric("Current Element", build.currentElement)
            col_dte2.metric("DTE Neutral", show_percent(build.totalDTE_Neutral))
            
            col_dte1.metric("DTE Fire", show_percent(build.totalDTE_Fire))
            col_dte2.metric("DTE Water", show_percent(build.totalDTE_Water))
            col_dte1.metric("DTE Wind", show_percent(build.totalDTE_Wind))
            col_dte2.metric("DTE Earth", show_percent(build.totalDTE_Earth))
            col_dte1.metric("DTE Dark", show_percent(build.totalDTE_Dark))
            col_dte2.metric("DTE Light", show_percent(build.totalDTE_Light))
        
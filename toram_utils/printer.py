from toram_utils import REFINE_LABELS, AWAKEN_ELEMENT,INTERUPT_UNAVAILABLE, SubWeapon,PURE_SUB_WEAPON


import streamlit as st

def print_crystas(crystas = []) :
    return f"{'[ '+crystas[0].name + ' ] ' if crystas[0] != None else '' } {'[ '+crystas[1].name + ' ] ' if crystas[1] != None else '' }"

def print_weapon(weapon):
    if (weapon == None):
        return "None"
    return f"{weapon.awakenElement + ' ' if weapon.awakenElement != None else ''}{weapon.type} @{weapon.WATK} {REFINE_LABELS[weapon.refine]} {print_crystas(weapon.slots)}"

def print_subweapon(subweapon : SubWeapon):
    if (subweapon == None):
        return "None"
    if (subweapon.type == PURE_SUB_WEAPON[-1]): #shield
        return f"{subweapon.type} @{subweapon.baseDEF} {REFINE_LABELS[subweapon.refine]} "
    
    if (subweapon.type == PURE_SUB_WEAPON[0]): #scroll
        return f"{subweapon.type} @{subweapon.baseWATK} ({subweapon.scrollMPRed} , {subweapon.scrollCastTimeRed}) "
         
    return f"{subweapon.awakenElement + ' ' if subweapon.awakenElement != None else ''}{subweapon.type} @{subweapon.baseWATK} {subweapon.baseStability} % "


def print_body_armor(barmor):
    if (barmor == None):
        return "None"
    return f"{barmor.type} Armor @{barmor.DEF} {REFINE_LABELS[barmor.refine]} "
def print_additionnal(add):
    if (add == None):
        return "None"
    return f"{add.name} @{add.DEF} {REFINE_LABELS[add.refine]} "
def print_ring(ring):
    if (ring == None):
        return "None"
    # if (isinstance(ring,dict)):
    #     return f"{ring['name']} @{ring['DEF']} {print_crystas(ring['slots'])} " 
    return f"{ring.name} @{ring.DEF} {print_crystas(ring.slots)} " 

def print_stat(stats = {}, conditionnal_stats = [], container = st) :
    
    # if (stats == {}):
    #     container.write("Build Doesn't meet Conditions")
        
    for stat, value in stats.items():
        container.write(format_stat(stat,value))
    
    if len(conditionnal_stats) > 0:
        for conditionnal_stat in conditionnal_stats:
            for condition, stats_condition in conditionnal_stat.items():
                container.write(f"With {condition} :")
                for stat, value in stats_condition.items():
                    container.write(format_stat(stat, value))
    
      
def format_stat(stat, value):
    if stat in AWAKEN_ELEMENT + INTERUPT_UNAVAILABLE :
        return f"{stat}"
    
    if stat.startswith("%"):
        stat_name = stat[1:]
        stat_name = stat_name.replace("stronger against", "Damage To")
        return f"+{value}% {stat_name}"
    if stat.endswith("%"):
        stat_name = stat[:-1]
        if (value > 0):
            return f"{stat_name} +{value}%"
        else :
            return f"{stat_name} {value}%"
    elif value > 0:
        return f"{stat} +{value}"
    else:
        return f"{stat} {value}"

def format_food_stat(foodBuffStat):
    formatted_food_stat = {}
    for i in range(1, 6):
        stat = foodBuffStat[f"food_stat_{i}"]
        value = foodBuffStat[f"food_value_{i}"]
        formatted_food_stat[stat] = value
    return formatted_food_stat

def show_percent(value):
    return str(value) + " %"

from toram_utils.consommables import Consommable
def print_conso(conso : Consommable):
    return f"{conso.name}"

from toram_utils.regislet import Registlet
def print_regisltet(reg : Registlet , showLevel = False ):
    if (showLevel):
        return f"{reg.name} lvl {reg.level}"
    return f"{reg.name}  --  Max Level : {reg.maxlevel}"

from toram_utils.skills.skills import Skill
def print_skill(skill : Skill):
    return f"{skill.name} Lvl {skill.level}"

def print_passive_skill(skill : Skill,container=st):
    if (skill.build_meet_weapon_condition):
        if (skill.passive_stats != {}):
            print_stat(stats=skill.passive_stats,container=container)
        if (skill.passive_description==""):
            container.write("You cannot benefic the passive effect of this skill with the current equipment")
        else:
            container.write(skill.passive_description)
        
    else :
        container.write("You cannot benefic the passive effect of this skill with the current equipment")

def print_active_skill(skill : Skill,container=st):
    if (skill.build_meet_weapon_condition):
        if (skill.active_stats != {}):
            print_stat(stats=skill.active_stats,container=container)
        if (skill.hasSpecialEffect):
            container.write(skill.active_description)
    else:
        container.write("The Build doesn't meet condition bro")
        
def print_dps_skill(skill : Skill,container=st):
    # if (skill.stats != {}):
    #     print_stat(stats=skill.stats,container=container)
    if (skill.build_meet_weapon_condition):
        # give special proprieties
        if (skill.hasSpecialAttribute):
            #print_stat(skill.specialAttribute, container=container) 
            container.write(skill.dps_description)    
        container.write(f" constant : {skill.constant}")
        container.write(f"multi : {skill.multi}")
    else :
        container.write("You cannot use this skill with the current equipment")
#if ( print_void and stats =={}):
        # if (hasSpecialEffect):
        #     container.write(description)
        # elif showPower:
        #     container.write(f"Constant : {constant}") 
        #     container.write(f"Multiplier : {multi}")
        # else:
        #     container.write("Build Doesn't meet Conditions")
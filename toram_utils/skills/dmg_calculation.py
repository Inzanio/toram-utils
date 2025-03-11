from toram_utils.stat_calculations import Build
from math import floor
# dmg calculation in toram has many step


def stability_interval ( stability , is_magic_stability = False) :
    stability_corrected = min(stability,100)
    min_stab = stability_corrected
    max_stab = 100
    if ( is_magic_stability) :
        min_stab = int(min(90,(100+stability_corrected)/2))
        max_stab = int(max(100,100+(stability_corrected-80)/2))
    return min_stab,max_stab

def base_dmg ( ATK , player_level, target_level, target_resistance):


    return ( ATK + player_level + 1 - target_level ) * (100 - target_resistance )/100

def effective_defense ( target_DEF , total_pierce) :
    
    return target_DEF*  (100 - total_pierce)/100

def skill_base_dmg ( base_dmg, effective_defense , skill_constant = 0 , skill_multiplier = 100 , is_unsheathe = False, total_unsheathe_percent = 0, total_unsheathe_flat =0 , is_critical = True , total_critical_damage = 150, total_dte = 100, physical_prorate = 250, stability = 80, is_magic_stability = True):
    
    dmg = floor(base_dmg - effective_defense)
    # add skill constant
    dmg = floor(dmg + skill_constant)
    # add unshathe flat
    if is_unsheathe :
        dmg = floor(dmg + total_unsheathe_flat )
    
    # -- start multiplier --
    
    # add crit dmg
    if (is_critical) :
        dmg = floor(dmg * total_critical_damage/100 )
    # add dte
    dmg = floor(dmg * total_dte/100 )
    # add skill multiplier
    dmg = floor(dmg * skill_multiplier/100 )
   
    # add unshathe flat 
    if is_unsheathe :
        dmg = floor(dmg * total_unsheathe_percent/100 )
    
    # i could stop here and return it at raw dmg
    ## add stability
    possible_dmg = {}
    min_stability , max_stability = stability_interval(stability, is_magic_stability)
    
    for stab in range(min_stability,max_stability+1) :
        possible_dmg[stab] = floor(dmg * stab/100)
    
    
    ## add prorate to all possible dmg
    possible_dmg = {stab: floor(dmg * physical_prorate/100 ) for stab, dmg in possible_dmg.items()}

    #
    # 
    # at the end add suprême multiplier
    # 1 + sum of all skill modifier if skill affected ( passive like sword techinuqes long range whack martial disciilie)
    # 1 + total srd / lrd
    # *0.7 if ahs lethargy
    #  1 + summ of all last dmg modifier ( if affected by brave aura or being caster of mana recharge)
    # 1 + summ of all combo modifier ( if skill is in a combo)
    # *(1-base drop gem dmg red / 100) if (use gem)
    # * 0.25 if attack was guarded
    # * (1+ utlima lion rage dmg bonys/100) if skill only 
# def add_multiplier (build : Build , raw_dmg : int):

class Hit :
    def  __init__(self):
        self.count = 1
        self.constant = 0
        self.multi = 0
        self.extra_stats = {}
        self.base_dmg = 0
        
    # hit = {
    #     "count": 1,
    #     "constant" : 0,
    #     "multi" : 0,
    #     "base_dmg":0,
    #     "is_magic": False,
    #     "extra_stats":{}
    # }
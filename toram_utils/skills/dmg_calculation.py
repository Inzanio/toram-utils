from toram_utils.stat_calculations import Build
from math import floor
# dmg calculation in toram has many step



def base_dmg (build : Build):
    # physical base dmg
    base_physical_dmg = (build.totalATK + build.playerLevel + 1 - build.target.level ) * (100 - build.target.physical_resistance  )/100
    # magic base dmg
    base_magic_dmg = (build.totalMATK + build.playerLevel + 1 - build.target.level ) * (100 - build.target.magic_resistance  )/100

    return { "physical" : base_physical_dmg , "magic" : base_magic_dmg }

def effective_defense ( build : Build) :
    effectiv_DEF = build.target.DEF *  (100 - build.totalPhysicalPierce)/100
    effectiv_MDEF = build.target.MDEF *  (100 - build.totalMagicPierce)/100
    
    return { "physical" : effectiv_DEF , "magic" : effectiv_MDEF }

def raw_dmg (build  : Build, skill_constant = 0 , skill_multiplier = 100 , is_unsheathe = False , is_critical = True, total_dte = 100, physical_prorate = 250):
    
    physical_raw_dmg = floor(base_dmg(build)["physical"] - effective_defense(build)["physical"])
    # add skill constant
    physical_raw_dmg = floor(physical_raw_dmg + skill_constant)
    # add unshathe flat
    if is_unsheathe :
        physical_raw_dmg = floor(physical_raw_dmg + build.totalUnsheathe_attack_flat )
    
    # -- start multiplier --
    
    # add crit dmg
    if (is_critical) :
        physical_raw_dmg = floor(physical_raw_dmg * build.totalCriticalDamage/100 )
    # add dte
    physical_raw_dmg = floor(physical_raw_dmg * total_dte/100 )
    # add skill multiplier
    physical_raw_dmg = floor(physical_raw_dmg * skill_multiplier/100 )
   
    # add unshathe flat 
    if is_unsheathe :
        physical_raw_dmg = floor(physical_raw_dmg * build.totalUnsheathe_attack_percent/100 )
    
    # i could stop here and return it at raw dmg
    ## add stability
    physical_raw_dmg = floor(physical_raw_dmg * build.totalStability/100 )
    ## add prorate
    physical_raw_dmg = floor(physical_raw_dmg * physical_prorate/100 )
    
    # at the end add suprême multiplier
    return {
        "physical" : physical_raw_dmg
    }

# def add_multiplier (build : Build , raw_dmg : int):
    
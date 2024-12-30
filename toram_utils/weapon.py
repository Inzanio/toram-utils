anvils = ["normal","bronze","silver","gold"]
anvils_message =["🔰 Normal (Nub) Anvil 🔰","🥉 Bronze Anvil 🥉","🥈 Silver Anvil 🥈","🥇 Gold Anvil 🥇"]
def max_WATK (baseWATK):
    return round(baseWATK * 1.1 + 10)

def anvil_of_weapon (baseWATK,WATK):
    max_watk = max_WATK(baseWATK)
    diff = max_watk - baseWATK
    
    if WATK < baseWATK :
        # failed Weapon xD
        return -2
    if WATK > (baseWATK + diff):
        # WATK too high xD
        return -1
    
    class_index = 3
    if WATK <= (baseWATK + diff/4):
        class_index = 0
    elif WATK <= (baseWATK + diff/2):
        class_index = 1
    elif WATK <= (baseWATK + diff*3/4):
        class_index = 2
    
    
    return class_index
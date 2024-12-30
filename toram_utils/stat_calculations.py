from math import floor

from toram_utils.equipment import Weapon, BodyArmor, Additionnal, Ring,STATS_ARMOR, SubWeapon, Equipment_label, BODY_ARMOR_TYPE, AWAKEN_ELEMENT, MAGIC_WEAPON_TYPE, Target, Monster
#from toram_utils.skills import Skill

class GameElements :
    NEUTRAL = None
    FIRE = "Fire Element"
    EARTH = "Earth Element"
    WIND = "Wind Element"
    WATER = "Water Element"
    LIGHT = "Light Element"
    DARK = "Dark Element"


class GameWeaponsType:
    KTN = "KTN"
    OHS = "OHS"
    THS = "THS"
    HB = "HB"
    BW = "BW"
    BWG = "BWG"
    KNK = "KNK"
    MD = "MD"
    STF = "STF"
    DS = "DS"
    BH = "BH"
    
# class BodyArmorType:
#     Light="Light"
#     Normal = "Normal"
#     Heavy ="Heavy"
   
    
# WEAPON_STAT_CSPD_MULTIPLIER =[
#         {"weapon" : GameWeaponsType.OHS ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.THS ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.BW ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.BWG ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.STF ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.MD ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.KNK ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.HB ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.KTN ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.DS ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#         {"weapon" : GameWeaponsType.BH ,"base" : 0 ,"STR" : 0 , "AGI" : 1.16 , "INT":0 , "DEX" : 2.94, "VIT": 0},
#     ]
WEAPON_STAT_ASPD_MULTIPLIER =[
        {"weapon" :"OHS" ,"base" : 100 ,"STR" : 0.2 , "AGI" :4.2 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : "THS" ,"base" : 50 ,"STR" : 0.2 , "AGI" : 2.1 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : "BW" ,"base" : 75 ,"STR" : 0 , "AGI" : 3.1 , "INT":0 , "DEX" : 0.2, "VIT": 0},
        {"weapon" : "BWG" ,"base" : 30 ,"STR" : 0 , "AGI" : 2.2 , "INT":0 , "DEX" : 0.2, "VIT": 0},
        {"weapon" : "STF" ,"base" : 60 ,"STR" : 0 , "AGI" : 1.8, "INT":0.2 , "DEX" : 0, "VIT": 0},
        {"weapon" : "MD" ,"base" : 90 ,"STR" : 0 , "AGI" : 4 , "INT":0.2 , "DEX" : 0, "VIT": 0},
        {"weapon" : "KNK" ,"base" : 120 ,"STR" : 0.1 , "AGI" : 4.6 , "INT":0 , "DEX" : 0.1, "VIT": 0},
        {"weapon" : "HB" ,"base" : 25 ,"STR" : 0.2 , "AGI" : 3.5 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : "KTN" ,"base" : 200 ,"STR" : 0.3 , "AGI" : 3.9 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : "DS" ,"base" : 100 ,"STR" : 0.2 , "AGI" : 4.2 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : "BH" ,"base" : 1000 ,"STR" : 0 , "AGI" : 9.6 , "INT":0 , "DEX" : 0, "VIT": 0},
    ]
WEAPON_STAT_ATK_MULTIPLIER =[
        {"weapon" : GameWeaponsType.OHS ,"base" : 0 ,"STR" : 2 , "AGI" :0 , "INT":0 , "DEX" : 2, "VIT": 0},
        {"weapon" : GameWeaponsType.THS ,"base" : 0 ,"STR" : 3 , "AGI" : 0 , "INT":0 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.BW ,"base" : 0 ,"STR" : 1 , "AGI" : 0 , "INT":0 , "DEX" : 3, "VIT": 0},
        {"weapon" : GameWeaponsType.BWG ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":0 , "DEX" : 4, "VIT": 0},
        {"weapon" : GameWeaponsType.STF ,"base" : 0 ,"STR" : 3 , "AGI" : 0, "INT":1 , "DEX" : 0, "VIT": 0},
        {"weapon" : GameWeaponsType.MD ,"base" : 0 ,"STR" : 0 , "AGI" : 2 , "INT":2 , "DEX" : 0, "VIT": 0},
        {"weapon" : GameWeaponsType.KNK ,"base" : 0 ,"STR" : 0 , "AGI" : 2 , "INT":0 , "DEX" : 0.5, "VIT": 0},
        {"weapon" : GameWeaponsType.HB ,"base" : 0 ,"STR" : 2.5, "AGI" : 1.5 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : GameWeaponsType.KTN ,"base" : 0 ,"STR" :1.5, "AGI" : 0, "INT":0 , "DEX" : 2.5, "VIT": 0},
        {"weapon" : GameWeaponsType.DS ,"base" : 0 ,"STR" : 1 , "AGI" : 1, "INT":0 , "DEX" : 2, "VIT": 0},
        {"weapon" : GameWeaponsType.BH ,"base" : 0,"STR" : 1 , "AGI" :0, "INT":0 , "DEX" : 0, "VIT": 0},
    ]
WEAPON_STAT_MATK_MULTIPLIER =[
        {"weapon" : GameWeaponsType.OHS ,"base" : 0 ,"STR" : 0 , "AGI" :0 , "INT":3 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.THS ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":3 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.BW ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":3 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.BWG ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":3 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.STF ,"base" : 0 ,"STR" : 0 , "AGI" : 0, "INT":4 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.MD ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":4 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.KNK ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":4 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.HB ,"base" : 0 ,"STR" : 0, "AGI" : 1 , "INT":2 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.KTN ,"base" : 0 ,"STR" :0, "AGI" : 1, "INT":2 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.DS ,"base" : 0 ,"STR" : 0 , "AGI" : 0, "INT":3 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.BH ,"base" : 0 ,"STR" : 0 , "AGI" :0 , "INT":3 , "DEX" : 1, "VIT": 0},
    ]
WEAPON_STAT_STAB_MULTIPLIER =[
        {"weapon" : GameWeaponsType.OHS ,"base" : 0 ,"STR" : 0.025 , "AGI" :0 , "INT":0 , "DEX" : 0.075, "VIT": 0},
        {"weapon" : GameWeaponsType.THS ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":0 , "DEX" : 1, "VIT": 0},
        {"weapon" : GameWeaponsType.BW ,"base" : 0.05 ,"STR" : 0 , "AGI" : 0 , "INT":0, "DEX" : 0.05, "VIT": 0},
        {"weapon" : GameWeaponsType.BWG ,"base" : 0.05 ,"STR" : 0 , "AGI" : 0 , "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : GameWeaponsType.STF ,"base" : 0 ,"STR" : 0.05 , "AGI" : 0, "INT":0 , "DEX" : 0, "VIT": 0},
        {"weapon" : GameWeaponsType.MD ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":0 , "DEX" : 0.1, "VIT": 0},
        {"weapon" : GameWeaponsType.KNK ,"base" : 0 ,"STR" : 0 , "AGI" : 0 , "INT":0 , "DEX" : 0.025, "VIT": 0},
        {"weapon" : GameWeaponsType.HB ,"base" : 0 ,"STR" : 0.05, "AGI" : 0 , "INT":0 , "DEX" : 0.05, "VIT": 0},
        {"weapon" : GameWeaponsType.KTN ,"base" : 0.075 ,"STR" :0, "AGI" : 0, "INT":0 , "DEX" : 0.025, "VIT": 0},
        {"weapon" : GameWeaponsType.DS ,"base" : 0.025 ,"STR" : 0 , "AGI" : 0, "INT":0 , "DEX" : 0.075, "VIT": 0},
        {"weapon" : GameWeaponsType.BH ,"base" : 1 ,"STR" : 0 , "AGI" :0 , "INT": 0, "DEX" : 1/2.85, "VIT": 0},
    ]
# class GameSubWeaponsType:
#     SCROLL = "Scroll"
#     DAGGER = "DAGGER"
#     SHIELD = "SHIELD"
#     ARROW = "ARROW"

# The class the represent a Build                   
class Build:
    #constructeur
   
    def __init__(self,name):

        self.name = name
        self._main_weapon = None
        self._sub_weapon = None
        self._body_armor = None
        self._additional = None
        self._ring = None
        self._target = None
        self._consommables = []
        self._registlets = []
        self._passive_skills = []
        self._active_skills = []
        self._dps_skills = []
        
    
    
    def set_basic_stat(self, basicStats = {}):
        self.playerLevel = basicStats["playerLevel"]
        self.baseSTR = basicStats["baseSTR"]
        self.baseINT = basicStats["baseINT"]
        self.baseVIT = basicStats["baseVIT"]
        self.baseAGI = basicStats["baseAGI"]
        self.baseDEX = basicStats["baseDEX"]
        #PersonnalSTATLabel = ["None","TEC","MTL","LUK","CRT"]
        self.baseTEC = basicStats["personnalSTAT_Value"] if basicStats["PersonnalSTAT_Label"] == "TEC" else 0
        self.baseMTL = basicStats["personnalSTAT_Value"] if basicStats["PersonnalSTAT_Label"] == "MTL" else 0
        self.baseLUK = basicStats["personnalSTAT_Value"] if basicStats["PersonnalSTAT_Label"] == "LUK" else 0
        self.baseCRT = basicStats["personnalSTAT_Value"] if basicStats["PersonnalSTAT_Label"] == "CRT" else 0
     
    def set_food_buff(self, food_buff_dict):

        food_buff = {}
        for key, value in food_buff_dict.items():
            if "food_stat_" in key:
                stat = value
                value_key = key.replace("food_stat_", "food_value_")
                food_buff[stat] = food_buff_dict[value_key]

        self.food_buff = food_buff   
    # def init_total_stats (self):
    #     default_values = {
    #         "MaxMP": 100,
    #         "Attack MP Recovery":10
    #     }
    #     for stat in STATS_ARMOR:
    #         stat_name = stat.replace(" ", "_")  # Remplacer les espaces par des tirets bas
    #         setattr(self, stat_name, default_values.get(stat, 0))
    
    @property
    def main_weapon(self):
        return self._main_weapon
    @property
    def sub_weapon(self):
        return self._sub_weapon
    @property
    def body_armor(self):
        return self._body_armor
    @property
    def additional(self):
        return self._additional
    @property
    def ring(self):
        return self._ring
    
    @main_weapon.setter
    def main_weapon(self, value):
        if value is not None and not isinstance(value, Weapon):
            raise ValueError(f"Main Weapon Should be Instance of class Weapon but got {type(value)}")
        self._main_weapon = value
        
    @sub_weapon.setter
    def sub_weapon(self, value):
        if value is not None and not isinstance(value, SubWeapon):
            raise ValueError(f"Sub Weapon Should be Instance of class SubWeapon but got {type(value)}")
        self._sub_weapon = value

    @body_armor.setter
    def body_armor(self, value):
        if value is not None and not isinstance(value, BodyArmor):
            raise ValueError(f"Body Armor Should be Instance of class BodyArmor but got {type(value)}")
        self._body_armor = value

    @additional.setter
    def additional(self, value):
        if value is not None and not isinstance(value, Additionnal):
            raise ValueError(f"Additional Should be Instance of class Additionnal but got {type(value)}")
        self._additional = value

    @ring.setter
    def ring(self, value):
        if value is not None and not isinstance(value, Ring):
            raise ValueError(f"Ring Should be Instance of class Ring but got {type(value)}")
        self._ring = value
        
    @property
    def target(self):
        return self._target
    @target.setter
    def target(self,value : Target):
        self._target = value
    
    @property
    def consommables(self):
        return self._consommables
    @consommables.setter
    def consommables(self,value : list):
        #print("Value of Conso : ", value)
        if (value is not None and isinstance(value,list)):
            self._consommables = value
    
    @property
    def registlets(self):
        return self._registlets
    @registlets.setter
    def registlets(self,value : list):
        #print("Value of Conso : ", value)
        if (value is not None and isinstance(value,list)):
            self._registlets = value

    @property
    def passive_skills(self):# -> list[Skill]:
        skills = []
        for skill_info in self._passive_skills:
            skill_class = skill_info["skillClass"]
            lvl = skill_info["level"]
            ## ----------- Extremely Important ----------------- ##
            skills.append(skill_class(lvl,self))
        return skills
    @passive_skills.setter
    def passive_skills(self,value : list):
        #print("Value of Conso : ", value)
        if (value is not None and isinstance(value,list)):
            self._passive_skills = value
    
    @property
    def active_skills(self):#-> list[Skill]:
        skills = []
        for skill_info in self._active_skills:
            skill_class = skill_info["skillClass"]
            lvl = skill_info["level"]
            ## ----------- Extremely Important ----------------- ##
            skill = skill_class(lvl,self)
            
            skills.append(skill)
       
        return skills
    @active_skills.setter
    def active_skills(self,value : list):
        #print("Value of Conso : ", value)
        if (value is not None and isinstance(value,list)):
            self._active_skills = value
    
    @property
    def dps_skills(self):
        return self._dps_skills
    @dps_skills.setter
    def dps_skills(self,value : list):
        #print("Value of Conso : ", value)
        if (value is not None and isinstance(value,list)):
            self._dps_skills = value



    def build_meet_condition(self, condition):
        if condition is None:
            return True  # Si la condition est None, on considère qu'elle est toujours vraie

        # Vérification des conditions liées aux armes et armures
        for key, value in Equipment_label.items():
           
            if value == condition:
                
                if self.main_weapon and self.main_weapon.type == key:
                    return True
                if self.sub_weapon and self.sub_weapon.type == key:
                    return True
                if self.body_armor and self.body_armor.type == key:
                    return True
        return False
    
    def calculate_augmentation(self, stat_key):
        augmentation = 0
        # augmentation from equipment
        for equipment in [self.main_weapon, self.sub_weapon, self.body_armor, self.additional, self.ring]:
            if equipment:
                augmentation += equipment.stats.get(stat_key, 0)
                augmentation += sum(slot.stats.get(stat_key, 0) for slot in equipment.slots if slot)
                #print(f"equipment {equipment.type}, conditional stat {equipment.conditionnal_stats}")
                for stats in equipment.conditionnal_stats + (equipment.slots[0].conditionnal_stats if equipment.slots[0] else []) + (equipment.slots[1].conditionnal_stats if equipment.slots[1] else []):
    
                    for condition, values in stats.items():
                        # print("Build meet conditions : ",self.build_meet_condition(condition))
                        # print("Stat name", stat_key,"in",values,":", stat_key in values)
                        if self.build_meet_condition(condition) and stat_key in values:
                            augmentation += values[stat_key]

        # augmentation from consommables
        for conso in self.consommables:
            augmentation += conso.stats.get(stat_key, 0)
            
        # augmentation from registlet
        for reg in self.registlets:
            augmentation += reg.stats.get(stat_key, 0)
            
        for pskill in self.passive_skills:
            augmentation += pskill.passive_stats.get(stat_key, 0)

        for askill in self.active_skills:
            augmentation += askill.active_stats.get(stat_key, 0)

        return augmentation

    def calculate_percent_augmentation(self, stat_name):
        return self.calculate_augmentation(f"{stat_name} %")

    def calculate_direct_augmentation(self, stat_name):
        return self.calculate_augmentation(stat_name)

    def calculate_total_stat(self, stat_name, base_stat = None):
        direct_augmentation = self.calculate_direct_augmentation(stat_name)
        # food buff effect
        food_buff = self.food_buff.get(stat_name, 0)
        
        direct_augmentation += food_buff
        if (base_stat == None):
            return direct_augmentation

        percent_augmentation = self.calculate_percent_augmentation(stat_name)
        return floor( base_stat * (1 + percent_augmentation / 100) ) + direct_augmentation
    
    # Total Stat calc
    @property
    def totalSTR(self):
        return self.calculate_total_stat("STR",base_stat=self.baseSTR)
    @property
    def totalINT(self):
        return self.calculate_total_stat("INT",base_stat=self.baseINT)
    @property
    def totalVIT(self):
        return self.calculate_total_stat("VIT",base_stat=self.baseVIT)
    @property
    def totalAGI(self):
        return self.calculate_total_stat("AGI",base_stat=self.baseAGI)
    @property
    def totalDEX(self):
        return self.calculate_total_stat("DEX",base_stat=self.baseDEX)
    
    #Max HP calculation
    @property
    def baseHP(self) :
        return 93+floor((self.totalVIT+22.4)*self.playerLevel/3 )
    
    @property
    def totalHP(self):
        return self.calculate_total_stat("MaxHP",base_stat=self.baseHP)
        
    #Max MP calculation
    @property
    def totalMP(self) : 
        total_mp_from_equip = self.calculate_total_stat("MaxMP")
        return min(100 + self.playerLevel + floor(self.totalINT/10) + (self.baseTEC -1 if self.baseTEC > 0 else 0 )  + total_mp_from_equip, 2000 )
    
    #AMPR calculation
    @property
    def baseAMPR(self):
        return 10 + floor(self.totalMP/100)
    @property
    def totalAMPR (self) :
        return self.calculate_total_stat("Attack MP Recovery",base_stat=self.baseAMPR)
    
    # --- Critical ---
    @property
    def baseCriticalDamage (self):
        return 150 + floor(self.totalSTR/5) if self.totalSTR >= self.totalAGI else 150 + floor((self.totalSTR + self.totalAGI)/10)
    @property
    def totalCriticalDamage(self):
        totalCD = self.calculate_total_stat("Critical Damage", base_stat=self.baseCriticalDamage)
        return totalCD if totalCD <= 300 else 300 + floor((totalCD - 300)/2)
    
    @property
    def totalMagicCriticalDamageRatio(self):
        ratio = 50
        
        return ratio
    
    @property
    def totalMagicCriticalDamage(self):
        return 100 + floor( (self.totalCriticalDamage - 100) * self.totalMagicCriticalDamageRatio/100 )
    
    
    @property
    def totalMagicCriticalRateRatio(self):
        ratio = 0
        if self.main_weapon and self.main_weapon.type in MAGIC_WEAPON_TYPE :
            ratio += 25 if self.currentElement is None else 0
    
        return ratio

    @property
    def totalMagicCriticalRate(self):
        return floor (self.totalCriticalRate * self.totalMagicCriticalRateRatio)
    
    @property
    def baseCriticalRate(self):
        return 25 + floor(self.baseCRT / 3.4 )
    @property
    def totalCriticalRate(self):
        return self.calculate_total_stat("Critical Rate", base_stat=self.baseCriticalRate)
    
    # --- Accuracy ---
    @property
    def baseAccuracy(self):
        return self.playerLevel + self.totalDEX
    @property
    def totalAccuracy(self):
        return self.calculate_total_stat("Accuracy", base_stat=self.baseAccuracy)
    
    # --- Dodge --- 
    @property
    def baseDodge(self):
        flee_factor = 1 # normal armor
        if self.body_armor == None :
            flee_factor = 2
        elif self.body_armor.type == BODY_ARMOR_TYPE[0]: # "Light"
            flee_factor = 1.75
        elif self.body_armor.type == BODY_ARMOR_TYPE[2]: # "heavy armor"
            flee_factor = 0.75
        return (self.playerLevel + self.totalAGI ) * flee_factor
    @property
    def totalDodge(self):
        return self.calculate_total_stat("Dodge", base_stat=self.baseDodge)
    
    # --- ASPD & Motion ---
    def calculate_stat_from_attribute(self, entry):
        return entry["base"] + floor (entry["STR"] * self.totalSTR + entry["AGI"] * self.totalAGI + entry["INT"] * self.totalINT + entry["DEX"] * self.totalDEX + entry["VIT"] * self.totalVIT)

    @property
    def baseASPD(self):
        if self.main_weapon is None: 
            entry = WEAPON_STAT_ASPD_MULTIPLIER[-1] 
            return self.calculate_stat_from_attribute(entry) + self.playerLevel
        
        for entry in WEAPON_STAT_ASPD_MULTIPLIER:
            if entry["weapon"] == self.main_weapon.type:
                return self.calculate_stat_from_attribute(entry) + self.playerLevel
        return 0 + self.playerLevel
    @property
    def totalASPD (self):
        return self.calculate_total_stat("ASPD",base_stat=self.baseASPD)
    
    @property
    def totalMotion (self):
        
        return min(floor((self.totalASPD - 1000)/180) +  self.calculate_total_stat("Motion Speed %"), 50) if self.totalASPD >1000 else 0
    
    # --- CSPD ---
    @property
    def baseCSPD(self):
        return floor( self.totalAGI * 1.16 + self.totalDEX * 2.94 + self.playerLevel)
    @property
    def totalCSPD(self):
        return self.calculate_total_stat("CSPD",base_stat=self.baseCSPD)
    
    @property
    def totalCSPD_Reduction (self):
        
        return (min(floor((self.totalCSPD - 1000)/180), 50) + 50) if self.totalCSPD >1000 else max( self.totalCSPD/20 , 0 ) 
    # --- ATK / MATK ---

    @property
    def totalWATK(self):
        if self.main_weapon == None:
            return 0
        
        return self.main_weapon.totalWATK + self.calculate_total_stat("Weapon ATK",base_stat=self.main_weapon.WATK)
    
    @property
    def baseATK(self):
        if self.main_weapon is None: 
            entry = WEAPON_STAT_ATK_MULTIPLIER[-1] 
            return self.calculate_stat_from_attribute(entry)+ self.playerLevel + self.totalWATK
        
        for entry in WEAPON_STAT_ATK_MULTIPLIER:
            if entry["weapon"] == self.main_weapon.type:
                return self.calculate_stat_from_attribute(entry)+ self.playerLevel + self.totalWATK
        
        return self.playerLevel + self.totalWATK
    @property
    def totalStability(self):
        
        if self.main_weapon is None: 
            entry = WEAPON_STAT_STAB_MULTIPLIER[-1] 
            return max( self.calculate_stat_from_attribute(entry) + self.calculate_total_stat("Stability %"),0)
        
        for entry in WEAPON_STAT_STAB_MULTIPLIER:
            if entry["weapon"] == self.main_weapon.type:
                return max (self.calculate_stat_from_attribute(entry) + self.main_weapon.stability + self.calculate_total_stat("Stability %"),0)
        
        return 0
    
    @property
    def totalMagicStability(self):
        return floor((100 + self.totalStability)/2)
    
    @property
    def totalATK(self):
        return self.calculate_total_stat("ATK", base_stat=self.baseATK)
    
    @property
    def baseMATK(self):
      
        if self.main_weapon is None: 
            entry = WEAPON_STAT_MATK_MULTIPLIER[-1] 
            return self.calculate_stat_from_attribute(entry) + self.playerLevel
        
        matk_watk = 0 
        
        if self.main_weapon.type in MAGIC_WEAPON_TYPE :
            matk_watk = self.totalWATK
        elif self.main_weapon.type == "KNK" :
            matk_watk = floor(self.totalWATK/2)
    
        for entry in WEAPON_STAT_MATK_MULTIPLIER:
            if entry["weapon"] == self.main_weapon.type:
                return self.calculate_stat_from_attribute(entry)+ self.playerLevel + matk_watk 
        
        return matk_watk
    
    @property
    def totalMATK(self):
        return self.calculate_total_stat("MATK", base_stat=self.baseMATK)
    
    @property
    def totalSRD(self):
        return self.calculate_total_stat("Short Range Damage %")
    
    @property
    def totalLRD(self):
        return self.calculate_total_stat("Long Range Damage %")
    
    @property
    def totalPhysicalPierce(self):
        return self.calculate_total_stat("Physical Pierce %")
    @property
    def totalMagicPierce(self):
        return self.calculate_total_stat("Magic Pierce %")
    
    
    #"Unsheathe Attack","Unsheathe Attack %",
    
    @property
    def totalUnsheathe_attack_flat(self):
        return self.calculate_total_stat("Unsheathe Attack")
    @property
    def totalUnsheathe_attack_percent(self):
        return self.calculate_total_stat("Unsheathe Attack %")
    # "% stronger against Fire","% stronger against Water","% stronger against Wind","% stronger against Earth",
    # "% stronger against Light","% stronger against Dark",
    
    @property
    def currentElement(self):
        if self.main_weapon is None:
            return None
        
        return self.main_weapon.awakenElement
    
    @property
    def totalINT_DTE(self):
        
        return floor(self.baseINT/10) if self.main_weapon is not None and self.main_weapon.type in MAGIC_WEAPON_TYPE and self.currentElement is not None else 0
    
    
    @property
    def totalDTE_Fire(self):
        return self.calculate_total_stat("% stronger against Fire") + (25 if self.currentElement == GameElements.WATER else 0) + self.totalINT_DTE
    @property
    def totalDTE_Water(self):
        return self.calculate_total_stat("% stronger against Water")+ (25 if self.currentElement == GameElements.WIND else 0) + self.totalINT_DTE
    @property
    def totalDTE_Wind(self):
        return self.calculate_total_stat("% stronger against Wind")+ (25 if self.currentElement == GameElements.EARTH else 0) + self.totalINT_DTE
    @property
    def totalDTE_Earth(self):
        return self.calculate_total_stat("% stronger against Earth")+ (25 if self.currentElement == GameElements.FIRE else 0) + self.totalINT_DTE
    @property
    def totalDTE_Light(self):
        return self.calculate_total_stat("% stronger against Light")+ (25 if self.currentElement == GameElements.DARK else 0) + self.totalINT_DTE
    @property
    def totalDTE_Dark(self):
        return self.calculate_total_stat("% stronger against Dark")+ (25 if self.currentElement == GameElements.LIGHT else 0) + self.totalINT_DTE
    @property
    def totalDTE_Neutral(self):
        return self.calculate_total_stat("% stronger against Neutral") + self.totalINT_DTE
    
    # "Fire Resistance %","Water Resistance %","Wind Resistance %","Earth Resistance %",
    # "Light Resistance %","Dark Resistance %",
    
    @property
    def totalFire_Resistance(self):
        return self.calculate_total_stat("Fire Resistance %")
    @property
    def totalWater_Resistance(self):
        return self.calculate_total_stat("Water Resistance %")
    @property
    def totalWind_Resistance(self):
        return self.calculate_total_stat("Wind Resistance %")
    @property
    def totalEarth_Resistance(self):
        return self.calculate_total_stat("Earth Resistance %")
    @property
    def totalLight_Resistance(self):
        return self.calculate_total_stat("Light Resistance %")
    @property
    def totalDark_Resistance(self):
        return self.calculate_total_stat("Dark Resistance %")
    @property
    def totalNeutral_Resistance(self):
        return self.calculate_total_stat("Neutral Resistance %")
    
    
    # "% stronger against Neutral","Neutral Resistance %","Neutral Element",
    
    #"Physical Resistance %","Magic Resistance %",
    @property
    def totalPhysical_Resistance(self):
        return self.calculate_total_stat("Physical Resistance %")
    @property
    def totalMagic_Resistance(self):
        return self.calculate_total_stat("Magic Resistance %")
    
     # "Physical Barrier","Magic Barrier","Fractional Barrier %","Reflect %",
    # "Barrier Cooldown %","Revive Time %",
    # "Ailment Resistance %","Guard Power %","Guard Recharge %","Evasion Recharge %","Aggro %",
    # "Anitcipate %","Guard Break %",
    
    @property
    def totalAilmentResistance(self):
        return self.calculate_total_stat("Ailment Resistance %")
    @property
    def totalAggro(self):
        return self.calculate_total_stat("Ailment Resistance %")
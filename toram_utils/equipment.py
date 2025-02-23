from math import floor
# Define Equipment like its in Toram

# As Equipment, We have Weapons, Armor, Crystas

STATS = [
    # --------------- Player STAT -------------------#
    "STR","STR %","INT","INT %","VIT","VIT %","AGI","AGI %","DEX","DEX %", 
    
    # --------------- HP, MP -------------------#
    "Natural HP Regen","Natural HP Regen %","Natural MP Regen","Natural MP Regen %",
    "MaxHP","MaxHP %","MaxMP","MaxMP %","Attack MP Recovery","Attack MP Recovery %",
    
    # --------------- ATK , MATK , SRD, LRD, Unsheathe, Stab, PP, MP -------------------#
    "ATK","ATK %","MATK","MATK %","Weapon ATK","Weapon ATK %",
    "Short Range Damage %","Long Range Damage %",
    "Unsheathe Attack","Unsheathe Attack %",
    "Stability %", "Physical Pierce %","Magic Pierce %",
    
    # --------------- DEF,MDEF, Resists,Barrier -------------------#
    "DEF","DEF %","MDEF","MDEF %",
    "Physical Resistance %","Magic Resistance %",
    "Physical Barrier","Magic Barrier","Fractional Barrier %","Reflect %",
    "Barrier Cooldown %","Revive Time %",
    "Ailment Resistance %","Guard Power %","Guard Recharge %","Evasion Recharge %","Aggro %",
    "Anitcipate %","Guard Break %",
    
    # --------------- Acc, Dodge, ASPD, CSPD -------------------#
    "Accuracy","Accuracy %","Dodge","Dodge %",
    "ASPD","ASPD %","CSPD","CSPD %","Motion Speed %",
    
    # --------------- Critical -------------------#
    "Critical Rate","Critical Rate %","Critical Damage","Critical Damage %",
    
    # --------------- Elements -------------------#
    "Fire Element","Water Element","Wind Element","Earth Element",
    "Light Element","Dark Element",
    "% Damage To Fire","% Damage To Water","% Damage To Wind","% Damage To Earth",
    "% Damage To Light","% Damage To Dark",
    "Fire Resistance %","Water Resistance %","Wind Resistance %","Earth Resistance %",
    "Light Resistance %","Dark Resistance %",
    
    "% Damage To Neutral","Neutral Resistance %","Neutral Element",
    
    # --------------- Reduce DMG -------------------#v
    "Reduce Dmg (Player Epicenter) %","Reduce Dmg (Foe Epicenter) %","Reduce Dmg (Floor) %",
    "Reduce Dmg (Charge) %","Reduce Dmg (Bullet) %","Reduce Dmg (Bowling) %",
    "Reduce Dmg (Meteor) %","Reduce Dmg (Straight Line) %",
    
    "Reduce Vortex %","Reduce Explosion %","Tumble Unavailable", "Flinch Unavailable","Stun Unavailable","EXP Gain %","Drop Rate %",
    "Additional Melee %","Additional Magic %"
]
AWAKEN_ELEMENT = ["Fire Element","Water Element","Wind Element","Earth Element",
    "Light Element","Dark Element"]
STATS_ARMOR = [stat for stat in STATS if stat not in AWAKEN_ELEMENT]

FOOD_BUFF_STAT = ["MaxHP","MaxMP","Critical Rate","Attack MP Recovery","STR","INT","VIT","AGI","DEX","ATK","MATK","Weapon ATK","Physical Resistance %","Magic Resistance %","% Damage To Fire","% Damage To Water","% Damage To Wind","% Damage To Earth",
    "% Damage To Light","% Damage To Dark","% Damage To Neutral","EXP Gain %","Drop Rate %","Fire Resistance %","Water Resistance %","Wind Resistance %","Earth Resistance %",
    "Light Resistance %","Dark Resistance %","Neutral Resistance %","Physical Barrier","Magic Barrier","Fractional Barrier %","Aggro %","Aggro -%","Accuracy","Dodge"]


INTERUPT_UNAVAILABLE = ["Tumble Unavailable", "Flinch Unavailable","Stun Unavailable"]



WEAPON_TYPE =["OHS","THS","KTN","HLB","STF","MD","KNK","BW","BWG"]

PURE_SUB_WEAPON = ["Scroll","Dagger","Arrow","Shield"]
POSSIBLE_SUB = ["OHS","KTN","KNK","MD"] + PURE_SUB_WEAPON
REFINABLE_SUB = ["OHS","KTN","KNK","Shield","MD"]
Equipment_label = {
    "OHS":"One Hand Sword",
    "THS": "Two Hand Sword",
    "KTN":"Katana",
    "HLB":"Halberd",
    "STF":"Staff",
    "MD":"Magic Device",
    "KNK": "Knuckle",
    "BW": "Bow",
    "BWG":"Arrow",
    "Scroll": "Ninjutsu Scroll",
    "Dagger": "Dagger",
    "Arrow": "Arrow",
    "Shield": "Shield",
    "HeavyArmor" : "Heavy Armor",
    "LightArmor": "Light Armor",
}
class EquipmentType :
    OHS ="OHS"
    THS ="THS"
    KTN="KTN"
    HB="HLB"
    STF="STF"
    MD="MD"
    KNK="KNK"
    BW="BW"
    BWG="BWG"
    SCROLL="Scroll"
    DAGGER="Dagger"
    ARROW="Arrow"
    SHIELD="Shield"
    HEAVY_ARMOR="HeavyArmor" 
    LIGHT_ARMOR="LightArmor"
    
MAGIC_WEAPON_TYPE = ["STF","MD"]
STAT_CONDITIONS = [None] +  list(Equipment_label.values())
ARMOR_TYPE = ["BodyArmor","Additonnal","Ring"]

BODY_ARMOR_TYPE = ["Light","Normal","Heavy"]

EQUIPMENT_TYPE = ["Weapon"] + ARMOR_TYPE
XTALL_TARGET = ["All"] + EQUIPMENT_TYPE


WEAPON_BASE_RANGE = {
    "OHS": 2,
    "THS":3,
    "KTN":2,
    "HLB":4,
    "STF": 2,
    "MD":6,
    "KNK":1,
    "BW":10,
    "BWG":8
}

# weapon = {
#     "name":"9th anniv sword",
#     "WATK": 550,
#     "type": "OHS",
#     "stats":{
#         "ATK%":14,
#         "STR%":10,
#         "CD%":20,
#         "CD":200
#     },
#     "slot_1":None,
#     "slot_2":None
    
#     }

# equipment = {
#     "name":"9th anniv Armor",
#     "DEF": 350,
#     "type":"Armor",
#     "stats":{
#         "physical_resistance":20,
#         "magic_resistance":20,
#         "max_hp":20,
#         "max_mp":200
#     },
#     "slot_1": None,
#     "slot_2": None
# }

# conditionnal_stats = [
#     {
#         "OHS" : {
#             "ATK %" : 5
#         }
#     }
# ]
REFINE_LABELS = [0,"+1","+2","+3","+4","+5","+6","+7","+8","+9","+E","+D","+C","+B","+A","+S"]

class EquipmentBase :
    def __init__(self, stats = {}, refine = 15,name="",slots =[],conditionnal_stats = []):
        self.stats =stats
        self.conditionnal_stats = conditionnal_stats
        self.slots = slots
        self.refine = refine
        self.name = name

    def to_dict(self):
        return {
            "stats": self.stats,
            "conditionnal_stats": self.conditionnal_stats,
            "slots": [slot.to_dict() if hasattr(slot, "to_dict") else slot for slot in self.slots],
            "refine": self.refine,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 15),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )
    

class Crysta :
    def __init__(self, name= "", stats={} , target = XTALL_TARGET[0],conditionnal_stats = []):
        self.name = name
        self.target = target
        self.stats=stats
        self.conditionnal_stats = conditionnal_stats
        
    def to_dict(self):
        return {
            "name": self.name,
            "stats": self.stats,
            "target": self.target,
            "conditionnal_stats": self.conditionnal_stats
        }

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            name=dict_obj.get("name", ""),
            stats=dict_obj.get("stats", {}),
            target=dict_obj.get("target", XTALL_TARGET[0]),
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )

class Weapon(EquipmentBase) :
    def __init__(self,type = "OHS", baseWATK = 550, WATK = 550, stats = {}, refine=15, stability=80,name="",slots =[], conditionnal_stats = [], max_range = None):
        super().__init__(stats=stats,refine=refine,name=name,slots = slots,conditionnal_stats = conditionnal_stats)
        self.baseWATK = baseWATK
        self.WATK = WATK
        self.type = type
        self.stability = stability
        self.awakenElement = None
        self.max_range = max_range if max_range else WEAPON_BASE_RANGE[self.type]
        self.set_element()
    
    def set_element(self):
        for stat,value in self.stats.items():
            if stat in AWAKEN_ELEMENT :
                self.awakenElement = stat
                return True

    @property    
    def totalWATK(self):
        return floor(self.baseWATK * (1+(self.refine * self.refine)/100)) + self.refine
    
    def to_dict(self):
        dict_obj = super().to_dict()
        dict_obj.update({
            "type": self.type,
            "baseWATK": self.baseWATK,
            "WATK": self.WATK,
            "stability": self.stability
        })
        return dict_obj

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            type=dict_obj.get("type", "OHS"),
            baseWATK=dict_obj.get("baseWATK", 550),
            WATK=dict_obj.get("WATK", 550),
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 15),
            stability=dict_obj.get("stability", 80),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )

class SubWeapon(EquipmentBase):
    def __init__(self, stats = {}, refine=0, name="", slots=[None,None], conditionnal_stats=[], type = "Shield",baseDEF=0, baseWATK = 0, baseStability =0, scrollCastTimeRed = 0, scrollMPRed = 0):
        super().__init__(stats=stats, refine=refine, name=name, slots=slots, conditionnal_stats=conditionnal_stats)
        self.type = type
        self.baseDEF = baseDEF
        self.baseWATK = baseWATK
        self.baseStability = baseStability
        self.scrollCastTimeRed = scrollCastTimeRed
        self.scrollMPRed = scrollMPRed
        self.awakenElement = None
        self.set_element()
    
    def set_element(self):
        for stat,value in self.stats.items():
            if stat in AWAKEN_ELEMENT :
                self.awakenElement = stat
                return True
        
    def to_dict(self):
        return {
            "baseDEF": self.baseDEF,
            "baseStability": self.baseStability,
            "baseWATK": self.baseWATK,
            "conditionnal_stats": self.conditionnal_stats,
            "name": self.name,
            "refine": self.refine,
            "scrollCastTimeRed": self.scrollCastTimeRed,
            "scrollMPRed": self.scrollMPRed,
            "slots": self.slots,
            "stats": self.stats,
            "type": self.type,
        }

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj is None:
            return None
        return cls(
            baseDEF=dict_obj.get("baseDEF", 0),
            baseStability=dict_obj.get("baseStability", 0),
            baseWATK=dict_obj.get("baseWATK", 0),
            conditionnal_stats=dict_obj.get("conditionnal_stats", []),
            name=dict_obj.get("name", ""),
            refine=dict_obj.get("refine", 0),
            scrollCastTimeRed=dict_obj.get("scrollCastTimeRed", 0),
            scrollMPRed=dict_obj.get("scrollMPRed", 0),
            slots=dict_obj.get("slots", [None,None]),
            stats=dict_obj.get("stats", {}),
            type=dict_obj.get("type", ""),
        )
# Armor 
class ArmorLike(EquipmentBase):
   
    def __init__(self, DEF= 0, stats={}, refine = 15,name="",slots =[],conditionnal_stats = []):
        super().__init__(stats= stats,refine=refine, name=name, slots=slots,conditionnal_stats = conditionnal_stats)
        self.DEF = DEF
    def to_dict(self):
        dict_obj = super().to_dict()
        dict_obj.update({
            "DEF": self.DEF
        })
        return dict_obj

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            DEF=dict_obj.get("DEF", 0),
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 15),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )
        
class BodyArmor (ArmorLike):
    
    def __init__(self,stats={}, refine = 15,DEF=0, type="Normal",name="",slots =[],conditionnal_stats = []):
        super().__init__(stats=stats, refine = refine,DEF=DEF,name=name,slots=slots,conditionnal_stats = conditionnal_stats)
        self.type = type # "Light", "Normal", "Heavy"
    def to_dict(self):
        dict_obj = super().to_dict()
        dict_obj.update({
            "type": self.type
        })
        return dict_obj

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 15),
            DEF=dict_obj.get("DEF", 0),
            type=dict_obj.get("type", "Normal"),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )
class Additionnal(ArmorLike):
    def __init__(self, stats={}, refine = 15,DEF=0,name="",slots =[],conditionnal_stats = []):
        super().__init__(stats=stats, refine = refine,DEF=DEF,name=name,slots =slots,conditionnal_stats = conditionnal_stats)
    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 15),
            DEF=dict_obj.get("DEF", 0),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )
class Ring(ArmorLike):
    def __init__(self,stats={}, refine = 0,DEF=0,name="",slots =[],conditionnal_stats = []):
        super().__init__(stats=stats,refine=refine,DEF=DEF,name=name,slots=slots,conditionnal_stats = conditionnal_stats)
    
    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj == None :
            return None
        return cls(
            stats=dict_obj.get("stats", {}),
            refine=dict_obj.get("refine", 0),
            DEF=dict_obj.get("DEF", 0),
            name=dict_obj.get("name", ""),
            slots=[Crysta.from_dict(slot) if isinstance(slot, dict) else slot for slot in dict_obj.get("slots", [])],
            conditionnal_stats=dict_obj.get("conditionnal_stats", [])
        )

class Target :
    def __init__(self):
        self.element = None
        self.DEF = 0
        self.MDEF = 0
        self.dodge = 0
        self.critical_resist = 0
        self.physical_resistance = 0
        self.magic_resistance = 0
        self.level = 1
        self.name = "Raffy"

class Monster(Target):
    def __init__(self):
        super().__init__()
        
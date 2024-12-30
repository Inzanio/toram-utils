from helpers.firestore import get_all_data,db
import streamlit as st

registlet_db = "regislet"

RegisletNames = ["Max MP Boost","Max HP Boost","Magic Attack Boost","Physical Attack Boost","Physical Defense Boost","Magic Defense Boost"
                ,"Attack Speed Boost", "Magic Speed Boost"
                ]

REGISTLET_STAT = ["MaxHP","MaxMP","ATK","MATK","DEF","MDEF","ASPD","CSPD"]
class Registlet :
    def __init__(self, name : str, level = 0, stat_per_level=0 , maxlevel=0, stats ={}, effects = {} , description = ""):
        self.name = name
        self.level = level
        self.maxlevel = maxlevel
        self._stats = stats
        self.effects = effects
        self.stat_per_level = stat_per_level
        self.description = description

    @property
    def stats(self):
        d = {}
        for key,value in self._stats.items():
            d[key] = self.stat_per_level * self.level
        return d
    
    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "maxlevel": self.maxlevel,
            "stats": self.stats,
            "stat_per_level": self.stat_per_level,
            "description": self.description,
            "effects": self.effects
        }

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            name=dict_obj.get("name", ""),
            level=dict_obj.get("level", 0),
            maxlevel=dict_obj.get("maxlevel", 1),
            stats=dict_obj.get("stats", {}),
            stat_per_level=dict_obj.get("stat_per_level", 1),
            description = dict_obj.get("description", ""),
            effects = dict_obj.get("effects", {}),
        )

def add_registlet(regs : Registlet):
    
    doc_ref = db.collection(registlet_db).document(regs.name)
    doc_ref.set(regs.to_dict())
    get_all_data.clear(registlet_db)
    load_registlets()


def load_registlets():
    
    # Create a reference to the Google post.
    st.session_state.regisltets = []
    docs = get_all_data(registlet_db)
    for doc in docs:
        st.session_state.regisltets.append(Registlet.from_dict(doc))
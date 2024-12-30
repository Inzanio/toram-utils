from helpers.firestore import get_all_data,db
import streamlit as st

consommables_db = "consommables"

class ConsommableType:
    HP_BOOST = "HP Boost"
    MP_BOOST = "MP Boost"
    ATK_BOOST = "ATK Boost"
    MATK_BOOST = "MATK Boost"
    ACCURACY_BOOST = "Accuracy Boost"
    DODGE_BOOST = "Dodge Boost"
    PHYSICAL_DEFENSE_BOOST = "Physical Defense Boost"
    MAGIC_DEFENSE_BOOST = "Magic Defense Boost"
    MP_RECOVERY_BOOST = "MP Recovery Boost"
    HP_RECOVERY_BOOST = "HP Recovery Boost"
    ASPD_BOOST = "ASPD Boost"
    CSPD_BOOST = "CSPD Boost"
    ELEMENT_BOOST = "Element Boost"
    ELEMENT_RESISTANCE_BOOST = "Element Resistance Boost"

    @classmethod
    def list(cls):
        return [getattr(cls, attr) for attr in dir(cls) if not attr.startswith('__') and not callable(getattr(cls, attr))]
    
class Consommable :
    
    def __init__(self, type: str, name: str , stats :dict):
        self.name = name
        self.type = type
        self.stats = stats
        
    def to_dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "stats": self.stats
        }

    @classmethod
    def from_dict(cls, dict_obj):
        if dict_obj is None:
            return None
        return cls(
            type=dict_obj.get("type", ""),
            name=dict_obj.get("name", ""),
            stats=dict_obj.get("stats", {})
        )

def add_consommable(conso : Consommable):
    
    doc_ref = db.collection(consommables_db).document(conso.name)
    doc_ref.set(conso.to_dict())
    get_all_data.clear(consommables_db)
    load_consommables()

import streamlit as st


def load_consommables():
    
    # Create a reference to the Google post.
    st.session_state.consommables = []
    docs = get_all_data(consommables_db)
    for doc in docs:
        st.session_state.consommables.append(Consommable.from_dict(doc))
import streamlit as st
from toram_utils.equipment import FOOD_BUFF_STAT
from helpers.firestore import db, get_all_data

food_buff_db = "food_buffs"

class FoodBuff :
    def __init__(self, stat_names:list,code,owner_name="", levels = [10,10]):
        self.stat_names = stat_names
        self.code = code
        self.owner_name = owner_name
        self.levels = levels
    def to_dict(self):
        return {
            "stat_names": self.stat_names,
            "code": self.code,
            "owner_name": self.owner_name,
            "levels": self.levels
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            stat_names=data.get("stat_names"),
            code=data.get("code"),
            owner_name=data.get("owner_name", ""),  # Utiliser get() pour éviter KeyError
            levels=data.get("levels", [10,10])  # Utiliser get() pour éviter KeyError et utiliser la valeur par défaut si nécessaire
        )
def add_food_buff(food_buff : FoodBuff):
    
    doc_ref = db.collection(food_buff_db).document(food_buff.code)
    doc_ref.set(food_buff.to_dict())
    get_all_data.clear(food_buff_db)
    
    load_food_buffs()


def load_food_buffs():
    
    #Create a reference to the Google post.
    st.session_state.food_buffs = []
    docs = get_all_data(food_buff_db)
    for doc in docs:
        st.session_state.food_buffs.append(FoodBuff.from_dict(doc))

import streamlit as st
from toram_utils import Crysta
from helpers.firestore import get_all_data,db

def init():
    
    if "ontest" not in st.session_state :
        st.session_state.ontest = False
    
    if "playerLevel" not in st.session_state :
        st.session_state.playerLevel = 290
    if "currentCrystaStat" not in st.session_state :
        st.session_state.currentCrystaStat = {}
    if "currentCrystaConditionnalStat" not in st.session_state :
        st.session_state.currentCrystaConditionnalStat = []
    if "weapons" not in st.session_state :
        st.session_state.weapons = [None]
    if "subWeapons" not in st.session_state :
        st.session_state.subWeapons = [None]
    if "bodyArmors" not in st.session_state:
        st.session_state.bodyArmors = [None]
    if "additionnals" not in st.session_state:
        st.session_state.additionnals = [None]
    if "rings" not in st.session_state:
        st.session_state.rings = [None]
    if "crystas" not in st.session_state : 
        st.session_state.crystas = []
    if "foodBuffStat" not in st.session_state :
        st.session_state.foodBuffStat = {}
    if "currentMainWeapon" not in st.session_state : 
        st.session_state.currentMainWeapon = None
    if "currentSubWeapon" not in st.session_state : 
        st.session_state.currentSubWeapon = None
    if "currentBodyArmor" not in st.session_state : 
        st.session_state.currentBodyArmor = None
    if "currentAdditionnal" not in st.session_state : 
        st.session_state.currentAdditionnal = None
    if "currentRing" not in st.session_state : 
        st.session_state.currentRing = None
    if "currentConsoStat" not in st.session_state :
        st.session_state.currentConsoStat = {}
    if "consommables" not in st.session_state :
        st.session_state.consommables = []
    if "selected_consommables" not in st.session_state :
        st.session_state.selected_consommables = []
    if "regisltets" not in st.session_state :
        st.session_state.regisltets = []
    if "selected_regisltets" not in st.session_state :
        st.session_state.selected_regisltets = []
    if "currentRegistletStat" not in st.session_state :
        st.session_state.currentRegistletStat = {}
    if "selected_skills" not in st.session_state :
        st.session_state.selected_skills = []
    if "selected_passive_skills" not in st.session_state :
        st.session_state.selected_passive_skills = []
    if "selected_active_skills" not in st.session_state :
        st.session_state.selected_active_skills = []
    if "selected_dps_skills" not in st.session_state :
        st.session_state.selected_dps_skills = []
    if "food_buffs" not in st.session_state :
        st.session_state.food_buffs = []  
    if "special_items_prices" not in st.session_state :
        st.session_state.special_items_prices = {}  
    
    st.session_state.currentEquipmentStat = {}
    st.session_state.currentEquipmentConditonnalStat = []
    # if "ontest" not in st.session_state :
    #     st.session_state.ontest = True
def persist_session_data():
    init()
    for key in st.session_state:
        st.session_state[key] = st.session_state[key]
        
crystas_db = "crystas"

def load_crytas():
    # Create a reference to the Google post.
    st.session_state.crystas = []
    docs = get_all_data(crystas_db)
    for doc in docs:
        st.session_state.crystas.append(Crysta.from_dict(doc))
        
    
# def save_crystas():
#     if "crystas" in st.session_state : 
#         save_element(st.session_state.crystas,"crystas.joblib")
#     else :
#         st.error("Failed to Saved the crystas Data, because 'crystas' don't exist in st.session_state")
    
def add_crysta(crysta : Crysta):
    
    doc_ref = db.collection("crystas").document(crysta.name)
    doc_ref.set(crysta.to_dict())
    get_all_data.clear(crystas_db)
    load_crytas()


def under_developement(): 
    st.write("⚠️:red[UNDER DEVELOPMENT]⚠️")
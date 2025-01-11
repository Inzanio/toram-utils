from helpers.firestore import db, get_all_data
import streamlit as st
weapon_type = ["OHS","THS","KTN","HLB","STF","MD","KNK","BW","BWG"]

PIERCERS= ["Piercer " + weapon for weapon in weapon_type] + ["Fairy Silk", "Spiril Needle", "High-Grade Ornament"]
PRIME_PIERCERS = ["PRIME Piercer " + weapon for weapon in weapon_type] + ["Legendary Piercer","Legendary Silk", "Legendary Needle", "Legendary Ornament"]

ALL_PIERCERS = PIERCERS + PRIME_PIERCERS

SPECIALS_ITEMS = ALL_PIERCERS + ["Extraction Crysta"]
prices_db = "prices"


class PricesList :

    def __init__(self, name = "",prices= {}):
        self.name = name
        self.prices =prices
        
    def to_dict(self):
        
        return {
            "name": self.name,
            "prices": self.prices
        }

    @classmethod
    def from_dict(cls, data):
        name = data.get("name", "")
        prices = data.get("prices", {})

        return cls(name=name, prices=prices)
    
def add_price(pl : PricesList):
    doc_ref = db.collection(prices_db).document(pl.name)
    
    doc_ref.set(pl.to_dict())
    get_all_data.clear(prices_db)
    load_special_items_prices()
    
def load_special_items_prices():
    # Create a reference to the Google post.
    st.session_state.special_items_prices = {}
    docs = get_all_data(prices_db)
    for doc in docs:
        if doc["name"] in SPECIALS_ITEMS :
            st.session_state.special_items_prices[doc["name"]] = PricesList.from_dict(doc)
            
def format_price(price):
    return "{:,}".format(int(price))
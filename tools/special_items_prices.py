import streamlit as st
from toram_utils.prices_list import SPECIALS_ITEMS,format_price
from helpers.session import persist_session_data
persist_session_data()

col1,col2 = st.columns([8,4],vertical_alignment="top")
col1.title("🎀Looking for an item price ?")
col2.image("./img/toram-utils-retainer_doll.png",width=180)
item_name = st.selectbox("💡Select the Special Item you wanna know the current price", options=SPECIALS_ITEMS)

item = st.session_state.special_items_prices.get(item_name)

if (item) :
# Trouver le prix le plus courant
    current_price = min(item.prices.values(), key=lambda x: float(x))

    # Calculer 10% du prix le plus courant
    pourcentage = 0.1
    delta = float(current_price) * pourcentage

    # Calculer l'intervalle
    intervalle_inf = int(current_price) - int(delta)
    intervalle_sup = int(current_price)

 
    st.write(f"👉You may have it beetween 💵:green[{format_price(intervalle_inf)}S] and :blue[{format_price(intervalle_sup)}S]💸")
    
    with st.expander("See Demand price Evolution") :
        import pandas as pd
        df = pd.DataFrame(list(item.prices.items()), columns=["Date", "Prices"])
        st.line_chart(df, x="Date",y="Prices")
#st.session_state.food_buffs[0].stat_names
# food_buffs = [ fb for fb in  st.session_state.food_buffs if (food_stat in fb.stat_names and fb.levels[fb.stat_names.index(food_stat)] is not None )]
# food_buffs.sort(key=lambda fb: fb.levels[fb.stat_names.index(food_stat)], reverse=True)
# if (len(food_buffs)>0): 
#     st.write(f" 🌟 List of land's code for :blue[{food_stat}]") 
#     cols = st.columns(3)
#     for i, food_buff in enumerate(food_buffs):
#         with cols[i % 3]:  # Répartir les expanders sur les colonnes
            
#             c = st.container(border=True)
#             c.write(f"🏡 {food_buff.owner_name if food_buff.owner_name != '' else 'an OP player'} ⚡Level {food_buff.levels[food_buff.stat_names.index(food_stat)]}")
#             c.code(food_buff.code,language=None)
# else:
#     st.write(f"💔 Sad, no land's code for :blue[{food_stat}] has been registered yet 😭") 
#     st.write(f"If you know some please register 🥺")

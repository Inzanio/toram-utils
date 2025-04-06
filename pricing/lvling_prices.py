import streamlit as st
from math import floor,ceil


st.title("🔰Leveling Services Princing💰")

# need level range
level_cap = 300
cote=286
pricing_unit = 100000
col1,col2,col3 = st.columns(3)
col1.metric("🔝 Level", f"{300}",help=f"Current :blue[level max] in Toram")

col_start_lvl , col_end_lvl = st.columns(2)
start_level = col_start_lvl.number_input("Enter the level you will :green[start] with", min_value=1, max_value=level_cap-1)

start_level = start_level +1

end_level = col_end_lvl.number_input("Enter the level you want to reach", min_value=start_level+1, max_value=level_cap , value=level_cap )

cote = st.number_input(f"Play with :blue[my cote] and see how Price goes (may help for negociation)", min_value=1 , value=286 )
nb_level = end_level - start_level+1

st.write(f"So you wanna do :blue[{nb_level}] levels ?")


def price_ceil(price,unit=1000):
    return ceil(price / unit) * unit

def exp_require_for_next_lvl(current_lvl):
    return floor((current_lvl ** 4)* 0.025 + current_lvl*2)


def pricing(exp_req,cote=cote, pricing_unit = 100000):
    return price_ceil(floor(exp_req *( cote/pricing_unit )))

import pandas as pd

df = pd.DataFrame({
    "Level" : list(range(start_level, end_level+1)),
})
df["🌟Exp Required"] = df["Level"].apply(exp_require_for_next_lvl)

df["💲Prices (Spina)"] = df["🌟Exp Required"].apply(pricing)

# if (nb_level > 150) :
#     st.line_chart(df, x="Level", y="🌟Exp Required" )
st.dataframe(df,hide_index=True,use_container_width=True)

st.write(f"So in Sum you need 🌟:blue[{df["🌟Exp Required"].sum():,}] EXP")
st.write(f"And it will cost 💲:green[{df["💲Prices (Spina)"].sum():,}]")

col2.metric("My cote", f"⚖️{cote}",label_visibility="visible", help=f"A unit to calculate :green[price] base on :blue[exp] needed, More it :red[increase] more the :green[price] is :red[high].\nIt will :red[increase] with game :red[inflation]")
col3.metric("Total Coast",f"💲{df["💲Prices (Spina)"].sum():,}",label_visibility="visible",help=f"The total amount of :green[money] to level up from :blue[level {start_level}] to :blue[level {end_level}]")

st.write("⚠️ Note that all of this is when you have :blue[exp book] on, i'm still figuring out how to do princing when no book on.")
st.write("💡If you ok with this or wanna negociate further, or give some suggestion, just DM me in Discord 🤝")


import streamlit as st
from math import floor,ceil


st.title("🔰Leveling Services Princing💰")

# need level range
level_cap = 300

col1,col2 = st.columns(2)


col_start_lvl , col_end_lvl = st.columns(2)
start_level = col_start_lvl.number_input("Enter the level you will :green[start] with", min_value=1, max_value=level_cap-1)

start_level = start_level +1

end_level = col_end_lvl.number_input("Enter the level you want to reach", min_value=start_level+1, max_value=level_cap , value=level_cap )

nb_level = end_level - start_level+1

st.write(f"So you wanna do :blue[{nb_level}] levels ?")


def price_ceil(price,unit=1000):
    return ceil(price / unit) * unit

def exp_require_for_next_lvl(current_lvl):
    return floor((current_lvl ** 4)* 0.025 + current_lvl*2)


def pricing(level):
    price_from_exp = exp_require_for_next_lvl(level)/1000
    price_from_exp = price_from_exp * 12
    return price_ceil(level * 1800 + price_from_exp )


import pandas as pd

df = pd.DataFrame({
    "Level" : list(range(start_level, end_level+1)),
})
df["🌟Exp Required"] = df["Level"].apply(exp_require_for_next_lvl)

df["💲Prices (Spina)"] = df["Level"].apply(pricing)

# if (nb_level > 150) :
#     st.line_chart(df, x="Level", y="🌟Exp Required" )
st.dataframe(df,hide_index=True,use_container_width=True)

st.write(f"So in Sum you need 🌟:blue[{df["🌟Exp Required"].sum():,}] EXP")
st.write(f"And it will cost 💲:green[{df["💲Prices (Spina)"].sum():,}]")

col1.metric("🆙Level to do", f"{nb_level}")
col2.metric("Total Cost",f"💲{df["💲Prices (Spina)"].sum():,}",label_visibility="visible",help=f"The total amount of :green[money] to level up from :blue[level {start_level}] to :blue[level {end_level}]")

st.write("⚠️ Note that all of this is when you don't have :blue[exp book]. So, if you use :blue[exp book] can do discount let just discuss about ! ")
st.write("💡If you ok with this or wanna negociate further, or give some suggestion, just DM me in Discord 🤝")


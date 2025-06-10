import streamlit as st
from math import floor,ceil

discount = {
    "by_kill" : 1,
    "by_level" : 1,
    "hour_cost" : 15 # millions
}

st.title("🔰Leveling Services Princing💰")

PRICING_METHOD = ["By Hour","By Kill","By Level"]

st.write("Choose the way you wanna be charged !")
tab_by_hour , tab_by_kill, tab_by_level = st.tabs(PRICING_METHOD)
# need level range
level_cap = 300
    
def price_ceil(price,unit=100000):
    return ceil(price / unit) * unit
#  ( [BOSS level] * 600 /kill or [MINI BOSS level]*350 / kill)**   
#     *for example Castilia is boss lvl 310 so it will cost 310\*600/kill = 186k/kill and meteora is a mini boss level 302 so it will cost 302\*350/kill = 106k/kill* 
with tab_by_hour :
    hour_cost = discount["hour_cost"] * 1000000
    col1,col2 = st.columns(2)
    col2.metric("⏰1 Min ",f"💲{price_ceil(hour_cost/60, unit=10000):,}",label_visibility="visible",help=f"The total amount of :green[money] i charge by minutes")
    col1.metric("⏰1 Hour ",f"💲{hour_cost:,}",label_visibility="visible",help=f"The total amount of :green[money] i charge by hour")

with tab_by_kill :

    BOSS_TYPE = ["MINI BOSS","NORMAL BOSS","HIGH DIFFICULTY BOSS"]
    boss_type = st.pills("Boss type",options=BOSS_TYPE,default=BOSS_TYPE[0])
    boss_level = st.number_input("Boss level",min_value=1, max_value=400)
    boss_type_pricing = {
        BOSS_TYPE[0] : 750,
        BOSS_TYPE[1] : 1600,
        BOSS_TYPE[2] : 3100
    }
    total_cost = (10000 + boss_type_pricing[boss_type]*boss_level  + (300000 if boss_type == BOSS_TYPE[2] else 0))//discount["by_kill"] # 1.1 is the discount for bulk buying
    col1,col2 = st.columns(2)
    #col2.metric("⏰1 Min ",f"💲{price_ceil(hour_cost/60):,}",label_visibility="visible",help=f"The total amount of :green[money] i charge by minutes")
    col1.metric("Cost Per kill🗡️",f"💲{price_ceil(total_cost):,}",label_visibility="visible",help=f"The total amount of :green[money] i charge by kill")
with tab_by_level :
    col1,col2 = st.columns(2)


    col_start_lvl , col_end_lvl = st.columns(2)
    start_level = col_start_lvl.number_input("Enter the level you will :green[start] with", min_value=1, max_value=level_cap-1)

    start_level = start_level +1

    end_level = col_end_lvl.number_input("Enter the level you want to reach", min_value=start_level+1, max_value=level_cap , value=level_cap )

    nb_level = end_level - start_level+1

    st.write(f"So you wanna do :blue[{nb_level}] levels ?")




    def exp_require_for_next_lvl(current_lvl):
        return floor((current_lvl ** 4)* 0.025 + current_lvl*2)


    def pricing(level):
        price_from_exp = exp_require_for_next_lvl(level)/1000
        price_from_exp = price_from_exp * 25
        return price_ceil((level * 2000 + price_from_exp )//discount["by_level"])


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


with st.expander("List of Bosses to do for leveling :") :
    df_leveling = pd.read_csv("boss_fast_lvilng.csv")
    df_leveling.drop(columns=["Level"],inplace=True)
    st.dataframe(df_leveling,hide_index=True)
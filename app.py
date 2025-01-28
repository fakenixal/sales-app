import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Sales Dashboard',
                   page_icon=':💸:',
                   layout="wide",
)


df = pd.read_excel(io='random_sales.xlsx'
 )




#Sidebar

st.sidebar.header("Filter here:")
city = st.sidebar.multiselect(
    "Select the city:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

type = st.sidebar.multiselect(
    "Select the customer type:",
    options=df["Type"].unique(),
    default=df["Type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the customer gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Type == @type & Gender == @gender"
)



#Mainpage
st.title("📉 Dashboard")
st.markdown("##")

#KPIs
total_earned = df_selection["Spent"].sum()
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating =":star:" * int(round(average_rating, 0))

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Earned:")
    st.subheader(f"Rs. {total_earned:,}")
with right_column:
    st.subheader("Average Raging:")
    st.subheader(f"{average_rating} {star_rating}")

st.markdown("--")


#Sales by Product

sales_by_product = (
    df_selection.groupby("Product Type").sum()[["Spent"]].sort_values(by="Spent")
)
fig_product_spent = px.bar (
    sales_by_product,
    x="Spent",
    y=sales_by_product.index,
    orientation="h",
    title="<b>Sales by Product Type</b>",
    color_discrete_sequence=["#a8324e"]* len(sales_by_product),
    template="plotly_white",
)

st.plotly_chart(fig_product_spent)
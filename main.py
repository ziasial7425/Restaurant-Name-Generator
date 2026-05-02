import streamlit as st
import langchainhelper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Select Cuisine Type",
    ["Italian", "Chinese", "Mexican", "Indian", "French"]
)

if cuisine:
    response = langchainhelper.generate_restaurant_name(cuisine)

    st.header(response["restaurant_name"])

    st.write("### Menu Items:")
    for item in response["menu_items"]:
        st.write("-", item)

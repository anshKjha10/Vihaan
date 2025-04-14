import streamlit as st
import pandas as pd


df = pd.read_csv("indian_financial_advisors_extended.csv") 


st.set_page_config(page_title="Financial Advisor Recommender", layout="centered")
st.title("💼 Financial Advisor Recommender")
st.markdown("Find the best financial advisors based on your region 📍")

regions = sorted(df['Region'].dropna().unique())
selected_region = st.selectbox("Select your region", regions)

top_n = st.slider("Number of advisors to show", 1, 10, 5)

if st.button("Find Advisors"):
    region_df = df[df['Region'] == selected_region]
    region_sorted = region_df.sort_values(by='Rating (Out of 5)', ascending=False).reset_index(drop=True)

    if region_sorted.empty:
        st.warning("No advisors found in the selected region.")
    else:
        st.success(f"Top {min(top_n, len(region_sorted))} Advisors in {selected_region}:")
        for i in range(min(top_n, len(region_sorted))):
            row = region_sorted.iloc[i]
            st.markdown(f"""
                **{i+1}. {row['Advisor Name']}**
                - 🧑‍💼 Profession: {row['Profession']}
                - 📈 Experience: {row['Experience (Years)']} years
                - 🏅 Rating: {row['Rating (Out of 5)']}
                - 📜 Certifications: {row['Certifications']}
            """)

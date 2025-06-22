import streamlit as st
from career_model import CareerModel

st.set_page_config(page_title="Career Guide AI", page_icon="🎯")
st.title("🎯 Career Guide AI Chat Agent")
st.subheader("Tell me about your interests, and I’ll help guide your career path!")

user_input = st.text_input("💬 What's on your mind? (e.g., I like coding and design...)")

if user_input:
    model = CareerModel(interest=user_input)
    model.setup()  # ✅ Setup the model to initialize agents and paths
    career, link = model.step()

    st.success(f"✅ Suggested Career: **{career}**")
    st.markdown(f"📚 [Recommended Course]({link})")

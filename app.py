import streamlit as st

# 🔍 Predefined career mappings based on keywords
career_paths = {
    "coding": ("Software Developer", "https://www.coursera.org/specializations/python"),
    "design": ("UI/UX Designer", "https://www.coursera.org/learn/ui-ux-design"),
    "data": ("Data Scientist", "https://www.coursera.org/specializations/data-science-python"),
    "marketing": ("Digital Marketer", "https://www.coursera.org/specializations/digital-marketing"),
    "confused": ("Career Counsellor Recommended", "https://www.careerguide.com"),
    "ai": ("AI Engineer", "https://www.coursera.org/learn/introduction-to-ai"),
    "art": ("Graphic Designer", "https://www.coursera.org/learn/graphic-design")
}

# 🎯 App Title and Description
st.title("🎯 Career Guide AI Chat Agent")
st.subheader("Tell me about your interests, and I’ll help guide your career path!")

# 🧠 User Input
user_input = st.text_input("💬 What's on your mind? (e.g., I like coding and design...)")

# 🔍 Career Prediction Function
def predict_career(text):
    text = text.lower()
    for keyword in career_paths:
        if keyword in text:
            return career_paths[keyword]
    return ("General Advisor", "https://www.coursera.org")

# ✅ Display Result
if user_input:
    career, link = predict_career(user_input)
    st.success(f"✅ Suggested Career: **{career}**")
    st.markdown(f"📚 [Recommended Course]({link})")

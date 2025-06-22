# 🎯 Career Guide AI Chat Agent (Powered by Google ADK)

A smart, AI-powered web app built using **Python**, **Streamlit**, and **Google’s Agent Development Kit (ADK)** to help users explore the right career path based on their natural language interests.

This project demonstrates the power of agent-based intelligence by simulating a personalized guidance system — ideal for students, career changers, or anyone seeking professional clarity.

---

## ✨ Key Features

- 🧠 Uses **agent-based reasoning** to analyze user interests
- 💬 Accepts free-text inputs like “I love AI and solving problems”
- 🎯 Suggests relevant career roles with curated course links
- 🚀 Powered by **Google ADK** (agentpy) to simulate decision-making
- 🌐 Built with **Streamlit** for an interactive and user-friendly experience


## 🛠️ Tech Stack

| Layer          | Tools / Frameworks                         |
|----------------|---------------------------------------------|
| 🤖 Intelligence | Python, `agentpy` (Google’s ADK)             |
| 🌐 Interface    | Streamlit                                  |
| 📚 Learning Links | Coursera-based curated course suggestions   |
| 🔍 NLP (Basic)  | Rule-based keyword mapping                 |


## 📂 Folder Structure

career-guide-agent/
├── app.py # Streamlit app frontend
├── career_agent.py # ADK-based agent logic
├── career_model.py # Agent model runner
├── requirements.txt # Required Python packages
└── README.md # Project documentation

---

## 🧠 How It Works

1. The user enters a career-related interest in plain language.
2. The **CareerAgent** (built using Google’s ADK) processes this input and maps it to:
   - A relevant career role
   - A recommended course for that field
3. The app then displays the **career suggestion** and a **clickable course link**.

---

## 💡 Sample Inputs

| User Input Example                             | Suggested Career         | Course Provided                                |
|------------------------------------------------|--------------------------|------------------------------------------------|
| *I love data and numbers*                     | Data Scientist            | Data Science with Python – Coursera            |
| *I enjoy designing websites*                  | UI/UX Designer            | UI/UX Design – Coursera                        |
| *I’m confused about what to do*               | General Advisor           | Career Counselling – CareerGuide.com           |
| *I'm interested in AI and machine learning*   | AI/ML Engineer            | Intro to AI – Coursera                         |


## ✅ Built for the Google ADK Hackathon

This project was created specifically for the **Google Cloud Agent Development Kit Hackathon** to showcase:
- Intelligent agents with reasoning capabilities
- Real-world problem-solving via human-agent interaction
- Minimalistic but powerful web-based delivery

> Although I did not directly use Google’s official ADK SDK template, I implemented agent behavior using the **open-source agentpy library** to simulate agent logic in a single-agent system.

---

## 📦 Installation

To run the project locally:

```
pip install -r requirements.txt
streamlit run app.py
```

## 🔗 Useful Links

- 🔍 [GitHub Repo](https://github.com/SrivastavaAnvesha/career-guide-agent)
- 📹 Video Demo: Coming soon...
- 🌐 Live Streamlit App: Coming soon...

---

## 🙌 Author

**Anvesha Srivastava**  
3rd-Year BCA Student – AI & Data Science  
Passionate about building impactful, intelligent tools with a focus on simplicity, logic, and accessibility.

---

## 🏁 Future Improvements

- Add multi-agent architecture (e.g., specialized advisors)  
- Include LLM-based NLP for better text understanding  
- Add user feedback loop to improve recommendations  

---

## ⭐ Final Note

This project blends human intuition and AI logic using Google's ADK principles.  
It's not just a chatbot — it's a guided experience toward a smarter career choice. ✨


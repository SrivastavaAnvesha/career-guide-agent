# career_agent.py

from agentpy import Agent

class CareerAgent(Agent):
    def setup(self):
        self.interest = self.p.interest

        self.career_paths = {
            "coding": ("Software Developer", "https://www.coursera.org/specializations/python"),
            "design": ("UI/UX Designer", "https://www.coursera.org/learn/ui-ux-design"),
            "data": ("Data Scientist", "https://www.coursera.org/specializations/data-science-python"),
            "marketing": ("Digital Marketer", "https://www.coursera.org/specializations/digital-marketing"),
            "confused": ("Career Counsellor Recommended", "https://www.careerguide.com"),
            "ai": ("AI Engineer", "https://www.coursera.org/learn/introduction-to-ai"),
            "art": ("Graphic Designer", "https://www.coursera.org/learn/graphic-design")
        }

    def get_suggestion(self):
        text = self.interest.lower()
        for keyword in self.career_paths:
            if keyword in text:
                return self.career_paths[keyword]
        return ("General Advisor", "https://www.coursera.org")

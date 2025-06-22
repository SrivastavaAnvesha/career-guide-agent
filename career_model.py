from agentpy import Agent, Model, AgentList

class CareerAgent(Agent):
    def get_suggestion(self):
        interest = self.model.user_interest.lower()  # ✅ Access interest from model

        for key in self.model.career_paths:          # ✅ Access paths from model
            if key in interest:
                return self.model.career_paths[key]

        return ("Career Counsellor Recommended", "https://www.careerguide.com")

class CareerModel(Model):
    def __init__(self, interest, **kwargs):
        super().__init__(**kwargs)
        self.user_interest = interest               # ✅ Correctly save input

    def setup(self):
        self.career_paths = {                       # ✅ Set available careers
            "coding": ("Software Developer", "https://www.coursera.org/specializations/python"),
            "design": ("UI/UX Designer", "https://www.coursera.org/learn/ui-ux-design"),
            "data": ("Data Scientist", "https://www.coursera.org/specializations/data-science-python"),
            "marketing": ("Digital Marketer", "https://www.coursera.org/specializations/digital-marketing"),
            "confused": ("Career Counsellor Recommended", "https://www.careerguide.com"),
            "ai": ("AI Engineer", "https://www.coursera.org/learn/introduction-to-ai"),
            "art": ("Graphic Designer", "https://www.coursera.org/learn/graphic-design")
        }

        self.agents = AgentList(self, 1, CareerAgent)  # ✅ Create 1 agent

    def step(self):
        return self.agents[0].get_suggestion()         # ✅ Get suggestion

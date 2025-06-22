from agentpy import Agent, Model, AgentList

# Define agent class
class CareerAgent(Agent):
    def get_suggestion(self):
        interest = self.model.user_interest.lower()

        for key in self.model.career_paths:
            if key in interest:
                return self.model.career_paths[key]

        return ("Career Counsellor Recommended", "https://www.careerguide.com")

# Define model class
class CareerModel(Model):

    def __init__(self, interest, **kwargs):
        super().__init__(**kwargs)
        self.user_interest = interest

    def setup(self):
        self.career_paths = {
            "coding": ("Software Developer", "https://www.coursera.org/specializations/python"),
            "design": ("UI/UX Designer", "https://www.coursera.org/learn/ui-ux-design"),
            "data": ("Data Scientist", "https://www.coursera.org/specializations/data-science-python"),
            "marketing": ("Digital Marketer", "https://www.coursera.org/specializations/digital-marketing"),
            "confused": ("Career Counsellor Recommended", "https://www.careerguide.com"),
            "ai": ("AI Engineer", "https://www.coursera.org/learn/introduction-to-ai"),
            "art": ("Graphic Designer", "https://www.coursera.org/learn/graphic-design")
        }

        self.agents = AgentList(self, 1, CareerAgent)

    def step(self):
        return self.agents[0].get_suggestion()

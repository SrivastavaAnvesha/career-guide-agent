from agentpy import Agent, Model, AgentList


# Define a CareerAgent with fixed interest-to-career mappings
class CareerAgent(Agent):

    def get_suggestion(self):
        interest = self.model.interest.lower()

        # Predefined career paths
        self.career_paths = {
            "coding": ("Software Developer", "https://www.coursera.org/specializations/python"),
            "design": ("UI/UX Designer", "https://www.coursera.org/learn/ui-ux-design"),
            "data": ("Data Scientist", "https://www.coursera.org/specializations/data-science-python"),
            "marketing": ("Digital Marketer", "https://www.coursera.org/specializations/digital-marketing"),
            "confused": ("Career Counsellor Recommended", "https://www.careerguide.com"),
            "ai": ("AI Engineer", "https://www.coursera.org/learn/introduction-to-ai"),
            "art": ("Graphic Designer", "https://www.coursera.org/learn/graphic-design")
        }

        # Find the best match
        for key in self.career_paths:
            if key in interest:
                return self.career_paths[key]

        # Default if nothing matches
        return ("Career Counsellor Recommended", "https://www.careerguide.com")


# Define the model containing the agent
class CareerModel(Model):

    def setup(self):
        # Create one agent
        self.agents = AgentList(self, 1, CareerAgent)

    def step(self):
        return self.agents[0].get_suggestion()

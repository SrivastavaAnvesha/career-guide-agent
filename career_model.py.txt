# career_model.py

from agentpy import Model, AgentList
from career_agent import CareerAgent

class CareerModel(Model):
    def setup(self):
        self.agents = AgentList(self, 1, CareerAgent, {'interest': self.p.interest})

    def step(self):
        return self.agents[0].get_suggestion()

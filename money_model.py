import mesa
from ponzi_agent import PonziAgent
from money_agent import MoneyAgent
from robin_hood import RobinHood


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n):
        self.num_agents = n
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents - 1): # Ponzi is one of the 10
            a = MoneyAgent(i, self)
            self.schedule.add(a)
        p = PonziAgent(self)
        self.schedule.add(p)

    def step(self):
        """Move the model forward one tick."""
        self.schedule.step()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    empty_model = MoneyModel(10)
    empty_model.step()

import mesa


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def give(self, giver):
        self.wealth += 1
        giver.wealth -= 1

    def step(self):
        # Agent's step, or action per tick
        if self.wealth == 0:
            return
        # randomly select an agent to pay
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.give(self)
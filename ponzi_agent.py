import mesa


class PonziAgent(mesa.Agent):
    """An agent who does a Ponzi Scheme."""

    def __init__(self, model):
        super().__init__(-2, model)
        self.wealth = 1

    def give(self, giver):
        # When another agent gives Ponzi money, it gives them back two and keeps the one
        # This is a broken metric that adds more money to the system and does not work in the real world
        # But Ponzi doesn't know that and thinks that this is how it works
        self.wealth += 1
        giver.wealth += 1

    def step(self):
        # On its turn, Ponzi gives two money each to as many random other agents as it has money to give
        while self.wealth > 1:
            all_agents = self.model.schedule.agents
            all_agents.remove(self)

            other_agent = self.random.choice(all_agents)
            other_agent.wealth += 2
            self.wealth -= 2

import mesa


class RobinHood(mesa.Agent):
    """An agent which redistributes wealth."""

    def __init__(self, model):
        super().__init__(-1, model)
        self.wealth = 0

    def give(self, giver):
        self.wealth += 1
        giver.wealth -= 1

    def step(self):
        # each tick, take all but one money from any agent with more than 2
        # and distribute it to agents with less than 2
        # if another agent pays the Equalizer, that is also redistributed in this step
        wealthy_agents = [a for a in self.model.schedule.agents if a.wealth > 1]
        poor_agents = [a for a in self.model.schedule.agents if a.wealth < 1]

        if self in wealthy_agents:
            wealthy_agents.remove(self)
        if self in poor_agents:
            poor_agents.remove(self)

        for agent in wealthy_agents:
            self.wealth += (agent.wealth - 1)
            agent.wealth = 1

        while self.wealth > 0:
            poor = self.random.choice(poor_agents)
            poor.wealth += 1
            self.wealth -= 1
            poor_agents.remove(poor)

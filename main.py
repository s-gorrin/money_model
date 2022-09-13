from money_model import *
import matplotlib.pyplot as plt

print("Running model...")

full_run = True

if full_run:
    all_wealth = []
    for j in range(100):
        model = MoneyModel(10)
        for i in range(10):
            model.step()
        for agent in model.schedule.agents:
            if agent.unique_id != -1:   # exclude robin hood
                all_wealth.append(agent.wealth)

    plt.hist(all_wealth, bins=range(max(all_wealth) + 1))
    plt.show()
else:
    model = MoneyModel(10)
    for i in range(10):
        model.step()
        for agent in model.schedule.agents:
            print("agent " + str(agent.unique_id) + " has $" + str(agent.wealth) + ".")

print("Done.")

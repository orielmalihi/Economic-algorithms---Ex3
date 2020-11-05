class Agent:
    options = []

    def __init__(self, position: int):
        self.position = position

    def value(self, index: int):
        if index >= len(Agent.options) or self.position >= len(Agent.options[index]):
            return
        else:
            return Agent.options[index][self.position]

def isParetoImprovement(agents: list, option1: int, option2: int)->bool:
        for agent in agents:
            if agent.value(option1) < agent.value(option2):
                return False
        return True

def isParetoOptimal(agents: list, option: int, allOptions: list)->bool:
    for another_option in allOptions:
        if option == another_option:
            continue
        elif isParetoImprovement(agents, another_option, option):
            return False
    return True



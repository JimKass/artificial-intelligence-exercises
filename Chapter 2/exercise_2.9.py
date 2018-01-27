import random
print("Hello")


class Environment:
    def __init__(self):
        self.env = {"A": "Dirty", "B": "Clean"}

    def make_dirty(self):
        for square, i in enumerate(self.env):
            if random.randint(1, 100) == 25:
                self.env[i] = "Dirty"


class VacuumAgent:
    def __init__(self, max_time_steps=100, environment=Environment()):
        self.rules = {["A", "Dirty"]:"clean",
                      ["B", "Dirty"]:"clean",
                      ["B", "Clean"]:"move_left",
                      ["A", "Clean"]:"move_right"}
        self.state = None
        self.max_time_steps = max_time_steps
        self.environment = environment
        self.current_time_step = 0
        self.current_square = "A"
        self.action = "idle"

    def tick(self):
        self.current_time_step += 1

    def move_left(self):
        if self.current_square == "B":
            self.current_square = "A"
        self.tick()

    def move_right(self):
        if self.current_square == "A":
            self.current_square = "B"

    def clean(self):
        self.environment.env[self.current_square] = "Clean"
        self.tick()

    def get_state(self):
        pass

    def rule_match(self, state, rules):
        for percept in rules:
            if percept == state:
                self.action = rules[percept]

    def percieve(self):
        pass

    def agent_function(self):
        pass


def main():
    environment = Environment()
    agent = VacuumAgent(environment=environment)
    while agent.current_time_step <= agent.max_time_steps:
        environment.make_dirty()
        agent.agent_function()
        print("{}, Action: {}, Current Position: {}".format(environment, agent.action, agent.current_square))

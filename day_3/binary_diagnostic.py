class Submarine:
    diagnostic_report: list[str]
    gamma: str
    epsilon: str
    oxygen: str
    scubber: str

    consumption_rating: int
    life_support_rating: int

    def __init__(self, path: str):
        with open(path) as file:
            self.diagnostic_report = [line.strip() for line in file.readlines()]
        self.gamma = ""
        self.epsilon = ""
        self.oxygen = ""
        self.scubber = ""
        self.consumption_rating = 0
        self.life_support_rating = 0

    def check_power_consumption(self):
        error_matrix = zip(*reversed(self.diagnostic_report))

        gamma = ""
        epsilon = ""

        for bit in error_matrix:
            # determine common bit
            if bit.count('1') >= len(bit) / 2:
                gamma = gamma + '1'
                epsilon = epsilon + '0'
            else:
                gamma = gamma + '0'
                epsilon = epsilon + '1'

        # update key figures
        self.gamma = gamma
        self.epsilon = epsilon
        self.consumption_rating = int(gamma, 2) * int(epsilon, 2)

    def check_life_support(self):
        # for each position
            # iterate i to point on bit
            # estimate common bit
            # filter all strings in logs
            # next position
        pass

    def printReport(self):
        print("System analysis\n"+ 35*"=" + "\n"
              + f"Epsilon:\t\t\t\t\t{self.epsilon}\n"
              + f"Gamma:\t\t\t\t\t\t{self.gamma}\n"
              + f"Oxygen Generator Rating:\t{self.oxygen}\n"
              + f"CO2 Scubber Rating:\t{self.scubber}\n"
              + 35 * "=" + "\n"
              + f"Power Consumption Rating:\t{self.consumption_rating}\n"
              + f"Life Support Rating:\t\t{self.life_support_rating}\n")


if __name__ == '__main__':
    subby = Submarine("trial_input.txt")
    subby.check_power_consumption()
    subby.printReport()
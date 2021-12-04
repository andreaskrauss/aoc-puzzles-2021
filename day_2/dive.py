

class Submarine:
    y: int     # depth
    x: int     # position

    def __init__(self, position: int = 0, depth: int = 0):
        self.x = position
        self.y = depth

    def down(self, delta: int):
        self.y = self.y + delta

    def up(self, delta: int):
        self.y = self.y - delta

    def forward(self, delta: int):
        self.x = self.x + delta

    def parseCall(self, command: str):
        call, delta = command.split(" ")
        return [call, int(delta)]

    def call(self, command: str, delta: int):
        act = self.__getattribute__(command)        # Dispatch pattern
        act(delta)

    def __str__(self):
        return f"Position: {self.x} - Depth: {self.y}"

    def reveal(self):
        return [self.x, self.y]


if __name__ == '__main__':
    sub = Submarine()
    # read commands
    with open("input.txt") as logs:
        logbook = [line.strip() for line in logs.readlines()]

    # call commands
    for log in logbook:
        [command, delta] = sub.parseCall(log)
        sub.call(command, delta)

    # print result
    print(sub)
    [pos, depth] = sub.reveal()
    print(f"Solution: {pos * depth}")

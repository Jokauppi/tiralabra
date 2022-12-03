class ConsoleIO():
    def __init__(self):
        pass

    def input(self, query: str):
        return str(input(query))

    def output(self, message):
        print(message)

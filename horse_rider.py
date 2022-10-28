class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rider = Rider("arizona ranger")
horse = Horse('Plotva', rider)

print(horse.rider.name)
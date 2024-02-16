class Team:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Team Name: {self.name}"


team1 = Team("JIUGO!")
team2 = Team("AmateurGrammer")

print(team1)
print(team1.name)


import random
# creating a player class which has the required attributes.
class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience

    def __str__(self):
        return self.name


class Teams:
    def __init__(self, team_name, players):
        self.team_name = team_name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self, captain):
        self.captain = captain

    def set_batting_order(self, batting_order):
        self.batting_order = batting_order

    def send_next_player(self):
        if self.batting_order:
            return self.batting_order.pop(0)
        else:
            return None

    def choose_bowler(self):
        if len(self.players) == 0:
            return None

        bowler = self.players.pop()
        self.players.append(bowler)
        return bowler

class Field:
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

# It will do umpiring. It may be Out or not out and handle the wickets 
class Umpire:
    def __init__(self, field):
        self.field = field
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, batsman, bowler):
        batting_prob = batsman.batting * random.uniform(0.8, 1.2)
        bowling_prob = 1
        if bowler:
            bowling_prob = bowler.bowling * random.uniform(0.8, 1.2)
        outcome_prob = (batting_prob + bowling_prob) / 2

        # Simulating the outcome
        outcome = random.randint(0,1)
        if outcome ==0:
            return "Out"
        else:
            return "NOT OUT"
        return outcome

    def handle_wicket(self):
        self.wickets += 1
        if self.wickets==10:
            print("Innings")

    def handle_runs(self, runs):
        self.score += runs

    def handle_over(self):
        self.overs += 1

    def make_decision(self, decision):
        if decision>1:
            self.score+=1 

# It will do commentary by printing batsman and bowler names and score
class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, ball, over, batsman, bowler, umpire):
        print(f"Over: {over + 1} | Ball: {ball + 1}")
        print(f"Batsman: {batsman} | Bowler: {bowler}")
        print(f"Score: {umpire.score}/{umpire.wickets}")
        print()


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(self.field)
        self.commentator = Commentator()

    def start_match(self):
        print("Match started!")
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.set_batting_order(self.team1.players[:])
        self.team2.set_batting_order(self.team2.players[:])

        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)

        self.end_match()

    def play_innings(self, batting_team, bowling_team):
        print(f"{batting_team.team_name} is batting...")
        batsman = batting_team.send_next_player()
        while batsman and self.umpire.wickets < 10:
            bowler = bowling_team.choose_bowler()
            for ball in range(6):
                outcome = self.umpire.predict_outcome(batsman, bowler)
                if outcome == "Out":
                    self.umpire.handle_wicket()
                    self.commentator.provide_commentary(ball, self.umpire.overs, batsman, bowler, self.umpire)
                    print(f"{batsman} is out!")
                    break
                else:
                    runs = random.choice([0, 1, 2, 3, 4, 6])
                    self.umpire.handle_runs(runs)
                    self.commentator.provide_commentary(ball, self.umpire.overs, batsman, bowler, self.umpire)
                    print(f"{batsman} scores {runs} run(s)!")
            self.umpire.handle_over()
            batsman = batting_team.send_next_player()
    #end the innings if wickets fall down to 10 or number of overs is completed.
    def end_match(self):
        print("Match ended!")
        print(f"Final Score: {self.umpire.score}/{self.umpire.wickets}")




# Create players
player1 = Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.9, 0.1, 0.95, 0.7, 0.8)
player3 = Player("Rohit Sharma", 0.85, 0.1, 0.9, 0.75, 0.85)
player4 = Player("Jasprit Bumrah", 0.1, 0.9, 0.8, 0.5, 0.8)
player5 = Player("Ravindra Jadeja", 0.7, 0.6, 0.9, 0.8, 0.85)
player6 = Player("Shikhar Dhawan", 0.75, 0.1, 0.85, 0.8, 0.8)
player7 = Player("KL Rahul", 0.85, 0.1, 0.9, 0.8, 0.85)
player8 = Player("Hardik Pandya", 0.8, 0.5, 0.8, 0.7, 0.8)
player9 = Player("Bhuvneshwar Kumar", 0.2, 0.8, 0.7, 0.6, 0.75)
player10 = Player("Yuzvendra Chahal", 0.3, 0.7, 0.75, 0.6, 0.8)
player11 = Player("Mohammed Shami", 0.2, 0.9, 0.8, 0.7, 0.85)

# Create teams
team1 = Teams("Team 1", [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11])
team2 = Teams("Team 2", [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11])

# Create field
field = Field("Medium", 0.8, "Dry", 0.1)

# Create and start the match
innings1= Match(team1, team2, field)
innings2= Match(team2, team1, field)


innings1.start_match()
innings2.start_match()

if innings1.umpire.score>innings2.umpire.score:
    print("Team 1 is winner")
else:
    print("Team 2 is winner")

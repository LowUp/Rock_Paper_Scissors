class Rules:

    def rules(self, num):
        game_rule = {
            1: "Rock",
            2: "Paper",
            3: "Scissor"
        }
        return game_rule.get(num, "Invalid number")




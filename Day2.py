class Day2:
    scores = [[3, 6, 0],
              [0, 3, 6],
              [6, 0, 3]]

    opponent_choices = {'A': 0, 'B': 1, 'C': 2}
    my_choices = {'X': 0, 'Y': 1, 'Z': 2}
    desired_scores = {'X': 0, 'Y': 3, 'Z': 6}

    def task_1(self, inp):
        score1 = 0
        score2 = 0
        for item in inp:
            item1, item2 = item.split(' ')
            score1 += self.get_score(item1, item2)
            score2 += self.get_scores2(item1, item2)
        return [score1, score2]

    def get_scores2(self, opponent, me):
        draws = self.scores[self.opponent_choices[opponent]]
        my_index = draws.index(self.desired_scores[me])
        score = my_index + self.desired_scores[me] + 1
        return score

    def get_score(self, opponent, me):
        opponent_choice = self.opponent_choices[opponent]
        my_choice = self.my_choices[me]
        score = self.scores[opponent_choice][my_choice] + my_choice + 1
        return score

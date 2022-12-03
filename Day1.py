class Day1:
    @staticmethod
    def task_1(inp):
        calories = 0
        highest = 0
        for item in inp:
            if item != "":
                calories += int(item)
            else:
                if calories > highest:
                    highest = calories
                calories = 0
        return highest

    @staticmethod
    def task_2(inp):
        calories = 0
        calories_list = []
        for item in inp:
            if item != "":
                calories += int(item)
            else:
                calories_list.append(calories)
                calories = 0
        calories_list.sort(reverse=True)
        return calories_list[0] + calories_list[1] + calories_list[2]

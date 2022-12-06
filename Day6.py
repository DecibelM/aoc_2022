class Day6:
    @staticmethod
    def task_1(inp):

        i = 0
        inp = inp[0]
        characters = 14
        while i < len(inp):
            current = []
            for j in range(i, i + characters):
                current.append(inp[j])
            is_unique = True
            for item in current:
                if current.count(item) > 1:
                    is_unique = False
            if is_unique:
                result = i + characters
                break
            i += 1
        return result

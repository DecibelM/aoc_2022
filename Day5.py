class Day5:
    @staticmethod
    def task_1(inp, task):
        crates = []
        moves = []
        i = 0
        while inp[i] != "\n":
            crates.append(inp[i].strip('\n'))
            i += 1

        while i < len(inp):
            if inp[i] != "\n":
                moves.append(inp[i].strip('\n').split(' '))
            i += 1

        piles = crates.pop(len(crates) - 1).strip().split(' ')
        no_of_piles = int(piles[-1])
        piles_list = []
        for i in range(0, no_of_piles):
            piles_list.append([])

        for i in reversed(crates):
            for j in range(0,len(i)):
                current = i[j]
                if current != ' ' and current != '[' and current != ']':
                    if j == 1:
                        list_no = 0
                    else:
                        list_no = int((j - 1)/4)
                    piles_list[list_no].append(i[j])

        for move in moves:
            number = int(move[1])
            fr = int(move[3]) - 1
            to = int(move[5]) - 1
            if task == 1:
                Day5.solve1(piles_list, number, fr, to)
            elif task == 2:
                Day5.solve2(piles_list, number, fr, to)
        result = ''
        for list in piles_list:
            result += list.pop()
        return result

    @staticmethod
    def solve2(piles_list, number, fr, to):
        moved = []
        for i in range(0, number):
            moved.append(piles_list[fr].pop())
        for item in reversed(moved):
            piles_list[to].append(item)

    @staticmethod
    def solve1(piles_list, number, fr, to):
        for i in range(0, number):
            moved = piles_list[fr].pop()
            piles_list[to].append(moved)

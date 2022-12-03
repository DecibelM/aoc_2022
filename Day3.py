class Day3:
    @staticmethod
    def task1(inp):
        score = 0
        for item in inp:
            item_size = int(len(item)/2)
            letter = Day3.find_letter(item[0:item_size], item[item_size:len(item)])
            score += Day3.get_score(letter)
        return score

    @staticmethod
    def get_score(l):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if l in letters:
            score = letters.index(l) + 1
        elif l.lower() in letters:
            score = letters.index(l.lower()) + 27
        else:
            score = 0
        return score

    @staticmethod
    def find_letter(compartment_1, compartment_2):
        for l in compartment_1:
            if l in compartment_2:
                return l
        return None

    @staticmethod
    def find_letter_2(elf_1, elf_2, elf_3):
        for l in elf_1:
            if l in elf_2 and l in elf_3:
                print(l)
                return l
        return None

    @staticmethod
    def task2(inp):
        i = 0
        score = 0
        while i < len(inp):
            elf_1 = inp[i]
            elf_2 = inp[i+1]
            elf_3 = inp[i+2]

            letter = Day3.find_letter_2(elf_1, elf_2, elf_3)
            score += Day3.get_score(letter)
            i += 3
        return score

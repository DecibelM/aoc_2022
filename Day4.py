class Day4:
    @staticmethod
    def task_1(inp):
        counter1 = 0
        counter2 = 0
        for item in inp:
            item1, item2 = item.split(',')
            item1_start, item1_end = item1.split('-')
            item2_start, item2_end = item2.split('-')

            list1 = [*range(int(item1_start), int(item1_end) + 1)]
            list2 = [*range(int(item2_start), int(item2_end) + 1)]

            intersection = set(list1).intersection(list2)
            intersection_size = len(intersection)

            if intersection_size == len(list1) or intersection_size == len(list2):
                counter1 += 1

            if intersection_size != 0:
                counter2 += 1

        return [counter1, counter2]

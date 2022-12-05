from Day1 import Day1
from Day2 import Day2
from Day3 import Day3
from Day4 import Day4
from Day5 import Day5
from input import Imports

importClass = Imports()

"""
print("Day 1:")
inp = Imports.get_input("input/input1.txt")
print(Day1.task_1(inp))
print(Day1.task_2(inp))

print("Day 2: ")
inp = Imports.get_input("input/input2.txt")
day2 = Day2()
print(day2.task_1(inp))

print("Day 3: ")
inp = Imports.get_input("input/input3.txt")
print(Day3.task1(inp))
print(Day3.task2(inp))


print("Day 4: ")
inp = Imports.get_input("input/input4.txt")
print(Day4.task_1(inp))
"""
print("Day 5: ")
inp = Imports.get_input_no_strip("input/input5.txt")
print(Day5.task_1(inp, 1))
print(Day5.task_1(inp, 2))

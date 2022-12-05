class Imports:
    @staticmethod
    def get_input(path):
        f = open(path, "r")
        rules = []
        for x in f:
            rules.append(x.strip())
        return rules

    @staticmethod
    def get_input_no_strip(path):
        f = open(path, "r")
        rules = []
        for x in f:
            rules.append(x)
        return rules

    @staticmethod
    def get_input_chunk(path):
        f = open(path, "r")
        data = f.read()
        fixed_data = data.split("\n\n")
        return fixed_data

    def getInput_split_by_comma(self, path):
        f = open(path, "r")
        data = f.read()
        fixed_data = data.split(",")
        fixed_data = [int(num) for num in fixed_data]
        return fixed_data

class Square:
    def __init__(self, rank, file, color):
        if color not in ['black', 'white']:
            raise ValueError("Color must be either 'black' or 'white'")
        self.color = color
        self.rank = rank
        self.file = file
        self.name = f"{file}{rank}"

    def __str__(self):
        return f"Square {self.name} is {self.color}"
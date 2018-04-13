class ProgrammingLanguage:


    def __init__(self, name="", typing="", reflection=False, year=0):
        # type: (object) -> object

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = 0

    def is_dynamic(self):

        if "Dynamic" == self.typing:
            return True
        else:
            return False

    def __str__(self):
        return "{}, {}, Reflection = {}, {}".format(self.name, self.typing, self.reflection, self.year)

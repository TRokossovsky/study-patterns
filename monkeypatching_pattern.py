#  Realization of Monkey-patching pattern[Unwanted]


class Monkey:

    def scream(self):
        print('Screaming as classed Monkey')


def new_scream(self):
    print('Screaming as unclassed Monkey')


Monkey.scream = new_scream
monkey = Monkey()
monkey.scream()

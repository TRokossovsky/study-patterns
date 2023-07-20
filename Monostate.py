#  Monostate realisation


class Monostate:
    _shared_state = {}

    def __init__(self, data):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            #  Any huge calculations, etc.
            self.data = data

    def __str__(self):
        return str(self.data)


m = Monostate(21)
m1 = Monostate(12)
m2 = Monostate(33)

print(m, m1, m2)

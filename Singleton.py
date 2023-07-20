#  Singleton realisation on DB framework


class DB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def __del__(self):
        DB.__instance = None

    def connect(self):
        pass

    def close(self):
        pass

    def read(self):
        pass

    def write(self, data):
        pass

class HandlerSignals:
    __slots__ = ['methods']

    def __init__(self):
        self.methods = {}

    def reg_signal(self, name):
        def reg(func):
            self.methods[name] = func

        return reg

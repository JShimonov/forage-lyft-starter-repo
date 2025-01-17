from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, indicator_light):
        self.indicator_light = indicator_light

    def engine_should_be_serviced(self):
        if self.indicator_light:
            return True
        return False

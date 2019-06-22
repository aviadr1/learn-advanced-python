from singleton import make_singleton

class HomePlanet:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'HomePlanet({self.name!r})'

earth = HomePlanet('earth')
make_singleton(HomePlanet)

from parameters import Parameters
from game import play


def run_basic():
    params = Parameters()
    params.scenario = 'basic'
    play(params)


def run_deadly_corridor():
    params = Parameters()
    params.scenario = 'deadly_corridor'
    play(params)


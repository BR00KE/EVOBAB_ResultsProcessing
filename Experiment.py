from Generation import Generation

class Experiment:
    'Class for each experiment which should hold averaged stats for each generation over all repeats'
    
    def __init__(self, directory, experimentNumber):
        ##where baseline is a bool
        char = '2'
        
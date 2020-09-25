from PopulationStats import PopulationStats

class Experiment:
    'Class for each experiment which should hold averaged stats for each generation over all repeats'
    
    def __init__(self, directory, experimentNumber):
        char = '2'
        self.generations = [None] * 100 ##100 generations per experiment
        
        # ten repeats for each experiment 
        for repeat in range(10):
            print(repeat)
            
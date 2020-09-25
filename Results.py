from Experiment import Experiment

class Results: 
    'class that is wrapper for either all baseline or all complexity cost experiments'
    def __init__(self, directory):
        
        # Evolutions conducted over 12 environments
        self.experiments = [None] * 12 
        
        for i in range(12):
            self.experiments[i] = Experiment(directory,i)
        
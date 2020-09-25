from Experiment import Experiment

class Results: 
    'class that is wrapper for either all baseline or all complexity cost experiments'
    def __init__(self, directory):
        self.dir = directory
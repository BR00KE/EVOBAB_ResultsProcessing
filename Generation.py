class Generation:
    'average the stats for each generation over all repeats for given experiment'
    
    def __init__(self,directory,experiment,repeat,genNumber):
        ##read in the things and put them in the class instance variables
        string = 'hello'
        self.averageComplexity = 0.0
        self.averageFitness = 0.0
        self.highestFitness = 0.0
        self.highestComplexity = 0.0
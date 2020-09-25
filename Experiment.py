from Generation import Generation
class GenStats:
    'class to hold the average complexity and novelty over all repeats for generation'
    def __init__(self, averageComplexity, averageFitness, highestComplexity, highestFitness):
        self.averageComplexity = averageComplexity
        self.averageFitness = averageFitness
        self.highestComplexity = highestComplexity
        self.highestFitness = highestFitness
        
class Experiment:
    'Class for each experiment which should hold averaged stats for each generation over all repeats'
    
    def __init__(self, directory, experimentNumber):
        
        self.generationStats = [None] * 100 # 100 generations per experiment
        
        # largest complexity score achieved over all repeats and all generations
        self.highestComplexityExperiment = 0.0
        # largest fitness score achieved over all repeats and all generations
        self.highestFitnessExperiment = 0.0   
        
        # 100 generations per run
        # ten repeats for each experiment         
        for generationNumber in range(1,101):
            complexity = 0.0
            fitness = 0.0
            highestFitness = 0.0
            highestComplexity =0.0
            for repeat in range(10):
                genStats = Generation(directory,experimentNumber,repeat,generationNumber)
                complexity = complexity + genStats.averageComplexity
                fitness = fitness + genStats.averageFitness
                if(genStats.highestFitness>highestFitness):
                    highestFitness = genStats.highestFitness
                if(genStats.highestComplexity>highestComplexity):
                    highestComplexity = genStats.highestComplexity
        
            self.generationStats[generationNumber] = GenStats(complexity/10,fitness/10,highestComplexity,highestFitness)
            if(highestFitness > self.highestFitnessExperiment):
                self.highestFitnessExperiment = highestFitness
            if(highestComplexity > self.highestComplexityExperiment):
                self.highestComplexityExperiment = highestComplexity
                
            
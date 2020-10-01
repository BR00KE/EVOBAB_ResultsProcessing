from Generation import Generation
class GenStats:
    'class to hold the average complexity and novelty over all repeats for generation'
    def __init__(self, averageComplexity, averageFitness, averageHighestFitness, averageHighestComplexity, highestComplexity, highestFitness):
        self.averageComplexity = averageComplexity
        self.averageFitness = averageFitness
        self.averageHighestFitness = averageHighestFitness
        self.averageHighestComplexity = averageHighestComplexity
        self.highestComplexity = highestComplexity
        self.highestFitness = highestFitness
        
class Experiment:
    'Class for each experiment which should hold averaged stats for each generation over all repeats'
    
    def __init__(self, directory, experimentNumber):
        
        self.generationStats = [None] * 100 # 100 generations per experiment
        
        #array for avgComplexity over generations 
        self.avgComplexityArray = [None] *100
        #array for avgFitness over generations 
        self.avgFitnessArray = [None] *100
        
        # array of the average highest fitness individuals for each generation over the ten repeats
        self.avgHighestFitnessArray = [None] * 100
        # array of the average complexity of the individuals with the highest fitness at each generation over the ten repeats
        self.avgHighestComplexityArray = [None] * 100
        
        #highest fitness and associated complexity at generation 100 for each of the repeats
        self.highestFitnessPerRepeat = [None] * 10
        self.highestComplexityPerRepeat = [None] * 10
        #average fitness and average complexity at generation 100 for each of the repeats
        self.averageFitnessPerRepeat = [None] * 10
        self.averageComplexityPerRepeat = [None] * 10
        
        # complexity of individual that achieved the highest fitness 
        self.highestComplexityExperiment = 0.0
        # largest fitness score achieved over all repeats and all generations
        self.highestFitnessExperiment = 0.0   
        
        self.lowestFitnessExperiment = 100.0
        
        # 100 generations per run
        for generationNumber in range(1,101):
            complexity = 0.0
            fitness = 0.0
            highestFitness = 0.0
            highestComplexity =0.0
            
            lowestFitness = 100.0
            
            totalHighestFitness = 0.0
            totalHighestComplexity = 0.0 
            
            # ten repeats for each experiment    
            for repeat in range(10):
                genStats = Generation(directory,experimentNumber,repeat,generationNumber)
                complexity = complexity + genStats.averageComplexity
                fitness = fitness + genStats.averageFitness
                
                totalHighestComplexity += genStats.highestComplexity
                totalHighestFitness += genStats.highestFitness
                
                if(genStats.highestFitness>highestFitness):
                    highestFitness = genStats.highestFitness
                    highestComplexity = genStats.highestComplexity
        
                if(genStats.lowestFitness<lowestFitness):
                    lowestFitness = genStats.lowestFitness
                
                if(generationNumber==100):
                    self.highestFitnessPerRepeat[repeat] = genStats.highestFitness
                    self.highestComplexityPerRepeat[repeat] = genStats.highestComplexity
                    self.averageFitnessPerRepeat[repeat] = genStats.averageFitness
                    self.averageComplexityPerRepeat[repeat] = genStats.averageComplexity
                
            # generations labeled from 1 but indexing from 0
            # average over all repeats for avg of pop at given generation 
            averageComplexity = complexity/10
            self.avgComplexityArray[generationNumber-1] = averageComplexity
            averageFitness = fitness/10
            self.avgFitnessArray[generationNumber-1] = averageFitness
            
            averageHighestComplexity = totalHighestComplexity/10
            self.avgHighestComplexityArray[generationNumber-1] = averageHighestComplexity
            averageHighestFitness = totalHighestFitness/10
            self.avgHighestFitnessArray[generationNumber-1] = averageHighestFitness
            
            self.generationStats[generationNumber-1] = GenStats(averageComplexity,averageFitness,averageHighestFitness, averageHighestComplexity, highestComplexity,highestFitness)
            
            if(highestFitness > self.highestFitnessExperiment):
                self.highestFitnessExperiment = highestFitness
            if(highestComplexity > self.highestComplexityExperiment):
                self.highestComplexityExperiment = highestComplexity
                
            if(lowestFitness<self.lowestFitnessExperiment):
                self.lowestFitnessExperiment = lowestFitness
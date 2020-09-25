class Generation:
    'average the stats over the population for a given experiment,repeat,and generation'
    
    def __init__(self,directory,experiment,repeat,genNumber):
        ##read in the things and put them in the class instance variables
        
        totalComplexity = 0.0
        totalFitness = 0.0
        highestFitness = 0.0
        highestComplexity = 0.0
        file = directory + "Experiment" + str(experiment) + "/novelty_output" + str(repeat) + "/" + "Generation-"+ str(genNumber) +"-PopStats_Complexity-Fitness-Novelty.txt"
        # read in 
        popstats = open(file,"r")
        stats = popstats.readline()
        while stats:
            line_split = stats.split(" ")
            totalComplexity = totalComplexity + float(line_split[0])
            totalFitness = totalFitness + float(line_split[1])
            if(float(line_split[0])>highestComplexity):
                highestComplexity = float(line_split[0])
            if(float(line_split[1])>highestFitness):
                highestFitness = float(line_split[1])
            stats = popstats.readline()
        popstats.close()
        
        self.averageComplexity = totalComplexity/100
        self.averageFitness = totalFitness/100
        self.highestFitness = highestFitness
        self.highestComplexity = highestComplexity       
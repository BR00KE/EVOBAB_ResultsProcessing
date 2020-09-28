from Results import Results
import matplotlib.pyplot as plt

def main():
    print("initialising baseline")
    baseline = Results("noveltyResults/baseline/")
    
    
    print("initialising complexityCost")
    complexityCost = Results("noveltyResults/complexityCost/")
    
    print("plotting graphs")
    x_axis = list(range(1,101))
    
    print("plotting fitness trends")
    fitnessTrend, (baselinef, complexityCostf) = plt.subplots(1,2,sharey=True)
    # fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    fitnessTrend.set_figheight(5)
    fitnessTrend.set_figwidth(14)
    
    baselinef.set_title("Baseline Experiment")
    baselinef.set_ylabel("Average Fitness of Population")
    baselinef.set_xlabel("Generation")
    baselinef.plot(x_axis, baseline.experiments[0].avgFitnessArray, color = 'tab:grey', label='Environment 1')
    baselinef.plot(x_axis, baseline.experiments[1].avgFitnessArray, color = 'tab:olive', label='Environment 2')
    baselinef.plot(x_axis, baseline.experiments[2].avgFitnessArray, color = 'tab:green', label='Environment 3')
    baselinef.plot(x_axis, baseline.experiments[3].avgFitnessArray, color = 'tab:brown', label='Environment 4')
    baselinef.plot(x_axis, baseline.experiments[4].avgFitnessArray, color = 'tab:orange', label='Environment 5')
    baselinef.plot(x_axis, baseline.experiments[5].avgFitnessArray, color = 'tab:red', label='Environment 6')
    baselinef.plot(x_axis, baseline.experiments[6].avgFitnessArray, color = 'tab:pink', label='Environment 7')
    baselinef.plot(x_axis, baseline.experiments[7].avgFitnessArray, color = 'tab:purple', label='Environment 8')
    baselinef.plot(x_axis, baseline.experiments[8].avgFitnessArray, color = 'magenta', label='Environment 9')
    baselinef.plot(x_axis, baseline.experiments[9].avgFitnessArray, color = 'cyan', label='Environment 10')
    baselinef.plot(x_axis, baseline.experiments[10].avgFitnessArray, color = 'tab:blue', label='Environment 11')
    baselinef.plot(x_axis, baseline.experiments[11].avgFitnessArray, color = 'blue', label='Environment 12')
    
    complexityCostf.set_title("Complexity Cost Experiment")
    complexityCostf.set_ylabel("Average Fitness of Population")
    complexityCostf.set_xlabel("Generation")    
    complexityCostf.plot(x_axis, complexityCost.experiments[0].avgFitnessArray, color = 'tab:grey')
    complexityCostf.plot(x_axis, complexityCost.experiments[1].avgFitnessArray, color = 'tab:olive')
    complexityCostf.plot(x_axis, complexityCost.experiments[2].avgFitnessArray, color = 'tab:green')
    complexityCostf.plot(x_axis, complexityCost.experiments[3].avgFitnessArray, color = 'tab:brown')
    complexityCostf.plot(x_axis, complexityCost.experiments[4].avgFitnessArray, color = 'tab:orange')
    complexityCostf.plot(x_axis, complexityCost.experiments[5].avgFitnessArray, color = 'tab:red')
    complexityCostf.plot(x_axis, complexityCost.experiments[6].avgFitnessArray, color = 'tab:pink')
    complexityCostf.plot(x_axis, complexityCost.experiments[7].avgFitnessArray, color = 'tab:purple')
    complexityCostf.plot(x_axis, complexityCost.experiments[8].avgFitnessArray, color = 'magenta')
    complexityCostf.plot(x_axis, complexityCost.experiments[9].avgFitnessArray, color = 'cyan')
    complexityCostf.plot(x_axis, complexityCost.experiments[10].avgFitnessArray, color = 'tab:blue')
    complexityCostf.plot(x_axis, complexityCost.experiments[11].avgFitnessArray, color = 'blue')    
    
    fitnessTrend.legend(loc='center right')
    fitnessTrend.savefig('avgFitnessOverGenerations.png')
    
    print("plotting complexity trends")
    complexityTrend, (baselinec, complexityCostc) = plt.subplots(1,2,sharey=True)
    # fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    complexityTrend.set_figheight(5)
    complexityTrend.set_figwidth(14)
    
    baselinec.set_title("Baseline Experiment")
    baselinec.set_ylabel("Average Complexity of Population")
    baselinec.set_xlabel("Generation")
    baselinec.plot(x_axis, baseline.experiments[0].avgComplexityArray, color = 'tab:grey', label='Environment 1')
    baselinec.plot(x_axis, baseline.experiments[1].avgComplexityArray, color = 'tab:olive', label='Environment 2')
    baselinec.plot(x_axis, baseline.experiments[2].avgComplexityArray, color = 'tab:green', label='Environment 3')
    baselinec.plot(x_axis, baseline.experiments[3].avgComplexityArray, color = 'tab:brown', label='Environment 4')
    baselinec.plot(x_axis, baseline.experiments[4].avgComplexityArray, color = 'tab:orange', label='Environment 5')
    baselinec.plot(x_axis, baseline.experiments[5].avgComplexityArray, color = 'tab:red', label='Environment 6')
    baselinec.plot(x_axis, baseline.experiments[6].avgComplexityArray, color = 'tab:pink', label='Environment 7')
    baselinec.plot(x_axis, baseline.experiments[7].avgComplexityArray, color = 'tab:purple', label='Environment 8')
    baselinec.plot(x_axis, baseline.experiments[8].avgComplexityArray, color = 'magenta', label='Environment 9')
    baselinec.plot(x_axis, baseline.experiments[9].avgComplexityArray, color = 'cyan', label='Environment 10')
    baselinec.plot(x_axis, baseline.experiments[10].avgComplexityArray, color = 'tab:blue', label='Environment 11')
    baselinec.plot(x_axis, baseline.experiments[11].avgComplexityArray, color = 'blue', label='Environment 12')
    
    complexityCostc.set_title("Complexity Cost Experiment")
    complexityCostc.set_ylabel("Average Complexity of Population")
    complexityCostc.set_xlabel("Generation")    
    complexityCostc.plot(x_axis, complexityCost.experiments[0].avgComplexityArray, color = 'tab:grey')
    complexityCostc.plot(x_axis, complexityCost.experiments[1].avgComplexityArray, color = 'tab:olive')
    complexityCostc.plot(x_axis, complexityCost.experiments[2].avgComplexityArray, color = 'tab:green')
    complexityCostc.plot(x_axis, complexityCost.experiments[3].avgComplexityArray, color = 'tab:brown')
    complexityCostc.plot(x_axis, complexityCost.experiments[4].avgComplexityArray, color = 'tab:orange')
    complexityCostc.plot(x_axis, complexityCost.experiments[5].avgComplexityArray, color = 'tab:red')
    complexityCostc.plot(x_axis, complexityCost.experiments[6].avgComplexityArray, color = 'tab:pink')
    complexityCostc.plot(x_axis, complexityCost.experiments[7].avgComplexityArray, color = 'tab:purple')
    complexityCostc.plot(x_axis, complexityCost.experiments[8].avgComplexityArray, color = 'magenta')
    complexityCostc.plot(x_axis, complexityCost.experiments[9].avgComplexityArray, color = 'cyan')
    complexityCostc.plot(x_axis, complexityCost.experiments[10].avgComplexityArray, color = 'tab:blue')
    complexityCostc.plot(x_axis, complexityCost.experiments[11].avgComplexityArray, color = 'blue')    
    
    complexityTrend.legend(loc='center right')
    complexityTrend.savefig('avgComplexityOverGenerations.png')    
    
    
    print("program done")
    
    
if __name__=="__main__":
    main()
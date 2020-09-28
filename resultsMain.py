from Results import Results
import matplotlib.pyplot as plt

def main():
    print("initialising baseline")
    baseline = Results("noveltyResults/baseline/")
    
    
    print("initialising complexityCost")
    complexityCost = Results("noveltyResults/complexityCost/")
    
    print("plotting graphs")
    x_axis = list(range(1,101))
    
    fitnessTrend, (baselinef, complexityCostf) = plt.subplots(1,2,sharey=True)
    # fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    fitnessTrend.set_figheight(5)
    fitnessTrend.set_figwidth(14)
    
    baselinef.set_title("Baseline Experiment")
    baselinef.set_ylabel("Average Fitness of Population")
    baselinef.set_xlabel("Generation")
    baselinef.plot(x_axis, baseline.experiments[0].avgFitnessArray, color = 'red', label='Environment 1')
    baselinef.plot(x_axis, baseline.experiments[1].avgFitnessArray, color = 'blue', label='Environment 2')
    baselinef.plot(x_axis, baseline.experiments[2].avgFitnessArray, color = 'green', label='Environment 3')
    baselinef.plot(x_axis, baseline.experiments[3].avgFitnessArray, color = 'tab:brown', label='Environment 4')
    baselinef.plot(x_axis, baseline.experiments[4].avgFitnessArray, color = 'tab:gray', label='Environment 5')
    baselinef.plot(x_axis, baseline.experiments[5].avgFitnessArray, color = 'tab:orange', label='Environment 6')
    baselinef.plot(x_axis, baseline.experiments[6].avgFitnessArray, color = 'tab:cyan', label='Environment 7')
    baselinef.plot(x_axis, baseline.experiments[7].avgFitnessArray, color = 'tab:purple', label='Environment 8')
    baselinef.plot(x_axis, baseline.experiments[8].avgFitnessArray, color = 'tab:pink', label='Environment 9')
    baselinef.plot(x_axis, baseline.experiments[9].avgFitnessArray, color = 'magenta', label='Environment 10')
    baselinef.plot(x_axis, baseline.experiments[10].avgFitnessArray, color = 'tab:blue', label='Environment 11')
    baselinef.plot(x_axis, baseline.experiments[11].avgFitnessArray, color = 'black', label='Environment 12')
    
    complexityCostf.set_title("Complexity Cost Experiment")
    complexityCostf.set_ylabel("Average Fitness of Population")
    complexityCostf.set_xlabel("Generation")    
    complexityCostf.plot(x_axis, complexityCost.experiments[0].avgFitnessArray, color = 'red')
    complexityCostf.plot(x_axis, complexityCost.experiments[1].avgFitnessArray, color = 'blue')
    complexityCostf.plot(x_axis, complexityCost.experiments[2].avgFitnessArray, color = 'green')
    complexityCostf.plot(x_axis, complexityCost.experiments[3].avgFitnessArray, color = 'tab:brown')
    complexityCostf.plot(x_axis, complexityCost.experiments[4].avgFitnessArray, color = 'tab:gray')
    complexityCostf.plot(x_axis, complexityCost.experiments[5].avgFitnessArray, color = 'tab:orange')
    complexityCostf.plot(x_axis, complexityCost.experiments[6].avgFitnessArray, color = 'tab:cyan')
    complexityCostf.plot(x_axis, complexityCost.experiments[7].avgFitnessArray, color = 'tab:purple')
    complexityCostf.plot(x_axis, complexityCost.experiments[8].avgFitnessArray, color = 'tab:pink')
    complexityCostf.plot(x_axis, complexityCost.experiments[9].avgFitnessArray, color = 'magenta')
    complexityCostf.plot(x_axis, complexityCost.experiments[10].avgFitnessArray, color = 'tab:blue')
    complexityCostf.plot(x_axis, complexityCost.experiments[11].avgFitnessArray, color = 'black')    
    
    # fitnessTrend.tight_layout()
    
    fitnessTrend.legend(loc='center right')
    #fitnessTrend.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    fitnessTrend.show()
    fitnessTrend.savefig('avgFitnessOverGenerations.png')
    print("program done")
    
    
if __name__=="__main__":
    main()
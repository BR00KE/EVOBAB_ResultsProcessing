from Results import Results
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
from scipy import stats

def main():
    print("initialising baseline")
    baseline = Results("noveltyResults/baseline/")
    
    print("initialising complexityCost")
    complexityCost = Results("noveltyResults/complexityCost/")
       
    ######################################################################################################################################
    #print("levene test for equal variance")
    
    #for e in range(12):
        #af = stats.levene(baseline.experiments[e].averageFitnessPerRepeat, complexityCost.experiments[e].averageFitnessPerRepeat)
        #ac = stats.levene(baseline.experiments[e].averageComplexityPerRepeat, complexityCost.experiments[e].averageComplexityPerRepeat)
        #hf = stats.levene(baseline.experiments[e].highestFitnessPerRepeat, complexityCost.experiments[e].highestFitnessPerRepeat)
        #hc = stats.levene(baseline.experiments[e].highestComplexityPerRepeat, complexityCost.experiments[e].highestComplexityPerRepeat)
        
        #if(af.pvalue<=0.05 or ac.pvalue<=0.05 or hf.pvalue<=0.05 or hc.pvalue<=0.05):
            #print("different varaince " + str(e))
    
    #for s in range(4):
        #af = stats.levene(baseline.experiments[3*s+0].averageFitnessPerRepeat, baseline.experiments[3*s+1].averageFitnessPerRepeat, baseline.experiments[3*s+2].averageFitnessPerRepeat)
        #ac = stats.levene(baseline.experiments[3*s+0].averageComplexityPerRepeat, baseline.experiments[3*s+1].averageComplexityPerRepeat, baseline.experiments[3*s+2].averageComplexityPerRepeat)
        #hf = stats.levene(baseline.experiments[3*s+0].highestFitnessPerRepeat, baseline.experiments[3*s+1].highestFitnessPerRepeat, baseline.experiments[3*s+2].highestFitnessPerRepeat)
        #hc = stats.levene(baseline.experiments[3*s+0].highestComplexityPerRepeat, baseline.experiments[3*s+1].highestComplexityPerRepeat, baseline.experiments[3*s+2].highestComplexityPerRepeat)
        
        #if(af.pvalue<=0.05 or ac.pvalue<=0.05 or hf.pvalue<=0.05 or hc.pvalue<=0.05):
            #print("different varaince baseline set " + str(s+1))
            
        #af = stats.levene(complexityCost.experiments[3*s+0].averageFitnessPerRepeat, complexityCost.experiments[3*s+1].averageFitnessPerRepeat, complexityCost.experiments[3*s+2].averageFitnessPerRepeat)
        #ac = stats.levene(complexityCost.experiments[3*s+0].averageComplexityPerRepeat, complexityCost.experiments[3*s+1].averageComplexityPerRepeat, complexityCost.experiments[3*s+2].averageComplexityPerRepeat)
        #hf = stats.levene(complexityCost.experiments[3*s+0].highestFitnessPerRepeat, complexityCost.experiments[3*s+1].highestFitnessPerRepeat, complexityCost.experiments[3*s+2].highestFitnessPerRepeat)
        #hc = stats.levene(complexityCost.experiments[3*s+0].highestComplexityPerRepeat, complexityCost.experiments[3*s+1].highestComplexityPerRepeat, complexityCost.experiments[3*s+2].highestComplexityPerRepeat)
        
        #if(af.pvalue<=0.05 or ac.pvalue<=0.05 or hf.pvalue<=0.05 or hc.pvalue<=0.05):
            #print("different varaince complexityCost set " + str(s+1))
    ######################################################################################################################################
    #print("making Mann-Whitney Statistical comparison table")
    
    #table = []
    #for e in range(12):
        #enviro = [ e+1 ]
        #u_statistic, p_value = stats.mannwhitneyu(baseline.experiments[e].averageFitnessPerRepeat, complexityCost.experiments[e].averageFitnessPerRepeat)
        #enviro.append(p_value)
        #u_statistic, p_value = stats.mannwhitneyu(baseline.experiments[e].averageComplexityPerRepeat, complexityCost.experiments[e].averageComplexityPerRepeat)
        #enviro.append(p_value)
        #u_statistic, p_value = stats.mannwhitneyu(baseline.experiments[e].highestFitnessPerRepeat, complexityCost.experiments[e].highestFitnessPerRepeat)
        #enviro.append(p_value)
        #u_statistic, p_value = stats.mannwhitneyu(baseline.experiments[e].highestComplexityPerRepeat, complexityCost.experiments[e].highestComplexityPerRepeat)
        #enviro.append(p_value)        
        #table.append(enviro)
    #df = pd.DataFrame(np.array(table), columns = ['Environment','Average Fitness', ' Average Robot Complexity', 'Best Fitness', 'Complexity Associated with Best Fitness'])
    #print(df.to_latex(index=False))
    ######################################################################################################################################
    print("box and whisker plots")
    mpl.use('agg')
        
    boxPlots, axes = plt.subplots(1,4, sharey=True)
    boxPlots.set_figheight(4)
    boxPlots.set_figwidth(16)
    
    labelsSet1 = ['1','1','2','2','3','3']
    labelsSet2 = ['4','4','5','5','6','6']
    labelsSet3 = ['7','7','8','8','9','9']
    labelsSet4 = ['10','10','11','11','12','12']
    
    colors = ['green','blue','green','blue','green','blue']
    
    set1data=[]
    set2data=[]
    set3data=[]
    set4data=[]
    #create set data alternating baseline and complexityCost
    for e in range(6):
        if(e%2==0):
            i = int(e/2)
            set1data.append(baseline.experiments[i].highestComplexityPerRepeat)
            set2data.append(baseline.experiments[3+i].highestComplexityPerRepeat)
            set3data.append(baseline.experiments[6+i].highestComplexityPerRepeat)
            set4data.append(baseline.experiments[9+i].highestComplexityPerRepeat)
        else:
            i = int((e-1)/2)
            set1data.append(complexityCost.experiments[i].highestComplexityPerRepeat)
            set2data.append(complexityCost.experiments[3+i].highestComplexityPerRepeat)
            set3data.append(complexityCost.experiments[6+i].highestComplexityPerRepeat)
            set4data.append(complexityCost.experiments[9+i].highestComplexityPerRepeat)            
    
    
    bplotSet1 = axes[0].boxplot(set1data, vert=True, patch_artist=True, labels = labelsSet1)
    axes[0].set_title('Environment Set 1')
    axes[0].set_ylabel('Robot Complexity')
    axes[0].set_xlabel('Environment Number')
    bplotSet2 = axes[1].boxplot(set2data, vert=True, patch_artist=True, labels = labelsSet2)
    axes[1].set_title('Environment Set 2')
    axes[1].set_xlabel('Environment Number')
    #axes[0][1].set_ylabel('Task Performance')
    bplotSet3 = axes[2].boxplot(set3data, vert=True, patch_artist=True, labels = labelsSet3)
    axes[2].set_title('Environment Set 3')
    axes[2].set_xlabel('Environment Number')
    #axes[2].set_ylabel('Task Performance')
    bplotSet4 = axes[3].boxplot(set4data, vert=True, patch_artist=True, labels = labelsSet4)
    axes[3].set_title('Environment Set 4')    
    axes[3].set_xlabel('Environment Number')
    #axes[1][1].set_ylabel('Task Performance')
    
    for bplot in (bplotSet1,bplotSet2,bplotSet3,bplotSet4):
        for patch,color in zip(bplot['boxes'],colors):
            patch.set_facecolor(color)
    
    green_patch = mpatches.Patch(color='green',label='Baseline')
    blue_patch = mpatches.Patch(color='blue',label = 'Complexity\n Cost')
    boxPlots.legend(handles=[green_patch,blue_patch], title='Experiment',loc=4)
    boxPlots.savefig('highestAverageComplexityBoxplot.png')        
    
    ######################################################################################################################################
    #print("plotting graphs")
    #x_axis = list(range(1,101))
    
    #print("plotting highest fitness trend")
    #highestFitnessTrend, (baselinehf, complexityCosthf) = plt.subplots(1,2,sharey=True)
    ## fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    #highestFitnessTrend.set_figheight(5)
    #highestFitnessTrend.set_figwidth(14)
    
    #baselinehf.set_title("Baseline Experiment")
    #baselinehf.set_ylabel("Average Highest Fitness")
    #baselinehf.set_xlabel("Generation")
    #baselinehf.plot(x_axis, baseline.experiments[0].avgHighestFitnessArray, color = 'tab:grey', label='Environment 1')
    #baselinehf.plot(x_axis, baseline.experiments[1].avgHighestFitnessArray, color = 'tab:olive', label='Environment 2')
    #baselinehf.plot(x_axis, baseline.experiments[2].avgHighestFitnessArray, color = 'tab:green', label='Environment 3')
    #baselinehf.plot(x_axis, baseline.experiments[3].avgHighestFitnessArray, color = 'tab:brown', label='Environment 4')
    #baselinehf.plot(x_axis, baseline.experiments[4].avgHighestFitnessArray, color = 'tab:orange', label='Environment 5')
    #baselinehf.plot(x_axis, baseline.experiments[5].avgHighestFitnessArray, color = 'tab:red', label='Environment 6')
    #baselinehf.plot(x_axis, baseline.experiments[6].avgHighestFitnessArray, color = 'tab:pink', label='Environment 7')
    #baselinehf.plot(x_axis, baseline.experiments[7].avgHighestFitnessArray, color = 'tab:purple', label='Environment 8')
    #baselinehf.plot(x_axis, baseline.experiments[8].avgHighestFitnessArray, color = 'magenta', label='Environment 9')
    #baselinehf.plot(x_axis, baseline.experiments[9].avgHighestFitnessArray, color = 'cyan', label='Environment 10')
    #baselinehf.plot(x_axis, baseline.experiments[10].avgHighestFitnessArray, color = 'tab:blue', label='Environment 11')
    #baselinehf.plot(x_axis, baseline.experiments[11].avgHighestFitnessArray, color = 'blue', label='Environment 12')
    
    #complexityCosthf.set_title("Complexity Cost Experiment")
    #complexityCosthf.set_ylabel("Average Highest Fitness")
    #complexityCosthf.set_xlabel("Generation")    
    #complexityCosthf.plot(x_axis, complexityCost.experiments[0].avgHighestFitnessArray, color = 'tab:grey')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[1].avgHighestFitnessArray, color = 'tab:olive')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[2].avgHighestFitnessArray, color = 'tab:green')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[3].avgHighestFitnessArray, color = 'tab:brown')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[4].avgHighestFitnessArray, color = 'tab:orange')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[5].avgHighestFitnessArray, color = 'tab:red')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[6].avgHighestFitnessArray, color = 'tab:pink')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[7].avgHighestFitnessArray, color = 'tab:purple')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[8].avgHighestFitnessArray, color = 'magenta')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[9].avgHighestFitnessArray, color = 'cyan')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[10].avgHighestFitnessArray, color = 'tab:blue')
    #complexityCosthf.plot(x_axis, complexityCost.experiments[11].avgHighestFitnessArray, color = 'blue')    
    
    #highestFitnessTrend.legend(loc='center right')
    #highestFitnessTrend.savefig('highestFitnessOverGenerations.png')
    
    #print("plotting highest complexity trends")
    #highestComplexityTrend, (baselinehc, complexityCosthc) = plt.subplots(1,2,sharey=True)
    ## fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    #highestComplexityTrend.set_figheight(5)
    #highestComplexityTrend.set_figwidth(14)
    
    #baselinehc.set_title("Baseline Experiment")
    #baselinehc.set_ylabel("Average Highest Complexity")
    #baselinehc.set_xlabel("Generation")
    #baselinehc.plot(x_axis, baseline.experiments[0].avgHighestComplexityArray, color = 'tab:grey', label='Environment 1')
    #baselinehc.plot(x_axis, baseline.experiments[1].avgHighestComplexityArray, color = 'tab:olive', label='Environment 2')
    #baselinehc.plot(x_axis, baseline.experiments[2].avgHighestComplexityArray, color = 'tab:green', label='Environment 3')
    #baselinehc.plot(x_axis, baseline.experiments[3].avgHighestComplexityArray, color = 'tab:brown', label='Environment 4')
    #baselinehc.plot(x_axis, baseline.experiments[4].avgHighestComplexityArray, color = 'tab:orange', label='Environment 5')
    #baselinehc.plot(x_axis, baseline.experiments[5].avgHighestComplexityArray, color = 'tab:red', label='Environment 6')
    #baselinehc.plot(x_axis, baseline.experiments[6].avgHighestComplexityArray, color = 'tab:pink', label='Environment 7')
    #baselinehc.plot(x_axis, baseline.experiments[7].avgHighestComplexityArray, color = 'tab:purple', label='Environment 8')
    #baselinehc.plot(x_axis, baseline.experiments[8].avgHighestComplexityArray, color = 'magenta', label='Environment 9')
    #baselinehc.plot(x_axis, baseline.experiments[9].avgHighestComplexityArray, color = 'cyan', label='Environment 10')
    #baselinehc.plot(x_axis, baseline.experiments[10].avgHighestComplexityArray, color = 'tab:blue', label='Environment 11')
    #baselinehc.plot(x_axis, baseline.experiments[11].avgHighestComplexityArray, color = 'blue', label='Environment 12')
    
    #complexityCosthc.set_title("Complexity Cost Experiment")
    #complexityCosthc.set_ylabel("Average Highest Complexity")
    #complexityCosthc.set_xlabel("Generation")    
    #complexityCosthc.plot(x_axis, complexityCost.experiments[0].avgHighestComplexityArray, color = 'tab:grey')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[1].avgHighestComplexityArray, color = 'tab:olive')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[2].avgHighestComplexityArray, color = 'tab:green')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[3].avgHighestComplexityArray, color = 'tab:brown')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[4].avgHighestComplexityArray, color = 'tab:orange')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[5].avgHighestComplexityArray, color = 'tab:red')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[6].avgHighestComplexityArray, color = 'tab:pink')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[7].avgHighestComplexityArray, color = 'tab:purple')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[8].avgHighestComplexityArray, color = 'magenta')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[9].avgHighestComplexityArray, color = 'cyan')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[10].avgHighestComplexityArray, color = 'tab:blue')
    #complexityCosthc.plot(x_axis, complexityCost.experiments[11].avgHighestComplexityArray, color = 'blue')    
    
    #highestComplexityTrend.legend(loc='center right')
    #highestComplexityTrend.savefig('highestComplexityOverGenerations.png')    
    ######################################################################################################################################
    #print("plotting fitness trends")
    #fitnessTrend, (baselinef, complexityCostf) = plt.subplots(1,2,sharey=True)
    ## fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    #fitnessTrend.set_figheight(5)
    #fitnessTrend.set_figwidth(14)
    
    #baselinef.set_title("Baseline Experiment")
    #baselinef.set_ylabel("Average Fitness of Population")
    #baselinef.set_xlabel("Generation")
    #baselinef.plot(x_axis, baseline.experiments[0].avgFitnessArray, color = 'tab:grey', label='Environment 1')
    #baselinef.plot(x_axis, baseline.experiments[1].avgFitnessArray, color = 'tab:olive', label='Environment 2')
    #baselinef.plot(x_axis, baseline.experiments[2].avgFitnessArray, color = 'tab:green', label='Environment 3')
    #baselinef.plot(x_axis, baseline.experiments[3].avgFitnessArray, color = 'tab:brown', label='Environment 4')
    #baselinef.plot(x_axis, baseline.experiments[4].avgFitnessArray, color = 'tab:orange', label='Environment 5')
    #baselinef.plot(x_axis, baseline.experiments[5].avgFitnessArray, color = 'tab:red', label='Environment 6')
    #baselinef.plot(x_axis, baseline.experiments[6].avgFitnessArray, color = 'tab:pink', label='Environment 7')
    #baselinef.plot(x_axis, baseline.experiments[7].avgFitnessArray, color = 'tab:purple', label='Environment 8')
    #baselinef.plot(x_axis, baseline.experiments[8].avgFitnessArray, color = 'magenta', label='Environment 9')
    #baselinef.plot(x_axis, baseline.experiments[9].avgFitnessArray, color = 'cyan', label='Environment 10')
    #baselinef.plot(x_axis, baseline.experiments[10].avgFitnessArray, color = 'tab:blue', label='Environment 11')
    #baselinef.plot(x_axis, baseline.experiments[11].avgFitnessArray, color = 'blue', label='Environment 12')
    
    #complexityCostf.set_title("Complexity Cost Experiment")
    #complexityCostf.set_ylabel("Average Fitness of Population")
    #complexityCostf.set_xlabel("Generation")    
    #complexityCostf.plot(x_axis, complexityCost.experiments[0].avgFitnessArray, color = 'tab:grey')
    #complexityCostf.plot(x_axis, complexityCost.experiments[1].avgFitnessArray, color = 'tab:olive')
    #complexityCostf.plot(x_axis, complexityCost.experiments[2].avgFitnessArray, color = 'tab:green')
    #complexityCostf.plot(x_axis, complexityCost.experiments[3].avgFitnessArray, color = 'tab:brown')
    #complexityCostf.plot(x_axis, complexityCost.experiments[4].avgFitnessArray, color = 'tab:orange')
    #complexityCostf.plot(x_axis, complexityCost.experiments[5].avgFitnessArray, color = 'tab:red')
    #complexityCostf.plot(x_axis, complexityCost.experiments[6].avgFitnessArray, color = 'tab:pink')
    #complexityCostf.plot(x_axis, complexityCost.experiments[7].avgFitnessArray, color = 'tab:purple')
    #complexityCostf.plot(x_axis, complexityCost.experiments[8].avgFitnessArray, color = 'magenta')
    #complexityCostf.plot(x_axis, complexityCost.experiments[9].avgFitnessArray, color = 'cyan')
    #complexityCostf.plot(x_axis, complexityCost.experiments[10].avgFitnessArray, color = 'tab:blue')
    #complexityCostf.plot(x_axis, complexityCost.experiments[11].avgFitnessArray, color = 'blue')    
    
    #fitnessTrend.legend(loc='center right')
    #fitnessTrend.savefig('avgFitnessOverGenerations.png')
    
    #print("plotting complexity trends")
    #complexityTrend, (baselinec, complexityCostc) = plt.subplots(1,2,sharey=True)
    ## fitnessTrend.suptitle("Graph showing the average fitness of the population over all generations for evolutions in each environment for both experiments", wrap=True)
    
    #complexityTrend.set_figheight(5)
    #complexityTrend.set_figwidth(14)
    
    #baselinec.set_title("Baseline Experiment")
    #baselinec.set_ylabel("Average Complexity of Population")
    #baselinec.set_xlabel("Generation")
    #baselinec.plot(x_axis, baseline.experiments[0].avgComplexityArray, color = 'tab:grey', label='Environment 1')
    #baselinec.plot(x_axis, baseline.experiments[1].avgComplexityArray, color = 'tab:olive', label='Environment 2')
    #baselinec.plot(x_axis, baseline.experiments[2].avgComplexityArray, color = 'tab:green', label='Environment 3')
    #baselinec.plot(x_axis, baseline.experiments[3].avgComplexityArray, color = 'tab:brown', label='Environment 4')
    #baselinec.plot(x_axis, baseline.experiments[4].avgComplexityArray, color = 'tab:orange', label='Environment 5')
    #baselinec.plot(x_axis, baseline.experiments[5].avgComplexityArray, color = 'tab:red', label='Environment 6')
    #baselinec.plot(x_axis, baseline.experiments[6].avgComplexityArray, color = 'tab:pink', label='Environment 7')
    #baselinec.plot(x_axis, baseline.experiments[7].avgComplexityArray, color = 'tab:purple', label='Environment 8')
    #baselinec.plot(x_axis, baseline.experiments[8].avgComplexityArray, color = 'magenta', label='Environment 9')
    #baselinec.plot(x_axis, baseline.experiments[9].avgComplexityArray, color = 'cyan', label='Environment 10')
    #baselinec.plot(x_axis, baseline.experiments[10].avgComplexityArray, color = 'tab:blue', label='Environment 11')
    #baselinec.plot(x_axis, baseline.experiments[11].avgComplexityArray, color = 'blue', label='Environment 12')
    
    #complexityCostc.set_title("Complexity Cost Experiment")
    #complexityCostc.set_ylabel("Average Complexity of Population")
    #complexityCostc.set_xlabel("Generation")    
    #complexityCostc.plot(x_axis, complexityCost.experiments[0].avgComplexityArray, color = 'tab:grey')
    #complexityCostc.plot(x_axis, complexityCost.experiments[1].avgComplexityArray, color = 'tab:olive')
    #complexityCostc.plot(x_axis, complexityCost.experiments[2].avgComplexityArray, color = 'tab:green')
    #complexityCostc.plot(x_axis, complexityCost.experiments[3].avgComplexityArray, color = 'tab:brown')
    #complexityCostc.plot(x_axis, complexityCost.experiments[4].avgComplexityArray, color = 'tab:orange')
    #complexityCostc.plot(x_axis, complexityCost.experiments[5].avgComplexityArray, color = 'tab:red')
    #complexityCostc.plot(x_axis, complexityCost.experiments[6].avgComplexityArray, color = 'tab:pink')
    #complexityCostc.plot(x_axis, complexityCost.experiments[7].avgComplexityArray, color = 'tab:purple')
    #complexityCostc.plot(x_axis, complexityCost.experiments[8].avgComplexityArray, color = 'magenta')
    #complexityCostc.plot(x_axis, complexityCost.experiments[9].avgComplexityArray, color = 'cyan')
    #complexityCostc.plot(x_axis, complexityCost.experiments[10].avgComplexityArray, color = 'tab:blue')
    #complexityCostc.plot(x_axis, complexityCost.experiments[11].avgComplexityArray, color = 'blue')    
    
    #complexityTrend.legend(loc='center right')
    #complexityTrend.savefig('avgComplexityOverGenerations.png')    
    ######################################################################################################################################
    
    #Shapiro-wilk test for dataset normality
    #test rejects the hypothesis of normality when the p-value is p <=0.05
    #failing the normality test allows you to state with 95% confidence that the data does not fit the normal distribution
    #np.random.seed(12345678)
    #print("Shapiro-Wilk tests for dataset normality")
    
    #test normality of all the average fitness datasets
    #print("baseline")
    #for e in range(12):
        #avgFitnessTest = stats.shapiro(baseline.experiments[e].averageFitnessPerRepeat)
        #if(avgFitnessTest.pvalue<=0.05):
            #print("not normal " + str(e) + " " + str(avgFitnessTest.pvalue))
        #avgComplexityTest = stats.shapiro(baseline.experiments[e].averageComplexityPerRepeat)
        #if(avgComplexityTest.pvalue<=0.05):
            #print("not normal " + str(e) + " " + str(avgComplexityTest.pvalue)) 
        #highestFitnessTest = stats.shapiro(baseline.experiments[e].highestFitnessPerRepeat)
        #if(highestFitnessTest.pvalue<=0.05):
            #print("not normal higest fitness " + str(e) + " " + str(highestFitnessTest.pvalue))   
        #highestComplexityTest = stats.shapiro(baseline.experiments[e].highestComplexityPerRepeat)
        #if(highestComplexityTest.pvalue<=0.05):
            #print("not normal highest complexity " + str(e) + " " + str(highestComplexityTest.pvalue))       
    #print("complexityCost")
    #for e in range(12):
        #avgFitnessTest = stats.shapiro(complexityCost.experiments[e].averageFitnessPerRepeat)
        #if(avgFitnessTest.pvalue<=0.05):
            #print("not normal " + str(e) + " " + str(avgFitnessTest.pvalue))
        #avgComplexityTest = stats.shapiro(complexityCost.experiments[e].averageComplexityPerRepeat)
        #if(avgComplexityTest.pvalue<=0.05):
            #print("not normal " + str(e) + " " + str(avgComplexityTest.pvalue)) 
        #highestFitnessTest = stats.shapiro(complexityCost.experiments[e].highestFitnessPerRepeat)
        #if(highestFitnessTest.pvalue<=0.05):
            #print("not normal highest fitness " + str(e) + " " + str(highestFitnessTest.pvalue))   
        #highestComplexityTest = stats.shapiro(complexityCost.experiments[e].highestComplexityPerRepeat)
        #if(highestComplexityTest.pvalue<=0.05):
            #print("not normal highest complexity " + str(e)  + " " + str(highestComplexityTest.pvalue))    
    ######################################################################################################################################
    print("program done")
    
    
if __name__=="__main__":
    main()
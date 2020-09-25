from Results import Results

def main():
    print("initialising baseline")
    baseline = Results("noveltyResults/baseline/")
    
    
    print("initialising complexityCost")
    complexityCost = Results("noveltyResults/complexityCost/")
    
if __name__=="__main__":
    main()
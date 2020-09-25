from Results import Results

def main():
    print("initialising baseline")
    baseline = Results("noveltyResults/baseline")
    print(baseline.dir)
    
    
    print("initialising complexityCost")
    complexityCost = Results("noveltyResults/baseline")
    
if __name__=="__main__":
    main()
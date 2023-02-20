def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    for x in range(3):
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))
    #print("Compound Interest: "+str(intrest))
        A = client_one_principal * ( 1 + client_one_rate/100)**client_one_time
        CI = A - client_one_principal
        C = round(CI, 2)
        print(f"Compound Interest: {C}")
        if x<(2):
            print("---")
        
    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()

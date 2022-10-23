import pulp as p

# Generate a New LP Maximization Problem:

#GENERATE CLASSES
global Products
Products = {}
class Product:
    def __init__(self,Name,Recipe,Hours,SP):
        #Insert a string and get a dictionary out of it
        # Recipe = {"Wood":10;"Nails":20}
        self.Recipe = dict(subString.split(" = ") for subString in Recipe.split(";"))

        self.Hours = Hours

        self.Selling_Point = SP

        Products[Name] = self
        

global Materials
Materials = {}
class Material:
    def __init__(self,Name,Price):

        self.Price = Price
        Materials[Name] = self




def Solve(Budget,Hours):
    Lp_prob2 = p.LpProblem('Activity-Analysis_2', p.LpMaximize)

    # GENERATE OBJECTS

    Wood  = Material("Wood" ,2)
    Nails = Material("Nails",3)

    chair = Product("Chair","Wood = 5;Nails = 10",12,45)
    table = Product("Table","Wood = 10;Nails = 7",7,50)


    
    # Generate Problem Variables (>= 0):
    global Variables
    Variables = {}
    for i in Products:
        Variables[i] = p.LpVariable(i, lowBound = 0)




    '''
    Variables[Product1] = [Product1_Variable]
    '''



    # Create Profit Function:
    Profit = 0
    for i in Products:
        Profit += (Products[i].Selling_Point)*Variables[i]

    #Add it to the Problem
    Lp_prob2 += Profit 
      
    # Set Up the Constraints:
    Labour = 0
    Cost   = 0
    for i in Materials:
        for j in Products:
            Cost += Materials[i].Price*int(Products[j].Recipe[i])*Variables[j]
            Labour+= (Products[j].Hours/2) *Variables[j]
    #Labor constraint
    Lp_prob2 += Labour <= Hours

    #budget constraint
    Lp_prob2 +=  Cost<= Budget
    print(Lp_prob2)


    # Solve the Problem:
    status = Lp_prob2.solve()
    #print(p.LpStatus[status])
    End_Sale = 0
    Payload = {} 
    for i in Variables:
        Payload[i] = int(p.value(Variables[i]))
        End_Sale +=int(p.value(Variables[i]))*Products[i].Selling_Point
    print(Payload,End_Sale)
    return (Payload,End_Sale)

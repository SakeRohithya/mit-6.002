class item(object):
    def __init__(self,name,values,wt):
        self.name=name
        self.value=values
        self.wt = wt
        self.density = values/wt
    def getName(self):
         return self.name
    def getValue(self):
         return self.value
    def getWeight(self):
         return self.wt
    def getDensity(self):
         return self.density
    def __str__(self):
         return '< '+self.name+','+str(self.value) +','+ str(self.density) + '>'

def value(item):
    return item.getValue()
def density(item):
    return item.getDensity()

def greedy(items,keyfunction,maxwt):
    itemcopy=sorted(items,key=keyfunction,reverse=True)
    totwt = 0
    totvalue=0.0
    result = []
    for i in range(len(itemcopy)):
        if totwt + itemcopy[i].getWeight()<=maxwt:
            result.append(itemcopy[i])
            totwt = totwt + itemcopy[i].getWeight()
            totvalue = totvalue + itemcopy[i].getValue()
    
    return (result,totvalue,totwt)

    
def buildItems():
    names = ['clock','painting','radio','vase','book','computer']
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(values)):
        Items.append(item(names[i], values[i], weights[i]))

    return Items

def testgreedy(Items,maxwt,keyfunction):
    re,val,wt = greedy(Items,keyfunction,maxwt)
    print('Total Value of items in Knapsack: ',val)
    print('Total weight of items in Knapsack: ',wt)
    print('Items in knapsack')
    for i in range(len(re)):
        print(re[i])

def finalgreedy(maxwt=20):
    Items = buildItems()
    print('BY VALUE GREEDY METHOD')
    testgreedy(Items,maxwt,value)
    print('BY DENSITY GREEDY METHOD')
    testgreedy(Items,maxwt,density)
    

#finalgreedy()

def smalltest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)



def maxVal(toconsider,wt):
    items = []
    if toconsider==[] or wt ==0:
        result = (0,())
        






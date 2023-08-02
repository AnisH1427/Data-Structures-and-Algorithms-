class Temperature(object):
    def __init__(self):
        self.averageData=0
        self.count=0
        self.count_equal=0
        self.count_less=0
        
    def getData(self):
        print("-"*50)
        print("The average temperature of given days is :",self.averageData)
        print(f"{self.count} days has temperature more than the Average temperature")
        print(f"{self.count_equal} days has temperature equal to the Average temperature")
        print(f"{self.count_less} days has temperature less than the Average temperature")
        
    def takeInput(self):
        temp=int(input("How many days temperature you want ?\n"))
        print("-"*50)
        total=[] 
        
        #Asking user to input weather data and appending it to the list
        for i in range(1,temp+1):
            enterData=int(input("Day"+str(i)+"'s highest Temperature :"))
            total.append(enterData)
            
        #evaluating average temperature by rounding with 1 decimal points
        self.averageData=round(sum(total)/temp,1)
        
        #Evaluating three different range of temperature
        for i in total:
            if i>self.averageData:
                self.count+=1
            if i==self.averageData:
                self.count_equal+=1
            if i<self.averageData:
                self.count_less+=1
        self.getData()
getInfo=Temperature()
getInfo.takeInput()

        
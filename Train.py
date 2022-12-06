import requests
import pandas as pd

class Train:
    def __init__(self):
        self.api=input("Enter the API key: ")
        self.menu()
    
    def menu(self):
        print("""              1. Enter 1 to get train name from train number
              2. Enter 2 for search trains between two station
              3. Enter 3 to get train class
              4. Enter 4 to get train fare
              5. Enter 5 to exit.""")
        user_input=input("Enter the number : ")
        if user_input=="1":
            n=int(input("Enter the train number: "))
            self.train_name(n)
        elif user_input=="2":
            a,b=input("Enter both station code with space: ").split()
            self.train_search(a,b)
        elif user_input=="3":
            a=int(input("Enter train number: "))
            self.train_class(a)
        elif user_input=="4":
            a=int(input("Enter train number: "))
            b=input("Enter Source station code: ")
            c=input("Enter Destination station code: ")
            self.train_fare(a,b,c)
        elif user_input=="5":
            pass
        else:
            print("Invalid input")
            self.menu()
    
    def train_name(self,a):
        url = "https://irctc1.p.rapidapi.com/api/v1/searchTrain"
        querystring = {"query":a}
        headers = {
            "X-RapidAPI-Key": self.api,
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        for i in response["data"]:
            print("Train Number: ",i["train_number"],"  |  ","Train Name: ",i["eng_train_name"])
        self.menu()
    
    def train_search(self,p,q):
        trainName=[]
        trainNumber=[]
        departure=[]
        arrival=[]
        origin=[]
        destination=[]
        l=[trainName,trainNumber,departure,arrival,origin,destination]
        for i in l:
            i.clear()
        url = "https://irctc1.p.rapidapi.com/api/v2/trainBetweenStations"
        querystring = {"fromStationCode":p,"toStationCode":q}
        headers = {
            "X-RapidAPI-Key": self.api,
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        for i in response["data"]:
            trainName.append(i["train_name"])
            trainNumber.append(i["train_number"])
            departure.append(i["depart_time"])
            arrival.append(i["arrival_time"])
            origin.append(i["train_origin_station"])
            destination.append(i["train_destination_station"])
        Dic={"Train Number": trainNumber, "Train Name":trainName, "Departure Time":departure, "Arrival Time":arrival, "Origin Station": origin, "Last Station": destination}
        table=pd.DataFrame(Dic)
        table.style.set_properties(**{'text-align':'center'})
        print(table)
        self.menu()
    
    def train_class(self,a):
        url = "https://irctc1.p.rapidapi.com/api/v1/getTrainClasses"
        querystring = {"trainNo":a}
        headers = {
            "X-RapidAPI-Key": self.api,
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        for i in response["data"]:
            print(i)
        self.menu()
         
    def train_fare(self,a,b,c):
        c1=[]
        f1=[]
        c2=[]
        f2=[]
        l=[c1,f1,c2,f2]
        for i in l:
            i.clear()
        url = "https://irctc1.p.rapidapi.com/api/v2/getFare"
        querystring = {"trainNo":a,"fromStationCode":b,"toStationCode":c}
        headers = {
            "X-RapidAPI-Key": self.api,
            "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        for i in response["data"]["general"]:
            c1.append(i["classType"])
            f1.append(i["fare"])
        for i in response["data"]["tatkal"]:
            c2.append(i["classType"])
            f2.append(i["fare"])
        gendic={"Class":c1,"Fare":f1}
        tatdic={"Class":c2,"Fare":f2}
        gen=pd.DataFrame(gendic)
        tat=pd.DataFrame(tatdic)
        print("Enter 1 for General")
        print("Enter 2 for Tatkal")
        n=input("Enter the number: ")
        if n=="1":
            print(gen)
        elif n=="2":
            print(tat)
        else:
            print("Invalid Input")
        self.menu()
    



Train()
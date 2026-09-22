import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

anishsApplication = RailwayForm()
anishsApplication.name = "Anish"
anishsApplication.train = "Rajdhani Express"
anishsApplication.printData()
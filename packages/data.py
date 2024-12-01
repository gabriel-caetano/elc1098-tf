from packages.loader import loader
import os
import pandas as pd

class data:
    __folder: str
    __files: list[str]
    __data: list[loader]
    __header: list[str]
    __df: pd.DataFrame

    def __init__(self, folder):
        self.__folder = folder
        self.__files = os.listdir(self.__folder)
        self.__data = []
        self.__header = []

    def load(self):
        for file in self.__files:
            part = loader(f"{self.__folder}{file}")
            part.load()
            if (not len(self.__data)):
                self.__data.append(part)
                self.__header = part.getHeader()
            else:
                same_header = len(self.__header) == len(part.getHeader())
                if same_header:
                    for el in part.getHeader():
                        if el not in self.__header:
                            same_header = False
                
                if (same_header):
                    self.__data.append(part)
                else:
                    print('different cols being loaded')


    def getDataFrame(self):
        return pd.concat([ (x.getDataFrame()) for x in self.__data])
    
    def save(self):
        for d in self.__data:
            d.save()

    def print_cols(self):
        for d in self.__data:
            print(d.getHeader())
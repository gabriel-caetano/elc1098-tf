import pandas as pd

class loader:
    __df: pd.DataFrame
    __path: str
    __header: list[str]
    __center: str

    def __init__(self, path):
        self.__path = path
        self.__center = self.__path.split('/')[-1]
        self.__center = self.__center.split(' ')[0]
        self.__center = self.__center.split('_')[0]
        self.__center = self.__center.split('.')[0]
        self.__header = []


    def load(self):
        if self.__path.endswith('.xls'):
            self.__df = pd.read_excel(self.__path, engine='xlrd')
            self.__header = list(self.__df.columns.values)

        elif self.__path.endswith('.xlsx'):
            self.__df = pd.read_excel(self.__path, engine='openpyxl')
            self.__header = list(self.__df.columns.values)

        else:
            print("Arquivo inválido")
            return False
        if self.__center[0] != 'D':
            self.__df["CENTRO"] = self.__center
        print(f"Arquivo carregado com sucesso: {self.__path}")

    def getDataFrame(self):
        if (self.__df.empty):
            self.load()
        return self.__df
    
    def getHeader(self):
        return self.__header
    
    def save(self):
        name = self.__path.split('/')[-1].split('.')[0]
        self.__df.to_csv(f'ds/csv/{name}.csv', index=False, sep=",")
    

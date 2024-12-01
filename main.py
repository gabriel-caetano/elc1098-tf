from packages.loader import loader
from packages.data import data

def main():
    data_load = data("./ds/")
    data_load.load()
    data_load.save()
    data_load.print_cols()

    data_load = data("./ds/ief/")
    data_load.load()
    data_load.save()
    data_load.print_cols()




if __name__ == '__main__': 
    main()
if __name__=="__main__":
    from util import find
    month, date, year= list(map(int, input("enter date (mm/dd/yyyy):").split('/')))
    print(find(month,date,year))


def dooo(num):
    while num<10:
        num+=1
        yield num




if __name__ == '__main__':

    for i in dooo(0):
        print(i)
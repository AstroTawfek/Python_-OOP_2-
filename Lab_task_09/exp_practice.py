a = [10, 20, 30, 40, 50, 0]
b = int(input("Enter a number which to devide : "))
i = 0
while i<=len(a):
    try:
        result = b/a[i]
        if i==3 :
            print(y)
        elif i==4 :
            print(a[1]/'T')
    except ZeroDivisionError as e :
        print("Error :",e)
    except ValueError as e:
        print("Error :",e)
    except TypeError as e :
        print(print("Error :",e))
    except NameError as e :
        print("Error :",e)
    except IndexError as e :
        print("Error :",e)
    except :
        print("there is something error in try block.")
    else :
        print("Result : ", result)
    finally :
        print("The exception is handled successfully")
    i=i+1
try:
    a =[10, 20, 30, 0]
    
    try :
        for i in range a :
            b = int(input("Enter a number :" ))
            try :
                result = a/b
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
                
    except : 
        print("Error : ",e)
        
except :
    print("Something error occured")
    
else :
    print("Rest of the code is okay")
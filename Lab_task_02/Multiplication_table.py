def mult_table(x):
    for i in range(1,11,1):
        if i==4:
            continue

        print(f"{x} * {i} = {x*i}")
        
        if i==8:
            break
    
mult_table(int(input("Enter a Number : ")))
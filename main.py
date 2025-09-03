while True:
    system = input("temprature system? (c, f, k)");
    temprature = input("temprature?");
    try:
        temp = int(temprature)
        match system:
            case "c":
                print(f"{temp}c is {temp * 1.8 + 32}f is {temp - 273.15}k")
            case "f":
                c = (temp - 32)  *.5555
                print(f"{temp}f is {c}c is {c - 273.15}k")
            case "k":
                c = (temp + 273.15)
                print(f"{temp}k is {c}c is {c * 1.8 + 32}f")
            case _:
                print("invalid system")
    except:
        print("invalid temprature input") 
   

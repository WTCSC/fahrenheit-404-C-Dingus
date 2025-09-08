while True:
    i = input("input temp with type (f/c/k)>")
    if i == "exit" :
        break
    t = i.split("f")
    if len(t) == 1 :
        t = i.split("c")
        if len(t) == 1:
            t = i.split("k")
            try:
                c = int(t[0]) + 273.15
                print(f"{t[0]}k is {c}c is {c * 1.8 + 32}f")
            except:
                print("invalid syntax correct syntax ex(12f)")
        else:
            try:
                print(f"{t[0]}c is {(int(t[0]) * 1.8) + 32}f is {int(t[0])-273.15}k")
            except:
                print("invalid syntax correct syntax ex(12f)")
    else:
        try:
            c = (int(t[0])-32) * 0.55555
            print(f"{t[0]}f is {c}c is {c-273.15}k")
        except:
            print("invalid syntax correct syntax ex(12f)")

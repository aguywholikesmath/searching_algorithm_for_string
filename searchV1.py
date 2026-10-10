chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",","?","!"]
correctset = ["a"," ","a","n"]

for currentchar in chars:
    print(currentchar)
    if currentchar == correctset[0]:
        for currentchar1 in chars:
            print(f"{correctset[0]}{currentchar1}")
            if currentchar1 == correctset[1]:
                for currentchar2 in chars:
                    print(f"{correctset[0]}{correctset[1]}{currentchar2}")
                    if currentchar2 == correctset[2]:
                        for currentchar3 in chars:
                            print(f"{correctset[0]}{correctset[1]}{correctset[2]}{currentchar3}")
                            if currentchar3 == correctset[3]:
                                break
                        break
                break
        break
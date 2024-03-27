def islandscape(width, height):
    if width>height:
        return True
    else:
        return False
    
    
a = input("Enter the width: ")
b = input("Enter the height: ")
if islandscape(a,b):
    print("Landscape")
else:
    print("Portrait")
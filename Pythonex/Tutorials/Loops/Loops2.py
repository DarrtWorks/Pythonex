Colours = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]

for i in Colours: #Goes through the Colours array and adapts itself to the data type and data of the given position.
    print("The colours of the visible spectrum are:",i)
    if i == "Blue":
        print("Found Blue!!!!")
    for j in i:#Goes through each character of the given string!
            print("The letters of",i,"are as follows",j)
#Nested loop !!!!!!!
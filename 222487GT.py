import matplotlib.pyplot as plt
with open("globalterrorist.txt",'r') as fp:
    noOfTests = int(fp.readline().strip())
    
    #create two arrays to hold 
    #i) temporary array to hold each line of digits
    #ii) array that contains every line in the file
    arrayOfLine=[]
    arraysOfLines=[]

   #the below block of code appends all the lines into one array and each string value
   #of the digits becomes an integer
    
    for i in range(noOfTests):
        arrayOfLine=fp.readline().strip().split(",")
        #print(arrayOfLine)
        for j in range(len(arrayOfLine)):
            arrayOfLine[j]=int(arrayOfLine[j])
        arraysOfLines.append(arrayOfLine)
        
    #the array initialized below holds the sums of all the values in each array
    arrayOfSums=[]
    
    for k in range(noOfTests):
        arrayOfSums.append(sum(arraysOfLines[k]))
    
    similarityArray=[]
    
    #the below block of code slots in demo values in the array so they can be easily replaced
    for p in range(noOfTests):
        similarityArray.append(0)
    
    #we then use two loops to compare each array in the array of arrays and save the of similar arrays
    # to the 'similar' array
    for m in range(noOfTests):
        for n in range(m+1,noOfTests):
            if arraysOfLines[m]==arraysOfLines[n] and arrayOfSums[m]==arrayOfSums[n]:
                similarityArray[m]=n+1
                similarityArray[n]=m+1
            
    similarityArrayString=similarityArray           
    for q in range(len(similarityArray)):
        if similarityArrayString[q]==0:
            similarityArrayString[q]='no similar line'
            
    #print(similar)
    
    #we present our result below
    print("s/n    lines   sum     similarityID")
    print("-----------------------------------------")
    for r in range(noOfTests):
        print((r+1),"       ",arraysOfLines[r],"       ",arrayOfSums[r],"         ",similarityArrayString[r])
    
    
    #plotting the graph
    xaxis = [k +1 for k in range(noOfTests) ]
    yaxis = [similarityArray[i] for i in range(noOfTests)]
    fig, ax = plt.subplots()
    ax.plot(xaxis, yaxis)

    plt.plot(xaxis,yaxis)
    
    ax.set_xlabel("program indexOfSetOfNumbers")
    ax.set_ylabel("program similar")
    ax.set_label("plotting the similarity")

    ax.set_xlim(left=0, right = noOfTests+1)
    ax.set_ylim(bottom=0, top = noOfTests+1)
    
    plt.show()
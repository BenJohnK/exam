def printStud(**kwargs):
    id_found=0
    max_marks=0
    if 'id' in kwargs:
        details_list=[]
        idw=kwargs['id']
        f=open('student_list.txt','r')
        for lines in f:
            words=lines.rstrip("\n").split(" ")
            if int(words[3])>max_marks:
                max_marks=int(words[3])
            if int(words[0])==idw:
                id_found=1
                details_list.append(words[1]) 
                if 'property' in kwargs and kwargs['property']=='total':
                    details_list.append(words[3])
                if 'property' in kwargs and kwargs['property']=='course':
                    details_list.append(words[2])
        for x in details_list:
            print(x)
        if id_found==0:
            print("No student with that id")
        print("____Highest Score details_____")
        print("Highest mark is", max_marks)
        f.close()
        f=open('student_list.txt','r')
        for line in f:
            words=line.rstrip("\n").split(" ")
            if int(words[3])==max_marks:
                print("High scorer name:",words[1])
                print("High scorer course:",words[2])
    else:
        print("No student ID")

           
printStud(id=100,property='course')
#printStud(id=100,property='total') this also works...




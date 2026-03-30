def ug_course():
    print("U.G courses are\n1.Ai&ds\t\t2.Cse\n3.Ai&ml\t\t4.A.I\n5.Ece\t\t6.H&S\n7.Mech\t\t8.EEE\n9.BBA\t\t10.BCA\n")
    ans=input("Enter your Rollno: ")
    cgp=[]
    no_of_sem=int(input("Enter that how many sem results do you got(EX:2): "))
    for i in range(1,no_of_sem+1):
        sem_CGP=float(input(f"Enter you {i}sem CGP: "))
        cgp.append(sem_CGP)
    for j in range(len(cgp)-1):
        if cgp[j]<cgp[j+1] or cgp[j]==cgp[j+1]:
            result=0
        else:
            result=1 
    if result==0:
        result=cgp[len(cgp)-1]+0.25
        if result<=9.50:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get {result+0.25}")
        elif result>=9.50 and result<=10.0:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get {result+0.1}")
        elif result==10.25:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result-0.25}\nSuggestion:as your wel-wisher i feel you will keep on with this great CGP{result-0.25}\n")
        elif result>10.0:
            print("Please Enter a valid CGP\n")
    elif result==1:
        if result>=10.0:
            result=cgp[len(cgp)-1]-0.25
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get a better CGP then {result} in next sem so don't worry and be happy\n")
        else:
            print("Please Enter a valid CGP\n")
    else:
        print("Your result not found\n")
def pg_course():
    print("P.G courses are\n1.MBA\t\t2.MCA\n")
    ans=input("Enter your Rollno: ")
    cgp=[]
    no_of_sem=int(input("Enter that how many sem results do you got(EX:2): "))
    for i in range(1,no_of_sem+1):
        sem_CGP=float(input(f"Enter you {i}sem CGP: "))
        cgp.append(sem_CGP)
    for j in range(len(cgp)-1):
        if cgp[j]<cgp[j+1] or cgp[j]==cgp[j+1]:
            result=0
        else:
            result=1 
    if result==0:
        result=cgp[len(cgp)-1]+0.25
        if result<=9.50:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get {result+0.25}")
        elif result>=9.50 and result<=10.0:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get {result+0.1}")
        elif result==10.25:
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result-0.25}\nSuggestion:as your wel-wisher i feel you will keep on with this great CGP{result-0.25}\n")
        elif result>10.0:
            print("Please Enter a valid CGP\n")
    elif result==1:
        if result>=10.0:
            result=cgp[len(cgp)-1]-0.25
            print(f"Hi,{ans}\nAnalysis:According to your CGP history your next sem result is{result}\nSuggestion:as your wel-wisher i feel you will get a better CGP then {result} in next sem so don't worry and be happy\n")
        else:
            print("Please Enter a valid CGP\n")
    else:
        print("Your result not found\n")        
again=1
while again<again+1:
 def student_analysis():
     print("Welcome to Akhil's,\n*-*-*-*-*-*-*-*-*-*-*-*-*Svcn Student CGP analysis*-*-*-*-*-*-*-*-*-*-*-*-*")
     opt=int(input("1.Undergraduation(U.G)\n2.Postgraduation(P.G)\nSelect Your Course:\n"))
     match(opt):
         case 1:
             ug_course()
         case 2:
             pg_course()
         case _:
             print("please Enter correct Choice\n")
     print("Thank You! Please vist again\n")         
 student_analysis()                                 
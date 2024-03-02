percentage = int(input("enter percentage: "))
if(percentage > 0 and percentage<=100):
    if percentage>=80:
        print("Grade: A+")
    elif percentage>=75:
        print("Grade: A")
    elif percentage>=70:
        print("Grade: A-")
    elif percentage>=65:
        print("Grade: B+")
    elif percentage>=60:
        print("Grade: B")
    elif percentage>=55:
        print("Grade: B-")
    elif percentage>=50:
        print("Grade: C+")
    elif percentage>=45:
        print("Grade: C")
    elif percentage>=40:
        print("Grade: C-")
    else:
        print("Grade: Fail")
else:
    print("Invalid Percentage")
"""FourDirections"""
def main():
    """FourDirections"""
    text = str(input())
    a1 = ""
    a2 = ""
    a3 = ""
    a4 = ""
    a5 = ""
    for i in text:
        if i == "U":
            a1+="  *  "
            a2+=" *** "
            a3+="* * *"
            a4+="  *  "
            a5+="  *  "
        elif i =="D":
            a1+="  *  "
            a2+="  *  "
            a3+="* * *"
            a4+=" *** "
            a5+="  *  "
        elif i == "L":
            a1+="  *  "
            a2+=" *   "
            a3+="*****"
            a4+=" *   "
            a5+="  *  "
        elif i == "R":
            a1+="  *  "
            a2+="   * "
            a3+="*****"
            a4+="   * "
            a5+="  *  "
        a1+=" "
        a2+=" "
        a3+=" "
        a4+=" "
        a5+=" "
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
main()

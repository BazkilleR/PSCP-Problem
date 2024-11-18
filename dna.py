"""DNA"""
def main():
    """main"""
    txt1 = input()
    txt2= input()
    if len(txt2) > len(txt1):
        txt1, txt2 = txt2, txt1
    if txt1.replace("A" , "").replace("C" , "").replace("T" , "").replace("G" , "")\
    or txt2.replace("A" , "").replace("C" , "").replace("T" , "").replace("G" , ""):
        return "Error"
print(main())

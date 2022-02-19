with open("randomfile.txt", "a") as o:
    o.writelines('Hello\n')
    o.writelines('This text will be added to the file\n')
import sys,time,re,getpass
while True:
    password = getpass.getpass("Please enter password:")
    password2 = getpass.getpass("Please verify password")
    if password == password2:
        print("Login successed!")
        break
    else:
        print("Password is not the same!")
while True:
    a = input("user782\PythonLib> ")
    if a == "python":
        import traceback
        b = ""
        while True:
            a = input(">>>")
            if a == "/run":
                try:
                    exec(b)
                except Exception as e:
                    print(traceback.format_exc())
            if a == "/download":
                contin = True
                if contin:
                    if b == "":
                        print("The code is empty!")
                        contin = False
                    if contin:
                        e = input("Please enter filename: ")
                        with open(e,"w")as f:
                            f.write(b)
                        print("Download successfully!")
            if a == "/new":
                a = b = ""
            if a == "quit()":
                break
            else:
                b += a + "\n"
    if re.match("open%s(\S)*?" % " ",a):
        file = a[5:len(a)]
        print("Loading......")
        time.sleep(1)
        if a[len(a)-2:len(a)] != "-w":
            try:
                with open(file)as f:
                    a = f.read()
                    print(a)
            except FileNotFoundError:
                print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % file)
        else:
            file = a[5:len(a)-3]
            try:
                with open(file,"a")as f:
                    print("Please write text for the file(Enter \"/end\" to finish writing)")
                    while True:
                        a = input("")
                        if a == "/end":
                            break
                        else:
                            f.write(a + "\n")
                    print("Writing......")
                    time.sleep(1)
                    print("Complete!")
            except FileNotFoundError:
                print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % file)
    if a == "create file":
        ain = input("Please enter filename: ")
        with open(ain,"w")as f:
            print("Please write text for the file(Enter \"/end\" to finish writing)")
            while True:
                ainw = input("")
                if ainw == "/end":
                    break
                else:
                    f.write(ainw + "\n")
            print("Writing......")
            time.sleep(1)
            print("Complete!")
    if a == "create dir":
        dirn = input("Please enter folder's name:")
        import os
        os.mkdir(dirn)
        print(dirn + " created!")
    if re.match("rm%s(\S)*?" % " ",a):
        cont = True
        if a[len(a)-5:len(a)] == " -dir":
            filen = input("Please enter Folder's new name:")
            import os
            fileon = a[3:len(a)-5]
            try:
                os.rename(fileon,filen)
            except FileNotFoundError:
                print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % fileon)
                cont = False
            if cont:
                print("Rename complete!")
        else:
            filen = input("Please enter File's new name:")
            import os
            fileon = a[3:len(a)]
            try:
                os.rename(fileon,filen)
            except FileNotFoundError:
                print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % fileon)
                cont = False
            if cont:
                print("Rename complete!")
    if re.match("del%s(\S)*?" % " ",a):
        cont = True
        if a[len(a)-5:len(a)] == " -dir":
            lame = a[4:len(a)-5]
            y = input("Continue to delete " + lame + "?(y/n)")
            if y == "y":
                s = getpass.getpass("Please enter password:")
                if s == password:
                    try:
                        import shutil
                        shutil.rmtree(lame)
                        print(lame + " deleted!")
                    except FileNotFoundError:
                        print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % lame)
                    except NotADirectoryError:
                        print("Please remove ' -dir'")
                else:
                    print("Password not match!")
            else:
                print("Process stoped!")
        if a[len(a)-5:len(a)] != " -dir":
            lame = a[4:len(a)]
            y = input("Continue to delete " + lame + "?(y/n)")
            if y == "y":
                s = getpass.getpass("Please enter password:")
                if s == password:
                    try:
                        import os
                        os.remove(lame)
                        print(lame + " deleted!")
                    except FileNotFoundError:
                        print("FileNotFoundError: [Errno 2]No such file or directory: '%s'" % lame)
                    except IsADirectoryError:
                        print("Please add ' -dir' after folder name!")
                else:
                    print("Password not match!")
            else:
                print("Process stoped!")
    if re.match("get%s(\S)*?",a):
        import requests
        conti = True
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        try:
            data = requests.get(a[4:len(a)],headers = header)
        except Exception as e:
            print("Please check the url!")
            conti = False
        if conti:
            print(data)
    if a == "quit":
        break
    if a == "help":
        print("python : Go to the python editor")
        print("open filename : Open file")
        print("open filename -w : Append text in a file")
        print("create file : Create a new file")
        print("create dir : Create a folder")
        print("get url : Get HTML from url")
        print("rm filename : Rename a file")
        print("rm foldername -dir : Rename a folder")
        print("del filename : Remove a file")
        print("del foldername -dir : Remove a folder")
        print("help : Get help")
        print("quit : Quit")

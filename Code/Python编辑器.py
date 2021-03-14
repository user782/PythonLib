#encoding=utf-8
import traceback,time
b = ""
a = ""
while True:
    a = input(">>>")
    if a == "_run_":
        try:
            exec(b)
        except Exception as e:
            var = traceback.format_exc()
            print(var)
        finally:
            a = ""
    if a == "_new_":
        b = a = ""
    if a == "_download_":
        filename = input("请输入保存文件名：")
        file_ = input("请输入存储方式：1.纯文本(.txt)  2.Python File(.py)")
        if file_ == "1":
            file_ = ".txt"
        if file_ == "2":
            file_ = ".py"
        with open(filename + file_,"w",encoding = 'utf-8')as f:
            f.write(b)
        print("下载完毕！")
        a = ""
    b += a + "\n"

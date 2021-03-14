import sys,time
from random import *
class Pretty_print:
    def print_one_by_one(self,text):
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
    def print_line(self,text,flush=True):
        for i in text:
            print(i)
            if flush:
                time.sleep(0.05)
    def print_square(self,text,width,height,sleep=False):
        try:
            for i in range(height):
                sys.stdout.write(text * width + "\n")
                if sleep:
                    time.sleep(0.05)
        except TypeError:
            print("请检查数字是否错误！(仅支持int)")
    def print_triangle(self,text,height,width,sleep=False,flush=False,every_items=False):
        times = 1
        continue_ = True
        try:
            if width > 4:
                print("图形过宽")
                continue_ = ""
        except TypeError:
                print("请检查数字是否错误！(仅支持int)")
                continue_ = ""
        if continue_:
            try:
                if every_items:
                    for i in text:
                        i = " " * width + i
                        if flush:
                            for n in range(times):
                                sys.stdout.write(i)
                                time.sleep(0.05)
                            sys.stdout.write("\n")
                        else:
                            sys.stdout.write(i * times + "\n")
                        times += 1
                        if sleep:
                            time.sleep(0.05)
                else:
                    for i in range(height):
                        text = " " * width + text
                        if flush:
                            for n in range(times):
                                sys.stdout.write(text)
                                time.sleep(0.05)
                            sys.stdout.write("\n")
                        else:
                            sys.stdout.write(text * times + "\n")
                        times += 1
                        width -= 4
                        if sleep:
                            time.sleep(0.05)
            except TypeError:
                print("请检查数字是否错误！(仅支持int)")
    def magic_print(self,text,fg=True,bg=False,flush=True):
        for i in text:
            if flush:
                if fg and bg:
                    sys.stdout.write("\033[3{};4{}m".format(randint(2,6),randint(2,6)) + i)
                elif fg:
                    sys.stdout.write("\033[3{}m".format(randint(2,6)) + i)
                elif bg:
                    sys.stdout.write("\033[4{}m".format(randint(2,6)) + i)
                else:
                    sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.05)
            else:
                if fg and bg:
                    sys.stdout.write("\033[3{};4{}m".format(randint(2,6),randint(2,6)) + i)
                elif fg:
                    sys.stdout.write("\033[3{}m".format(randint(2,6)) + i)
                elif bg:
                    sys.stdout.write("\033[4{}m".format(randint(2,6)) + i)
                else:
                    sys.stdout.write(i)
        sys.stdout.write("\033[000m")
pprint = Pretty_print()
pprint.print_triangle("welcome",10,1,every_items=True)
pprint.magic_print("welcome")

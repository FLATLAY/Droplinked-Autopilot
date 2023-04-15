import datetime
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def get_colored_text(text, color):
    return color+text+bcolors().ENDC

def get_time_formated():
    tt = time.time()
    t = datetime.datetime.fromtimestamp(tt)
    return f"{t.year}-{t.month}-{t.day} {t.hour}:{t.minute}:{t.second}"

class Log:
    def error(msg):
        print(get_colored_text("[*] ", bcolors.BOLD)+get_colored_text(get_time_formated(), bcolors().OKCYAN) + " -> " + get_colored_text(msg, bcolors().FAIL))
    def warning(msg):
        print(get_colored_text("[*] ", bcolors.BOLD)+get_colored_text(get_time_formated(), bcolors().OKCYAN) + " -> " + get_colored_text(msg, bcolors().WARNING))
    def success(msg):
        print(get_colored_text("[*] ", bcolors.BOLD)+get_colored_text(get_time_formated(), bcolors().OKCYAN) + " -> " + get_colored_text(msg, bcolors().OKGREEN))
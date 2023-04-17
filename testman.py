import json
import sys

varss = {}
tests = []

class TestHandler:
    def __init__(self,test_file):
        self.tests_obj = json.loads(open(test_file).read())
        self.vars = self.tests_obj['vars']
        self.tests = self.tests_obj['tests']
        self.name = self.tests_obj['name']
        self.run_tests = self.tests_obj['run_tests']
        global varss
        varss = self.vars
        global tests
        tests = self.tests
    def add_test(self,test):
        self.tests.append(test)

test_handler = None

def save_test():
    global test_handler, varss, tests
    test_handler.tests_obj['vars'] = varss
    test_handler.tests_obj['tests'] = tests
    open("tests_p.json","w").write(json.dumps(test_handler.tests_obj,indent=4))


def add_action(test):
    action_name = input("Action name : ")
    action = {"action_name":action_name,"action_type":"", "value" : None}
    print("1. Click")
    print("2. Type")
    print("3. ChangeURL")
    inp = input(" > ")
    if (inp == "1"):
        action["action_type"] = "Click"
        var_name = input("name : ")
        varss[var_name] = input("XPATH : ")
        action["value"] = var_name
    elif (inp == "2"):
        action["action_type"] = "type"
        var_name = input("name : ")
        varss[var_name] = input("text : ")
        action["value"] = var_name
    elif (inp == "3"):
        action["action_type"] = "ChangeUrl"
        var_name = input("name : ")
        varss[var_name] = input("URL : ")
        action["value"] = var_name
    test["actions"].append(action)

def add_test():
    test_name = input("Test name : ")
    test = {"name":test_name,"actions":[]}
    while True:
        print("1. Add action")
        print("2. Save test")
        inp = input(" > ")
        if (inp == "1"):
            add_action(test)
        elif (inp == "2"):
            break
    test_handler.add_test(test)
    print("Test added")

def menu_handler():
    print("1. Add test")
    print("2. Save test")
    print("3. Exit")
    inp = input(" > ")
    while (inp != "3"):
        if (inp == "1"):
            add_test()
        elif (inp == "2"):
            save_test()
        print("1. Add test")
        print("2. Save test")
        print("3. Exit")
        inp = input(" > ")

def main():
    global test_handler
    if (len(sys.argv) == 1):
        print("Usage : python testman.py <test_file>")
        exit(0)
    test_file = sys.argv[1]
    test_handler = TestHandler(test_file)
    menu_handler()

if __name__ == '__main__':
    main()
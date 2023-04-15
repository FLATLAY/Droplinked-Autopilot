__author__ = 'k3rn3lpanic'
import selenium
from selenium import webdriver
import requests
import json
import logger
import actions
from actions import actions_map
import time
import sys
import os

__app_data_path__ = "\\".join(os.getenv('APPDATA').split("\\")[:-1])
print(__app_data_path__)
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={__app_data_path__}\\Local\\Google\\Chrome\\User Data")
    options.add_argument('--profile-directory=Profile 4') ## Change this to your profile number
    driver = webdriver.Chrome("chromedriver",options=options)
    return driver

def get_autopilot():
    return Autopilot(get_driver())

class Autopilot:
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(10)
    def run_tests(self,test_path):
        tests = json.loads(open(test_path).read())
        logger.Log.success("Loaded the test file!")
        tests_name = tests['name']
        run_tests = tests['run_tests']
        if (run_tests != 'all'):
            tests['tests'] = [test for test in tests['tests'] if test['test_name'] in run_tests]
        logger.Log.success(f"Testing name : {logger.get_colored_text(tests_name, logger.bcolors.UNDERLINE)}")
        logger.Log.success(f"Protocol : {logger.get_colored_text(tests['protocol'], logger.bcolors.UNDERLINE)}")
        logger.Log.error(f"Running {len(tests['tests'])} tests...")
        for i,test in enumerate(tests['tests']):
            logger.Log.warning(f"Running testcase{i+1} : {test['test_name']}")
            actions = test['actions']
            for action_index,action in enumerate(actions):
                action_type = action['action_type']
                amount = 1
                if ("amount" in action):
                    amount = action['amount']
                logger.Log.warning(f"...~=> Running Action{action_index+1} : {action['action_name']} * {amount}")
                for i in range(amount):
                    actions_map[action_type](self.driver,action['value'])
                    if ('timeout' in action):
                        if (action['timeout'] == -1):
                            input("Press enter to continue...")
                        else:
                            time.sleep(action['timeout'])
            logger.Log.error(f"Testcase{i+1} : {test['test_name']} finished!")

        inp = input("Press enter to exit...")
        self.driver.quit()


def main():
    tests_path = "tests.json"
    if(len(sys.argv) == 2):
        tests_path = sys.argv[1]
    autopilot = get_autopilot()
    autopilot.run_tests(tests_path)


if __name__ == '__main__':
    main()
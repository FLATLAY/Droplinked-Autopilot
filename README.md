# Droplinked-Autopilot
An automation browser level testing framework, to run tests on droplinked.com, using selenium in python. It uses a simple json file as tests 
template, and runs each test one by one, and logs the results. This tool can be used to generate new tests and run different test files.

### Prerequisites

* Python3
* ChromeDriver for your chrome version (https://chromedriver.chromium.org/downloads)
* Selenium (pip install selenium)

---

### Executing tests

```shell
python autopilot.py tests.json
```

### Tests

The test file, contains some fields which is : 
- vars : this part contains a map, of names to values for the tests
- name | protocol : name of the test sequence, protocol of it (todo)
- run_tests : a list of test names to run when the autopilot is started. for example you can write : ['test1' , 'test2']
- tests : each test has a test_name and an array of actions, and each action has : 
    - action_name : name of the action
    - action_type : It can be either `ChangeUrl`, `Click`, `type` and `CheckCart` right now, will be extended in future!
    - value : a variable name, which exists in `vars` section of the file
    - amount : number of times to do that action in a row
    - timeout : how many seconds to wait after the action is done, if timeout=-1, it waits for user input to resume

You can find a template of tests in `tests.json` file. Also you can use the `testman` tool (testman.py) to generate new tests. 

```shell
python testman.py tests.json
```

`testman` util, will help you create new tests, add actions to them, and save them in a new file.
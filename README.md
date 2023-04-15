# Droplinked-Autopilot
An automation browser level testing framework, to run tests on droplinked

### Prerequisites

* Python3
* ChromeDriver for your chrome version (https://chromedriver.chromium.org/downloads)
* Selenium (pip install selenium)

### Executing tests

```python
python autopilot.py tests.json
```

### Tests
You can view the tests.json file, it contains the tests and logic of testing droplinked, you can add more tests and logic to it.
It has a `name`, and a `run_tests` array, which contains the tests to run. `run_tests` could be set to 'all' to run all tests.

Tests could be found under the `tests` array, each test has a `name`, and some `actions` to perform.

Actions are the actions to perform on the browser, they have a `type`, and a `value`, the `type` is the action to perform, and the `value` is the value to perform the action on. Also some actions have a `timeout` value, which is the time to wait after performing the action.

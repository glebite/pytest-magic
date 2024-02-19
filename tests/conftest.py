import os.path
import json
import requests
import pytest


def rest_reporting(rep):
    """
    """
    data = {"file_name": rep.fspath,
            "test_name": rep.head_line,
            "outcome": rep.outcome
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post('http://localhost:6666/results', json=json.dumps(data), headers=headers)
    

@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
    """
    rep = yield

    if rep.when == "call":
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode, encoding="utf-8") as f:
            # let's also access a fixture for the fun of it
            if "tmp_path" in item.fixturenames:
                extra = " ({})".format(item.funcargs["tmp_path"])
            else:
                extra = ""
            rest_reporting(rep)
            f.write(str(rep._to_json()) + "\n")
            
    return rep

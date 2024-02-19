"""test_file.py - generic type tests for reporting
"""
import time
import random
import pytest


def test_fail():
    time.sleep(random.random() * 10)
    assert False


def test_pass():
    time.sleep(random.random() * 10)    
    assert True


def test_xfail():
    time.sleep(random.random() * 10)    
    pytest.xfail("Intentional")


def test_error():
    time.sleep(random.random() * 10)    
    assert 1/0


def test_skip():
    time.sleep(random.random() * 10)    
    pytest.skip("Skipping because...")

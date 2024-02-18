"""test_file.py - generic type tests for reporting
"""
import pytest


def test_fail():
    assert False


def test_pass():
    assert True


def test_xfail():
    pytest.xfail("Intentional")


def test_error():
    assert 1/0


def test_skip():
    pytest.skip("Skipping because...")

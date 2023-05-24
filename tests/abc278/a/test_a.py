"""hogehoge"""
import pytest

from task.abc278.a import main
from utility.mock_std import In, Out


def test_case1(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/abc278/a/input/input1.txt")
    stdout: object = Out("tests/abc278/a/output/output1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    res = main()
    print(res)
    assert stdout.outputs == stdout.validation


def test_case2(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/abc278/a/input/input2.txt")
    stdout: object = Out("tests/abc278/a/output/output2.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    res = main()
    print(res)
    assert stdout.outputs == stdout.validation


def test_case3(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("tests/abc278/a/input/input3.txt")
    stdout: object = Out("tests/abc278/a/output/output3.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    res = main()
    print(res)
    assert stdout.outputs == stdout.validation

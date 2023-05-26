"""hogehoge"""
import pytest

from abc278.task.b import main
from util.mock_std import In, Out


def test_case1(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("abc278/tests/b/input/input1.txt")
    stdout: object = Out("abc278/tests/b/output/output1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case2(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("abc278/tests/b/input/input2.txt")
    stdout: object = Out("abc278/tests/b/output/output2.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case3(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("abc278/tests/b/input/input3.txt")
    stdout: object = Out("abc278/tests/b/output/output3.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation

"""hogehoge"""
import pytest
from utility.mock_std import In, Out

from MobAtcoder_20230530.tasks.abc088b import main


def test_case1(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("MobAtcoder_20230530/tests/d/input/input1.txt")
    stdout: object = Out("MobAtcoder_20230530/tests/d/output/output1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case2(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("MobAtcoder_20230530/tests/d/input/input2.txt")
    stdout: object = Out("MobAtcoder_20230530/tests/d/output/output2.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case3(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("MobAtcoder_20230530/tests/d/input/input3.txt")
    stdout: object = Out("MobAtcoder_20230530/tests/d/output/output3.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation

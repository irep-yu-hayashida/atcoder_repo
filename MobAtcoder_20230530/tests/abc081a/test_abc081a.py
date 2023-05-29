"""hogehoge"""
import pytest
from utility.mock_std import In, Out

from MobAtcoder_20230530.tasks.abc081a import main


def test_case1(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("MobAtcoder_20230530/tests/abc081a/output/output2.txt")
    stdout: object = Out("MobAtcoder_20230530/tests/tests/abc081a/output/output1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation


def test_case2(monkeypatch: pytest.MonkeyPatch):
    stdin: object = In("MobAtcoder_20230530/tests/tests/abc081a/input/input2.txt")
    stdout: object = Out("MobAtcoder_20230530/tests/tests/abc081a/output/output2.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)
    main()
    assert stdout.outputs == stdout.validation

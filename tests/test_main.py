import pytest

from pynoback import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "Hello from pynoback!\n"

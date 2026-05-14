from pathlib import Path

import pytest

from md2print.cli import main


def test_cli_writes_default_output_file(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    exit_code = main([str(input_path)])

    assert exit_code == 0
    assert (tmp_path / "input.html").exists()


def test_cli_writes_compact_3ring_output_file(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    exit_code = main([str(input_path), "--preset", "compact-3ring"])

    assert exit_code == 0
    assert (tmp_path / "input_compact-3ring.html").exists()


def test_cli_rejects_missing_input() -> None:
    with pytest.raises(SystemExit) as exc_info:
        main([])

    assert exc_info.value.code == 2


def test_cli_returns_error_for_nonexistent_input(tmp_path: Path) -> None:
    exit_code = main([str(tmp_path / "missing.md")])

    assert exit_code == 1


def test_cli_rejects_all_as_invalid_preset(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        main([str(input_path), "--preset", "all"])

    assert exc_info.value.code == 2

from pathlib import Path

import pytest

from md2print.cli import build_parser, main


def test_cli_writes_default_output_file(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    exit_code = main([str(input_path)])

    assert exit_code == 0
    assert (tmp_path / "input.html").exists()


def test_cli_refuses_to_overwrite_default_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")
    output_path = tmp_path / "input.html"
    output_path.write_text("keep me", encoding="utf-8")

    exit_code = main([str(input_path)])

    assert exit_code == 1
    assert output_path.read_text(encoding="utf-8") == "keep me"
    assert "already exists" in capsys.readouterr().err


def test_cli_force_overwrites_default_output(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")
    output_path = tmp_path / "input.html"
    output_path.write_text("replace me", encoding="utf-8")

    exit_code = main([str(input_path), "--force"])

    assert exit_code == 0
    assert "replace me" not in output_path.read_text(encoding="utf-8")


def test_cli_writes_compact_3ring_output_file(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    exit_code = main([str(input_path), "--preset", "compact-3ring"])

    assert exit_code == 0
    assert (tmp_path / "input_compact-3ring.html").exists()


def test_cli_refuses_to_overwrite_explicit_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")
    output_path = tmp_path / "print.html"
    output_path.write_text("keep me", encoding="utf-8")

    exit_code = main([str(input_path), "--output", str(output_path)])

    assert exit_code == 1
    assert output_path.read_text(encoding="utf-8") == "keep me"
    assert "already exists" in capsys.readouterr().err


def test_cli_force_overwrites_explicit_output(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")
    output_path = tmp_path / "print.html"
    output_path.write_text("replace me", encoding="utf-8")

    exit_code = main([str(input_path), "--output", str(output_path), "--force"])

    assert exit_code == 0
    assert "replace me" not in output_path.read_text(encoding="utf-8")


def test_cli_rejects_missing_input() -> None:
    with pytest.raises(SystemExit) as exc_info:
        main([])

    assert exc_info.value.code == 2


def test_cli_help_shows_input_as_required() -> None:
    help_text = build_parser().format_help()

    assert "[-h]" in help_text
    assert " input" in help_text
    assert "[input]" not in help_text


def test_cli_list_presets_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(["--list-presets"])

    assert exit_code == 0
    out = capsys.readouterr().out
    assert "compact:" in out
    assert "compact-3ring:" in out


def test_cli_returns_error_for_nonexistent_input(tmp_path: Path) -> None:
    exit_code = main([str(tmp_path / "missing.md")])

    assert exit_code == 1


def test_cli_rejects_all_as_invalid_preset(tmp_path: Path) -> None:
    input_path = tmp_path / "input.md"
    input_path.write_text("# Hello\n", encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        main([str(input_path), "--preset", "all"])

    assert exc_info.value.code == 2

import pytest

from md2print.presets import PRESETS, get_preset


def test_launch_presets_exist() -> None:
    assert "compact" in PRESETS
    assert "compact-3ring" in PRESETS


def test_all_is_not_a_public_preset() -> None:
    assert "all" not in PRESETS


def test_compact_3ring_uses_wider_inside_margin() -> None:
    assert "--page-margin-inside: 0.9in;" in PRESETS["compact-3ring"].css_vars


def test_compact_3ring_does_not_mutate_compact_margin() -> None:
    assert "--page-margin-inside: 0.5in;" in PRESETS["compact"].css_vars


def test_get_preset_error_lists_valid_names() -> None:
    with pytest.raises(KeyError) as exc_info:
        get_preset("badname")

    message = str(exc_info.value)
    assert "Unknown preset 'badname'" in message
    assert "compact" in message
    assert "compact-3ring" in message

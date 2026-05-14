from md2print.presets import PRESETS


def test_launch_presets_exist() -> None:
    assert "compact" in PRESETS
    assert "compact-3ring" in PRESETS


def test_all_is_not_a_public_preset() -> None:
    assert "all" not in PRESETS


def test_compact_3ring_uses_wider_inside_margin() -> None:
    assert "--page-margin-inside: 0.9in;" in PRESETS["compact-3ring"].css_vars

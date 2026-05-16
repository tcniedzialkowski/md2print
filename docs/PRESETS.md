# Presets

Presets are coordinated print layouts, not loose style knobs.

## compact

`compact` is the default because density matters, but the first real print tests showed that dense output also needs footer-safe breathing room.

It uses compact body text, tight paragraph spacing, visible table borders, light code blocks that print well in black and white, and slightly larger vertical margins so browser headers and footers can be enabled for page numbers without crowding the document.

## compact-3ring

`compact-3ring` keeps the same density but changes the inside page margin to `0.9in`.

The CSS uses alternating `@page :left` and `@page :right` margins so duplex pages leave more room near the punched edge when placed in a 3-ring binder.

## Future Presets

Tighter variants such as `compact-tight` and `compact-3ring-tight` are intentionally deferred until more real print tests prove the need. Those variants would be for users who keep browser headers and footers disabled and want maximum page use.

# Presets

Presets are coordinated print layouts, not loose style knobs.

## compact

`compact` is the default because density is the product. It uses compact body text, tight paragraph spacing, visible table borders, and light code blocks that print well in black and white.

## compact-3ring

`compact-3ring` keeps the same density but changes the inside page margin to `0.9in`.

The CSS uses alternating `@page :left` and `@page :right` margins so duplex pages leave more room near the punched edge when placed in a 3-ring binder.

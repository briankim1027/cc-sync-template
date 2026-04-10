---
name: slack-gif-creator
description: Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like "make me a GIF for Slack of X doing Y".
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator - Flexible Toolkit

A toolkit for creating animated GIFs optimized for Slack. Provides validators for Slack's constraints, composable animation primitives, and optional helper utilities. **Apply these tools however needed to achieve the creative vision.**

## Slack's Requirements

| Property | Message GIFs | Emoji GIFs |
|----------|-------------|------------|
| Max size | ~2MB | 64KB (strict) |
| Dimensions | 480x480 | 128x128 |
| FPS | 15-20 | 10-12 |
| Colors | 128-256 | 32-48 |
| Duration | 2-5s | 1-2s |

**Emoji GIFs are challenging** - the 64KB limit is strict. Strategies: limit to 10-15 frames, use 32-48 colors, keep designs simple, avoid gradients, validate size frequently.

## Toolkit Structure

1. **Validators** - Check if a GIF meets Slack's requirements
2. **Animation Primitives** - Composable building blocks for motion
3. **Helper Utilities** - Optional functions for common needs

## Core Validators

```python
from core.gif_builder import GIFBuilder
from core.validators import check_slack_size, validate_dimensions, validate_gif, is_slack_ready

# After creating your GIF, validate it
passes, info = check_slack_size('emoji.gif', is_emoji=True)
passes, info = validate_dimensions(128, 128, is_emoji=True)
all_pass, results = validate_gif('emoji.gif', is_emoji=True)

# Quick check
if is_slack_ready('emoji.gif', is_emoji=True):
    print("Ready to upload!")
```

## Animation Primitives

Composable building blocks for motion. Apply to any object in any combination.

| Primitive | Module | Key Function | Key Parameters |
|-----------|--------|-------------|----------------|
| **Shake** | `templates.shake` | `create_shake_animation(object_type, object_data, num_frames, shake_intensity, direction)` | direction: `'both'`, `'horizontal'`, `'vertical'` |
| **Bounce** | `templates.bounce` | `create_bounce_animation(object_type, object_data, num_frames, bounce_height)` | bounce_height in pixels |
| **Spin** | `templates.spin` | `create_spin_animation(object_type, object_data, rotation_type, full_rotations)` | rotation_type: `'clockwise'`, `'wobble'`; also `create_loading_spinner(spinner_type)` |
| **Pulse** | `templates.pulse` | `create_pulse_animation(object_data, pulse_type, scale_range)` | pulse_type: `'smooth'`, `'heartbeat'`; also `create_attention_pulse(emoji)` |
| **Fade** | `templates.fade` | `create_fade_animation(fade_type)` | fade_type: `'in'`, `'out'`; also `create_crossfade(object1_data, object2_data)` |
| **Zoom** | `templates.zoom` | `create_zoom_animation(zoom_type, scale_range, add_motion_blur)` | zoom_type: `'in'`, `'out'`; also `create_explosion_zoom(emoji)` |
| **Explode** | `templates.explode` | `create_explode_animation(explode_type, num_pieces)` | explode_type: `'burst'`, `'shatter'`, `'dissolve'`; also `create_particle_burst(particle_count)` |
| **Wiggle** | `templates.wiggle` | `create_wiggle_animation(wiggle_type, intensity, cycles)` | wiggle_type: `'jello'`, `'wave'`; also `create_excited_wiggle(emoji)` |
| **Slide** | `templates.slide` | `create_slide_animation(direction, slide_type, overshoot)` | direction: `'left'`, `'right'`; slide_type: `'in'`, `'across'`; also `create_multi_slide(objects, stagger_delay)` |
| **Flip** | `templates.flip` | `create_flip_animation(object1_data, object2_data, flip_axis)` | flip_axis: `'horizontal'`, `'vertical'`; also `create_quick_flip(emoji1, emoji2)` |
| **Morph** | `templates.morph` | `create_morph_animation(object1_data, object2_data, morph_type)` | morph_type: `'crossfade'`, `'scale'`, `'spin_morph'` |
| **Move** | `templates.move` | `create_move_animation(object_type, object_data, start_pos, end_pos, motion_type, easing)` | motion_type: `'linear'`, `'arc'`, `'circle'`, `'wave'`; motion_params for arc_height, center, radius, etc. |
| **Kaleidoscope** | `templates.kaleidoscope` | `apply_kaleidoscope(frame, segments)` / `create_kaleidoscope_animation(base_frame, num_frames, segments, rotation_speed)` | Also `apply_simple_mirror(frame, mode)` with modes: `'horizontal'`, `'vertical'`, `'quad'`, `'radial'` |

**Composing primitives**: Combine freely in frame loops. Use `core.easing.interpolate(start, end, t, easing)` for smooth motion. See `references/composition-examples.md` for full examples.

## Helper Utilities

Optional helpers. **Use, modify, or replace with custom implementations as needed.**

### GIF Builder (Assembly & Optimization)

```python
from core.gif_builder import GIFBuilder

builder = GIFBuilder(width=480, height=480, fps=20)
for frame in my_frames:
    builder.add_frame(frame)
builder.save('output.gif', num_colors=128, optimize_for_emoji=False)
```

Key features: automatic color quantization, duplicate frame removal, size warnings, emoji mode.

### Text Rendering

```python
from core.typography import draw_text_with_outline, TYPOGRAPHY_SCALE

draw_text_with_outline(frame, "BONK!", position=(240, 100),
    font_size=TYPOGRAPHY_SCALE['h1'], text_color=(255, 68, 68),
    outline_color=(0, 0, 0), outline_width=4, centered=True)
```

### Color Management

```python
from core.color_palettes import get_palette

palette = get_palette('vibrant')  # or 'pastel', 'dark', 'neon', 'professional'
# palette has: background, primary, accent
```

### Visual Effects

```python
from core.visual_effects import ParticleSystem, create_impact_flash, create_shockwave_rings

particles = ParticleSystem()
particles.emit_sparkles(x=240, y=200, count=15)
particles.update()
particles.render(frame)

frame = create_impact_flash(frame, position=(240, 200), radius=100)
```

### Easing Functions

```python
from core.easing import interpolate

y = interpolate(start=0, end=400, t=progress, easing='ease_in')
# Available: linear, ease_in, ease_out, ease_in_out, bounce_out, elastic_out, back_out
```

### Frame Composition

```python
from core.frame_composer import (
    create_gradient_background, draw_emoji_enhanced,
    draw_circle_with_shadow, draw_star
)
```

## Optimization Strategies

**For Message GIFs (>2MB):** Reduce frames/FPS, reduce colors (128 -> 64), reduce dimensions (480 -> 320), enable duplicate frame removal.

**For Emoji GIFs (>64KB):** Limit to 10-12 frames, 32-40 colors max, avoid gradients, simplify design, use `optimize_for_emoji=True`.

## Philosophy

1. **Understand the creative vision** - What should happen? What's the mood?
2. **Design the animation** - Break into phases (anticipation, action, reaction)
3. **Apply primitives as needed** - Mix freely
4. **Validate constraints** - Check file size, especially for emoji GIFs
5. **Iterate if needed** - Reduce frames/colors if over limits

**The goal is creative freedom within Slack's technical constraints.**

## Dependencies

```bash
pip install pillow imageio numpy
```

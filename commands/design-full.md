# /design-full

Full design orchestration: Automatically generates required assets (logo, icons, hero images) using Gemini 3 Pro, then creates a complete UI screen with Stitch API. **One prompt to complete design!**

## Overview

This is the ultimate design command that combines:
1. **Asset Generation** (Gemini 3 Pro via Antigravity)
2. **UI Generation** (Google Stitch API)

Simply describe what you want, and the system automatically:
- Analyzes required assets
- Generates logo, hero image, icons
- Creates the complete UI screen
- Returns everything in one response

## Usage

```
/design-full "<full description of the page/screen>"
```

## Examples

### E-commerce Main Page
```
/design-full "친환경 유기농 식품 쇼핑몰 메인 페이지. 녹색 테마, 신선한 느낌, 모던한 디자인"
```

### SaaS Landing Page
```
/design-full "AI-powered project management tool landing page. Professional, blue gradient theme, with pricing section"
```

### Mobile App Onboarding
```
/design-full "Fitness tracking app welcome screen. Energetic, orange and black colors, motivational mood"
```

### Restaurant Website
```
/design-full "Japanese restaurant homepage. Minimal, elegant, dark theme with gold accents"
```

## Options

### Asset Hints
Control which assets to auto-generate:

```
/design-full "..." --logo --hero --icons
/design-full "..." --no-logo --hero
```

Default: Logo + Hero image (no icons)

### Design Preferences
Specify style and mood:

```
/design-full "..." --style modern --colors "blue gradient" --mood professional
```

### Device Type
Target device:

```
/design-full "..." --device MOBILE
/design-full "..." --device DESKTOP
/design-full "..." --device TABLET
```

Default: MOBILE

## Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Your Request                                 │
│  "/design-full 친환경 쇼핑몰 메인 페이지, 녹색 테마"             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              🎭 Orchestration Mode (Analysis)                   │
│  Auto-detect required assets:                                   │
│  ├── Logo: "Eco-friendly minimal logo"                          │
│  ├── Hero: "Fresh vegetables, nature background"                │
│  └── Colors: "Green gradient palette"                           │
└─────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Gemini 3 Pro │  │ Gemini 3 Pro │  │ Gemini 3 Pro │
    │ Logo Gen     │  │ Hero Gen     │  │ Icons Gen    │
    └──────────────┘  └──────────────┘  └──────────────┘
            │                 │                 │
            └─────────────────┼─────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Stitch API                                   │
│  Input: Enhanced prompt + Generated assets reference            │
│  Output: Complete UI + HTML/CSS                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Final Output                                 │
│  ├── Screen preview image                                       │
│  ├── Generated asset files (logo_*.png, hero_*.png)             │
│  ├── HTML/CSS code                                              │
│  └── Summary report                                             │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The command returns:

1. **Summary**
   - Number of assets generated
   - Asset types and file names
   - Any errors encountered

2. **Generated Assets**
   - Saved to current directory
   - File names with timestamps
   - Inline image previews

3. **UI Screen**
   - Stitch-generated screen result
   - Screen ID for further editing
   - Code download URL

## Authentication

Requires both:
1. **Stitch API** - gcloud authentication (existing)
2. **Antigravity** - Google OAuth for image generation

First use will prompt for Antigravity authentication via browser.

## Best Practices

1. **Be Descriptive**
   - Include theme, mood, colors in description
   - Mention target audience if relevant

2. **Iterate**
   - Use generated assets as starting point
   - Refine with `/design-system` for variations

3. **Reuse Assets**
   - Generated assets saved locally
   - Use with other screens for consistency

## Related Commands

- `/generate-asset` - Generate individual assets
- `/design` - Generate UI without auto-assets
- `/design-system` - Create variations with same style
- `/design-flow` - Generate multi-screen user flows

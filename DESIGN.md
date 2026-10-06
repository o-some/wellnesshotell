---
name: STILL — Nordic Light
description: Quiet hospitality editorial between silver-blue water and warm limestone.
colors:
  ink: "#24434b"
  muted: "#4f666c"
  paper: "#f6f5f0"
  water: "#dfe9e9"
  deep: "#173d47"
  line: "#b9c9c9"
  white: "#ffffff"
  action-hover: "#315c67"
  focus: "#a57439"
typography:
  display:
    fontFamily: "Still Serif, Georgia, serif"
    fontSize: "clamp(64px, 6.65vw, 96px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-.035em"
  headline:
    fontFamily: "Still Serif, Georgia, serif"
    fontSize: "clamp(42px, 4.2vw, 66px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-.035em"
  body:
    fontFamily: "Still Sans, Arial, sans-serif"
    fontSize: "15px"
    lineHeight: 1.75
  label:
    fontFamily: "Still Sans, Arial, sans-serif"
    fontSize: "10px"
    letterSpacing: ".15em"
rounded:
  field: "0px"
  circle: "50%"
spacing:
  section: "125px"
  section-mobile: "76px"
  form-gap: "24px"
components:
  button-primary:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.white}"
    padding: "16px 25px"
  button-primary-hover:
    backgroundColor: "{colors.action-hover}"
  button-light:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "16px 25px"
  button-light-hover:
    backgroundColor: "{colors.white}"
  field:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.field}"
    padding: "14px 0"
  interest:
    backgroundColor: "transparent"
    padding: "10px 15px"
  interest-selected:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.white}"
---

# Design System: STILL — Nordic Light

## Overview

**Creative North Star: "Nordic Light Spa"**

A quiet lakeside retreat between silver-blue water and warm limestone. Cormorant Garamond supplies editorial softness; Manrope keeps navigation and planning clear. The source direction is The Quiet Author Design 188, already selected for this project; its abstract typographic, color and material principles inform an independent STILL identity.

Full-bleed landscapes alternate with generous paper-like sections and asymmetrical interior photographs. Depth stays soft, typography stays left aligned, and the relationship between cool water and warm interiors carries the identity. This document refreshes the accepted direction against `public/index.html`, `public/styles.css`, and `public/app.js`; it does not propose a redesign.

**Key Characteristics:**
- Quiet serif headlines with occasional italic phrases.
- Broad photographic scenes and restrained blue-green controls.
- Native scrolling, slow atmospheric motion, and explicit motion controls.
- Clear concept labels beside planning actions.

## Colors

The palette is cool and mineral, balanced by warm paper and interior photography. Frontmatter values are the normative reusable primitives; the stylesheet also uses local section tints and image overlays.

### Primary
- **Deep water:** primary controls and the closing panel.
- **Water ink:** headings, body copy, and controls on pale surfaces.
- **Action hover:** the brighter blue-green response of primary buttons.

### Neutral
- **Warm paper:** the page, light buttons, floating introduction strip, and plan result.
- **Water:** an existing stylesheet primitive; section backgrounds currently use nearby local tints rather than this variable.
- **Muted slate:** secondary copy, captions, and helper notes.
- **Mineral line:** separators, tabs, and thin circular controls.
- **White:** text on dark imagery and filled primary actions.
- **Focus amber:** the visible keyboard outline, not a decorative luxury accent.

## Typography

Local font files register Cormorant Garamond as **Still Serif** and Manrope as **Still Sans**. Display italic has its own local font face. The frontmatter records base roles; individual editorial scenes have contextual sizes.

Hero and section headings use regular-weight serif, tight tracking, and balanced wrapping. Generic third-level headings are (34px); room titles reach (47px). Body paragraphs have a maximum width of (65ch), with shorter measures in split sections. Leads are (18px) with (1.7) line height. Small labels are uppercase and tracked; navigation and actions use the sans family, typically (12–13px).

At the narrow breakpoint, the hero scales between (52–76px), section headings become (43px), and supporting copy remains compact. Preserve complete German words and the intended line breaks.

## Layout

The main container has a maximum width of (1376px), with (64px) side gutters on desktop, (36px) below (1100px), and (20px) below (780px). Standard vertical section spacing is recorded in frontmatter; scene-specific spacing remains local.

Desktop layouts use deliberate unequal pairs: rooms (1.5fr / 1fr), dining (1.06fr / 1fr), and the planner (1fr / 1.12fr). Rituals form three columns. These become single columns at (780px). The introduction keeps an overlapping small image anchored to a taller image; the gallery remains horizontally scrollable with native scroll snapping on all sizes.

Additional adjustments exist at (390px) and from (1900px). The desktop hero is bounded between (720px) and (930px); the narrow hero uses (88svh) with (650–900px) bounds. Image crops use cover framing, with individual focal positions where needed.

The desktop dining photograph spans both the copy and breakfast rows, producing one continuous composition without an empty lower-left cell. Its minimum height is (650px), or (640px) at the intermediate breakpoint. Breakfast fills the right column with a (265px) image, reduced to (235px) at the intermediate breakpoint. On narrow screens the order is copy, main photograph, breakfast; the main image becomes (380px) tall and breakfast sits right aligned at (86%) width with a (230px) image.

Homepage strategy and its particular section sequence are recorded separately in `.impeccable/homepage.md`.

## Elevation & Depth

Most content is flat. Image gradients supply readable foreground contrast; restrained shadows distinguish the floating quick-planning strip, the overlapping introduction photograph, the scrolled header, and temporary feedback. Dining photographs now also receive soft ambient shadows; gallery imagery gains a shadow on hover. There is no repeated elevated card system.

The floating strip uses (0 20px 50px #233e4b14), the nested photograph (0 20px 35px #203e4614), the scrolled header (0 8px 30px #19353f0a), and the toast (0 10px 35px #162f4433). The dining main image uses (0 24px 65px #314b4917), breakfast (0 18px 40px #314b4912), and gallery hover (0 20px 40px #1838421a). The dining background is a local warm-mineral tint (#ecebe4). Hero and nature gradients are intentionally stronger than content surfaces because they carry white text.

Atmospheric motion combines a (24s) alternating hero drift, (35s) mist movement, a (22s) dining daylight gradient, and an (18s) pool reflection. Dining daylight slows to (28s) on narrow screens, where pool reflections are hidden. IntersectionObserver pauses ambient scenes outside the viewport; page visibility pauses CSS animation loops in hidden tabs.

Reveals take (1.2s) using the shared easing; ritual image hover takes (1.3s). Pool and nature parallax run only above (780px) through passive scrolling and requestAnimationFrame. Dining adds a separately clamped (-18px to 18px) depth shift on its slightly enlarged main image. Gallery hover lifts the image (-5px) with a (1.2s) transition on desktop. Reduced-motion CSS disables animations and transitions, removes image transforms, and hides button sheen. The visible pause control also stops pseudo-element motion and cancels an active room-image animation. Content starts visible before enhancement.

## Shapes

Images, planning fields, results, and interest choices use straight edges. Fine rules separate content without boxed card grids. Circular controls are reserved for gallery navigation and package arrows, with a small round concept marker. Icons are thin inline SVG strokes (1.2 units), usually (22px); they support directional actions rather than decorative feature tiles.

## Components

### Buttons and links

Primary actions are filled deep water, with white text, a (52px) minimum height, and a restrained (-2px) hover lift. Light actions reverse to paper and ink. Header actions begin transparent over the hero and become filled when the header fixes. Text actions use a thin underline rather than a filled container. Keyboard focus uses a (3px) amber outline with (5px) offset. A translucent diagonal sheen crosses filled buttons on hover or focus over (1.1s); overflow remains clipped to the action surface.

### Navigation

The header starts over the hero and becomes a fixed paper surface after (90px) of scrolling. Desktop links reveal a hairline underline on hover. At (780px), a two-line menu toggle opens a vertical paper navigation panel; Escape closes it and returns focus. No active-section indicator is implemented. A decorative (2px) reading-progress line tracks overall scroll position along the viewport top; it remains informational when motion is paused.

### Photographic articles and gallery

Ritual articles have unboxed copy beneath a cropped image, with restrained image enlargement on hover. The native horizontal gallery exposes circular previous/next controls, a five-item counter, keyboard arrows, and disabled end controls. Images have descriptive alternatives and captions; the source set contains 15 distinct images, combining eight generated images and seven licensed stock images.

### Room selection

Three text tabs share a bottom rule; the selected tab has a (2px) deep-water underline. Arrow keys, Home, and End move selection. The adjoining image, title, copy, features, and counter update together. The changed image animates from (0.35) opacity and (1.035) scale to its resting state over (700ms) with the shared easing through the Web Animations API. Switching again cancels the previous animation; pause and reduced-motion preferences suppress it. The selection action carries the room preference into the planner.

### Fields and interest choices

Date and select controls are transparent, bottom ruled, square, and at least (54px) tall. Paired fields use equal columns. Interest checkboxes appear as outlined rectangular labels and become deep-water fills when checked. Keyboard focus remains visible on the label. Date errors appear as compact warm-brown text and invalid fields receive `aria-invalid`.

### Planner result and feedback

The result is a paper panel with a blue-green top rule and generous padding. It presents a local travel draft with download and edit actions, accompanied by an explicit non-booking note. Feedback appears in a small bottom-centered dark toast. The planner does not request contact information or send a reservation.

### FAQ

Native details and summary rows are separated by thin rules. Plus and minus marks communicate expansion; copy remains on the page background without elevated containers.

## Do's and Don'ts

### Do:
- **Do** preserve the water-and-limestone palette and serif/sans relationship.
- **Do** give photography a clear narrative role and retain readable image shading.
- **Do** keep native scrolling, visible keyboard focus, and reduced-motion support.
- **Do** keep concept and travel-draft labels legible near selection and download actions.

### Don't:
- **Don't** replace the restrained editorial system with generic luxury gold or icon tile grids.
- **Don't** hide essential content behind motion or depend on parallax on narrow screens.
- **Don't** present generated scenes or licensed inspiration images as proof of a real hotel.
- **Don't** make the planner look like a confirmed reservation or real availability result.

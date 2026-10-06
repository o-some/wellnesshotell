# Independent narrow review — third cinematic scene

**Verdict: SHIP the concept preview.** No material correction is required within this bounded review.

Reviewed `desktop-scene.png`, `desktop-transition.png`, `mobile-scene.png`, `mobile-transition.png`, `report.json`, and the new section and associated rules in `public/index.html` and `public/cinematic.css`.

The fireside image adds a distinct indoor destination after the woodland and dusk pool, while retaining the same blue evening light, mountain/lake setting, warm natural materials and restrained typography. It reads as the requested third scene, not a replacement of the approved dusk pool. The sequence `natur → abend → geborgen` is confirmed by source and the runtime report.

The pool-to-lounge transition looks deliberate in both supplied viewport sizes. The 96px desktop and 48px mobile masks soften the seam without creating a light band, separating border or apparent empty section. The mobile crop retains the fireplace and tactile chair/blanket, so the new scene is still identifiable on a narrow screen. The bottom captions have visible separation from the persistent pause control. Main text and the CTA remain legible in the supplied scene captures.

The new CTA points to `#auszeit`, with the existing concept planner preserved. The supplied runtime report records a successful planner result, all images loaded, no runtime errors, no horizontal overflow at seven widths from 360px through 2560px, an active scene transform, and `none` under reduced motion and pause.

Evidence limits: this review inspected supplied local screenshots, source and runtime results; it did not independently drive a browser or verify production deployment. Paused screenshots establish composition and transition appearance, not real-device animation performance. No new contrast measurement or screen-reader audit was performed; screenshot legibility is not a full accessibility certification. Existing hotel-concept and no-booking limitations continue to apply.

## Targeted contrast reassessment — supersedes initial ship verdict

**Verdict: FIX the mobile fireside supporting-copy background before deployment.** On closer inspection of the reported area in `mobile-scene.png` (approximately x220–300, y460), the small white supporting text crosses a bright flame. The existing horizontal gradient becomes weaker in precisely that region. The earlier general visual-legibility judgment was insufficiently specific; it should not be taken as evidence that this text meets contrast requirements.

Minimal correction: give mobile `.fireside-shade` a uniform dark tint with a minimum alpha of 0.67, retaining the existing blue-green hue and warm visible fire. This targets the text/background conflict without changing the image crop or layout. Inspect the corrected mobile scene only; no wider polish pass is warranted. No UI edits were made by this reviewer.

## Mobile text-over-fire correction — verified

Inspected `mobile-scene-final.png` solely for the reported supporting-copy conflict. The strengthened blue-green shade now keeps the flame substantially darker behind both text lines. The text is clearly separated from the background, while the warm fire remains identifiable. **Finding resolved; final verdict: SHIP the concept preview.** This is a targeted visual confirmation, not a new WCAG contrast measurement; the evidence limits above still apply.

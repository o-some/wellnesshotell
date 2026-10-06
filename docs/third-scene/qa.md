# Third-scene QA

Verified natural consecutive DOM order: nature, dusk pool, fireside. No horizontal overflow at seven widths from360 to2560px. All19 image elements loaded (18 distinct motifs). New scene parallax transform observed active; reduced-motion and manual pause give no transform. New CTA reaches #auszeit and the local planner shows its result; no browser errors.

Desktop/mobile scene and overlap screenshots checked. Narrow-device image focal point88% keeps the fire in frame, footer115px above bottom leaves space for the fixed motion switch. Root smooth scrolling is now disabled under manual pause as well as OS reduced motion. The test waits for anchor navigation before clicking the planner.

One detector run used regex fallback due missing optional parsers; findings are advisory and not a full accessibility certification. Existing source identity/controls retained; no runtime dependency added.

Targeted review requested stronger mobile contrast over the fireplace. Mobile-only shade now has minimum alpha 0.67; mobile-scene-final.png was reviewed and the finding resolved.

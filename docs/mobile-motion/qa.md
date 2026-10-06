# Mobile motion verification

Verified at 360, 390, 430, 768, and 1024 CSS px: no horizontal overflow. All 19 image elements loaded. Pool, forest, dusk, and fireside media retain their 30% overscan. Browser samples at two scroll positions show visible nature/dusk/fireside image movement (about 25–29px between samples) with full image coverage. Dawn crop and depth change with scroll. The local preview reported no browser errors.

The manual control and `prefers-reduced-motion` make parallax and the mobile aperture static. A targeted browser pass confirmed the 16-second light pulse runs only for visible dusk and fireside scenes and is disabled by pause/reduced motion. A selector priority issue initially paused dusk despite its being visible; this was fixed and the targeted pass repeated successfully. Final screenshots were captured after the images loaded.

No mobile frame content depends on motion; copy and controls remain present in the resting state. `report.json` and `ambient.json` contain the measured browser results.

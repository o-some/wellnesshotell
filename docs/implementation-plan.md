# Inventory and implementation plan
Inventory completed before implementation: repository contains README only; main is canonical; GitHub Pages configured for workflow deployment; no custom domain. No customer assets or brand exist. CAF 1.21.1, bootstrap 1.8.0; current premium-web integration loaded.

Source: kernel-resolved Design 188 Nordic Light Spa, asset SHA-256 075d7dfd0436e45ec17e90feb394596b9708d37ebddbeaa7ab2aabcb9764ca4f, visually inspected. Transfer pale lake blue, warm natural materials, refined serif, quiet photographic rhythm. Do not copy template art or text.

Direction delegated by user: STILL, a quiet lakeside hotel concept. Build in static HTML/CSS/JS. Full-bleed hero with mist and water, floating trip planner, asymmetric introduction, immersive pool, ritual choices, room comparison, culinary story, nature escape, image journal, useful FAQ and final conversion. Avoid decorative card grids, invented prices, testimonials and availability.

Motion budget: 4 families: slow hero drift; scroll parallax on 3 media scenes; locally staggered reveal; hover/selection feedback. Native scroll, reduced-motion final state, pause control, no pointer hijacking. Shadows and gradient shading serve depth and contrast.

Images: 7 generated concept photographs + 8 licensed Unsplash illustrative photos, local WebP and responsive derivatives. Image-generation skill used through native tool, no paid external API. Image content remains illustrative.

Validation: mobile widths 360/375/390/393/430, desktop 1280/1440/1920 and 2560; keyboard, nav, planner validation, download, gallery controls, reduced motion, images, no overflow; independent visual review using screenshots; deployed revision/asset readback.

Publish only public directory via GitHub Actions. Preserve factory and library read-only. Rollback via Git revert.

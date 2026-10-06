# Mobile motion update

The phone presentation was too static because the existing parallax and breathing chapter were disabled below 781px. Focal motion: let the nature, water, and fireside photographs travel slowly behind the fixed editorial copy while scrolling. Give the dawn photograph a small scroll-linked crop opening and depth movement. Keep ritual photographs static because their mobile frames have no image overscan.

Continuity: use the existing native scroll/requestAnimationFrame clock and existing scene sequence. Feedback: keep room tabs, planner and the persistent pause control as before. Budget: image travel is 35% of desktop strength; update only visible scenes, and use existing 30% image overscan. A bounded 2.2% mobile image inset and 32px travel cover the dawn scene. Paused and prefers-reduced-motion use static imagery.

Verify at phone widths, ensure actual transform changes during scroll, no clipped image edges or text, pause/reduced motion, no horizontal overflow, and working planner. Publish only through the existing GitHub Pages workflow.

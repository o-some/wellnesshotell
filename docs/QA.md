# Abnahmeumfang

## Tatsächlich geprüft

- 15 verschiedene Bilddateien, 7 generiert / 8 Unsplash, lokal vorhanden; alle im Seitenverlauf bzw. der Galerie sichtbar. Bildquellen und SHA-256 dokumentiert.
- Chrome mit agent-browser, 360/375/390/393/430/768/1280/1440/1920/2560 CSS-Pixel. Kein horizontaler Dokumentüberlauf. Desktop-Emulation, kein echtes iOS-Gerät.
- Zimmerwahl per Maus und Pfeiltasten, Übernahme in Planer, ungültige Datumsfolge, korrekter Reiseentwurf und realer Download der Textdatei.
- Datumswerte im automatischen Fehlerfall per DOM gesetzt, weil das CLI-Fill den lokalisierten nativen Datumseingang leerte. Submit und Download per tatsächlicher Browseraktion.
- Mobiles Menü öffnen/schließen/Escape, Galerie vor/zurück und vertikales Scrollen.
- Reduced Motion: CSS-Animation `none`; manuelle Bewegungspause vorhanden.
- Keine Browserfehler oder Konsolenmeldungen in der geprüften Interaktion.
- axe 4.12.1: 0 bestätigte Verstöße. Bild-/Overlay-Kontrast bleibt teilweise maschinell unbestimmbar; keine vollständige WCAG-Zertifizierung.
- Lokale Performance-Stichprobe: CLS 0, LCP 120 ms, FCP 120 ms. Lokale, ungedrosselte Messung, keine Aussage über reale Besucherdaten oder mobile Netzqualität.
- Unabhängige Sichtprüfung: mobile Wortabstände, Bildbeschreibung, redundante Labels und Pfeil-Iconsystem korrigiert; Nachprüfung separat gespeichert.

## Grenzen

Kein reales Buchungsbackend, kein E-Mail-Versand, keine Zahlung, keine Verfügbarkeit. Kein realer Hotelbetrieb. Keine realen iOS-/Android-Hardwaretests. Keine rechtliche Zertifizierung. Factory-Plan und Enrollment sind keine automatische Premium-Gesamtfreigabe. Die öffentliche Veröffentlichung ist vom Nutzer ausdrücklich als Hotelkonzept beauftragt.

## Bild-/Quellenhinweis

Die ersten Bildquellenlisten enthalten auch zwei später ersetzte Stockmotive; maßgeblich für die endgültige Auslieferung ist `image-manifest.json` (15 finale Motive) sowie die öffentliche Seite `bildnachweise.html`.

# STILL · Wellnesshotel

Hochwertiges, responsives Wellnesshotel-Konzept auf Basis der Chelonaki App Factory.

**Website:** https://o-some.github.io/wellnesshotell/

## Lokal ansehen

```sh
python3 -m http.server 4173 --directory public
```

GitHub ist die alleinige Codequelle und GitHub Pages der einzige Veröffentlichungsweg. `.github/workflows/pages.yml` veröffentlicht bei Push auf `main` ausschließlich `public/`. Keine Sites-Aktionen.

## Gestaltung und Umfang

Designreferenz: The Quiet Author, **188 – Nordic Light Spa**. Eigenständige Umsetzung als STILL, mit Cormorant Garamond, Manrope, Wasserblau, warmem Weiß und Naturmaterialien.

- 18 unterschiedliche hochwertige Bildmotive: 11 eigens erzeugte Konzeptbilder, 7 Unsplash-Inspirationen; alle lokal, mit WebP-Ableitungen und Herkunftsnachweis.
- Cineastische Morgen- und Abendszenen, große Spa-Bildstrecken, ruhige Hero-Bewegung, Desktop-Parallax, scrollgesteuerte Bildöffnung und dezente Hoverzustände; Bewegungspause und Reduced-Motion-Unterstützung.
- Drei Zimmeransichten mit Tastaturbedienung, Reiseideen, horizontale Galerie, FAQ und Reiseplaner mit Datumskontrolle und lokalem Textdownload.
- Responsiv geprüft von 360 bis 2560 CSS-Pixeln. Statische Auslieferung ohne Runtime-Abhängigkeiten oder Analytics.

## Ehrlicher Konzeptumfang

STILL ist **kein bestehender Hotelbetrieb**. Der Planer prüft keine Verfügbarkeit, sendet keine Anfrage und bestätigt keine Buchung. Es gibt keine erfundenen Bewertungen, Preise oder Standortangaben. Das Konzept ist `noindex`. Ein realer Hotelbetrieb benötigt echte Betreiber-/Datenschutzangaben, Angebote, eigene Hotelbilder und eine Buchungsintegration.

## Factory und Nachweise

Die Factory wurde tatsächlich geladen und genutzt: CAF 1.21.1, kanonischer Workspace-Adapter mit `WORKSPACE_READY`, Designresolver mit Bildhash, Premium-Plancompiler und Owner-54-Vertrag mit `CONTRACT_ENROLLED`. Umsetzung und Bildproduktion erfolgten mit nativen Codex-Werkzeugen. Eine vollständige maschinelle CAF-Aggregat-/Release-Zertifizierung wird nicht behauptet.

- `PRODUCT.md`, `DESIGN.md`, `docs/implementation-plan.md`
- `.masterbrain/`: Plan, Vertrag, Enrollment und Owner-Artefakte
- `docs/image-manifest.json`: Bildquellen, Dimensionen, Hashes
- `docs/qa/`: Browser-, Accessibility-, Performance- und Bildnachweise
- `docs/QA.md`: geprüfter Umfang und Grenzen

Originale generierter Bilder und Logoexporte liegen zusätzlich im übergeordneten CAF-Kundenordner. Skripte sind Arbeits-/Nachweisskripte; `prepare_factory.py` ist kein Reset-Befehl. Browser-QA-Skripte nutzen den vorhandenen lokalen agent-browser-Pfad und benötigen bei anderen Rechnern eine Pfadanpassung.

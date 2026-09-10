# FIT College — motion background

A 10 second, 1920x1080 animated gradient background built in Remotion. The mesh
is drawn in code from the palette in `src/palette.ts`, so it can be re-cut at any
size, length or aspect ratio without re-exporting artwork.

Palette and grain are taken from the source poster, re-oriented for a 90 degree
clockwise rotation: cool blues along the top-left, a near-black spine on the
diagonal, warm reds and ambers along the bottom-right.

## Run it

```bash
npm install
npm run studio          # live preview, scrub and edit props
npm run render -- src/index.ts FitCollegeBackground out/background.mp4
```

Headless machines need an explicit browser and the sandbox off:

```bash
npx remotion render src/index.ts FitCollegeBackground out/background.mp4 \
  --browser-executable=/path/to/chrome-headless-shell \
  --disable-headless-sandbox --crf=19
```

## Changing things

| What | Where |
| --- | --- |
| Title lines, corner labels, index number | `defaultProps` in `src/Root.tsx` |
| Colours and blob positions | `src/palette.ts` |
| Drift speed, blur, saturation | `src/Gradient.tsx` |
| Grain strength | `opacity` prop in `src/Grain.tsx` |
| Length / size / frame rate | `<Composition>` in `src/Root.tsx` |

Every blob drifts on a whole number of cycles across the 10 second span, so the
gradient loops seamlessly. The title reveal does not, by design.

Outfit is bundled in `public/fonts`, so renders never touch the network.

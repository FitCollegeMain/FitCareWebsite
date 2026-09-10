import {continueRender, delayRender, staticFile} from 'remotion';

// Outfit is bundled locally (public/fonts) so renders never touch the network.
export const FONT_FAMILY = 'Outfit';

let started = false;

export const ensureFont = () => {
  if (started) return;
  started = true;
  const handle = delayRender('Loading Outfit');
  const style = document.createElement('style');
  style.textContent = `
    @font-face {
      font-family: 'Outfit';
      font-style: normal;
      font-weight: 100 900;
      font-display: block;
      src: url('${staticFile('fonts/outfit-latin.woff2')}') format('woff2');
    }
    @font-face {
      font-family: 'Outfit';
      font-style: normal;
      font-weight: 100 900;
      font-display: block;
      src: url('${staticFile('fonts/outfit-latin-ext.woff2')}') format('woff2');
      unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB;
    }
  `;
  document.head.appendChild(style);
  document.fonts.ready.then(() => continueRender(handle));
};

import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';

const NOISE =
  "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='4' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='260' height='260' filter='url(%23n)'/></svg>";

// Cheap, convincing film grain: one tiled noise plate jittered a few pixels
// per frame so the texture crawls the way real grain does.
const jitter = (frame: number, salt: number) => {
  const n = Math.sin((frame + 1) * (12.9898 + salt) + salt * 78.233) * 43758.5453;
  return Math.floor((n - Math.floor(n)) * 260);
};

export const Grain: React.FC<{opacity?: number}> = ({opacity = 0.42}) => {
  const frame = useCurrentFrame();

  return (
    <>
      <AbsoluteFill
        style={{
          backgroundImage: `url("${NOISE}")`,
          backgroundRepeat: 'repeat',
          backgroundPosition: `${jitter(frame, 1)}px ${jitter(frame, 2)}px`,
          opacity,
          mixBlendMode: 'overlay',
          pointerEvents: 'none',
        }}
      />
      <AbsoluteFill
        style={{
          backgroundImage: `url("${NOISE}")`,
          backgroundRepeat: 'repeat',
          backgroundSize: '390px 390px',
          backgroundPosition: `${jitter(frame, 3)}px ${jitter(frame, 4)}px`,
          opacity: opacity * 0.55,
          mixBlendMode: 'soft-light',
          pointerEvents: 'none',
        }}
      />
      <AbsoluteFill
        style={{
          backgroundImage: `url("${NOISE}")`,
          backgroundRepeat: 'repeat',
          backgroundSize: '320px 320px',
          backgroundPosition: `${jitter(frame, 5)}px ${jitter(frame, 6)}px`,
          opacity: opacity * 0.30,
          mixBlendMode: 'screen',
          pointerEvents: 'none',
        }}
      />
    </>
  );
};

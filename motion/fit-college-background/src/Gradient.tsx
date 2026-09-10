import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {BASE, DARK_BLOBS, LIGHT_BLOBS, type Blob} from './palette';

const TAU = Math.PI * 2;

const BlobLayer: React.FC<{
  blob: Blob;
  progress: number;
  width: number;
  blend: 'screen' | 'multiply';
}> = ({blob, progress, width, blend}) => {
  const t = progress * TAU * blob.cycles + blob.phase;
  const cx = blob.x + Math.sin(t) * blob.ampX;
  const cy = blob.y + Math.cos(t * 1) * blob.ampY;
  // Each blob also breathes a little so the mesh never feels rigid.
  const scale = 1 + Math.sin(t * 1 + 1.3) * 0.07;
  const d = blob.size * width * scale;

  return (
    <div
      style={{
        position: 'absolute',
        left: cx * width - d / 2,
        top: cy * (width * 9) / 16 - d / 2,
        width: d,
        height: d,
        borderRadius: '50%',
        background: `radial-gradient(circle at 50% 50%, ${blob.color} 0%, ${blob.color} 34%, transparent 74%)`,
        opacity: blob.alpha,
        mixBlendMode: blend,
      }}
    />
  );
};

export const Gradient: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames, width} = useVideoConfig();
  const progress = frame / durationInFrames; // 0 -> 1, loops seamlessly

  // Very slow push-in on the whole mesh, returning to where it started.
  const breathe = 1.06 + Math.sin(progress * TAU) * 0.03;

  return (
    <AbsoluteFill style={{backgroundColor: BASE, overflow: 'hidden'}}>
      <AbsoluteFill
        style={{
          transform: `scale(${breathe})`,
          filter: 'blur(58px) saturate(1.22) contrast(1.04)',
          backgroundColor: BASE,
        }}
      >
        {LIGHT_BLOBS.map((b, i) => (
          <BlobLayer key={`l${i}`} blob={b} progress={progress} width={width} blend="screen" />
        ))}
        {DARK_BLOBS.map((b, i) => (
          <BlobLayer key={`d${i}`} blob={b} progress={progress} width={width} blend="multiply" />
        ))}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

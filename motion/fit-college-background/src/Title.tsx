import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {ensureFont, FONT_FAMILY as fontFamily} from './font';

ensureFont();

export type TitleProps = {
  lines: string[];
  labelTopLeft?: string;
  labelTopRight?: string;
  labelBottom?: string;
  index?: string;
};

const ease = (t: number) => 1 - Math.pow(1 - t, 3);

const Arrow: React.FC = () => (
  <svg width="22" height="22" viewBox="0 0 22 22" fill="none" style={{flexShrink: 0, marginTop: 2}}>
    <path d="M5 17 L17 5 M8 5 H17 V14" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const CornerLabel: React.FC<{text?: string; align: 'left' | 'right'; delay: number}> = ({
  text,
  align,
  delay,
}) => {
  const frame = useCurrentFrame();
  if (!text) return null;
  const t = ease(interpolate(frame, [delay, delay + 26], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}));
  return (
    <div
      style={{
        display: 'flex',
        gap: 12,
        alignItems: 'flex-start',
        opacity: t,
        transform: `translateY(${(1 - t) * 14}px)`,
        maxWidth: 340,
      }}
    >
      <Arrow />
      <div
        style={{
          fontFamily,
          fontWeight: 400,
          fontSize: 25,
          lineHeight: 1.32,
          color: 'rgba(255,255,255,0.94)',
          textAlign: align,
          letterSpacing: '-0.005em',
          whiteSpace: 'pre-line',
        }}
      >
        {text}
      </div>
    </div>
  );
};

export const Title: React.FC<TitleProps> = ({
  lines,
  labelTopLeft,
  labelTopRight,
  labelBottom,
  index = '01',
}) => {
  const frame = useCurrentFrame();
  const {durationInFrames, width} = useVideoConfig();

  // The whole block creeps upward for the full ten seconds so nothing ever
  // sits perfectly still.
  const drift = interpolate(frame, [0, durationInFrames], [10, -12]);

  const ruleIn = ease(
    interpolate(frame, [52, 96], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})
  );

  return (
    <AbsoluteFill
      style={{
        padding: '58px 72px',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
      }}
    >
      <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
        <CornerLabel text={labelTopLeft} align="left" delay={4} />
        <CornerLabel text={labelTopRight} align="left" delay={12} />
      </div>

      <div style={{transform: `translateY(${drift}px)`, paddingLeft: 4}}>
        {lines.map((line, i) => {
          const start = 10 + i * 11;
          const t = ease(
            interpolate(frame, [start, start + 40], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            })
          );
          return (
            <div key={i}>
              <div
                style={{
                  fontFamily,
                  fontWeight: 300,
                  fontSize: width * 0.072,
                  lineHeight: 1.08,
                  letterSpacing: '-0.024em',
                  color: '#fff',
                  opacity: t,
                  transform: `translateY(${(1 - t) * 74}px)`,
                  filter: `blur(${(1 - t) * 9}px)`,
                  whiteSpace: 'nowrap',
                }}
              >
                {line}
              </div>
            </div>
          );
        })}
      </div>

      <div style={{display: 'flex', alignItems: 'center', gap: 34, opacity: ruleIn}}>
        <div
          style={{
            fontFamily,
            fontWeight: 300,
            fontSize: 30,
            color: 'rgba(255,255,255,0.92)',
            letterSpacing: '0.02em',
          }}
        >
          {index}
        </div>
        <svg width={230} height="12" viewBox="0 0 230 12" fill="none">
          <path
            d={`M0 6 H${196 * ruleIn} M${(196 * ruleIn) - 12} 1 L${196 * ruleIn} 6 L${(196 * ruleIn) - 12} 11`}
            stroke="white"
            strokeWidth="1.4"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
        {labelBottom ? (
          <div
            style={{
              fontFamily,
              fontWeight: 400,
              fontSize: 25,
              lineHeight: 1.32,
              color: 'rgba(255,255,255,0.94)',
              whiteSpace: 'pre-line',
              marginLeft: 6,
            }}
          >
            {labelBottom}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

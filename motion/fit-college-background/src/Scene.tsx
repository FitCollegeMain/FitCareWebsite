import React from 'react';
import {AbsoluteFill} from 'remotion';
import {Gradient} from './Gradient';
import {Grain} from './Grain';
import {Title, type TitleProps} from './Title';

export const Scene: React.FC<TitleProps> = (props) => (
  <AbsoluteFill style={{backgroundColor: '#04060d'}}>
    <Gradient />
    <Grain />
    {/* Keeps the type readable wherever the mesh drifts underneath it. */}
    <AbsoluteFill
      style={{
        background:
          'radial-gradient(120% 90% at 30% 55%, rgba(0,0,0,0.20) 0%, rgba(0,0,0,0) 62%)',
      }}
    />
    <Title {...props} />
  </AbsoluteFill>
);

import React from 'react';
import {Composition} from 'remotion';
import {Scene} from './Scene';

export const RemotionRoot: React.FC = () => (
  <Composition
    id="FitCollegeBackground"
    component={Scene}
    durationInFrames={300}
    fps={30}
    width={1920}
    height={1080}
    defaultProps={{
      lines: ['Why should you', 'study at', 'FIT College?'],
      labelTopLeft: '',
      labelTopRight: '',
      labelBottom: '',
      index: '01',
    }}
  />
);

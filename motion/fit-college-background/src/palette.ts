// Palette lifted from the source poster, re-oriented for a 90deg clockwise
// rotation: cool blues run along the top-left, warm reds and ambers pool along
// the bottom-right, and a near-black spine cuts diagonally between them.
export type Blob = {
  color: string;
  x: number; // 0-1 across the frame
  y: number; // 0-1 down the frame
  size: number; // diameter as a fraction of frame width
  alpha: number;
  cycles: number; // full drift cycles across the 10s loop (integer = seamless)
  ampX: number;
  ampY: number;
  phase: number;
};

export const BASE = '#04060f';

// Luminous colour, blended with `screen` over the dark base.
export const LIGHT_BLOBS: Blob[] = [
  // Cool half
  {color: '#D6F2FF', x: 0.27, y: 0.01, size: 0.26, alpha: 1.00, cycles: 1, ampX: 0.030, ampY: 0.020, phase: 0.0},
  {color: '#38ACF5', x: 0.33, y: 0.11, size: 0.54, alpha: 1.00, cycles: 1, ampX: 0.038, ampY: 0.028, phase: 0.9},
  {color: '#0F79E8', x: 0.16, y: 0.05, size: 0.46, alpha: 0.95, cycles: 1, ampX: 0.032, ampY: 0.030, phase: 2.4},
  {color: '#1152DE', x: 0.52, y: 0.03, size: 0.58, alpha: 1.00, cycles: 1, ampX: 0.036, ampY: 0.026, phase: 1.7},
  {color: '#0A2FA6', x: 0.70, y: 0.06, size: 0.52, alpha: 0.90, cycles: 2, ampX: 0.022, ampY: 0.018, phase: 3.4},
  {color: '#07205F', x: 0.87, y: 0.13, size: 0.46, alpha: 0.70, cycles: 2, ampX: 0.020, ampY: 0.016, phase: 4.9},
  {color: '#0B49B4', x: 0.05, y: 0.22, size: 0.40, alpha: 0.70, cycles: 1, ampX: 0.028, ampY: 0.032, phase: 5.6},

  // Warm half
  {color: '#FFE6B4', x: 0.49, y: 1.00, size: 0.21, alpha: 1.00, cycles: 1, ampX: 0.026, ampY: 0.018, phase: 1.4},
  {color: '#FFA210', x: 0.53, y: 0.97, size: 0.40, alpha: 1.00, cycles: 1, ampX: 0.034, ampY: 0.024, phase: 2.2},
  {color: '#F8600E', x: 0.62, y: 0.99, size: 0.46, alpha: 1.00, cycles: 1, ampX: 0.036, ampY: 0.028, phase: 0.4},
  {color: '#EE3411', x: 0.71, y: 0.96, size: 0.50, alpha: 1.00, cycles: 1, ampX: 0.032, ampY: 0.026, phase: 5.1},
  {color: '#D2170B', x: 0.85, y: 0.90, size: 0.52, alpha: 1.00, cycles: 1, ampX: 0.030, ampY: 0.030, phase: 3.0},
  {color: '#B41208', x: 0.97, y: 0.72, size: 0.46, alpha: 0.90, cycles: 2, ampX: 0.020, ampY: 0.022, phase: 1.9},
  {color: '#6E0C04', x: 0.99, y: 0.50, size: 0.36, alpha: 0.65, cycles: 2, ampX: 0.018, ampY: 0.020, phase: 4.2},
];

// Near-black navy, blended with `multiply` to carve the dark diagonal back in.
export const DARK_BLOBS: Blob[] = [
  {color: '#01020a', x: 0.10, y: 0.66, size: 0.62, alpha: 0.95, cycles: 1, ampX: 0.026, ampY: 0.022, phase: 1.1},
  {color: '#01020a', x: 0.36, y: 0.52, size: 0.62, alpha: 0.94, cycles: 1, ampX: 0.030, ampY: 0.026, phase: 3.8},
  {color: '#01020a', x: 0.65, y: 0.44, size: 0.62, alpha: 0.90, cycles: 1, ampX: 0.028, ampY: 0.024, phase: 0.7},
  {color: '#02040e', x: 0.90, y: 0.33, size: 0.46, alpha: 0.78, cycles: 2, ampX: 0.018, ampY: 0.018, phase: 5.3},
  {color: '#02040e', x: 0.04, y: 0.95, size: 0.48, alpha: 0.92, cycles: 2, ampX: 0.016, ampY: 0.014, phase: 2.2},
  {color: '#02040e', x: 0.99, y: 0.03, size: 0.44, alpha: 0.88, cycles: 2, ampX: 0.016, ampY: 0.016, phase: 4.4},
];

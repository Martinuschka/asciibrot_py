#!/usr/bin/env python3
"""ASCII-Mandelbrot direkt im Terminal.

Nutzung:
    python3 mandelbrot.py
    python3 mandelbrot.py --width 120 --height 45 --iter 120
    python3 mandelbrot.py --center -0.7441,0.0005 --zoom 0.005
"""

import argparse

# Zeichenskala: wenig Iterationen (weit außen) -> Punkt, viele -> dichte Zeichen
CHARS = " .:-=+*#%@"

def mandelbrot_pixel(cr: float, ci: float, max_iter: int) -> int:
    """Gibt die Anzahl der Iterationen bis zur Divergenz zurück."""
    zr, zi = 0.0, 0.0
    for n in range(max_iter):
        # z = z^2 + c
        zr, zi = zr * zr - zi * zi + cr, 2.0 * zr * zi + ci
        if zr * zr + zi * zi > 4.0:
            return n
    return max_iter

def render(width: int, height: int, max_iter: int,
           center_r: float, center_i: float, zoom: float) -> str:
    # zoom = Höhe des sichtbaren Ausschnitts in der komplexen Ebene.
    # Der Faktor 2.1 gleicht das breitere Terminal-Zeichen aus.
    scale_r = zoom * (width / height) / 2.1
    scale_i = zoom / 2.0

    lines = []
    for row in range(height):
        ci = center_i + (row / height - 0.5) * scale_i * 2.0
        line = []
        for col in range(width):
            cr = center_r + (col / width - 0.5) * scale_r * 2.0
            n = mandelbrot_pixel(cr, ci, max_iter)
            # Iterationszahl auf die Zeichenskala mappen
            idx = int(n / max_iter * (len(CHARS) - 1))
            line.append(CHARS[idx])
        lines.append("".join(line))
    return "\n".join(lines)

def main() -> None:
    parser = argparse.ArgumentParser(description="ASCII-Mandelbrot im Terminal")
    parser.add_argument("--width", type=int, default=100,
                        help="Breite in Zeichen (Standard: 100)")
    parser.add_argument("--height", type=int, default=38,
                        help="Höhe in Zeichen (Standard: 38)")
    parser.add_argument("--iter", type=int, default=80,
                        help="Maximale Iterationen (Standard: 80)")
    parser.add_argument("--center", type=str, default="-0.5,0",
                        help="Zentrum als 'real,imag' (Standard: -0.5,0)")
    parser.add_argument("--zoom", type=float, default=3.0,
                        help="Höhe des Ausschnitts, kleinerer = näher (Standard: 3.0)")
    args = parser.parse_args()

    center_r, center_i = (float(v) for v in args.center.split(","))

    print(render(args.width, args.height, args.iter,
                 center_r, center_i, args.zoom))

if __name__ == "__main__":
    main()
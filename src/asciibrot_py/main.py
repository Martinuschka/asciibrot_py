"""ASCII-Mandelbrot direkt im Terminal.

Nutzung:
    python3 mandelbrot.py
    python3 mandelbrot.py --width 120 --height 45 --iter 120
    python3 mandelbrot.py --center -0.7441,0.0005 --zoom 0.005
"""

import argparse
import sys
import time

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


def render(
    width: int,
    height: int,
    max_iter: int,
    center_r: float,
    center_i: float,
    zoom: float,
) -> str:
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


def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()


def get_user_rate():
    """Ask user for zoom rate or to quit."""
    while True:
        try:
            user_input = input("Enter zoom rate (frames per second, or 'q' to quit): ")
            if user_input.lower() == "q":
                return None
            rate = float(user_input)
            if rate < 0:
                print("Rate must be zero or positive.")
                continue
            return rate
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")


def zoom_loop(width, height, max_iter, center_r, center_i, initial_zoom, rate):
    """Continuously zoom into the fractal at the given rate."""
    zoom = initial_zoom
    zoom_factor = 0.9  # Each frame zooms in by 10%
    clear_screen()

    try:
        while True:
            rate_label = "max (no delay)" if rate == 0 else f"{rate:.2f} fps"
            frame = render(width, height, max_iter, center_r, center_i, zoom)
            sys.stdout.write(
                f"\x1b[HZoom: {zoom:.6f} | Rate: {rate_label} | "
                f"Press Ctrl+C to stop\x1b[K\n{frame}\n\x1b[J"
            )
            sys.stdout.flush()

            if rate > 0:
                time.sleep(1.0 / rate)

            # Zoom in for next frame
            zoom *= zoom_factor
    except KeyboardInterrupt:
        pass  # Will return to main menu


def main() -> None:
    parser = argparse.ArgumentParser(description="ASCII-Mandelbrot im Terminal")
    parser.add_argument(
        "--width", type=int, default=100, help="Breite in Zeichen (Standard: 100)"
    )
    parser.add_argument(
        "--height", type=int, default=38, help="Höhe in Zeichen (Standard: 38)"
    )
    parser.add_argument(
        "--iter", type=int, default=80, help="Maximale Iterationen (Standard: 80)"
    )
    parser.add_argument(
        "--center",
        type=str,
        default="-0.77568377,0.13646737",
        help="Zentrum als 'real,imag' (Standard: Spiralregion -0.77568377,0.13646737)",
    )
    parser.add_argument(
        "--zoom",
        type=float,
        default=3.0,
        help="Höhe des Ausschnitts, kleinerer = näher (Standard: 3.0)",
    )
    args = parser.parse_args()

    center_r, center_i = (float(v) for v in args.center.split(","))

    # Main interactive loop
    while True:
        try:
            rate = get_user_rate()
            if rate is None:
                print("Goodbye!")
                break

            zoom_loop(
                args.width, args.height, args.iter, center_r, center_i, args.zoom, rate
            )
        except KeyboardInterrupt:
            pass  # Continue to next iteration of main loop


if __name__ == "__main__":
    main()

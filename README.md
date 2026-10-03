# asciibrot_py

A small Python command-line tool that renders the Mandelbrot set as ASCII art directly in your terminal.

## What it does

`asciibrot_py` generates a fractal image using the Mandelbrot formula and prints it as a grid of characters. It is useful for quick visual exploration without needing a GUI or external libraries.

## Features

- Terminal-based ASCII rendering of the Mandelbrot set
- Adjustable image width and height
- Custom iteration depth for more detail
- Center and zoom controls for exploring different regions
- Simple installation and usage

## Installation

Using a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

If you use `uv` in this project:

```bash
uv sync
uv run asciibrot_py --help
```

## Usage

Run the program with the default settings:

```bash
asciibrot_py
```

Customize the output:

```bash
asciibrot_py --width 120 --height 40 --iter 100 --center -0.5,0 --zoom 3.0
```

## Options

- `--width`: Width of the rendered image in characters
- `--height`: Height of the rendered image in characters
- `--iter`: Maximum number of Mandelbrot iterations
- `--center`: Complex center as `real,imag` (for example `-0.5,0`)
- `--zoom`: Zoom level; smaller values zoom in

## Vista

Exciting coordinates to try out (show the famous Seahorse Valley):

```text
--center -0.7441,0.0005 --zoom 0.005 --iter 200
```

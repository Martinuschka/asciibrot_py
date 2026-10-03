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

Run the program with the default settings. The zoom starts at the Mandelbrot spiral region:

```bash
asciibrot_py
```

Customize the output or choose another center:

```bash
asciibrot_py --width 120 --height 40 --iter 100 --center -0.77568377,0.13646737 --zoom 3.0
```

## Options

- `--width`: Width of the rendered image in characters
- `--height`: Height of the rendered image in characters
- `--iter`: Maximum number of Mandelbrot iterations
- `--center`: Complex center as `real,imag` (default: spiral region `-0.77568377,0.13646737`)
- `--zoom`: Zoom level; smaller values zoom in

## Vista

The default zoom center is the famous Seahorse region:

```text
--center -0.77568377,0.13646737
```

## Overview

A Python project for creating presentation slides using Marp CLI.

## Usage

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)
- [marp-cli](https://github.com/marp-team/marp-cli)

You can install `marp-cli` with Homebrew or npm.

```bash
# Homebrew
brew install marp-cli

# npm
npm install -g @marp-team/marp-cli
```

### Setup

Install project dependencies.

```bash
make setup
```

### Generating Slides

Edit `src/slides.md` to create your slides. You can generate the PDF with the following command. The output will be saved in `output/slides.pdf`.

```bash
make run
```

### Other Commands

- `make help`: Show all available commands.
- `make test`: Run tests.
- `make format`: Format code.
- `make lint`: Run linter.

# Ramzan Coding Nights

This repository contains my projects developed during Ramzan Coding Nights:

1. **Todo CLI** - A command line todo application
2. **Unit Converter** - A utility for converting between different units

## Projects Structure

```
.
├── todo-cli/         # Todo list CLI application
├── unit-converter/   # Unit conversion utility
└── git-commands.md   # Git reference commands
```

## Getting Started

Each project has its own README with specific instructions.

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Ramzan-Coding-Nights
```

2. Remove any nested .git directories:
```bash
rm -rf todo-cli/.git
rm -rf unit-converter/.git
```

3. Reinitialize the repository:
```bash
git rm --cached todo-cli
git rm --cached unit-converter
git add .
git commit -m "Fix: Remove nested git repositories"
```

## Password Generator

To install dependencies for the password-generator project, you may need to increase the network timeout setting:

### Using Poetry
```bash
# Set the UV_HTTP_TIMEOUT environment variable to 60 seconds
$env:UV_HTTP_TIMEOUT=60

# Install dependencies using Poetry
cd password-generator
poetry install
```

### Using UV
```bash
# Set the UV_HTTP_TIMEOUT environment variable to 60 seconds
$env:UV_HTTP_TIMEOUT=60

# Install streamlit using UV
cd password-generator
uv add streamlit
```

Note: For Unix/Linux systems, use `export UV_HTTP_TIMEOUT=60` instead of `$env:UV_HTTP_TIMEOUT=60`.

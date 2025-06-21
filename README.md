# Python Virtual Environment Setup

A streamlined toolset for quickly setting up Python virtual environments with Jupyter Lab support.

## Overview

This project provides automated scripts to create and configure Python virtual environments, making it easy to get started with Python development and Jupyter notebooks.

## Prerequisites

- Python 3.12 or higher
- Bash shell (macOS/Linux)

## Quick Start

### 1. Initial Setup

Create a new virtual environment:

```bash
./setup_venv.sh
```

### 2. Verify Python Version

Check your Python version before proceeding:

```bash
python check_python_version.py
```

This script validates Python 3.12 compatibility.

### 3. Install Dependencies

Install required packages:

```bash
./install_deps.sh
```

### 4. Launch Jupyter Lab

Start Jupyter Lab for notebook development:

```bash
jupyter lab
```

## Development Workflow

### Activating the Virtual Environment

To activate the virtual environment in a new terminal session:

```bash
source ./myvenv/bin/activate
```

### Deactivating the Virtual Environment

When you're done working:

```bash
deactivate
```





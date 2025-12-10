# Python Inventory Data Pipeline (CLI + Modular Backend)

Python backend project focused on data processing and automation.  
Includes a modular architecture, a full CLI interface, JSON merging workflow, data validation, logging system, and reporting tools.  
Designed as a real backend-style pipeline for inventory updates and transformations.

---

## Overview

This repository groups my main Python backend work:

- A **modular inventory system** designed as a small data pipeline.
- A **monolithic version** of the same logic for comparison.
- A folder of **Python exercises** used to practice core language features and patterns.

The goal is to demonstrate the fundamentals of backend development with Python:
clean code, data workflows, automation via CLI, and proper logging and error handling.

---

## Main Features

### Inventory Data Pipeline
- Loads inventory and update files in JSON.
- Normalizes and restructures data.
- Applies updates (additions, changes, removals).
- Produces an updated inventory plus summary reports.

### **Command-Line Interface (CLI)**
- Powered by `argparse`.
- Receives paths and options from the terminal.
- Runs the entire workflow with a single command.

### **Modular Architecture**
Separated into clear components:
- I/O operations (JSON load/save)
- Core inventory logic
- Reporting tools
- CLI entry point
- Logging configuration  

Designed for maintainability and readability.

### **Logging System**
- Centralized logging using Python's `logging` module  
- Informational and debug messages for key actions  
- Error logging for unexpected situations or invalid files  

### **Data Validation & Error Handling**
- File existence checks  
- JSON decoding protection  
- Defensive handling of unknown or malformed entries  

---

## Repository Structure

```text
/inventario_modular/       # Modular implementation (recommended)
/inventario_monolitico/    # First monolithic prototype
/python_exercises/         # Practice exercises and learning scripts
```
---

## Tech Stack

- **Python 3.x**
- **Standard Library Only**:
  - `argparse` → CLI
  - `json` → data handling
  - `logging` → logging system
  - `pathlib` → file paths
  - other built-ins where appropriate  
No external dependencies required.

---

## How to Run the Modular Pipeline

Example invocation:

```bash
python -m inventario_modular \
    --inventario data/inventario.json \
    --actualizacion data/actualizacion.json \
    --salida salida/inventario_final.json \
    --top 10


````
**Main CLI arguments:**

* `--inventario` → path to the original inventory
* `--actualizacion` → path to the update file
* `--salida` → path to save the updated inventory
* `--top` → optional “Top N” report


**Learning Goals**

This project was built to practice and demonstrate:

* Backend-oriented problem solving with Python
* Data processing and pipeline automation
* Building professional CLIs
* Clean, modular code structure
* Logging and error handling best practices

It showcases the transition from a basic script to a clean, extensible backend-style pipeline.


**Status**

Active development and refinement as part of my backend training path.
Feel free to explore the code or contact me for further details.

```

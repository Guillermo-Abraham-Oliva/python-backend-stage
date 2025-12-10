# Python Inventory Data Pipeline (CLI + Modular Backend)
Status: Completed Stage (Learning milestone successfully closed)
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
  - **`argparse`** → CLI
  - **`json`** → data handling
  - **`logging`** → logging system
  - **`pathlib`** → file paths
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


## Learning Goals

This project was built to practice and demonstrate:

* Backend-oriented problem solving with Python
* Data processing and pipeline automation
* Building professional CLIs
* Clean, modular code structure
* Logging and error handling best practices

It showcases the transition from a basic script to a clean, extensible backend pipeline.


## What’s Next (Roadmap)

Having completed this Python backend learning stage, the next phase of my full-stack development path will focus on the modern JavaScript/TypeScript ecosystem.
Each stage will be developed in separate repositories to maintain a clean and professional progression history.

The roadmap I will follow consists of:

BLOCK 1 — FOUNDATIONS:
  * **HTML** Fundamentals
  * **CSS** Fundamentals
  * Core **JavaScript** (ES6+)
  * Small **JavaScript Projects** (DOM, events, components, fetch, state basics)

BLOCK 2 — REAL FRONTEND
  * **React** – Component model, hooks, context, basic state architecture
  * **TypeScript** – Strong typing, interfaces, generics, type-safe JS
  * **Next.js** – File-based routing, server-side rendering, server actions, API routes
  * **Next.js Project** – First real-world frontend/full-stack capable app

BLOCK 3 — REAL BACKEND
  * **Node.js** – Runtime fundamentals, modules, async patterns
  * **Express.js** – REST APIs, routing, middleware, controllers
  * **SQL** – Relational modeling, SELECT/INSERT/UPDATE, joins, indexing
  * **Backend Project (API)** – CRUD endpoints, architecture, error handling

BLOCK 4 — FULL-STACK PROFESSIONAL
  * **ORM Prisma + Database Migrations**
  * **Authentication + Basic Security** (sessions, JWT, hashing, input validation)
  * **Full-Stack Final Project** integrating:
       - Next.js
       - Node.js + Express
       - SQL + Prisma
       - Auth + protected routes
       - Deployment-ready structure
  * **Basic Testing (unit tests, API tests, component tests)


This roadmap represents the next complete stage toward becoming a professional full-stack developer.

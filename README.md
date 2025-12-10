
---

# Python Inventory Data Pipeline (CLI + Modular Backend)

![Status: Completed](https://img.shields.io/badge/Status-Completed-green)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Backend](https://img.shields.io/badge/Backend-Python%20Pipeline-orange)
![Architecture: Modular](https://img.shields.io/badge/Architecture-Modular-blueviolet)
![Learning Stage](https://img.shields.io/badge/Stage-Python%20Backend%20Learning-lightgrey)

**Status: Learning milestone completed – Python backend stage closed.**

Python backend project focused on data processing and automation.
Includes a modular architecture, a full CLI interface, JSON merging workflow, data validation, logging system, and reporting tools.
Designed as a real backend-style pipeline for inventory updates and transformations.

---

## Overview

This repository groups my main Python backend work:

* A modular inventory system designed as a small data pipeline.
* A monolithic version of the same logic for comparison.
* A folder of Python exercises used to practice core language features and patterns.

The goal is to demonstrate the fundamentals of backend development with Python: clean code, data workflows, automation via CLI, and proper logging and error handling.

---

## Main Features

### Inventory Data Pipeline

* Loads inventory and update files in JSON.
* Normalizes and restructures data.
* Applies updates (additions, changes, removals).
* Produces an updated inventory plus summary reports.

### Command-Line Interface (CLI)

* Powered by `argparse`.
* Receives file paths and options from the terminal.
* Runs the entire workflow with a single command.

### Modular Architecture

Separated into clear components:

* I/O operations (JSON load/save)
* Core inventory logic
* Reporting tools
* CLI entry point
* Logging configuration

Designed for maintainability and readability.

### Logging System

* Centralized logging using Python’s `logging` module
* Informational and debug messages for key workflow steps
* Error logging for invalid files or unexpected data

### Data Validation & Error Handling

* File existence checks
* JSON decoding protection
* Defensive handling of malformed or unknown entries

---

## Repository Structure

```
/inventario_modular/       # Modular implementation (recommended)
/inventario_monolitico/    # First monolithic prototype
/python_exercises/         # Practice exercises and learning scripts
```

---

## Tech Stack

**Python 3.x**
Standard Library Only:

* `argparse` → CLI
* `json` → data handling
* `logging` → logging system
* `pathlib` → file paths
* Other built-ins where appropriate

No external dependencies required.

---

## How to Run the Modular Pipeline

Example invocation:

```
python -m inventario_modular \
    --inventario data/inventario.json \
    --actualizacion data/actualizacion.json \
    --salida salida/inventario_final.json \
    --top 10
```

Main CLI arguments:

* `--inventario` → path to the original inventory
* `--actualizacion` → path to the update file
* `--salida` → path to save the updated inventory
* `--top` → optional “Top N” report

---

## Learning Goals

This project was built to practice and demonstrate:

* Backend-oriented problem solving with Python
* Data processing and automation pipelines
* Building professional CLIs
* Clean, modular code structure
* Logging and error handling best practices

It showcases the transition from a basic script to a clean, extensible backend-style pipeline.

---

## What’s Next (Roadmap)

Having completed this Python backend learning stage, the next phase of my full-stack development path will focus on the modern JavaScript/TypeScript ecosystem.
Each stage will be developed in **separate repositories**, maintaining a clean and professional progression history.

The roadmap I will follow consists of:

---

### **BLOCK 1 — FOUNDATIONS**

1. **Git** – version control fundamentals
2. **HTML** – structure, semantics, layout basics
3. **CSS** – styles, responsive design, positioning
4. **JavaScript (ES6+)** – variables, functions, arrays, objects, promises
5. **JavaScript Projects** – DOM, events, components, fetch, basic state patterns

---

### **BLOCK 2 — REAL FRONTEND**

6. **React** – components, hooks, props/state patterns, context
7. **TypeScript** – types, interfaces, generics, type-safe components
8. **Next.js** – routing, server actions, SSR/SSG, layouts
9. **Next.js Project** – first production-style frontend/full-stack capable app

---

### **BLOCK 3 — REAL BACKEND**

10. **Node.js** – runtime fundamentals, modules, async workflows
11. **Express.js** – REST API design, routing, middleware, controllers
12. **SQL** – relational modeling, normalization, joins, indexing
13. **Backend API Project** – CRUD, architecture, error handling, best practices

---

### **BLOCK 4 — FULL-STACK PROFESSIONAL**

14. **ORM Prisma** + migrations – schema, migrations, type-safe queries
15. **Auth + Basic Security** – sessions/JWT, hashing, input validation
16. **Full-Stack Final Project**, integrating:

    * Next.js
    * Node.js + Express
    * SQL + Prisma
    * Auth + protected routes
    * Deployment-ready architecture
17. **Basic Testing** – unit tests, API tests, component testing

---

This roadmap represents the next complete stage toward becoming a professional full-stack developer.

---



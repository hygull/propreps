# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

**propreps** is a personal learning and reference repository by Rishikesh Agrawani. It contains coding problem solutions, language examples, reference notes, and interview prep material. There is no build system, test framework, or application to run — it is a collection of standalone files.

## Running Code

Scripts are standalone. Run any Python script directly:

```bash
python3 src/scripts/01_functions.py
python3 src/interviews/scaler.com/25_oct_2025.py
```

Shell scripts:

```bash
bash src/shell_scripts/grep_examples.sh
```

## Repository Structure

- `src/markdowns/` — Markdown reference docs organized by topic (python, docker, git). Each file covers a specific Python module, concept, or tool with examples.
- `src/scripts/` — Numbered standalone Python scripts demonstrating specific concepts (functions, dataframes, match/case, etc.).
- `src/shell_scripts/` — Bash script examples (grep, awk, sed, loops, etc.) with supporting files in `src/shell_scripts/files/`.
- `src/interviews/` — Interview problem solutions organized by company and date.
- `src/notes/` — Notes created via the `/notes-taker` skill, organized by topic subdirectories.
- `src/package_or_library_details/` — Deep-dive reference docs for specific Python packages (collections, itertools, pandas).
- `assets/images/` — Screenshots of code snippets referenced from README.md.

## Claude Code Skills

The repo has a custom `/take-notes` skill (`.claude/skills/take-notes/SKILL.md`) that creates organized notes under `src/notes/` with automatic topic-based subdirectory grouping.

## Conventions

- Python files in `src/scripts/` are numbered sequentially (e.g., `07_string_formatting_...py`). Follow this pattern when adding new scripts.
- Markdown files use fenced code blocks with language tags for examples.
- The repository has no dependencies file — scripts use Python standard library or common packages (pandas, etc.) assumed to be installed.

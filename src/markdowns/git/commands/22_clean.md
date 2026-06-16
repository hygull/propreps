# git clean

Removes untracked files from the working tree.

## Dry Run (Preview)

```shell
# ALWAYS preview first — git clean is irreversible
$ git clean -n
$ git clean --dry-run
Would remove build/
Would remove temp.log
Would remove untitled.py
```

## Basic Usage

```shell
# Remove untracked files (requires -f flag for safety)
$ git clean -f
Removing temp.log
Removing untitled.py

# Remove untracked files in a specific directory
$ git clean -f src/

# Remove specific untracked file
$ git clean -f temp.log
```

## Remove Untracked Directories

```shell
# Remove untracked files AND directories
$ git clean -fd
Removing build/
Removing temp.log
Removing __pycache__/

# Preview first
$ git clean -nd
Would remove build/
Would remove __pycache__/
```

## Remove Ignored Files

```shell
# Remove only ignored files (files matching .gitignore)
$ git clean -fX
Removing .env
Removing __pycache__/
Removing *.pyc

# Remove both ignored AND untracked files
$ git clean -fx
Removing .env
Removing __pycache__/
Removing temp.log
Removing untitled.py

# Preview ignored files that would be removed
$ git clean -nX
Would remove .env
Would remove __pycache__/
Would remove node_modules/
```

## Interactive Mode

```shell
$ git clean -i
Would remove the following items:
  build/    temp.log    untitled.py

*** Commands ***
    1: clean    2: filter by pattern    3: select by numbers
    4: ask each    5: quit    6: help

What now> 4
Remove build/ [y/N]? y
Remove temp.log [y/N]? n
Remove untitled.py [y/N]? y
```

## Exclude Patterns

```shell
# Remove untracked files but exclude certain patterns
$ git clean -f -e "*.log"
# Removes all untracked except .log files

$ git clean -f -e "*.log" -e "temp/"
```

## Common Workflows

```shell
# Full reset: discard ALL changes (tracked + untracked)
$ git checkout -- .      # reset tracked files
$ git clean -fd          # remove untracked files and directories

# Modern equivalent
$ git restore .          # reset tracked files
$ git clean -fd          # remove untracked

# Nuclear option: make working tree identical to HEAD
$ git reset --hard HEAD
$ git clean -fdx         # remove untracked AND ignored files

# Clean up after a failed build
$ git clean -fdX         # remove only ignored files (build artifacts)

# Preview everything that would be cleaned
$ git clean -ndx
Would remove .env
Would remove build/
Would remove dist/
Would remove node_modules/
Would remove __pycache__/
```

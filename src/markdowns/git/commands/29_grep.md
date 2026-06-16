# git grep

Searches tracked files in the working tree for a pattern. Faster than `grep -r` because it only searches git-tracked files.

## Basic Usage

```shell
# Search for a string in all tracked files
$ git grep "TODO"
src/app.py:15:    # TODO: add error handling
src/auth.py:8:    # TODO: implement token refresh
tests/test_auth.py:3:# TODO: add edge case tests

# Search for a pattern
$ git grep "def authenticate"
src/auth.py:10:def authenticate(username, password):
```

## Case-Insensitive Search

```shell
$ git grep -i "todo"
src/app.py:15:    # TODO: add error handling
src/auth.py:8:    # Todo: implement token refresh
README.md:20:See the todo list below
```

## Show Line Numbers

```shell
$ git grep -n "import"
src/app.py:1:from flask import Flask
src/app.py:2:from auth import authenticate
src/auth.py:1:import jwt
src/auth.py:2:import hashlib
```

## Count Matches

```shell
# Show match count per file
$ git grep -c "TODO"
src/app.py:2
src/auth.py:1
tests/test_auth.py:3

# Total count across all files
$ git grep -c "TODO" | awk -F: '{sum += $2} END {print sum}'
6
```

## Search in Specific Files/Directories

```shell
# Search only in Python files
$ git grep "import" -- "*.py"

# Search only in a directory
$ git grep "TODO" -- src/

# Search in multiple file types
$ git grep "TODO" -- "*.py" "*.js"

# Exclude a path
$ git grep "TODO" -- . ":!node_modules" ":!vendor"
```

## Regex Search

```shell
# Extended regex
$ git grep -E "def (get|set|delete)_user"
src/users.py:10:def get_user(user_id):
src/users.py:25:def set_user(user_id, data):
src/users.py:40:def delete_user(user_id):

# Perl-compatible regex
$ git grep -P "TODO:\s+\w+"

# Fixed string (no regex interpretation)
$ git grep -F "user.get()"
```

## Context Lines

```shell
# Show N lines before and after each match
$ git grep -C 3 "authenticate"

# Show N lines before
$ git grep -B 2 "authenticate"

# Show N lines after
$ git grep -A 5 "authenticate"
```

## Multiple Patterns

```shell
# OR: match any pattern
$ git grep -e "TODO" -e "FIXME" -e "HACK"
$ git grep -e "TODO" --or -e "FIXME"

# AND: match all patterns in the same file
$ git grep -e "import" --and -e "flask" -- "*.py"

# NOT
$ git grep -e "TODO" --and --not -e "DONE"

# Complex boolean
$ git grep -e "TODO" --and \( -e "auth" --or -e "login" \)
```

## Search at a Specific Commit/Branch

```shell
# Search in a past commit
$ git grep "TODO" abc1234

# Search in another branch
$ git grep "authenticate" feature/auth

# Search in a tag
$ git grep "version" v1.0.0
```

## Show Only Filenames

```shell
# List files that contain the pattern
$ git grep -l "TODO"
src/app.py
src/auth.py
tests/test_auth.py

# List files that do NOT contain the pattern
$ git grep -L "TODO"
src/config.py
src/utils.py
README.md
```

## Word Match

```shell
# Match whole words only (not substrings)
$ git grep -w "get"
# Matches "get" but not "get_user" or "target"
```

## Show Function Context

```shell
# Show the function name containing each match
$ git grep -p "return None" -- "*.py"
src/auth.py=def authenticate(username, password):
src/auth.py:25:    return None
```

## Common Uses

```shell
# Find all API endpoints
$ git grep -n "@app.route" -- "*.py"

# Find all environment variable usage
$ git grep -n "os.environ" -- "*.py"

# Find all SQL queries
$ git grep -n "SELECT\|INSERT\|UPDATE\|DELETE" -- "*.py"

# Find unused imports (combine with other tools)
$ git grep -l "import requests" -- "*.py"

# Count TODOs per directory
$ git grep -c "TODO" -- src/ | sort -t: -k2 -rn
```

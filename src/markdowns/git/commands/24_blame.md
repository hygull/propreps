# git blame

Shows what revision and author last modified each line of a file.

## Basic Usage

```shell
$ git blame src/app.py
abc1234 (Alice  2025-06-10 14:30:00 +0530  1) from flask import Flask
def5678 (Bob    2025-06-12 09:15:00 +0530  2) from auth import authenticate
abc1234 (Alice  2025-06-10 14:30:00 +0530  3)
ghi9012 (Alice  2025-06-14 16:00:00 +0530  4) app = Flask(__name__)
abc1234 (Alice  2025-06-10 14:30:00 +0530  5)
def5678 (Bob    2025-06-12 09:15:00 +0530  6) @app.route("/login")
def5678 (Bob    2025-06-12 09:15:00 +0530  7) def login():
def5678 (Bob    2025-06-12 09:15:00 +0530  8)     return authenticate(request)
```

## Blame Specific Lines

```shell
# Show blame for lines 10 to 20 only
$ git blame -L 10,20 src/app.py

# From line 10 to end of file
$ git blame -L 10, src/app.py

# Show 5 lines starting from line 10
$ git blame -L 10,+5 src/app.py

# Blame a function (by regex matching the function name)
$ git blame -L :authenticate src/auth.py
```

## Blame at a Specific Commit

```shell
# Blame as of a past commit (who wrote what at that point)
$ git blame abc1234 -- src/app.py

# Blame before a certain commit
$ git blame abc1234^ -- src/app.py
```

## Show Email Instead of Name

```shell
$ git blame -e src/app.py
abc1234 (<alice@example.com> 2025-06-10 14:30:00 +0530 1) from flask import Flask
def5678 (<bob@example.com>   2025-06-12 09:15:00 +0530 2) from auth import authenticate
```

## Ignore Whitespace Changes

```shell
# Ignore whitespace when finding the origin of lines
$ git blame -w src/app.py
```

## Detect Moved/Copied Lines

```shell
# Detect lines moved within the same file
$ git blame -M src/app.py

# Detect lines moved from other files in the same commit
$ git blame -C src/app.py

# Detect lines copied from other files in any commit
$ git blame -C -C src/app.py

# Even more aggressive copy detection
$ git blame -C -C -C src/app.py
```

## Porcelain Format (Scripting)

```shell
# Machine-readable output
$ git blame --porcelain src/app.py
abc1234567890abcdef 1 1 3
author Alice
author-mail <alice@example.com>
author-time 1718012400
author-tz +0530
...

# Line-porcelain (per-line, easier to parse)
$ git blame --line-porcelain src/app.py
```

## Show Original Filename (After Renames)

```shell
# If the file was renamed, show the original path
$ git blame --follow src/new-name.py
```

## Date Formats

```shell
# Short date format
$ git blame --date=short src/app.py
abc1234 (Alice 2025-06-10  1) from flask import Flask

# Relative date
$ git blame --date=relative src/app.py
abc1234 (Alice 6 days ago  1) from flask import Flask

# ISO format
$ git blame --date=iso src/app.py
```

## Ignore Specific Revisions

```shell
# Ignore a commit (e.g., a formatting-only change)
$ git blame --ignore-rev abc1234 src/app.py

# Ignore multiple commits listed in a file
$ echo "abc1234" >> .git-blame-ignore-revs
$ echo "def5678" >> .git-blame-ignore-revs
$ git blame --ignore-revs-file .git-blame-ignore-revs src/app.py

# Set the ignore file globally for the repo
$ git config blame.ignoreRevsFile .git-blame-ignore-revs
```

## Common Uses

```shell
# Find who introduced a bug on a specific line
$ git blame -L 42,42 src/app.py
abc1234 (Bob 2025-06-12 09:15:00 +0530 42)     return None  # bug!

# Then see the full commit
$ git show abc1234

# Find when a line was added
$ git log -S "return None" --oneline -- src/app.py
abc1234 Add login endpoint
```

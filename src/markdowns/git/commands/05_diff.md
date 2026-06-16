# git diff

Shows changes between commits, staging area, and working tree.

## Working Directory vs Staging Area

```shell
# Show unstaged changes (what you haven't git added yet)
$ git diff
diff --git a/app.py b/app.py
index abc1234..def5678 100644
--- a/app.py
+++ b/app.py
@@ -1,5 +1,6 @@
 def hello():
-    print("Hello")
+    print("Hello, World!")
+    print("Welcome")
     return True

# Diff a specific file
$ git diff README.md
```

## Staged Changes

```shell
# Show what's staged (will go into next commit)
$ git diff --staged
$ git diff --cached

# Staged changes for a specific file
$ git diff --staged src/app.py
```

## Between Commits

```shell
# Diff between two commits
$ git diff abc1234 def5678

# Diff between a commit and HEAD
$ git diff abc1234 HEAD

# Diff between HEAD and its parent
$ git diff HEAD~1 HEAD
$ git diff HEAD^ HEAD

# Diff between two branches
$ git diff main feature/auth
$ git diff main..feature/auth

# Changes on feature branch since it diverged from main
$ git diff main...feature/auth
```

## Stat and Summary

```shell
# Show only file names and change counts
$ git diff --stat
 src/app.py     | 15 ++++++++-------
 src/utils.py   |  8 ++++++++
 tests/test.py  |  3 +--
 3 files changed, 16 insertions(+), 10 deletions(-)

# Show only file names
$ git diff --name-only
src/app.py
src/utils.py
tests/test.py

# Show file names with status (Added, Modified, Deleted)
$ git diff --name-status
M       src/app.py
A       src/utils.py
M       tests/test.py

# Summary of changes
$ git diff --shortstat
 3 files changed, 16 insertions(+), 10 deletions(-)
```

## Word-Level Diff

```shell
# Show word-by-word changes instead of line-by-line
$ git diff --word-diff
def hello():
    print({-"Hello"-}{+"Hello, World!"+})
    return True

# Word diff with color only (no markers)
$ git diff --word-diff=color

# Custom word regex
$ git diff --word-diff-regex="[a-zA-Z_]+"
```

## Filtering Diffs

```shell
# Only show changes in Python files
$ git diff -- "*.py"

# Only show changes in a directory
$ git diff -- src/

# Exclude a path
$ git diff -- . ":(exclude)package-lock.json"
$ git diff -- . ":!package-lock.json"

# Only show added files
$ git diff --diff-filter=A --name-only

# Only show modified files
$ git diff --diff-filter=M --name-only

# Only show deleted files
$ git diff --diff-filter=D --name-only
```

## Context Lines

```shell
# Show more context around changes (default is 3 lines)
$ git diff -U5
$ git diff --unified=10

# Show no context lines
$ git diff -U0
```

## Ignoring Whitespace

```shell
# Ignore all whitespace changes
$ git diff -w
$ git diff --ignore-all-space

# Ignore changes in amount of whitespace
$ git diff -b
$ git diff --ignore-space-change

# Ignore blank line changes
$ git diff --ignore-blank-lines
```

## Binary Files

```shell
# Check if there are binary file changes
$ git diff --stat
 image.png | Bin 1024 -> 2048 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)

# Show binary diffs as text (for hex comparison)
$ git diff --binary
```

## Diff Against Stash

```shell
# Diff working tree against latest stash
$ git diff stash@{0}

# Diff between two stashes
$ git diff stash@{0} stash@{1}
```

## Output to File (Patch)

```shell
# Save diff as a patch file
$ git diff > changes.patch

# Apply a patch
$ git apply changes.patch

# Check if a patch applies cleanly
$ git apply --check changes.patch
```

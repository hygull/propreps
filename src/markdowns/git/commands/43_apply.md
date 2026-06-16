# git apply

Applies a patch to the working tree without creating a commit. For commit-preserving application, see `git am`.

## Basic Usage

```shell
# Apply a patch file
$ git apply fix.patch
# Changes are applied to working tree (not staged, not committed)

# Apply a diff from stdout
$ git diff HEAD~1 | git apply

# Apply a patch created by git format-patch
$ git apply 0001-Add-auth-middleware.patch
```

## Check Before Applying

```shell
# Check if a patch applies cleanly (dry run)
$ git apply --check fix.patch
# No output = patch applies cleanly

$ git apply --check broken.patch
error: patch failed: src/app.py:10
error: src/app.py: patch does not apply

# Show stats without applying
$ git apply --stat fix.patch
 src/auth.py   |   15 +++++++++++++++
 src/config.py |    3 +++
 2 files changed, 18 insertions(+)
```

## Apply and Stage

```shell
# Apply and add changes to the staging area
$ git apply --index fix.patch
# Changes are applied AND staged (ready to commit)

# Apply directly to the staging area (working tree untouched)
$ git apply --cached fix.patch
```

## Reverse Apply

```shell
# Undo a previously applied patch
$ git apply --reverse fix.patch
$ git apply -R fix.patch

# Check if reverse application would work
$ git apply --reverse --check fix.patch
```

## Three-Way Merge

```shell
# Fall back to 3-way merge if direct apply fails
$ git apply --3way fix.patch
$ git apply -3 fix.patch
# If conflicts occur, they are marked with conflict markers
# just like a merge conflict
```

## Whitespace Handling

```shell
# Fix trailing whitespace errors while applying
$ git apply --whitespace=fix fix.patch

# Warn about whitespace errors
$ git apply --whitespace=warn fix.patch
warning: trailing whitespace detected

# Error on whitespace problems
$ git apply --whitespace=error fix.patch

# Strip trailing whitespace
$ git apply --whitespace=strip fix.patch

# Ignore all whitespace changes
$ git apply --whitespace=nowarn fix.patch
```

## Partial Apply

```shell
# Exclude certain files from the patch
$ git apply --exclude="*.test.py" fix.patch
$ git apply --exclude="docs/*" fix.patch

# Include only certain files
$ git apply --include="src/auth/*" fix.patch

# Apply to a subdirectory
$ git apply --directory=subproject/ fix.patch
# Prepends subproject/ to all file paths in the patch
```

## Context Lines

```shell
# Reduce required context lines for matching (default: 3)
$ git apply -C1 fix.patch
# Requires only 1 line of surrounding context to match

# No context matching (just line numbers)
$ git apply -C0 fix.patch
```

## Handle Renames and Binary Files

```shell
# Apply a patch that includes renames
$ git apply fix.patch
# Renames are detected if the patch includes rename headers

# Apply a binary patch
$ git apply --binary binary-changes.patch
```

## Verbose Output

```shell
# Show which files are being patched
$ git apply -v fix.patch
Checking patch src/auth.py...
Applied patch src/auth.py cleanly.
Checking patch src/config.py...
Applied patch src/config.py cleanly.
```

## Create Patches to Apply

```shell
# Create a patch from unstaged changes
$ git diff > my-changes.patch

# Create a patch from staged changes
$ git diff --cached > staged-changes.patch

# Create a patch between two commits
$ git diff abc1234 def5678 > between-commits.patch

# Create a patch between two branches
$ git diff main..feature/auth > feature.patch
```

## git apply vs git am

```shell
# git apply: modifies files, no commit created
$ git apply fix.patch
$ git status
Changes not staged for commit:
        modified:   src/auth.py

# git am: creates a commit with author/date/message preserved
$ git am 0001-Fix-auth.patch
Applying: Fix auth
$ git log -1
commit abc1234
Author: Original Author <author@example.com>
    Fix auth

# Use git apply for: quick local patches, diffs, partial application
# Use git am for: formatted patches from format-patch, email patches
```

## Common Workflows

```shell
# Colleague sends a diff via chat
$ pbpaste > fix.patch        # paste into file (macOS)
$ git apply --check fix.patch
$ git apply fix.patch

# Try a patch, revert if it doesn't work
$ git apply fix.patch
$ python -m pytest            # test it
$ git apply -R fix.patch      # undo if tests fail

# Apply a GitHub PR as a patch
$ curl -L https://github.com/user/repo/pull/123.patch | git apply --check
$ curl -L https://github.com/user/repo/pull/123.patch | git apply

# Port changes between unrelated repos
# In repo A:
$ git diff HEAD~3..HEAD -- src/ > changes.patch
# In repo B:
$ git apply --directory=lib/ changes.patch
```

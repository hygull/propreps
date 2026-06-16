# git status

Shows the state of the working tree and staging area.

## Basic Usage

```shell
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   src/auth.py
        modified:   src/app.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        docs/
        notes.txt
```

## Short Format

```shell
$ git status -s
$ git status --short
A  src/auth.py
M  src/app.py
 M README.md
?? docs/
?? notes.txt

# Status codes (two columns: staging area | working tree)
#  M  — modified in working tree (not staged)
# M   — modified and staged
# MM  — staged, then modified again
# A   — new file, staged
# D   — deleted and staged
# R   — renamed and staged
# ??  — untracked
# !!  — ignored
```

## Branch Info

```shell
# Show branch and tracking info in short format
$ git status -sb
$ git status --short --branch
## main...origin/main

## main...origin/main [ahead 2]

## main...origin/main [behind 3]

## main...origin/main [ahead 1, behind 2]

## feature/auth (no upstream)
```

## Show Ignored Files

```shell
$ git status --ignored
On branch main
Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
        .env
        __pycache__/
        node_modules/
        *.pyc

# Short format with ignored
$ git status -s --ignored
!! .env
!! __pycache__/
!! node_modules/
```

## Porcelain Format (Scripting)

```shell
# Machine-readable output (stable format across git versions)
$ git status --porcelain
A  src/auth.py
M  src/app.py
 M README.md
?? docs/

# Version 2 porcelain (more detailed)
$ git status --porcelain=v2
1 A. N... 000000 100644 100644 0000000 abc1234 src/auth.py
1 M. N... 100644 100644 100644 abc1234 def5678 src/app.py

# Useful in scripts
$ if [ -n "$(git status --porcelain)" ]; then
>   echo "Working directory is dirty"
> else
>   echo "Working directory is clean"
> fi
```

## Limiting Output

```shell
# Only show untracked files (not inside untracked directories)
$ git status -u no
$ git status --untracked-files=no

# Show individual files inside untracked directories
$ git status -u all

# Normal mode (show untracked directories, not their contents)
$ git status -u normal
```

## Ahead/Behind Count

```shell
# When your branch is ahead of remote
$ git status
On branch feature/auth
Your branch is ahead of 'origin/feature/auth' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

# When your branch is behind
$ git status
On branch main
Your branch is behind 'origin/main' by 5 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

# When diverged
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 2 and 3 different commits each, respectively.
```

## Clean Working Tree

```shell
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

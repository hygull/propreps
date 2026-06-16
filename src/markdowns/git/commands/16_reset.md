# git reset

Resets current HEAD to a specified state. Moves the branch pointer and optionally modifies staging area and working tree.

## Three Modes

```shell
# --soft: move HEAD only (staging area and working tree unchanged)
$ git reset --soft HEAD~1
# Commit is undone, changes remain staged and ready to re-commit

# --mixed (default): move HEAD + reset staging area (working tree unchanged)
$ git reset HEAD~1
$ git reset --mixed HEAD~1
# Commit is undone, changes are in working tree but unstaged

# --hard: move HEAD + reset staging area + reset working tree (DANGEROUS)
$ git reset --hard HEAD~1
# Commit is undone, ALL changes are GONE
```

## Unstage Files

```shell
# Unstage a file (keep changes in working directory)
$ git reset HEAD file.py
Unstaged changes after reset:
M       file.py

# Unstage everything
$ git reset HEAD
$ git reset

# Modern alternative
$ git restore --staged file.py
```

## Undo Commits

```shell
# Undo last commit, keep changes staged
$ git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
$ git reset HEAD~1

# Undo last 3 commits
$ git reset HEAD~3

# Undo to a specific commit
$ git reset abc1234

# Undo last commit AND discard all changes (DANGEROUS)
$ git reset --hard HEAD~1
```

## Reset to Remote State

```shell
# Make local branch match remote exactly (DANGEROUS — discards local changes)
$ git fetch origin
$ git reset --hard origin/main

# Useful when your local branch is messed up
$ git reset --hard origin/feature/auth
```

## Reset Specific Files

```shell
# Reset a file in staging area to match HEAD (unstage it)
$ git reset HEAD -- src/app.py

# Reset a file to match a specific commit (in staging area only)
$ git reset abc1234 -- src/app.py
# Now the file in staging matches that commit, working tree unchanged
```

## Soft Reset for Squashing

```shell
# Squash last 5 commits into one
$ git reset --soft HEAD~5
$ git commit -m "Combined feature: auth system"
# All changes from those 5 commits are now in one commit
```

## Mixed Reset for Re-staging

```shell
# Undo last commit and selectively re-stage
$ git reset HEAD~1
# Now all changes are unstaged
$ git add src/auth.py
$ git commit -m "Just the auth changes"
# Remaining changes stay in working directory for a separate commit
```

## Recovery After Reset

```shell
# Find "lost" commits using reflog
$ git reflog
abc1234 HEAD@{0}: reset: moving to HEAD~3
def5678 HEAD@{1}: commit: Important work
ghi9012 HEAD@{2}: commit: More important work
jkl3456 HEAD@{3}: commit: Critical fix

# Recover by resetting back
$ git reset --hard def5678

# Or create a branch at the lost commit
$ git branch recovery def5678
```

## Reset vs Revert

```shell
# git reset: REWRITES history (moves branch pointer backward)
# Use for: local/unpushed commits only
$ git reset --hard HEAD~1  # commit is gone from history

# git revert: ADDS a new commit that undoes a previous one
# Use for: shared/pushed commits (safe for team)
$ git revert abc1234  # creates a new "undo" commit
```

## Visual Summary

```
Working Tree    Staging Area    HEAD (Commits)
     |               |               |
     |    --soft      |     ← ← ←    |  (moves HEAD only)
     |               |               |
     |    --mixed     ← ← ← ← ← ←  |  (moves HEAD + resets staging)
     |               |               |
     ← ← --hard ← ← ← ← ← ← ← ←  |  (moves HEAD + resets staging + resets working tree)
```

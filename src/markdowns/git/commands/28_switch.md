# git switch

Switches branches. Modern replacement for `git checkout` (branch operations only).

## Switch to an Existing Branch

```shell
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

$ git switch develop
Switched to branch 'develop'

# Switch to the previous branch
$ git switch -
Switched to branch 'main'
```

## Create and Switch to New Branch

```shell
# Create a new branch and switch to it
$ git switch -c feature/auth
Switched to a new branch 'feature/auth'

# Create from a specific commit
$ git switch -c hotfix/login abc1234
Switched to a new branch 'hotfix/login'

# Create from a tag
$ git switch -c release/v2 v1.5.0

# Force create (overwrite if exists)
$ git switch -C feature/auth
```

## Track a Remote Branch

```shell
# Switch to a remote branch (auto-creates local tracking branch)
$ git switch feature/auth
Branch 'feature/auth' set up to track remote branch 'feature/auth' from 'origin'.
Switched to a new branch 'feature/auth'

# Explicit remote tracking
$ git switch -c feature/auth origin/feature/auth
$ git switch --track origin/feature/auth
```

## Detached HEAD

```shell
# Switch to a specific commit (detached HEAD)
$ git switch --detach abc1234
HEAD is now at abc1234 Some commit message

# Switch to a tag in detached HEAD
$ git switch --detach v1.0.0

# Go back to a branch
$ git switch main
```

## Handle Uncommitted Changes

```shell
# If you have uncommitted changes that conflict:
$ git switch feature/auth
error: Your local changes to the following files would be overwritten by checkout:
        src/app.py
Please commit your changes or stash them before you switch branches.

# Merge uncommitted changes into the target branch
$ git switch -m feature/auth

# Or stash first
$ git stash
$ git switch feature/auth
$ git stash pop
```

## Orphan Branch

```shell
# Create a branch with no history (fresh start)
$ git switch --orphan gh-pages
Switched to a new branch 'gh-pages'
# Working tree is empty — no commits, no parent
```

## git switch vs git checkout

```shell
# These are equivalent:
$ git switch main                     # modern
$ git checkout main                   # old

$ git switch -c feature/auth          # modern
$ git checkout -b feature/auth        # old

$ git switch -                        # modern
$ git checkout -                      # old

$ git switch --detach abc1234         # modern
$ git checkout abc1234                # old

# Key difference: git switch ONLY does branch operations
# git checkout also does file restoration — which is now git restore
```

## Common Workflows

```shell
# Start working on a new feature
$ git switch main
$ git pull
$ git switch -c feature/new-dashboard

# Quick fix on main while working on a feature
$ git stash
$ git switch main
$ git switch -c hotfix/login-fix
# ... make fix ...
$ git switch feature/new-dashboard
$ git stash pop

# Review someone's PR locally
$ git fetch origin
$ git switch pr-branch-name
```

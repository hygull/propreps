# git worktree

Manages multiple working trees attached to the same repository. Work on multiple branches simultaneously without stashing or cloning.

## Basic Usage

```shell
# Create a new worktree for a branch
$ git worktree add ../project-feature feature/auth
Preparing worktree (checking out 'feature/auth')
HEAD is now at abc1234 Add login endpoint

# Now you have two directories:
# /path/to/project         → main branch
# /path/to/project-feature → feature/auth branch
```

## Create Worktree with New Branch

```shell
# Create a new branch and worktree in one step
$ git worktree add -b feature/dashboard ../project-dashboard
Preparing worktree (new branch 'feature/dashboard')
HEAD is now at abc1234 Latest commit on main

# Create from a specific commit
$ git worktree add -b hotfix/login ../hotfix abc1234
```

## Create Worktree for Detached HEAD

```shell
# Worktree at a specific commit (no branch)
$ git worktree add --detach ../project-test abc1234
```

## List Worktrees

```shell
$ git worktree list
/home/user/project           abc1234 [main]
/home/user/project-feature   def5678 [feature/auth]
/home/user/project-dashboard ghi9012 [feature/dashboard]

# Verbose/porcelain output
$ git worktree list --porcelain
worktree /home/user/project
HEAD abc1234567890
branch refs/heads/main

worktree /home/user/project-feature
HEAD def5678901234
branch refs/heads/feature/auth
```

## Remove a Worktree

```shell
# Remove a worktree (directory must be clean)
$ git worktree remove ../project-feature
$ git worktree remove /home/user/project-feature

# Force remove (even with uncommitted changes)
$ git worktree remove --force ../project-feature
```

## Prune Stale Worktrees

```shell
# Clean up worktree metadata for manually deleted directories
$ git worktree prune

# Preview what would be pruned
$ git worktree prune --dry-run

# Verbose output
$ git worktree prune -v
```

## Move a Worktree

```shell
# Move a worktree to a different location
$ git worktree move ../project-feature ../new-location
```

## Lock/Unlock Worktrees

```shell
# Lock a worktree (prevents pruning — useful for removable media)
$ git worktree lock ../project-feature
$ git worktree lock --reason "on USB drive" ../project-feature

# Unlock
$ git worktree unlock ../project-feature
```

## Common Workflows

```shell
# Work on a hotfix while keeping feature work intact
$ git worktree add -b hotfix/critical ../hotfix main
$ cd ../hotfix
# ... fix the bug ...
$ git commit -am "Fix critical bug"
$ git push origin hotfix/critical
$ cd ../project
$ git worktree remove ../hotfix

# Review a PR without leaving your current work
$ git fetch origin
$ git worktree add ../pr-review origin/feature/someone-else
$ cd ../pr-review
# ... review, test ...
$ cd ../project
$ git worktree remove ../pr-review

# Run tests on one branch while coding on another
# Terminal 1:
$ cd /path/to/project          # main branch
$ git worktree add ../test-runner feature/auth
# Terminal 2:
$ cd /path/to/test-runner
$ python -m pytest  # test feature/auth
```

## Important Notes

```shell
# You CANNOT checkout the same branch in two worktrees
$ git worktree add ../second-main main
fatal: 'main' is already checked out at '/home/user/project'

# All worktrees share the same .git data
# Commits made in any worktree are visible to all others

# Worktrees have independent:
#   - Working tree (files)
#   - Staging area (index)
#   - HEAD
# Worktrees share:
#   - Object database
#   - Refs (branches, tags)
#   - Config
#   - Hooks
```

# git merge

Joins two or more development histories together.

## Basic Usage

```shell
# Merge a branch into the current branch
$ git checkout main
$ git merge feature/auth
Merge made by the 'ort' strategy.
 src/auth.py   | 45 +++++++++++++++++++++++++++++++++++++++++++++
 src/config.py |  3 +++
 2 files changed, 48 insertions(+)
 create mode 100644 src/auth.py
```

## Fast-Forward Merge

```shell
# When current branch is a direct ancestor, git just moves the pointer
$ git merge feature/auth
Updating abc1234..def5678
Fast-forward
 src/auth.py | 45 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 45 insertions(+)

# Force a merge commit even when fast-forward is possible
$ git merge --no-ff feature/auth
Merge made by the 'ort' strategy.

# Only allow fast-forward (abort if not possible)
$ git merge --ff-only feature/auth
fatal: Not possible to fast-forward, aborting.
```

## Merge with a Custom Message

```shell
$ git merge feature/auth -m "Merge feature/auth: add JWT authentication"
Merge made by the 'ort' strategy.
```

## Handling Merge Conflicts

```shell
$ git merge feature/auth
Auto-merging src/app.py
CONFLICT (content): Merge conflict in src/app.py
Automatic merge failed; fix conflicts and then commit the result.

# See which files have conflicts
$ git status
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   src/app.py

# The conflict markers in the file look like:
# <<<<<<< HEAD
# current branch content
# =======
# incoming branch content
# >>>>>>> feature/auth

# After manually fixing conflicts:
$ git add src/app.py
$ git commit
# (editor opens with pre-filled merge commit message)

# Or use a merge tool
$ git mergetool
```

## Abort a Merge

```shell
# Cancel an in-progress merge (go back to pre-merge state)
$ git merge --abort

# If merge is already committed, revert it
$ git revert -m 1 HEAD
```

## Squash Merge

```shell
# Combine all commits from a branch into one (no merge commit)
$ git merge --squash feature/auth
Squashing commit -- not updating HEAD
Automatic merge went well; stopped before committing as requested

$ git commit -m "Add user authentication (squashed from feature/auth)"
[main abc1234] Add user authentication (squashed from feature/auth)
```

## Merge Strategies

```shell
# Use a specific merge strategy
$ git merge -s ort feature/auth           # default strategy (replaces recursive)
$ git merge -s recursive feature/auth      # older default
$ git merge -s ours feature/auth           # keep current branch, ignore incoming
$ git merge -s subtree feature/auth        # for subtree merges

# Strategy options
$ git merge -X theirs feature/auth    # auto-resolve conflicts favoring incoming
$ git merge -X ours feature/auth      # auto-resolve conflicts favoring current
$ git merge -X patience feature/auth  # patience diff algorithm
```

## Merge Without Committing

```shell
# Merge but don't auto-commit (lets you review/modify before committing)
$ git merge --no-commit feature/auth
Automatic merge went well; stopped before committing as requested

$ git diff --staged  # review what's being merged
$ git commit -m "Merge feature/auth with manual adjustments"
```

## Check Before Merging

```shell
# Preview what would be merged
$ git log main..feature/auth --oneline
abc1234 Add login endpoint
def5678 Add auth middleware
ghi9012 Add JWT utilities

# See the actual diff
$ git diff main...feature/auth

# Check for conflicts without merging (dry run)
$ git merge --no-commit --no-ff feature/auth
$ git merge --abort  # undo the test
```

## Octopus Merge (Multiple Branches)

```shell
# Merge multiple branches at once
$ git merge feature/auth feature/dashboard feature/settings
```

## Continue After Conflict Resolution

```shell
# After resolving conflicts
$ git add .
$ git merge --continue
# (same as git commit during a merge)
```

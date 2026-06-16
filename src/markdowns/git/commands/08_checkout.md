# git checkout

Switches branches or restores working tree files. (For branch switching, `git switch` is the modern alternative.)

## Switch Branches

```shell
# Switch to an existing branch
$ git checkout develop
Switched to branch 'develop'

# Switch to the previous branch
$ git checkout -
Switched to branch 'main'

# Create and switch to a new branch
$ git checkout -b feature/auth
Switched to a new branch 'feature/auth'

# Create branch from a specific commit/tag and switch to it
$ git checkout -b hotfix/login abc1234
$ git checkout -b release/v2 v1.5.0
```

## Restore Files

```shell
# Discard changes in a file (restore from staging area)
$ git checkout -- app.py

# Restore a file from a specific commit
$ git checkout abc1234 -- src/config.py

# Restore all files in a directory
$ git checkout -- src/

# Restore a deleted file
$ git checkout HEAD -- deleted-file.py

# Restore a file from another branch
$ git checkout main -- src/utils.py
```

## Detached HEAD

```shell
# Checkout a specific commit (detached HEAD state)
$ git checkout abc1234
Note: switching to 'abc1234'.
You are in 'detached HEAD' state.

# Checkout a tag
$ git checkout v1.0.0
HEAD is now at abc1234 Release v1.0.0

# Create a branch from detached HEAD to keep changes
$ git checkout -b save-my-work

# Go back to a branch
$ git checkout main
```

## Checkout Remote Branch

```shell
# Checkout a remote branch (creates local tracking branch)
$ git checkout feature/auth
Branch 'feature/auth' set up to track remote branch 'feature/auth' from 'origin'.
Switched to a new branch 'feature/auth'

# Explicit remote tracking
$ git checkout -b feature/auth origin/feature/auth
$ git checkout --track origin/feature/auth
```

## Conflict Resolution

```shell
# During a merge conflict, pick one side
$ git checkout --ours conflicted-file.py    # keep current branch's version
$ git checkout --theirs conflicted-file.py  # keep incoming branch's version

# After choosing, stage the resolved file
$ git add conflicted-file.py
```

## Checkout with Merge

```shell
# Switch branch, carrying uncommitted changes along (merge them in)
$ git checkout -m other-branch

# Force checkout (DISCARD all local changes)
$ git checkout -f main
$ git checkout --force main
```

## Patch Mode

```shell
# Interactively discard selected hunks from working tree
$ git checkout -p
$ git checkout --patch
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,5 +1,6 @@
-    print("Hello")
+    print("Hello, World!")
Discard this hunk from worktree [y,n,q,a,d,s,e,?]?
```

## Modern Alternatives (git switch / git restore)

```shell
# git switch — for branch operations
$ git switch main                    # same as: git checkout main
$ git switch -c feature/auth         # same as: git checkout -b feature/auth
$ git switch -                       # same as: git checkout -
$ git switch --detach abc1234        # same as: git checkout abc1234

# git restore — for file operations
$ git restore app.py                 # same as: git checkout -- app.py
$ git restore --staged app.py        # same as: git reset HEAD app.py
$ git restore --source=abc1234 app.py  # same as: git checkout abc1234 -- app.py
```

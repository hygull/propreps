# git restore

Restores working tree files and/or the staging area. Modern replacement for parts of `git checkout`.

## Discard Working Tree Changes

```shell
# Restore a file to its staged version (discard unstaged edits)
$ git restore src/app.py

# Restore multiple files
$ git restore src/app.py src/utils.py

# Restore all files in current directory
$ git restore .

# Restore all files in a specific directory
$ git restore src/
```

## Unstage Files

```shell
# Unstage a file (move from staging area back to working tree)
$ git restore --staged src/app.py

# Unstage everything
$ git restore --staged .

# Equivalent old syntax
$ git reset HEAD src/app.py
```

## Restore from a Specific Source

```shell
# Restore a file from a specific commit
$ git restore --source=abc1234 src/app.py

# Restore from HEAD (default)
$ git restore --source=HEAD src/app.py

# Restore from another branch
$ git restore --source=feature/auth src/utils.py

# Restore from a tag
$ git restore --source=v1.0.0 src/config.py
```

## Restore Both Staged and Working Tree

```shell
# Restore a file completely (unstage AND discard changes)
$ git restore --staged --worktree src/app.py
$ git restore -SW src/app.py

# Restore everything to match HEAD
$ git restore --staged --worktree .
```

## Restore Deleted Files

```shell
# Bring back a deleted file
$ git restore deleted-file.py

# Bring back from a specific commit
$ git restore --source=abc1234 deleted-file.py

# Restore a file that was deleted and staged
$ git restore --staged deleted-file.py
$ git restore deleted-file.py
```

## Patch Mode (Selective Restore)

```shell
# Interactively choose which hunks to restore
$ git restore -p src/app.py
$ git restore --patch src/app.py
diff --git a/src/app.py b/src/app.py
--- a/src/app.py
+++ b/src/app.py
@@ -1,5 +1,6 @@
-    print("Hello")
+    print("Hello, World!")
Discard this hunk from worktree [y,n,q,a,d,s,e,?]?

# Interactively unstage hunks
$ git restore --staged -p src/app.py
```

## Restore with Pathspec

```shell
# Restore all Python files
$ git restore "*.py"

# Restore everything except one file
$ git restore . -- ":!src/keep-this.py"
```

## git restore vs git checkout

```shell
# These are equivalent:
$ git restore src/app.py              # modern
$ git checkout -- src/app.py          # old

$ git restore --staged src/app.py     # modern
$ git reset HEAD src/app.py           # old

$ git restore --source=abc1234 file   # modern
$ git checkout abc1234 -- file        # old
```

## Common Workflows

```shell
# "Oops, I messed up this file" — discard changes
$ git restore src/app.py

# "I accidentally staged this" — unstage it
$ git restore --staged .env

# "I need the old version of this file" — restore from history
$ git restore --source=HEAD~5 src/config.py

# "Reset everything to last commit" — nuclear option
$ git restore --staged --worktree .
```

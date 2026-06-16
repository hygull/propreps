# git rebase

Reapplies commits on top of another base tip. Rewrites history for a cleaner commit graph.

## Basic Usage

```shell
# Rebase current branch onto main
$ git checkout feature/auth
$ git rebase main
Successfully rebased and updated refs/heads/feature/auth.

# Before rebase:
#   A---B---C  (main)
#        \
#         D---E  (feature/auth)
#
# After rebase:
#   A---B---C  (main)
#             \
#              D'---E'  (feature/auth)
```

## Interactive Rebase

```shell
# Rebase last 3 commits interactively
$ git rebase -i HEAD~3

# Editor opens with:
pick abc1234 Add auth middleware
pick def5678 Fix typo in middleware
pick ghi9012 Add login endpoint

# Commands:
# pick   (p) — use commit as-is
# reword (r) — use commit but edit the message
# edit   (e) — pause at this commit for amending
# squash (s) — meld into previous commit (combine messages)
# fixup  (f) — meld into previous commit (discard this message)
# drop   (d) — remove this commit
# exec   (x) — run a shell command

# Example: squash the typo fix into the first commit
pick abc1234 Add auth middleware
fixup def5678 Fix typo in middleware
pick ghi9012 Add login endpoint
# Save and close editor
Successfully rebased and updated refs/heads/feature/auth.
```

## Rebase onto a Specific Commit

```shell
# Rebase onto a specific commit
$ git rebase abc1234

# Rebase onto a tag
$ git rebase v1.5.0

# Rebase a range of commits onto another branch
$ git rebase --onto main feature/base feature/auth
# Takes commits from feature/base..feature/auth and replays onto main
```

## Handling Conflicts

```shell
$ git rebase main
CONFLICT (content): Merge conflict in src/app.py
error: could not apply abc1234... Add auth middleware
hint: Resolve all conflicts manually, then run "git rebase --continue".

# Fix the conflict in the file, then:
$ git add src/app.py
$ git rebase --continue

# Or skip this commit entirely
$ git rebase --skip

# Or abort and go back to pre-rebase state
$ git rebase --abort
```

## Autosquash

```shell
# Create fixup commits during development
$ git commit --fixup=abc1234
[feature/auth def5678] fixup! Add auth middleware

# Later, auto-squash them during rebase
$ git rebase -i --autosquash main
# The fixup commits are automatically reordered and marked as fixup

# Enable autosquash by default
$ git config --global rebase.autoSquash true
```

## Preserve Merge Commits

```shell
# Rebase while keeping merge commits in history
$ git rebase --rebase-merges main
$ git rebase -r main
```

## Exec (Run Commands During Rebase)

```shell
# Run tests after each rebased commit
$ git rebase -i HEAD~5 --exec "python -m pytest"

# Or add exec lines in the interactive editor:
pick abc1234 Add auth
exec python -m pytest
pick def5678 Add login
exec python -m pytest
```

## Autostash

```shell
# Automatically stash and pop uncommitted changes around rebase
$ git rebase main --autostash
Created autostash: abc1234
Successfully rebased and updated refs/heads/feature/auth.
Applied autostash.

# Enable autostash by default
$ git config --global rebase.autoStash true
```

## Rebase vs Merge

```shell
# Merge: preserves history as it happened (merge commits)
$ git merge feature/auth
#   A---B---C---M  (main)
#        \     /
#         D---E  (feature/auth)

# Rebase: creates linear history (cleaner, but rewrites commits)
$ git rebase main
#   A---B---C---D'---E'  (feature/auth → main)

# Golden rule: NEVER rebase commits that have been pushed/shared
# Rebase is for cleaning up LOCAL commits before pushing
```

## Common Workflow

```shell
# Update feature branch with latest main (rebase approach)
$ git checkout feature/auth
$ git fetch origin
$ git rebase origin/main

# Clean up commits before merging
$ git rebase -i main
# Squash, reword, reorder as needed

# Then merge into main
$ git checkout main
$ git merge feature/auth
```

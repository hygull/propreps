# git range-diff

Compares two commit ranges (e.g., two versions of a branch). Shows what changed between patch series — essential for reviewing rebased or force-pushed branches.

## Basic Usage

```shell
# Compare two versions of a branch (three-dot syntax)
$ git range-diff main..feature/auth@{1} main..feature/auth
# Compares the old version of feature/auth against the new version
# relative to main

# Output shows paired commits:
1:  abc1234 = def5678 Add auth middleware
2:  ghi9012 ! jkl3456 Fix login validation
    @@ Commit message
         Fix login validation
    +    Also handle edge case for empty passwords
    @@  src/auth.py
         def validate(password):
    -        return len(password) > 0
    +        return password and len(password) >= 8

3:  mno7890 < -       Remove debug logging (dropped)
-:  ------- > pqr1234 Add rate limiting (new)

# Legend:
#  = : commit is identical (unchanged)
#  ! : commit was modified (diff shown)
#  < : commit was dropped (only in old range)
#  > : commit was added (only in new range)
```

## Three Arguments Syntax

```shell
# range-diff <base> <old-tip> <new-tip>
$ git range-diff main feature/auth@{1} feature/auth

# Equivalent to the two-range syntax:
$ git range-diff main..feature/auth@{1} main..feature/auth

# Compare between two different bases
$ git range-diff old-base old-tip new-base new-tip
```

## Review a Force-Push

```shell
# After someone force-pushes a PR branch:
$ git fetch origin
$ git range-diff origin/main..origin/feature/auth@{1} origin/main..origin/feature/auth

# Using reflog to find the old version
$ git reflog origin/feature/auth
abc1234 origin/feature/auth@{0}: fetch: forced-update
def5678 origin/feature/auth@{1}: fetch

$ git range-diff origin/main..def5678 origin/main..abc1234
```

## Compare Patch Versions

```shell
# Compare v1 and v2 of a patch series (from format-patch)
$ git range-diff main..feature-v1 main..feature-v2

# Or using tags
$ git range-diff main..review/v1 main..review/v2
```

## Creation-Factor

```shell
# Control how aggressively commits are paired
# Range: 0 (only exact matches) to 100 (pair everything)
# Default: 60

# More aggressive pairing (finds matches even if heavily modified)
$ git range-diff --creation-factor=80 main..old main..new

# Stricter pairing (only pair near-identical commits)
$ git range-diff --creation-factor=30 main..old main..new
```

## Output Formatting

```shell
# No color (for piping)
$ git range-diff --no-color main..old main..new

# Stat only (no full diffs)
$ git range-diff --stat main..old main..new
1:  abc1234 = def5678 Add auth middleware
2:  ghi9012 ! jkl3456 Fix login validation
     src/auth.py | 2 +-
     1 file changed, 1 insertion(+), 1 deletion(-)

# Show only changed commits (skip identical ones)
$ git range-diff main..old main..new | grep -v "^[0-9]*:.*=$"
```

## Context Lines

```shell
# Show more context around changes within the commit diffs
$ git range-diff -U5 main..old main..new

# No context (just changed lines)
$ git range-diff -U0 main..old main..new
```

## Common Workflows

```shell
# Review what changed after a rebase
$ git range-diff main..feature@{1} main..feature
# Shows how each commit changed during the rebase

# Review a colleague's PR update
# Before: they had 3 commits. After force-push: still 3 but modified.
$ git fetch origin
$ git range-diff origin/main..origin/feature@{1} origin/main..origin/feature

# Compare your local branch before/after interactive rebase
$ git tag pre-rebase    # mark current state
$ git rebase -i main    # do the rebase
$ git range-diff main..pre-rebase main..HEAD
$ git tag -d pre-rebase # clean up

# Verify a cherry-pick series matches the original
$ git range-diff main..feature/auth release/v1.x~3..release/v1.x

# Review changes between PR review rounds
# Round 1: reviewer sees commits A, B, C
# Round 2: author rebased, now A', B', C', D
$ git range-diff main..round1-tag main..feature/auth
# Clearly shows what the author changed between review rounds
```

## Understanding the Output

```shell
# Full output explanation:
$ git range-diff main..old main..new

# Line 1: pairing summary
1:  abc1234 = def5678 Add auth middleware
#   │       │   │       └── commit subject
#   │       │   └────────── new commit hash
#   │       └────────────── status (= identical, ! modified, < dropped, > added)
#   └────────────────────── old commit hash

# For modified (!) commits, a nested diff is shown:
2:  ghi9012 ! jkl3456 Fix login validation
    @@ Commit message        ← changes in the commit MESSAGE
    @@ src/auth.py           ← changes in the commit DIFF
    @@ src/auth.py: def validate
    -        old line in old version's diff
    +        new line in new version's diff

# The outer diff compares DIFFS — it's a "diff of diffs"
# Green +/- in the inner diff = what was added/removed in the commit
# Outer context shows what stayed the same between versions
```

## range-diff vs diff

```shell
# git diff: compares file contents between two points
$ git diff old-branch new-branch
# Shows the total difference in files

# git range-diff: compares commit SERIES
$ git range-diff main..old-branch main..new-branch
# Shows how individual commits evolved (paired by similarity)
# Tells you: which commits changed, which were added/dropped, and how
```

# git cherry-pick

Applies the changes introduced by existing commits onto the current branch.

## Basic Usage

```shell
# Apply a single commit to the current branch
$ git cherry-pick abc1234
[main def5678] Add login validation
 Date: Mon Jun 16 10:00:00 2025 +0530
 1 file changed, 10 insertions(+)

# Cherry-pick multiple commits
$ git cherry-pick abc1234 def5678 ghi9012
```

## Cherry-Pick a Range

```shell
# Apply a range of commits (exclusive start, inclusive end)
$ git cherry-pick abc1234..ghi9012
# Applies def5678 and ghi9012 (NOT abc1234)

# Include the start commit too
$ git cherry-pick abc1234^..ghi9012
# Applies abc1234, def5678, and ghi9012
```

## Without Committing

```shell
# Apply changes but don't auto-commit (stage them only)
$ git cherry-pick --no-commit abc1234
$ git cherry-pick -n abc1234

# Useful for combining multiple cherry-picks into one commit
$ git cherry-pick -n abc1234
$ git cherry-pick -n def5678
$ git commit -m "Combined: login validation + error handling"
```

## Handling Conflicts

```shell
$ git cherry-pick abc1234
CONFLICT (content): Merge conflict in src/app.py
error: could not apply abc1234... Add login validation

# Fix conflicts in the file, then:
$ git add src/app.py
$ git cherry-pick --continue

# Or skip this commit
$ git cherry-pick --skip

# Or abort entirely (go back to pre-cherry-pick state)
$ git cherry-pick --abort
```

## Preserve Original Author

```shell
# By default, cherry-pick preserves the original author
$ git cherry-pick abc1234
$ git log -1
Author: Original Author <original@example.com>
    Add login validation

# Reset the author to yourself
$ git cherry-pick abc1234
$ git commit --amend --reset-author
```

## Edit Commit Message

```shell
# Edit the commit message during cherry-pick
$ git cherry-pick -e abc1234
$ git cherry-pick --edit abc1234
# Editor opens with the original message — modify as needed
```

## Append Cherry-Pick Info

```shell
# Add "(cherry picked from commit ...)" to the message
$ git cherry-pick -x abc1234

$ git log -1
    Add login validation

    (cherry picked from commit abc1234567890abcdef)
```

## Cherry-Pick from Another Branch

```shell
# Pick a commit from feature branch into main
$ git checkout main
$ git cherry-pick feature/auth~2    # 2nd-to-last commit on feature/auth

# Pick the tip of another branch
$ git cherry-pick feature/hotfix

# Pick from a remote branch
$ git fetch origin
$ git cherry-pick origin/feature/fix
```

## Cherry-Pick Merge Commits

```shell
# Merge commits have multiple parents — you must specify which parent
# -m 1: use first parent (usually the branch being merged INTO)
$ git cherry-pick -m 1 abc1234

# -m 2: use second parent (the branch being merged)
$ git cherry-pick -m 2 abc1234
```

## Common Workflows

```shell
# Hotfix: apply a fix from develop to main
$ git checkout main
$ git cherry-pick abc1234
$ git push origin main

# Backport: apply a fix to an older release branch
$ git checkout release/v1.x
$ git cherry-pick abc1234
$ git push origin release/v1.x

# Selective merge: pick only some commits from a feature branch
$ git log feature/auth --oneline
abc1234 Add login (want this)
def5678 WIP debug code (skip this)
ghi9012 Add logout (want this)

$ git checkout main
$ git cherry-pick abc1234 ghi9012
```

# git branch

Lists, creates, renames, and deletes branches.

## List Branches

```shell
# List local branches (* marks the current branch)
$ git branch
  develop
  feature/auth
* main

# List remote branches
$ git branch -r
  origin/develop
  origin/feature/auth
  origin/main

# List all branches (local + remote)
$ git branch -a
  develop
  feature/auth
* main
  remotes/origin/develop
  remotes/origin/feature/auth
  remotes/origin/main

# List with last commit info
$ git branch -v
  develop      abc1234 Update config
  feature/auth def5678 Add login
* main         ghi9012 Merge feature/auth

# List with upstream tracking info
$ git branch -vv
  develop      abc1234 [origin/develop] Update config
  feature/auth def5678 [origin/feature/auth: ahead 2] Add login
* main         ghi9012 [origin/main] Merge feature/auth
```

## Create Branches

```shell
# Create a new branch (does NOT switch to it)
$ git branch feature/dashboard

# Create and switch to a new branch
$ git checkout -b feature/dashboard
Switched to a new branch 'feature/dashboard'

# Modern way: create and switch
$ git switch -c feature/dashboard
Switched to a new branch 'feature/dashboard'

# Create a branch from a specific commit
$ git branch hotfix/login abc1234

# Create a branch from a tag
$ git branch release/v2 v1.5.0

# Create a branch from a remote branch
$ git branch feature/auth origin/feature/auth

# Create and track a remote branch
$ git checkout -b feature/auth origin/feature/auth
$ git switch -c feature/auth origin/feature/auth
```

## Rename Branches

```shell
# Rename the current branch
$ git branch -m new-name
$ git branch --move new-name

# Rename a specific branch
$ git branch -m old-name new-name

# Force rename (even if new-name already exists)
$ git branch -M new-name

# After renaming, update the remote
$ git push origin -u new-name
$ git push origin --delete old-name
```

## Delete Branches

```shell
# Delete a merged branch
$ git branch -d feature/auth
Deleted branch feature/auth (was def5678).

# Force delete an unmerged branch
$ git branch -D feature/experimental
Deleted branch feature/experimental (was abc1234).

# Delete a remote branch
$ git push origin --delete feature/auth
$ git push origin :feature/auth

# Clean up stale remote-tracking branches
$ git fetch --prune
$ git remote prune origin
```

## Filtering Branches

```shell
# Branches merged into current branch
$ git branch --merged
  feature/auth
* main

# Branches NOT merged into current branch
$ git branch --no-merged
  feature/dashboard
  feature/experimental

# Branches merged into a specific branch
$ git branch --merged main

# Branches containing a specific commit
$ git branch --contains abc1234
  feature/auth
  main

# Filter by pattern
$ git branch --list "feature/*"
  feature/auth
  feature/dashboard

# Sort by committer date
$ git branch --sort=-committerdate
* main
  feature/dashboard
  feature/auth
  develop
```

## Set Upstream Tracking

```shell
# Set upstream for current branch
$ git branch -u origin/main
$ git branch --set-upstream-to=origin/main

# Set upstream for a specific branch
$ git branch -u origin/develop develop

# Remove upstream tracking
$ git branch --unset-upstream

# Push and set upstream in one command
$ git push -u origin feature/auth
```

## Copy a Branch

```shell
# Copy current branch to a new name
$ git branch -c copy-of-main

# Copy a specific branch
$ git branch -c feature/auth feature/auth-backup

# Force copy (overwrite if exists)
$ git branch -C feature/auth feature/auth-backup
```

## Show Branch Details

```shell
# Show which commit each branch points to
$ git branch -v --format="%(refname:short) %(objectname:short) %(subject)"
develop abc1234 Update config
feature/auth def5678 Add login endpoint
main ghi9012 Merge feature/auth

# Show the merge base between two branches
$ git merge-base main feature/auth
jkl3456abcdef1234567890
```

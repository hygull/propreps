# git fetch

Downloads objects and refs from a remote repository without merging.

## Basic Usage

```shell
# Fetch from the default remote (origin)
$ git fetch
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 5), reused 10 (delta 5)
Unpacking objects: 100% (10/10), done.
From github.com:user/repo
   abc1234..def5678  main       -> origin/main
 * [new branch]      feature/x  -> origin/feature/x

# Fetch from a specific remote
$ git fetch upstream
```

## Fetch Specific Branch

```shell
# Fetch only one branch
$ git fetch origin main

# Fetch a specific branch to a local ref
$ git fetch origin feature/auth:refs/remotes/origin/feature/auth
```

## Fetch All Remotes

```shell
$ git fetch --all
Fetching origin
Fetching upstream
```

## Fetch with Prune

```shell
# Remove remote-tracking branches that no longer exist on the remote
$ git fetch --prune
$ git fetch -p
From github.com:user/repo
 - [deleted]         (none)     -> origin/feature/old-branch
   abc1234..def5678  main       -> origin/main

# Prune tags too
$ git fetch --prune --prune-tags
```

## Fetch Tags

```shell
# Fetch all tags
$ git fetch --tags
From github.com:user/repo
 * [new tag]         v1.0.0     -> v1.0.0
 * [new tag]         v1.1.0     -> v1.1.0

# Fetch without auto-fetching tags
$ git fetch --no-tags
```

## Shallow Fetch

```shell
# Fetch only recent history
$ git fetch --depth=1

# Deepen a shallow clone
$ git fetch --deepen=10

# Fetch full history for a shallow clone
$ git fetch --unshallow
```

## Dry Run

```shell
# See what would be fetched without actually fetching
$ git fetch --dry-run
From github.com:user/repo
   abc1234..def5678  main       -> origin/main
```

## After Fetching

```shell
# See what changed on the remote
$ git log HEAD..origin/main --oneline
def5678 Latest remote commit
ghi9012 Another remote commit

# See the diff
$ git diff HEAD origin/main

# Merge the fetched changes
$ git merge origin/main

# Or rebase onto the fetched changes
$ git rebase origin/main
```

## Fetch vs Pull

```shell
# git fetch: downloads changes, does NOT modify working tree
$ git fetch origin
$ git log origin/main  # inspect remote changes
$ git merge origin/main  # manually merge when ready

# git pull: fetch + merge in one step
$ git pull origin main
# Equivalent to:
#   git fetch origin
#   git merge origin/main
```

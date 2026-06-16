# git pull

Fetches and integrates changes from a remote branch (fetch + merge).

## Basic Usage

```shell
# Pull from tracking upstream branch
$ git pull
remote: Enumerating objects: 5, done.
remote: Total 3 (delta 1), reused 3 (delta 1)
Unpacking objects: 100% (3/3), done.
From github.com:user/repo
   abc1234..def5678  main       -> origin/main
Updating abc1234..def5678
Fast-forward
 src/app.py | 5 +++++
 1 file changed, 5 insertions(+)

# Pull from a specific remote and branch
$ git pull origin main
$ git pull upstream develop
```

## Pull with Rebase

```shell
# Rebase instead of merge (cleaner linear history)
$ git pull --rebase
$ git pull -r

# Pull with rebase from a specific branch
$ git pull --rebase origin main

# Set rebase as default for pulls
$ git config --global pull.rebase true

# Or per-branch
$ git config branch.main.rebase true
```

## Fast-Forward Only

```shell
# Only pull if it can be fast-forwarded (no merge commit)
$ git pull --ff-only

# Fails if local has diverged:
$ git pull --ff-only
fatal: Not possible to fast-forward, aborting.

# Set as default
$ git config --global pull.ff only
```

## Pull with Autostash

```shell
# Automatically stash and pop uncommitted changes around pull
$ git pull --autostash
Created autostash: abc1234
Updating def5678..ghi9012
Fast-forward
Applied autostash.

# Set as default
$ git config --global rebase.autoStash true
```

## Handling Conflicts

```shell
$ git pull origin main
Auto-merging src/app.py
CONFLICT (content): Merge conflict in src/app.py
Automatic merge failed; fix conflicts and then commit the result.

# Fix the conflicts, then:
$ git add src/app.py
$ git commit

# Or abort the merge
$ git merge --abort

# If pulling with rebase and conflicts occur:
$ git add src/app.py
$ git rebase --continue
# Or:
$ git rebase --abort
```

## Pull Specific Branch

```shell
# Pull a remote branch into the current branch
$ git pull origin feature/auth

# Pull and create a merge commit even if fast-forward is possible
$ git pull --no-ff origin main
```

## Pull All Remotes

```shell
# Fetch all remotes, then merge current tracking branch
$ git pull --all
Fetching origin
Fetching upstream
```

## Verbose Pull

```shell
$ git pull -v
From github.com:user/repo
 = [up to date]      main       -> origin/main
Already up to date.
```

## Common Workflows

```shell
# Safe pull workflow (inspect before merging)
$ git fetch origin
$ git log HEAD..origin/main --oneline
$ git diff HEAD origin/main --stat
$ git pull origin main

# Pull with rebase workflow (keeps history clean)
$ git pull --rebase origin main
# If conflicts arise during rebase:
$ git add .
$ git rebase --continue
```

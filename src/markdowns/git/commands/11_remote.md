# git remote

Manages connections to remote repositories.

## List Remotes

```shell
# List remote names
$ git remote
origin
upstream

# List with URLs
$ git remote -v
origin    git@github.com:user/repo.git (fetch)
origin    git@github.com:user/repo.git (push)
upstream  https://github.com/original/repo.git (fetch)
upstream  https://github.com/original/repo.git (push)
```

## Add a Remote

```shell
# Add a new remote
$ git remote add origin git@github.com:user/repo.git

# Add an upstream remote (for forks)
$ git remote add upstream https://github.com/original/repo.git

# Add with a custom name
$ git remote add staging git@deploy-server:/srv/git/app.git
```

## Remove a Remote

```shell
$ git remote remove upstream
$ git remote rm upstream
```

## Rename a Remote

```shell
$ git remote rename origin github
$ git remote -v
github  git@github.com:user/repo.git (fetch)
github  git@github.com:user/repo.git (push)
```

## Change Remote URL

```shell
# Switch from HTTPS to SSH
$ git remote set-url origin git@github.com:user/repo.git

# Switch from SSH to HTTPS
$ git remote set-url origin https://github.com/user/repo.git

# Verify the change
$ git remote -v
origin  git@github.com:user/repo.git (fetch)
origin  git@github.com:user/repo.git (push)

# Set different push and fetch URLs
$ git remote set-url --push origin git@github.com:user/repo.git
```

## Show Remote Details

```shell
$ git remote show origin
* remote origin
  Fetch URL: git@github.com:user/repo.git
  Push  URL: git@github.com:user/repo.git
  HEAD branch: main
  Remote branches:
    develop      tracked
    feature/auth tracked
    main         tracked
  Local branches configured for 'git pull':
    develop merges with remote develop
    main    merges with remote main
  Local refs configured for 'git push':
    develop pushes to develop (up to date)
    main    pushes to main    (up to date)
```

## Prune Stale References

```shell
# Remove remote-tracking branches that no longer exist on the remote
$ git remote prune origin
Pruning origin
 * [pruned] origin/feature/old-branch
 * [pruned] origin/feature/deleted-branch

# Prune during fetch
$ git fetch --prune
$ git fetch -p
```

## Multiple Remotes Workflow (Fork)

```shell
# Fork workflow setup
$ git clone git@github.com:user/forked-repo.git
$ cd forked-repo
$ git remote add upstream https://github.com/original/repo.git

$ git remote -v
origin    git@github.com:user/forked-repo.git (fetch)
origin    git@github.com:user/forked-repo.git (push)
upstream  https://github.com/original/repo.git (fetch)
upstream  https://github.com/original/repo.git (push)

# Sync fork with upstream
$ git fetch upstream
$ git checkout main
$ git merge upstream/main
$ git push origin main
```

## Push to Multiple Remotes

```shell
# Add a second push URL to an existing remote
$ git remote set-url --add --push origin git@github.com:user/repo.git
$ git remote set-url --add --push origin git@gitlab.com:user/repo.git

# Now git push origin pushes to both GitHub and GitLab
$ git remote -v
origin  git@github.com:user/repo.git (fetch)
origin  git@github.com:user/repo.git (push)
origin  git@gitlab.com:user/repo.git (push)
```

# git push

Updates remote refs along with associated objects.

## Basic Usage

```shell
# Push the current branch to its upstream
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.20 KiB | 1.20 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To github.com:user/repo.git
   abc1234..def5678  main -> main

# Push to a specific remote and branch
$ git push origin main
$ git push origin feature/auth
```

## Set Upstream and Push

```shell
# Push and set upstream tracking (first push of a new branch)
$ git push -u origin feature/auth
$ git push --set-upstream origin feature/auth
Branch 'feature/auth' set up to track remote branch 'feature/auth' from 'origin'.

# After setting upstream, just use git push
$ git push
```

## Push All Branches

```shell
# Push all local branches
$ git push --all origin

# Push all tags
$ git push --tags origin

# Push a specific tag
$ git push origin v1.0.0
```

## Force Push

```shell
# Force push (DANGEROUS — overwrites remote history)
$ git push --force origin feature/auth
$ git push -f origin feature/auth

# Force push with lease (safer — fails if remote has new commits you haven't seen)
$ git push --force-with-lease origin feature/auth

# Force push with lease and expected value
$ git push --force-with-lease=feature/auth:abc1234 origin feature/auth
```

## Delete Remote Branch

```shell
# Delete a remote branch
$ git push origin --delete feature/auth
To github.com:user/repo.git
 - [deleted]         feature/auth

# Alternative syntax
$ git push origin :feature/auth
```

## Push Tags

```shell
# Push a single tag
$ git push origin v1.0.0

# Push all tags
$ git push origin --tags

# Push annotated tags only (not lightweight tags)
$ git push origin --follow-tags

# Delete a remote tag
$ git push origin --delete v1.0.0
$ git push origin :refs/tags/v1.0.0
```

## Dry Run

```shell
# See what would be pushed without actually pushing
$ git push --dry-run origin main
To github.com:user/repo.git
   abc1234..def5678  main -> main
```

## Push to Multiple Remotes

```shell
# Push to a specific remote
$ git push origin main
$ git push upstream main

# Push to all remotes at once (using a script)
$ git remote | xargs -I {} git push {} main
```

## Push Specific Commits

```shell
# Push up to a specific commit (not everything on the branch)
$ git push origin abc1234:main

# Push a local branch to a differently named remote branch
$ git push origin local-branch:remote-branch
```

## Push Configuration

```shell
# Set default push behavior
$ git config --global push.default current    # push current branch to same-named remote
$ git config --global push.default simple     # default — push to upstream if names match
$ git config --global push.default matching   # push all matching branches

# Auto-setup remote tracking on push
$ git config --global push.autoSetupRemote true
# Now "git push" on a new branch auto-creates the upstream
```

## Common Scenarios

```shell
# Rejected push (remote has new commits)
$ git push origin main
To github.com:user/repo.git
 ! [rejected]        main -> main (non-fast-forward)
hint: Updates were rejected because the tip of your current branch is behind

# Solution: pull first, then push
$ git pull --rebase origin main
$ git push origin main

# Push after amending a commit (force push needed)
$ git commit --amend -m "Fixed message"
$ git push --force-with-lease origin feature/auth
```

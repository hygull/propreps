# git clone

Clones an existing repository into a new directory.

## Basic Usage

```shell
# Clone via HTTPS
$ git clone https://github.com/user/repo.git
Cloning into 'repo'...
remote: Enumerating objects: 150, done.
remote: Total 150 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (150/150), 45.00 KiB | 1.50 MiB/s, done.

# Clone via SSH
$ git clone git@github.com:user/repo.git

# Clone into a specific directory name
$ git clone https://github.com/user/repo.git my-local-name
Cloning into 'my-local-name'...
```

## Shallow Clone

```shell
# Clone only the latest commit (faster, smaller)
$ git clone --depth 1 https://github.com/torvalds/linux.git
Cloning into 'linux'...

# Clone last N commits
$ git clone --depth 5 https://github.com/user/repo.git

# Later, fetch the full history if needed
$ git fetch --unshallow
```

## Clone a Specific Branch

```shell
# Clone and checkout a specific branch
$ git clone -b develop https://github.com/user/repo.git
Cloning into 'repo'...
$ cd repo && git branch
* develop

# Clone only a single branch (no other remote-tracking branches)
$ git clone --single-branch -b feature/auth https://github.com/user/repo.git
```

## Bare Clone

```shell
# Clone as a bare repository (no working tree)
$ git clone --bare https://github.com/user/repo.git
Cloning into bare repository 'repo.git'...

# Clone as a mirror (bare + all refs including hidden ones)
$ git clone --mirror https://github.com/user/repo.git
```

## Partial Clone (Large Repos)

```shell
# Clone without downloading blobs (files) — fetch them on demand
$ git clone --filter=blob:none https://github.com/user/large-repo.git

# Clone without files larger than 1MB
$ git clone --filter=blob:limit=1m https://github.com/user/repo.git

# Clone without trees (extreme — fetches on checkout)
$ git clone --filter=tree:0 https://github.com/user/repo.git
```

## Recursive Clone (Submodules)

```shell
# Clone including all submodules
$ git clone --recurse-submodules https://github.com/user/repo.git

# If you forgot --recurse-submodules after cloning
$ git submodule update --init --recursive

# Clone with submodules fetched in parallel
$ git clone --recurse-submodules -j4 https://github.com/user/repo.git
```

## Clone with Specific Configuration

```shell
# Clone and set a config value in the new repo
$ git clone -c core.autocrlf=false https://github.com/user/repo.git

# Clone with multiple config options
$ git clone -c http.proxy=http://proxy:8080 -c core.compression=9 https://github.com/user/repo.git
```

## Local Clone

```shell
# Clone from a local path (uses hardlinks for efficiency)
$ git clone /path/to/existing/repo new-repo

# Force a full copy (no hardlinks)
$ git clone --no-hardlinks /path/to/existing/repo new-repo

# Clone from a local bare repository
$ git clone /srv/git/project.git
```

## Check What You Cloned

```shell
$ git clone https://github.com/user/repo.git && cd repo

$ git remote -v
origin  https://github.com/user/repo.git (fetch)
origin  https://github.com/user/repo.git (push)

$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/develop
  remotes/origin/feature/auth

$ git log --oneline -5
abc1234 Latest commit message
def5678 Previous commit
ghi9012 Another commit
jkl3456 Earlier commit
mno7890 Initial commit
```

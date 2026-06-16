# git archive

Creates an archive (tar or zip) of files from a specific tree/commit. Exports a clean snapshot without the .git directory.

## Basic Usage

```shell
# Create a tar archive of HEAD
$ git archive HEAD -o project.tar
$ ls -lh project.tar
-rw-r--r--  1 user  staff  2.5M project.tar

# Create a gzip-compressed tar
$ git archive HEAD | gzip > project.tar.gz

# Create a zip archive
$ git archive --format=zip HEAD -o project.zip
$ git archive HEAD --format=zip -o project.zip
```

## Archive a Specific Branch/Tag/Commit

```shell
# Archive a specific branch
$ git archive main -o main-snapshot.tar

# Archive a tagged release
$ git archive v1.2.0 -o release-v1.2.0.tar.gz --format=tar.gz

# Archive a specific commit
$ git archive abc1234 -o snapshot.zip --format=zip
```

## Archive a Subdirectory

```shell
# Export only a specific directory
$ git archive HEAD src/auth/ -o auth-module.tar

# Archive with a prefix directory
$ git archive --prefix=my-project/ HEAD -o project.tar
# Files inside the archive are under my-project/:
#   my-project/README.md
#   my-project/src/app.py
#   ...

# Common: prefix with version
$ git archive --prefix=project-v1.2.0/ v1.2.0 -o project-v1.2.0.tar.gz --format=tar.gz
```

## Formats

```shell
# Available formats
$ git archive --list
tar
tgz
tar.gz
zip

# Tar (uncompressed)
$ git archive --format=tar HEAD -o project.tar

# Tar + gzip
$ git archive --format=tar.gz HEAD -o project.tar.gz
$ git archive --format=tgz HEAD -o project.tgz

# Zip
$ git archive --format=zip HEAD -o project.zip

# Zip with compression level (0=none, 9=max)
$ git archive --format=zip -9 HEAD -o project.zip
```

## Archive from Remote

```shell
# Archive from a remote repository (without cloning)
$ git archive --remote=git@github.com:user/repo.git HEAD -o project.tar
$ git archive --remote=ssh://server/repo.git v1.0.0 -o release.tar.gz --format=tar.gz

# Note: --remote doesn't work with HTTPS on GitHub/GitLab
# (they offer their own download APIs instead)
```

## Export Attributes

```shell
# Use .gitattributes to control what's included in archives
$ cat .gitattributes
# Exclude these from archives
.gitignore     export-ignore
.gitattributes export-ignore
tests/         export-ignore
docs/internal/ export-ignore
.github/       export-ignore
*.test.py      export-ignore

# Set a substitution for $Format:...$
VERSION        export-subst

# Now git archive will exclude those files/directories
$ git archive HEAD -o clean-release.tar
```

## Pipe to stdout

```shell
# Pipe directly (useful for remote extraction)
$ git archive HEAD | tar -x -C /tmp/export/

# Pipe to a remote server
$ git archive HEAD | ssh server "cd /var/www && tar -x"

# Pipe through gzip
$ git archive HEAD | gzip > project.tar.gz
```

## Common Workflows

```shell
# Create a release archive
$ VERSION=$(git describe --tags --abbrev=0)
$ git archive --prefix="${VERSION}/" "${VERSION}" -o "${VERSION}.tar.gz" --format=tar.gz
# Creates v1.2.0.tar.gz with files under v1.2.0/

# Deploy to a server
$ git archive main | ssh deploy-server "cd /var/www/app && tar -x"

# Create a clean export for code review
$ git archive feature/auth --prefix=review/ -o review.zip --format=zip

# Archive only source code (no tests, no docs)
$ git archive HEAD src/ lib/ -o source-only.tar

# Diff export: changes since last tag
$ git diff --name-only v1.0.0..HEAD | xargs git archive HEAD -o changes.zip --format=zip --

# Backup a specific version
$ git archive --format=tar.gz --prefix=backup-$(date +%Y%m%d)/ HEAD -o backup-$(date +%Y%m%d).tar.gz
```

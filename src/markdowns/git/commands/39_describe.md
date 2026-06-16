# git describe

Gives a human-readable name to a commit based on the nearest tag. Useful for version strings and build identifiers.

## Basic Usage

```shell
# Describe current HEAD relative to nearest annotated tag
$ git describe
v1.2.0-14-gabc1234
#  │       │   └── abbreviated commit hash (with 'g' prefix for "git")
#  │       └────── 14 commits since the tag
#  └────────────── nearest annotated tag

# When HEAD is exactly on a tag
$ git describe
v1.2.0
```

## Describe a Specific Commit

```shell
$ git describe abc1234
v1.1.0-8-gdef5678

$ git describe HEAD~5
v1.2.0-9-gghi9012

# Describe a branch tip
$ git describe feature/auth
v1.2.0-3-gjkl3456
```

## Include Lightweight Tags

```shell
# By default, only annotated tags are used
# Include lightweight tags too:
$ git describe --tags
v1.2.1-rc1-3-gabc1234

# Include all refs (branches too)
$ git describe --all
heads/main-0-gabc1234
```

## Long Format

```shell
# Always show full format, even when on a tag
$ git describe --long
v1.2.0-0-gabc1234
# 0 commits since tag, currently AT the tag

# Without --long, being on a tag just shows the tag name:
$ git describe
v1.2.0
```

## Abbreviation Length

```shell
# Control how many hex chars of the hash to show
$ git describe --abbrev=10
v1.2.0-14-gabc1234567

# Full hash
$ git describe --abbrev=40
v1.2.0-14-gabc1234567890abcdef1234567890abcdef1234

# No hash at all
$ git describe --abbrev=0
v1.2.0-14
```

## Match Patterns

```shell
# Only consider tags matching a pattern
$ git describe --match "v1.*"
v1.2.0-14-gabc1234

$ git describe --match "release-*"
release-2025.06-3-gdef5678

# Exclude certain tags
$ git describe --exclude "v*-rc*"
v1.2.0-14-gabc1234

# Multiple match patterns
$ git describe --match "v*" --match "release-*"
```

## Dirty Suffix

```shell
# Append "-dirty" if working tree has uncommitted changes
$ git describe --dirty
v1.2.0-14-gabc1234-dirty

$ git describe --dirty="-modified"
v1.2.0-14-gabc1234-modified

# Clean working tree:
$ git describe --dirty
v1.2.0-14-gabc1234
```

## First Parent Only

```shell
# Follow only first parents (useful for mainline-only description)
$ git describe --first-parent
v1.2.0-10-gabc1234
# Ignores commits from merged branches
```

## Always Produce Output

```shell
# Normally fails if no tags exist:
$ git describe
fatal: No names found, cannot describe anything.

# Use --always to fall back to abbreviated hash
$ git describe --always
abc1234

# Combine with --dirty
$ git describe --always --dirty
abc1234-dirty
```

## Common Workflows

```shell
# Generate a version string for builds
$ VERSION=$(git describe --tags --always --dirty)
$ echo "Building version: $VERSION"
Building version: v1.2.0-14-gabc1234

# Use in a Makefile
# VERSION := $(shell git describe --tags --always --dirty)

# Use in Python
# import subprocess
# version = subprocess.check_output(["git", "describe", "--tags", "--always"]).strip()

# Check if current commit is a tagged release
$ git describe --exact-match 2>/dev/null && echo "This is a release" || echo "Not a release"

# Changelog between two described versions
$ git log $(git describe --abbrev=0)..HEAD --oneline
# Shows commits since last tag

# Find the last release tag
$ git describe --abbrev=0
v1.2.0
```

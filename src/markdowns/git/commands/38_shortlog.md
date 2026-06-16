# git shortlog

Summarizes `git log` output, grouping commits by author.

## Basic Usage

```shell
$ git shortlog
Alice (15):
      Add user authentication
      Fix login validation
      Update auth middleware
      Add password reset
      ...

Bob (8):
      Add dashboard layout
      Fix responsive grid
      Update chart component
      ...

Charlie (3):
      Fix typo in README
      Update dependencies
      Add .gitignore rules
```

## Count Only (Summary)

```shell
# Show only commit counts per author
$ git shortlog -s
    15  Alice
     8  Bob
     3  Charlie

# Sorted by commit count (most active first)
$ git shortlog -sn
    15  Alice
     8  Bob
     3  Charlie

# Numbered + email
$ git shortlog -sne
    15  Alice <alice@example.com>
     8  Bob <bob@example.com>
     3  Charlie <charlie@example.com>
```

## Group by Email

```shell
# Group by committer email instead of name
$ git shortlog -e
Alice <alice@example.com> (12):
      Add user authentication
      Fix login validation
      ...

Alice <alice@company.com> (3):
      Update config
      ...

# Use .mailmap to merge duplicate authors
$ cat .mailmap
Alice <alice@example.com> <alice@company.com>
$ git shortlog -sn
    15  Alice
```

## Filter by Date

```shell
# Commits in a date range
$ git shortlog --since="2025-06-01" --until="2025-06-30" -sn
    10  Alice
     5  Bob
     2  Charlie

# Commits from last week
$ git shortlog --since="1 week ago" -sn

# Commits this month
$ git shortlog --since="1 month ago" -sn
```

## Filter by Path

```shell
# Commits touching specific files/directories
$ git shortlog -sn -- src/auth/
     8  Alice
     3  Bob

# Commits touching Python files
$ git shortlog -sn -- "*.py"

# Multiple paths
$ git shortlog -sn -- src/ tests/
```

## Filter by Branch/Range

```shell
# Commits on a specific branch
$ git shortlog -sn feature/auth
     5  Alice
     2  Bob

# Commits between two tags (e.g., for release notes)
$ git shortlog v1.0.0..v2.0.0
Alice (6):
      Add user authentication
      Fix login validation
      Add password reset
      ...

Bob (3):
      Add dashboard layout
      Fix responsive grid
      ...

# Commits on feature branch since diverging from main
$ git shortlog main..feature/auth
```

## Exclude Merges

```shell
# Skip merge commits
$ git shortlog --no-merges -sn
    12  Alice
     7  Bob
     3  Charlie
```

## Custom Format

```shell
# Custom format for each commit line
$ git shortlog --format="%h %s" v1.0.0..v2.0.0
Alice (6):
      abc1234 Add user authentication
      def5678 Fix login validation
      ...

# Include date
$ git shortlog --format="%ad %s" --date=short
Alice (6):
      2025-06-10 Add user authentication
      2025-06-12 Fix login validation
      ...
```

## Generate Changelog

```shell
# Simple changelog between releases
$ echo "## What's Changed" && git shortlog --no-merges v1.0.0..v2.0.0
## What's Changed
Alice (6):
      Add user authentication
      Fix login validation
      Add password reset
      Update auth middleware
      Add token refresh
      Improve error messages

Bob (3):
      Add dashboard layout
      Fix responsive grid
      Update chart component

# Flat changelog (no grouping)
$ git log --no-merges --pretty=format:"- %s (%an)" v1.0.0..v2.0.0
- Add user authentication (Alice)
- Fix login validation (Alice)
- Add dashboard layout (Bob)
```

## From stdin

```shell
# Pipe log output into shortlog
$ git log --no-merges --since="2025-01-01" | git shortlog -sn
```

## Common Uses

```shell
# Who's contributed the most to this project?
$ git shortlog -sn --all

# Who's been active this sprint?
$ git shortlog -sn --since="2 weeks ago"

# What did Alice work on this month?
$ git shortlog --author="Alice" --since="1 month ago"

# Release notes generation
$ git shortlog --no-merges v1.0.0..v2.0.0

# Contributors per directory (team ownership)
$ git shortlog -sn -- services/auth/
```

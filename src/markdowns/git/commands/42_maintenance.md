# git maintenance

Runs tasks to optimize Git repository data. Modern replacement for manual `git gc` calls.

## Run Maintenance Tasks

```shell
# Run all default maintenance tasks
$ git maintenance run

# Run a specific task
$ git maintenance run --task=gc
$ git maintenance run --task=commit-graph
$ git maintenance run --task=prefetch
$ git maintenance run --task=loose-objects
$ git maintenance run --task=incremental-repack
$ git maintenance run --task=pack-refs
```

## Available Tasks

```shell
# commit-graph: update commit-graph file (faster log, merge-base)
$ git maintenance run --task=commit-graph

# prefetch: fetch from all remotes in the background (no merge)
$ git maintenance run --task=prefetch

# gc: standard garbage collection
$ git maintenance run --task=gc

# loose-objects: pack loose objects into small packfiles
$ git maintenance run --task=loose-objects

# incremental-repack: repack without full gc
$ git maintenance run --task=incremental-repack

# pack-refs: pack loose refs into packed-refs file
$ git maintenance run --task=pack-refs
```

## Register for Scheduled Maintenance

```shell
# Register the current repository for automatic background maintenance
$ git maintenance register
# Adds the repo to the global maintenance config

# This sets up a schedule that runs tasks automatically:
# - hourly: commit-graph, prefetch
# - daily: loose-objects, incremental-repack
# - weekly: pack-refs

# Unregister
$ git maintenance unregister
```

## Start/Stop Background Maintenance

```shell
# Start the background maintenance scheduler
$ git maintenance start
# Creates a cron job / launchd plist / systemd timer

# Stop the background scheduler
$ git maintenance stop
# Removes the scheduled task

# On macOS: uses launchd
# On Linux: uses systemd timers or crontab
# On Windows: uses Task Scheduler
```

## Configuration

```shell
# See current maintenance config
$ git config --get-all maintenance.repo

# Configure which tasks run at which schedule
$ git config maintenance.commit-graph.schedule hourly
$ git config maintenance.prefetch.schedule hourly
$ git config maintenance.loose-objects.schedule daily
$ git config maintenance.incremental-repack.schedule daily
$ git config maintenance.gc.schedule weekly

# Enable/disable specific tasks
$ git config maintenance.gc.enabled false
$ git config maintenance.commit-graph.enabled true

# Set auto threshold for gc task
$ git config maintenance.auto true
```

## Maintenance vs GC

```shell
# git gc: all-at-once, can be slow on large repos
$ git gc
# Packs everything, prunes, rewrites refs — one big operation

# git maintenance: incremental, scheduled, background
$ git maintenance run
# Does smaller chunks of work more frequently
# Better for large repos — avoids long pauses

# For most repos, just register and forget:
$ git maintenance register
$ git maintenance start
```

## Check Maintenance Status

```shell
# See which repos are registered
$ git config --global --get-all maintenance.repo
/home/user/project-a
/home/user/project-b
/home/user/monorepo

# Check the schedule (macOS)
$ ls ~/Library/LaunchAgents/org.git-scm.git.maintenance*

# Check the schedule (Linux)
$ systemctl --user list-timers | grep git
```

## Common Workflows

```shell
# Set up a large monorepo for optimal performance
$ cd /path/to/monorepo
$ git maintenance register
$ git maintenance start
# Background maintenance now runs automatically

# One-time optimization for a slow repo
$ git maintenance run --task=commit-graph
$ git maintenance run --task=incremental-repack

# Full maintenance (like gc but incremental)
$ git maintenance run --task=gc

# Speed up git log on large repos
$ git maintenance run --task=commit-graph
# Commit-graph makes log/merge-base operations much faster

# Speed up fetches
$ git maintenance run --task=prefetch
# Pre-fetches from all remotes so the next git pull is fast
```

```bash
ip-10-8-250-16:tmp hygull$ git clone --filter=blob:none --sparse https://github.com/hygull/propreps.git 
Cloning into 'propreps'...
remote: Enumerating objects: 1499, done.
remote: Counting objects: 100% (67/67), done.
remote: Compressing objects: 100% (40/40), done.
remote: Total 1499 (delta 24), reused 50 (delta 13), pack-reused 1432 (from 1)
Receiving objects: 100% (1499/1499), 147.67 KiB | 1.14 MiB/s, done.
Resolving deltas: 100% (759/759), done.
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (2/2), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 1 (delta 0), pack-reused 1 (from 1)
Receiving objects: 100% (3/3), 2.42 KiB | 2.42 MiB/s, done.
```

```bash
ip-10-8-250-16:tmp hygull$ ls
backend-adhoc-fixes.zip			foresight-engine-backend.zip
classification_2.0.zip			gtrends_breakout.zip
classification-dashboard-backend.zip	propreps
```

```bash
ip-10-8-250-16:tmp hygull$ cd propreps/
ip-10-8-250-16:propreps hygull$ ls
CLAUDE.md	LICENSE		README.md
```

```bash
ip-10-8-250-16:propreps hygull$ git sparse-checkout set src
remote: Enumerating objects: 118, done.
remote: Counting objects: 100% (94/94), done.
remote: Compressing objects: 100% (92/92), done.
remote: Total 118 (delta 3), reused 51 (delta 2), pack-reused 24 (from 1)
Receiving objects: 100% (118/118), 143.99 KiB | 267.00 KiB/s, done.
Resolving deltas: 100% (3/3), done.
Updating files: 100% (121/121), done.
```

```bash
ip-10-8-250-16:propreps hygull$ ls
CLAUDE.md	LICENSE		README.md	src
```

```bash
ip-10-8-250-16:propreps hygull$ git sparse-checkout set .vscode
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 1 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (1/1), 83 bytes | 83.00 KiB/s, done.
```

```bash
ip-10-8-250-16:propreps hygull$ ls
CLAUDE.md	LICENSE		README.md
```

```bash
ip-10-8-250-16:propreps hygull$ ls -a
.		..		.git		.vscode		CLAUDE.md	LICENSE		README.md
```

```bash
ip-10-8-250-16:propreps hygull$ git sparse-checkout set src
ip-10-8-250-16:propreps hygull$ ls -a
.		..		.git		CLAUDE.md	LICENSE		README.md	src
```

```bash
ip-10-8-250-16:propreps hygull$ git sparse-checkout set .vscode
ip-10-8-250-16:propreps hygull$ ls -a
.		..		.git		.vscode		CLAUDE.md	LICENSE		README.md
```

```bash
ip-10-8-250-16:propreps hygull$ git sparse-checkout add src
ip-10-8-250-16:propreps hygull$ ls -a
.		.git		CLAUDE.md	README.md
..		.vscode		LICENSE		src
```

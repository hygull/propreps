```shell
Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv 
first_name	last_name	age	relation
Subhash	Agrawani	58	Father
Sanshya	Agrawani	52	Mother
Rishikesh	Agrawani	32	Myself
Hemkesh	Agrawani	30	Brother
Malinikesh	Agrawani	28	Sister
```

```shell
Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv | grep Father
Subhash	Agrawani	58	Father
```

```shell
Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv | awk '/Father/ {print $0}'
Subhash	Agrawani	58	Father
```

```shell
Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ grep "Father" files/family.tsv 
Subhash	Agrawani	58	Father
```
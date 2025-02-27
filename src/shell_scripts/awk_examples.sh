```shell
Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv 
first_name	last_name	age	relation
Subhash	Agrawani	58	Father
Sandhya	Agrawani	52	Mother
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

```shell
ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $1}'
Sandhya
ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $2}'
Agrawani
ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $2,$3}'
Agrawani 52
ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $1,$2,$3}'
Sandhya Agrawani 52
```

```shell
ip-192-168-1-107:shell_scripts hygull$ awk '{print}' files/family.tsv 
first_name	last_name	age	relation
Subhash	Agrawani	58	Father
Sandhya	Agrawani	52	Mother
Rishikesh	Agrawani	32	Myself
Hemkesh	Agrawani	30	Brother
Malinikesh	Agrawani	28	Sister
```

```shell
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1}' files/family.tsv 
Sanshya
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2}' files/family.tsv 
Agrawani
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2,$3}' files/family.tsv 
Agrawani 52
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2, $3}' files/family.tsv 
Agrawani 52
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1 $2, $3}' files/family.tsv 
SandhyaAgrawani 52
ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1, $2, $3}' files/family.tsv 
Sandhya Agrawani 52
```

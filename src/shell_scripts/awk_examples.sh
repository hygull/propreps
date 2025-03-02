
# Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv 
# first_name	last_name	age	relation
# Subhash	Agrawani	58	Father
# Sandhya	Agrawani	52	Mother
# Rishikesh	Agrawani	32	Myself
# Hemkesh	Agrawani	30	Brother
# Malinikesh	Agrawani	28	Sister


# Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv | grep Father
# Subhash	Agrawani	58	Father


# Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ cat files/family.tsv | awk '/Father/ {print $0}'
# Subhash	Agrawani	58	Father


# Rishikeshs-MacBook-Pro-2:shell_scripts hygull$ grep "Father" files/family.tsv 
# Subhash	Agrawani	58	Father


# ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $1}'
# Sandhya
# ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $2}'
# Agrawani
# ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $2,$3}'
# Agrawani 52
# ip-192-168-1-107:shell_scripts hygull$ grep "Mother" files/family.tsv | awk '{print $1,$2,$3}'
# Sandhya Agrawani 52


# ip-192-168-1-107:shell_scripts hygull$ awk '{print}' files/family.tsv 
# first_name	last_name	age	relation
# Subhash	Agrawani	58	Father
# Sandhya	Agrawani	52	Mother
# Rishikesh	Agrawani	32	Myself
# Hemkesh	Agrawani	30	Brother
# Malinikesh	Agrawani	28	Sister


# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1}' files/family.tsv 
# Sanshya
# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2}' files/family.tsv 
# Agrawani
# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2,$3}' files/family.tsv 
# Agrawani 52
# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $2, $3}' files/family.tsv 
# Agrawani 52
# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1 $2, $3}' files/family.tsv 
# SandhyaAgrawani 52
# ip-192-168-1-107:shell_scripts hygull$ awk '/Mother/ {print $1, $2, $3}' files/family.tsv 
# Sandhya Agrawani 52


# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR}' files/family.tsv 
# 1
# 2
# 3
# 4
# 5
# 6
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $0}' files/family.tsv 
# 1 first_name	last_name	age	relation
# 2 Subhash	Agrawani	58	Father
# 3 Sandhya	Agrawani	52	Mother
# 4 Rishikesh	Agrawani	32	Myself
# 5 Hemkesh	Agrawani	30	Brother
# 6 Malinikesh	Agrawani	28	Sister
# ip-192-168-1-107:shell_scripts hygull$ 
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $0, $1}' files/family.tsv 
# 1 first_name	last_name	age	relation first_name
# 2 Subhash	Agrawani	58	Father Subhash
# 3 Sandhya	Agrawani	52	Mother Sandhya
# 4 Rishikesh	Agrawani	32	Myself Rishikesh
# 5 Hemkesh	Agrawani	30	Brother Hemkesh
# 6 Malinikesh	Agrawani	28	Sister Malinikesh
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $1}' files/family.tsv 
# 1 first_name
# 2 Subhash
# 3 Sandhya
# 4 Rishikesh
# 5 Hemkesh
# 6 Malinikesh
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $2}' files/family.tsv 
# 1 last_name
# 2 Agrawani
# 3 Agrawani
# 4 Agrawani
# 5 Agrawani
# 6 Agrawani
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $3}' files/family.tsv 
# 1 age
# 2 58
# 3 52
# 4 32
# 5 30
# 6 28
# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $4}' files/family.tsv 
# 1 relation
# 2 Father
# 3 Mother
# 4 Myself
# 5 Brother
# 6 Sister


# ip-192-168-1-107:shell_scripts hygull$ awk '{print NR, $NF}' files/family.tsv 
# 1 relation
# 2 Father
# 3 Mother
# 4 Myself
# 5 Brother
# 6 Sister
# ip-192-168-1-107:shell_scripts hygull$ awk '{print $NF}' files/family.tsv 
# relation
# Father
# Mother
# Myself
# Brother
# Sister
# ip-192-168-1-107:shell_scripts hygull$ awk '{print $1, $NF}' files/family.tsv 
# first_name relation
# Subhash Father
# Sandhya Mother
# Rishikesh Myself
# Hemkesh Brother
# Malinikesh Sister
# ip-192-168-1-107:shell_scripts hygull$ 


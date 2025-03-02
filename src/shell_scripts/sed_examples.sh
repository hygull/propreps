# ip-192-168-1-107:shell_scripts hygull$ cat files/rishikesh_details.txt 
# There is dev named Rishi Agrawani but Rishi is shy guy.
# Rishi is a senior staff software engineer at Aipalette.
# Let's move forward.
# Whenever time permits, Rishi goes outside to enjoy the temples, gardens, etc.

sed 's/Rishi/Rishikesh/' files/rishikesh_details.txt # Running this command, returns the below file's content after successfully replacing the words
# There is dev named Rishikesh Agrawani but Rishi is shy guy.
# Rishikesh is a senior staff software engineer at Aipalette.
# Let's move forward.
# Whenever time permits, Rishikesh goes outside to enjoy the temples, gardens, etc.

sed 's/Rishi/Rishikesh/g' files/rishikesh_details.txt # Running this command, will replace all occurrences of Rishi from lines
# There is dev named Rishikesh Agrawani but Rishikesh is shy guy.
# Rishikesh is a senior staff software engineer at Aipalette.
# Let's move forward.
# Whenever time permits, Rishikesh goes outside to enjoy the temples, gardens, etc.

echo "Hello Rishi! How are you Rishi?" | sed 's/Rishi/Rishikesh/'
# Hello Rishikesh! How are you Rishi?

echo "Hello Rishi! How are you Rishi?" | sed 's/Rishi/Rishikesh/g'
# Hello Rishikesh! How are you Rishi?
# Hello Rishikesh! How are you Rishikesh?
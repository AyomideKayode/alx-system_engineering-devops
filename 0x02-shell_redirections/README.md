Tasks for Shell Redirections

Task 0: echo Hello, World = scripts that prints Hello world

Task 1: echo "\"(Ôo)'" = script that displays a confuse smiley

Task 2: cat /etc/passwd = display the content of /etc/passwd file

Task 3: cat /etc/passwd /etc/hosts = display content of both files

Task 4: tail /etc/passwd = display last 10 ines of the file

Task 5: head /etc/passwd = display first 10 lines of file

Task 6: head --lines=3 iacta | tail --lines=1 = script that displays the third line of the file ```iacta```

Task 7: echo 'Best School' > "\*\\\'\"Best School\"\'\\\*$\?\*\*\*\*\*:)" = shell script that creates file named exactly with the added characters containing the text ```Best School```

Task 8: ls -la > ls_cwd_content = script that writes into the file ```ls_cwd_content``` the result of the command ```ls -la```. If the file ```ls_cwd_content``` already exists, it should be overwritten. If the file ```ls_cwd_content``` does not exist, create it.

Task 9: echo -en "" | tail --lines=1 iacta >> iacta = script that duplicates the last line of the file ```iacta```

Tal 10: find . -type f -name "*.js" -delete =  script that deletes all the regular files (not the directories) with a ```.js``` extension that are present in the current directory and all its subfolders. 

Task 11: find -mindepth 1 -type d | wc -l =  script that counts the number of directories and sub-directories in the current directory. *The current and parent directories should not be taken into account. *Hidden directories should be counted

Task 12: ls -t | head = script that displays the 10 newest files in the current directory. *One file per line. *Sorted from the newest to the oldest

Tak 13: sort | uniq -u = script that takes a list of words as input and prints only words that appear exactly once.

Task 14: grep -i root /etc/passwd = Display lines containing the pattern “root” from the file ```/etc/passwd```

Task 15: grep -i bin /etc/passwd = Display the number of lines that contain the pattern “bin” in the file ```/etc/passwd```

Task 16: grep -iA 3 root /etc/passwd = Display lines containing the pattern “root” and 3 lines after them in the file ```/etc/passwd```

Task 17: grep -iv bin /etc/passwd = Display all the lines in the file ```/etc/passwd``` that do not contain the pattern “bin”

Task 18:

Task 19: tr Ac Ze = Replace all characters ```A``` and ```c``` from input to ```Z``` and ```e``` respectively.

Task 20: tr -d cC = script that removes all letters ```c``` and ```C``` from input.

Tak 21: rev = script that reverse its input.

Task 22: cut -d ':' -f 1,6 /etc/passwd | sort = script that displays all users and their home directories, sorted by users. *Based on the ```/etc/passwd``` file

Task 23: find . -empty -printf "%f\n" = Write a command that finds all empty files and directories in the current directory and all sub-directories.

Task 24:

Task 25: cut -c 1 | tr -d '\n' | sort =  script that decodes acrostics that use the first letter of each line.

Task 26: 

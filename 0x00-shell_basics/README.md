0x00-shell_basics 

0: pwd = print working directory

1: ls = list contents of current directory

2: cd = change working directory

3: ls -l = list contents of current directory in a long format

4: ls -la = list contents of current directory in a long format and include hidden files

5: ls -lan = list contents of current directory in a long format, include hidden files and arrange with user group IDs displayed numerically

6: mkdir /tmp/my_first_directory = create a directory named my_first_directory inside the /tmp directory

7: mv /tmp/betty /tmp/my_first_directory = move a file named betty into another directory named /tmp/my_first_directory

8: rm /tmp/my_first_directory/betty = remove the betty file located inside the /tmp/my_first_directory

9: rmdir /tmp/my_first_directory = removes the directory located in the /tmp directory

10: cd - = change directory to previous directory you were in

11: ls -la . /boot .. = List all files/directories, including hidden files/directories, from 3 separate directories: current directory, parent of working directory, and /boot directory.

12: file /tmp/iamafile = Prints the type of file iamafile.

13: ln -s /bin/ls __ls__ = Create a symbolic link named __ls__ for /bin/ls

14: cp -u *.html .. = Copy all html files from the current directory to the parent directory, but only copy files that didn't exist in the parent directory or are newer versions than the ones that already exist in the parent directory. 

15: mv [[:upper:]]* /tmp/u  = Move all files that begin with a capital letter to /tmp/u

16: rm *~ = Deletes all files in the current directory that end with a ~

17: mkdir -p welcome/to/school = Create directory ```welcome``` in current directory. Create directory ```to``` inside directory ```welcome```. Create directory ```school``` inside directory ```to```. The -p option creates any intermediate directories in the path argument.

18: ls -map = List all files and directories of the current directory, separated by commas. Directory names should end with a forward slash (/). The listing should be alph ordered, except for dot (.) or dot dot (..), which should be listed at the beginning. The -a option is to show any hidden files. The -p option writes a / at the end of directory names. The -m option streams the output, separating each listing with commas.

19: ```touch school``` to create a file named school. Open file with an editor and put in these lines '0 string SCHOOL School data' and '!:mime School'. Save and exit file. And from the shell directory, run the command to create a magic file that can be used with the command ```file``` to detect ```School``` data files. ```School``` data files always contain the string ```SCHOOL``` at offset 0. 'file -C -m school'

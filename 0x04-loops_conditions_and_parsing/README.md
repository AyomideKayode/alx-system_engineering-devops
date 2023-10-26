# Project: 0x04. Loops, conditions and parsing

## Resources

#### Read or watch:

* [Loops Sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
* [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
* [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
* [File test operators](https://tldp.org/LDP/abs/html/fto.html)
* [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

## Learning Objectives

### General

* How to create SSH keys
* What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code>
* How to use <code>while</code>, <code>until</code> and <code>for</code> loops
* How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements
* How to use the <code>cut</code> command
* What are files and other comparison operators, and how to use them

## Description of what each file shows (Tasks):
0. [Create a SSH RSA key pair](./0-RSA_public_key.pub) :
* Read for this task:
	- [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys)
	- [Windows users](https://docs.rackspace.com/docs/generating-rsa-keys-with-ssh-puttygen)
* man: `ssh-keygen`
* You will soon have to manage your own servers concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&feature=youtu.be&t=46). We need to set them up with your RSA public key so that you can access them via SSH.
* Create a RSA key pair.
* Requirements:

	- Share your public key in your answer file `0-RSA_public_key.pub`
	- Fill the `SSH public key` field of your `intranet profile` with the public key you just generated
	- **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
	- If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase
* SSH and RSA keys will be covered in depth in a later project.
1. [For Best School loop](./1-for_best_school) :
* Write a Bash script that displays `Best School` 10 times.
- Requirement:
	- You must use the `for` loop (`while` and `until` are forbidden)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ head -n 2 1-for_best_school
	#!/usr/bin/env bash
	# Script that prints Best School to stdout 10 times using the for loop.
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./1-for_best_school 
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
* Note that:
	- The first line of my Bash script starts with `#!/usr/bin/env bash`
	- The second line of my Bash scripts is a comment explaining what it is doing
2. [While Best School loop](./2-while_best_school) :
* Write a Bash script that displays `Best School` 10 times.
- Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./2-while_best_school 
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$
	```
3. [Until Best School loop](./3-until_best_school) :
* Write a Bash script that displays `Best School` 10 times.
- Requirements:
	- You must use the `until` loop (`for` and `while` are forbidden)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./3-until_best_school 
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
4. [If 9, say Hi!](./4-if_9_say_hi) :
* Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.
* Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
	- You must use the `if` statement
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./4-if_9_say_hi 
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Best School
	Hi
	Best School
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
5. [4 bad luck, 8 is your chance](./5-4_bad_luck_8_is_your_chance) :
* Write a Bash script that loops from 1 to 10 and:
	- displays `bad luck` for the 4th loop iteration
	- displays `good luck` for the 8th loop iteration
	- displays `Best School` for the other iterations
* Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
	- You must use the `if`, `elif` and `else` statements
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./5-4_bad_luck_8_is_your_chance 
	Best School
	Best School
	Best School
	bad luck
	Best School
	Best School
	Best School
	good luck
	Best School
	Best School
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
* For the most curious:
	- [4 in the Chinese culture](https://en.wikipedia.org/wiki/Chinese_numerology#Four)
6. [Superstitious numbers](./6-superstitious_numbers) :
* Write a Bash script that displays numbers from 1 to 20 and:
	- displays `4` and then `bad luck from China` for the 4th loop iteration
	- displays `9` and then `bad luck from Japan` for the 9th loop iteration
	- displays `17` and then `bad luck from Italy` for the 17th loop iteration
- Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
	- You must use the `case` statement
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./6-superstitious_numbers 
	1
	2
	3
	4
	bad luck from China
	5
	6
	7
	8
	9
	bad luck from Japan
	10
	11
	12
	13
	14
	15
	16
	17
	bad luck from Italy
	18
	19
	20
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
7. [Clock](./7-clock) :
* Write a Bash script that displays the time for 12 hours and 59 minutes:
	- display hours from 0 to 12
	- display minutes from 1 to 59
- Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
- Note that in this example, we only display the first 70 lines using the head command.
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./7-clock | head -n 70
	Hour: 0
	1
	2
	3
	4
	5
	6
	7
	8
	9
	10
	11
	12
	13
	14
	15
	16
	17
	18
	19
	20
	21
	22
	23
	24
	25
	26
	27
	28
	29
	30
	31
	32
	33
	34
	35
	36
	37
	38
	39
	40
	41
	42
	43
	44
	45
	46
	47
	48
	49
	50
	51
	52
	53
	54
	55
	56
	57
	58
	59
	Hour: 1
	1
	2
	3
	4
	5
	6
	7
	8
	9
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
8. [For ls](./8-for_ls) :
* Write a Bash script that displays:
	- The content of the current directory
	- In a list format
	- Where only the part of the name after the first dash is displayed (refer to the example)
* Requirements:
	- You must use the for loop (while and until are forbidden)
	- Do not display hidden files
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ls
	0-RSA_public_key.pub  4-if_9_say_hi                  8-for_ls
	1-for_best_school     5-4_bad_luck_8_is_your_chance  README.md
	2-while_best_school   6-superstitious_numbers
	3-until_best_school   7-clock
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./8-for_ls 
	RSA_public_key.pub
	for_best_school
	while_best_school
	until_best_school
	if_9_say_hi
	4_bad_luck_8_is_your_chance
	superstitious_numbers
	clock
	for_ls
	README.md
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
9. [To file, or not to file](./9-to_file_or_not_to_file) :
* Write a Bash script that gives you information about the school file.
- Requirements:
	- You must use `if` and, `else` (`case` is forbidden)
	- Your Bash script should check if the file exists and print:
		- if the file exists: `school file exists`
		- if the file does not exist: `school file does not exist`
	- If the file exists, print:
		- if the file is empty: `school file is empty`
		- if the file is not empty: `school file is not empty`
		- if the file is a regular file: `school is a regular file`
		- if the file is not a regular file: (nothing)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ file school
	school: cannot open `school' (No such file or directory)
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./9-to_file_or_not_to_file
	school file does not exist
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ touch school
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./9-to_file_or_not_to_file
	school file exists
	school file is empty
	school is a regular file
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ echo 'betty' > school
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./9-to_file_or_not_to_file
	school file exists
	school file is not empty
	school is a regular file
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ rm school 
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ mkdir school
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./9-to_file_or_not_to_file
	school file exists
	school file is not empty
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
10. [FizzBuzz](./10-fizzbuzz) :
* Write a Bash script that displays numbers from 1 to 100.
- Requirements:
	- Displays `FizzBuzz` when the number is a multiple of `3` and `5`
	- Displays `Fizz` when the number is multiple of `3`
	- Displays `Buzz` when the number is a multiple of `5`
	- Otherwise, displays the number
	- In a list format
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./10-fizzbuzz | head -20
	1
	2
	Fizz
	4
	Buzz
	Fizz
	7
	8
	Fizz
	Buzz
	11
	Fizz
	13
	14
	FizzBuzz
	16
	17
	Fizz
	19
	Buzz
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
11. [Read and cut](./100-read_and_cut) :
* help: `read`
- Write a Bash script that displays the content of the file `/etc/passwd`.
- Your script should only display:
	- username
	- user id
	- Home directory path for the user
- Requirements:
	- You must use the `while` loop (`for` and `until` are forbidden)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ ./100-read_and_cut 
	root:0:/root
	daemon:1:/usr/sbin
	bin:2:/bin
	sys:3:/dev
	sync:4:/bin
	games:5:/usr/games
	man:6:/var/cache/man
	lp:7:/var/spool/lpd
	mail:8:/var/mail
	news:9:/var/spool/news
	uucp:10:/var/spool/uucp
	proxy:13:/bin
	www-data:33:/var/www
	backup:34:/var/backups
	list:38:/var/list
	irc:39:/var/run/ircd
	gnats:41:/var/lib/gnats
	nobody:65534:/nonexistent
	systemd-network:100:/run/systemd/netif
	systemd-resolve:101:/run/systemd/resolve
	syslog:102:/home/syslog
	messagebus:103:/nonexistent
	_apt:104:/nonexistent
	lxd:105:/var/lib/lxd/
	uuidd:106:/run/uuidd
	dnsmasq:107:/var/lib/misc
	landscape:108:/var/lib/landscape
	sshd:109:/run/sshd
	pollinate:110:/var/cache/pollinate
	kazzywiz:1000:/home/kazzywiz
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```
12. [Tell the story of passwd](./101-tell_the_story_of_passwd) :
* Read:
	- [IFS (internal field separator)](https://tldp.org/LDP/abs/html/internalvariables.html)
	- [Understanding /etc/passwd](https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/)
- The file `/etc/passwd` has already been covered in a [previous project](../0x02-shell_redirections/) and you should be familiar with it. Today we will make up a story based on it.
- Write a Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + `IFS`.
- Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`
- Requirements:
	- You must use the while loop (for and until are forbidden)
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_$ ./101-tell_the_story_of_passwd 
	The user root is part of the 0 gang, lives in /root and rides /bin/bash. 0's place is protected by the passcode x, more info about the user here: root
	The user daemon is part of the 1 gang, lives in /usr/sbin and rides /usr/sbin/nologin. 1's place is protected by the passcode x, more info about the user here: daemon
	The user bin is part of the 2 gang, lives in /bin and rides /usr/sbin/nologin. 2's place is protected by the passcode x, more info about the user here: bin
	The user sys is part of the 3 gang, lives in /dev and rides /usr/sbin/nologin. 3's place is protected by the passcode x, more info about the user here: sys
	The user sync is part of the 65534 gang, lives in /bin and rides /bin/sync. 4's place is protected by the passcode x, more info about the user here: sync
	The user games is part of the 60 gang, lives in /usr/games and rides /usr/sbin/nologin. 5's place is protected by the passcode x, more info about the user here: games
	The user man is part of the 12 gang, lives in /var/cache/man and rides /usr/sbin/nologin. 6's place is protected by the passcode x, more info about the user here: man
	The user lp is part of the 7 gang, lives in /var/spool/lpd and rides /usr/sbin/nologin. 7's place is protected by the passcode x, more info about the user here: lp
	The user mail is part of the 8 gang, lives in /var/mail and rides /usr/sbin/nologin. 8's place is protected by the passcode x, more info about the user here: mail
	The user news is part of the 9 gang, lives in /var/spool/news and rides /usr/sbin/nologin. 9's place is protected by the passcode x, more info about the user here: news
	The user uucp is part of the 10 gang, lives in /var/spool/uucp and rides /usr/sbin/nologin. 10's place is protected by the passcode x, more info about the user here: uucp
	The user proxy is part of the 13 gang, lives in /bin and rides /usr/sbin/nologin. 13's place is protected by the passcode x, more info about the user here: proxy
	The user www-data is part of the 33 gang, lives in /var/www and rides /usr/sbin/nologin. 33's place is protected by the passcode x, more info about the user here: www-data
	The user backup is part of the 34 gang, lives in /var/backups and rides /usr/sbin/nologin. 34's place is protected by the passcode x, more info about the user here: backup
	The user list is part of the 38 gang, lives in /var/list and rides /usr/sbin/nologin. 38's place is protected by the passcode x, more info about the user here: Mailing List Manager
	The user irc is part of the 39 gang, lives in /var/run/ircd and rides /usr/sbin/nologin. 39's place is protected by the passcode x, more info about the user here: ircd
	The user gnats is part of the 41 gang, lives in /var/lib/gnats and rides /usr/sbin/nologin. 41's place is protected by the passcode x, more info about the user here: Gnats Bug-Reporting System (admin)
	The user nobody is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 65534's place is protected by the passcode x, more info about the user here: nobody
	The user systemd-network is part of the 102 gang, lives in /run/systemd/netif and rides /usr/sbin/nologin. 100's place is protected by the passcode x, more info about the user here: systemd Network Management,,,
	The user systemd-resolve is part of the 103 gang, lives in /run/systemd/resolve and rides /usr/sbin/nologin. 101's place is protected by the passcode x, more info about the user here: systemd Resolver,,,
	The user syslog is part of the 106 gang, lives in /home/syslog and rides /usr/sbin/nologin. 102's place is protected by the passcode x, more info about the user here: 
	The user messagebus is part of the 107 gang, lives in /nonexistent and rides /usr/sbin/nologin. 103's place is protected by the passcode x, more info about the user here: 
	The user _apt is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 104's place is protected by the passcode x, more info about the user here: 
	The user lxd is part of the 65534 gang, lives in /var/lib/lxd/ and rides /bin/false. 105's place is protected by the passcode x, more info about the user here: 
	The user uuidd is part of the 110 gang, lives in /run/uuidd and rides /usr/sbin/nologin. 106's place is protected by the passcode x, more info about the user here: 
	The user dnsmasq is part of the 65534 gang, lives in /var/lib/misc and rides /usr/sbin/nologin. 107's place is protected by the passcode x, more info about the user here: dnsmasq,,,
	The user landscape is part of the 112 gang, lives in /var/lib/landscape and rides /usr/sbin/nologin. 108's place is protected by the passcode x, more info about the user here: 
	The user sshd is part of the 65534 gang, lives in /run/sshd and rides /usr/sbin/nologin. 109's place is protected by the passcode x, more info about the user here: 
	The user pollinate is part of the 1 gang, lives in /var/cache/pollinate and rides /bin/false. 110's place is protected by the passcode x, more info about the user here: 
	The user kazzywiz is part of the 1000 gang, lives in /home/kazzywiz and rides /bin/bash. 1000's place is protected by the passcode x, more info about the user here: ,,,
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ 
	```

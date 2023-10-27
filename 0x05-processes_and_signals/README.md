# Project: 0x05. Processes and Signals

## Resources

#### Read or watch:

* [Linux PID](https://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
* [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
## Learning Objectives

### General

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored
## Description of what each file shows (Tasks)
* Files that start with with:
0. [What is my PID](./0-what-is-my-pid) :
* Write a Bash script that displays its own PID.
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./0-what-is-my-pid 
	4690
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
* <em>This may vary on your computer.</em>
1. [List your processes](./1-list_your_processes) :
* Write a Bash script that displays a list of currently running processes.
* Requirements:
	- Must show all processes, for all users, including those which might not have a TTY
	- Display in a user-oriented format
	- Show process hierarchy
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./1-list_your_processes | head -20
	USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
	root         1  0.0  0.2 225124  8840 ?        Ss   14:00   0:00 /sbin/init
	root         2  0.0  0.0   2324  1196 ?        Sl   14:00   0:00 /init
	root         5  0.0  0.0   2352    72 ?        Sl   14:01   0:00  \_ plan9 --control-socket 6 --log-level 4 --server-fd 7 --pipe-fd 9 --log-truncate
	root      1004  0.0  0.0   2332   112 ?        Ss   14:01   0:00  \_ /init
	root      1006  0.0  0.0   2348   116 ?        S    14:01   0:00  |   \_ /init
	kazzywiz  1011  0.0  0.1  23248  5328 pts/0    Ss   14:01   0:00  |       \_ -bash
	kazzywiz  6998  0.0  0.0  13324  3144 pts/0    S+   15:15   0:00  |           \_ bash ./1-list_your_processes
	kazzywiz  7000  0.0  0.0  37968  3284 pts/0    R+   15:15   0:00  |           |   \_ ps auxf
	kazzywiz  6999  0.0  0.0   7948   900 pts/0    S+   15:15   0:00  |           \_ head -20
	root      1012  0.0  0.0  78640  3572 pts/1    Ss   14:01   0:00  \_ /bin/login -f
	kazzywiz  1182  0.0  0.1  23084  4808 pts/1    S+   14:01   0:00  |   \_ -bash
	root      1451  0.0  0.0   2328   116 ?        Ss   14:56   0:00  \_ /init
	root      1453  0.0  0.0   2344   120 ?        S    14:56   0:00  |   \_ /init
	kazzywiz  1456  0.0  0.0   4640   780 pts/2    Ss+  14:56   0:00  |       \_ sh -c "$VSCODE_WSL_EXT_LOCATION/scripts/wslServer.sh" f1b07bd25dfad64b0167beb15359ae573aecd2cc stable code-server .vscode-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	kazzywiz  1457  0.0  0.0   4640   868 pts/2    S+   14:56   0:00  |           \_ sh /mnt/c/Users/user/.vscode/extensions/ms-vscode-remote.remote-wsl-0.81.8/scripts/wslServer.sh f1b07bd25dfad64b0167beb15359ae573aecd2cc stable code-server .vscode-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	kazzywiz  1462  0.0  0.0   4640   828 pts/2    S+   14:56   0:00  |               \_ sh /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/bin/code-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	kazzywiz  1466  1.7  2.4 976944 98600 pts/2    Sl+  14:56   0:20  |                   \_ /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/node /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/server-main.js --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	kazzywiz  1500  0.4  1.6 676344 64832 pts/2    Sl+  14:56   0:05  |                       \_ /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/node /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/bootstrap-fork --type=ptyHost --logsPath /home/kazzywiz/.vscode-server/data/logs/20231027T145627
	kazzywiz  1636  0.0  0.1  23208  5396 pts/5    Ss+  14:56   0:00  |                       |   \_ /bin/bash --init-file /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/vs/workbench/contrib/terminal/browser/media/shellIntegration-bash.sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$
	```
2. [Show your Bash PID](./2-show_your_bash_pid) :
* Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
- Requirements:
	- You cannot use `pgrep`
	- The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ shell 2-show_your_bash_pid 
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./2-show_your_bash_pid 
	kazzywiz  1011  0.0  0.1  23248  5328 pts/0    Ss+  14:01   0:00  |       \_ -bash
	kazzywiz  1182  0.0  0.1  23084  4808 pts/1    S+   14:01   0:00  |   \_ -bash
	kazzywiz  1636  0.0  0.1  23208  5408 pts/5    Ss   14:56   0:00  |                       |   \_ /bin/bash --init-file /home/kazzywiz/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/vs/workbench/contrib/terminal/browser/media/shellIntegration-bash.sh
	kazzywiz  9825  0.0  0.0  13324  3168 pts/5    S+   15:25   0:00  |                       |       \_ bash ./2-show_your_bash_pid
	kazzywiz  9829  0.0  0.0  14864  1008 pts/5    S+   15:25   0:00  |                       |           \_ grep bash
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
3. [Show your Bash PID made easy](./3-show_your_bash_pid_made_easy) :
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
- Requirements:
	- You cannot use `ps`
	```sh
	sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
	4404 bash
	4555 bash
	sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
	4404 bash
	4557 bash
	sylvain@ubuntu$ 
	```
- Here we can see that:
	- For the first iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4555`
	- For the second iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4557`
* P.S (pun intended😅): 
	- The key point to note here is that the bash processes have the same PID in both iterations because they are the same processes that were running before you ran the script. However, the PID of the script (3-show_your_bash_pid_made_easy) is different in each iteration because a new instance of the script is being executed, and each instance of the script has a unique PID.
	- In the context of the script, it's listing the bash processes it finds, along with the PID of the script itself. This is why you see different script PIDs in each iteration, but the bash process PID remains the same because it's the same running bash process.
4. [To infinity and beyond](./4-to_infinity_and_beyond) :
* Write a Bash script that displays To infinity and beyond indefinitely.
	- Requirements:
		- In between each iteration of the loop, add a `sleep 2`
	```sh
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./4-to_infinity_and_beyond 
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	^C
	kazzywiz@Kazzywiz:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
- <em>Note that I `ctrl+c` (killed) the Bash script in the example.</em>

| Task | File |
| ---- | ---- |
| 5. Don't stop me now! | [5-dont_stop_me_now](./5-dont_stop_me_now) |
| 6. Stop me if you can | [6-stop_me_if_you_can](./6-stop_me_if_you_can) |
| 7. Highlander | [7-highlander](./7-highlander) |
| 8. Beheaded process | [8-beheaded_process](./8-beheaded_process) |
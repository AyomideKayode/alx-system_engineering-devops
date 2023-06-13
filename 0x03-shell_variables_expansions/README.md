Tasks for Shell, init files, variables and expansions.

Tak 0: alias ```ls="rm *"``` = script that creates an alias with the name ```ls``` for the value ```rm *```

Tak 1: echo hello $USER = script that prints hello user, where user is the current Linux user.

Tak 2: export PATH=$PATH:/action = Add ```/action``` to the ```PATH```. ```/action``` should be the last directory the shell looks into when looking for a program.

Task 3: echo $PATH | tr -s ":" "\n" | wc -l = script that counts the number of directories in the ```PATH```

Task 4: 

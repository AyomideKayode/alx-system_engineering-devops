Tasks for Shell, init files, variables and expansions.

Tak 0: alias ```ls="rm *"``` = script that creates an alias with the name ```ls``` for the value ```rm *```

Tak 1: echo hello $USER = script that prints hello user, where user is the current Linux user.

Tak 2: export PATH=$PATH:/action = Add ```/action``` to the ```PATH```. ```/action``` should be the last directory the shell looks into when looking for a program.

Task 3: echo $PATH | tr -s ":" "\n" | wc -l = script that counts the number of directories in the ```PATH```

Task 4: printenv = script that lists environment variables

Task 5: set = script that lists all local variables and environment variables, and functions.

Task 6: BEST="School" =  script that creates a new local variable with name of ```BEST``` and value of ```School```

Task 7: export BEST="School" = script that creates a new global variable with the name of ```BEST``` and value of ```School```

Task 8: echo "$((TRUEKNOWLEDGE+=128))" = script that prints the result of the addition of 128 with the value stored in the environment variable ```TRUEKNOWLEDGE```, followed by a new line

Task 9: echo $((POWER/DIVIDE)) = script that prints the result of POWER divided by DIVIDE, followed by a new line.

Task 10: echo $((BREATH**LOVE)) = script that displays the result of ```BREATH``` to the power ```LOVE```

Task 11: echo "$((2#$BINARY))" = script that converts a number from base 2 to base 10.

Task 12: printf "%s\n" {a..z}{a..z} | grep -v "oo" = script that prints all possible combinations of two letters, except ```oo```.

Task 13: printf "%.2f\n" $NUM = script that prints a number with two decimal places, followed by a new line.

Task 14:

Task 15:

Task 16:

Task 17:

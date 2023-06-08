0x01-shell_permissions exercise.

Task 0: su betty = a script that switches the current user to user betty

Task 1: id -un = a script that prints the effective username of the current user

Task 2: groups = script that prints all the groups the current user is part of

Task 3: sudo chown betty hello = script that changes the owner of the file ```hello``` to user betty

Task 4: touch hello = script that creates an empty file called ```hello```

Task 5: chmod u+x hello = script that adds execute permissions to the owner of current working dir

Task 6: chmod ug+x,o+r hello = script that adds execute permission to owner and the group owner, and read permission to other users

Task 7: chmod ugo+x hello = script that adds execution permission to the owner, group owner and othe users

Task 8: chmod 007 hello = script that sets permission to the file ```hello``` as follows; Owner- no permission at all, Group- no permission at all, Other users- all permissions

Task 9: chmod 753 hello = script that sets mode of the file ```hello``` to this: -rwxr-x-wx

Task 10: chmod --reference=ollh hello = script that sets the mode of the file ```hello``` to the same as file ```olleh```

Task 11: chmod -R +X . = script that add execute permissions to all subdirectories of the current directory for the owner, group owner and all other users

Task 12: mkdir -m 751 my_dir = script that creates a dir called ```my_dir``` with permissions 751 in the working dir

Task 13: chgrp school hello = script that changes the group owner to ```school``` for the file ```hello```

Task 14: chown vincent:staff * = script that changes the owner to ```vincent``` and group owner to ```staff``` for all files and dir in the working dir

Task 15: chown -h vincent:staff _hello = script that changes the owner and the group owner of ```hello``` to ```vincent``` and ```staff``` respectively

Task 16: chown --from=guillaume betty hello = script that changes the owner of the file ```hello``` to user ```betty``` only if it is owned by user ```guillaume```

Task 17:

Task 18:

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

| Task | File |
| ---- | ---- |
| 1. For Best School loop | [1-for_best_school](./1-for_best_school) |
| 2. While Best School loop | [2-while_best_school](./2-while_best_school) |
| 3. Until Best School loop | [3-until_best_school](./3-until_best_school) |
| 4. If 9, say Hi! | [4-if_9_say_hi](./4-if_9_say_hi) |
| 5. 4 bad luck, 8 is your chance | [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance) |
| 6. Superstitious numbers | [6-superstitious_numbers](./6-superstitious_numbers) |
| 7. Clock | [7-clock](./7-clock) |
| 8. For ls | [8-for_ls](./8-for_ls) |
| 9. To file, or not to file | [9-to_file_or_not_to_file](./9-to_file_or_not_to_file) |
| 10. FizzBuzz | [10-fizzbuzz](./10-fizzbuzz) |
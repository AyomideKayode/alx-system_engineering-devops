# Project: 0x14. MySQL

![sql_map](./my_SQL.png)

## Resources

### Read or watch:-

- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

## Learning Objectives

### General

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Tasks

0. [Install MySQL](./README.md) :

First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

- MySQL distribution must be 5.7.x
- Make sure that `task #3` of your [SSH project](../0x0B-ssh/) is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status
- Please make sure you have your `README.md` pushed to GitHub.
Example:

```sh
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

1. [Let us in!](./1-create_holberton_user) :

In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

- Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
- Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
- In addition to that, make sure that `task #3` of your [SSH project](../0x0B-ssh/) is completed for `web-01` and `web-02`. **You will likely need to add the public key to web-02 as you only added it to web-01 for this project**. The checker will connect to your servers to check MySQL status

Example:

```sh
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password: (password for the newly created user, not your mysql password)
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

2. [If only you could see what I've seen with your eyes](./2-database_to_replicate_from) :

In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.

Example:

```sh
mysql> SELECT * FROM nexus6;
+----+---------+
| id | name    |
+----+---------+
|  1 | Ayomide |
+----+---------+
1 row in set (0.00 sec)

mysql>
```

| 3. Quite an experience to live in fear, isn't it?      | [SOON](./)                                                                                                                         |
| 4. Setup a Primary-Replica infrastructure using MySQL  | [4-mysql_configuration_primary](./4-mysql_configuration_primary), [4-mysql_configuration_replica](./4-mysql_configuration_replica) |
| 5. MySQL backup                                        | [5-mysql_backup](./5-mysql_backup)                                                                                                 |

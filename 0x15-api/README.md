# Project: 0x15. API

## Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources

### Read or watch -

- [Friends don't let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://peps.python.org/pep-0008/)

## Learning Objectives

### General

- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

## Tasks

0. [Gather data from an API](./0-gather_data_from_an_API.py) :

Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

Requirements:

- You must use `urllib` or `requests` module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
  - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  - Second and N next lines display the title of completed tasks: `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)

Example:

```sh
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x15-api$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks (8/20):
Ervin Howell: 8 completed tasks out of 20
        distinctio vitae autem nihil ut molestias quo
        voluptas quo tenetur perspiciatis explicabo natus
        aliquam aut quasi
        veritatis pariatur delectus
        nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
        repellendus veritatis molestias dicta incidunt
        excepturi deleniti adipisci voluptatem et neque optio illum ad
        totam atque quo nesciunt
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x15-api$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks (6/20):
Patricia Lebsack: 6 completed tasks out of 20
        odit optio omnis qui sunt
        doloremque aut dolores quidem fuga qui nulla
        sint amet quia totam corporis qui exercitationem commodi
        sequi dolorem sed
        eum ipsa maxime ut
        tempore molestias dolores rerum sequi voluptates ipsum consequatur
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x15-api$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T"
EmployeeSPatriciaSLebsackSisSdoneSwithStasksS(6/20):
PatriciaSLebsack:S6ScompletedStasksSoutSofS20
ToditSoptioSomnisSquiSsunt
TdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TsequiSdoloremSsed
TeumSipsaSmaximeSut
TtemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
ayomide@Kazzywiz:~/alx-system_engineering-devops/0x15-api$
```

| Task                                  | File                                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| 0. Gather data from an API            | [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)                       |
| 1. Export to CSV                      | [1-export_to_CSV.py](./1-export_to_CSV.py)                                           |
| 2. Export to JSON                     | [2-export_to_JSON.py](./2-export_to_JSON.py)                                         |
| 3. Dictionary of list of dictionaries | [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py) |
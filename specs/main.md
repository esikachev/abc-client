# The main spec of ABC project

In this doc, I would like to describe the main aims and ideas of ABC project,
provide some examples of usage. 

ABC is a project for working with storing, backup and moving of config and
other files.

## Use case
For example, you have a laptop and configured tmux, bash, vim tools. In a case
of emergency with your laptop, you can lose all data and you will need to
configure these tools again. Sure, you can use a GitHub for storing this
files, but imagine that you store the old revision of these files in a repo.

## Approximate features
1. Add file for polling by abc
```shell
$ abc add <filename>
```
2. Forced sync of files. Also, files will by sync periodically.
```shell
$ abc sync
```
3. Init local and remote repo(when first time runned)
```shell
$ abc init
```

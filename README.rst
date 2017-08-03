abc-client
==========

This is the client for abc-server located at https://github.com/esikachev/abc-server.

**How to use:**

1. Install abc-server. Instruction is here: https://github.com/esikachev/abc-server/blob/master/README.rst

2. Run command for initialize local repo

.. sourcecode:: console

    $ tox -e venv -- abc --init
..

3. Run command for adding file to sync

.. sourcecode:: console

    $ tox -e venv -- abc --add ~/.vimrc
..

4. Run command for upload files to remote repo

.. sourcecode:: console

    $ tox -e venv -- abc --sync
..

5. Run command for apply files to local host

.. sourcecode:: console

    $ tox -e venv -- abc --apply
..

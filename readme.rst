=================
Setup
=================

Go to sphinx-paver folder and::

  python bootstrap.py

This will create a virtualenv environment. To activate the envinronment do::

  source virtualenv/bin/activate

.. note::
   This should be done every time you open a new shell

Now initialize Sphinx::

  sphinx-quickstart

Specify to use different source and build folders::

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/N) [n]: y

Build for the first time the html pages::

    make html

Now you can start the server which will rebuild automatically if the source folder changes::

    paver server
==========
Installing
==========

You may need to install some things to
test and see by yourself how the AI gets
smarter and smarter over time.

Python 3
########

As long as we don't have the binaries to
share with you, you'll need to install
python 3.6+ in your computer, but don't
worry, it's not a complicated thing.

Go to the `python <https://www.python.org>`_
and head to the "Downloads" section. Then,
select your OS in the list and it'll redirect
you to a list of python releases. Download the
latest 3.x version and follow the setup installing
instructions to get python working on your machine.

.. note:: If you are using Windows, don't forget to check the "Add to PATH" option while installing, because if you forget to check it, you won't be able to run python console, pip, or any python file in CMD

But I can hear someone say:

    *I can't find Linux in the Downloads section*

No need to worry, you'll need to take a different
path (a shortcut, if you allow me to say) in order
to install python. Here's some examples based on
some major linux distros:

Ubuntu/Debian:

.. code-block:: console

    sudo apt-get install python3

Fedora/Red Hat:

.. code-block:: console

    sudo yum install python3

Arch/Manjaro:

.. code-block:: console

    sudo pacman -S python3

To check if python is installed, just open the
CMD (Windows) or the console (Linux/Mac) and type

.. code-block:: console

    python3 --version 

You should get a message like "Python 3.x.x"
indicating the python version you installed

Graphviz
########

Graphviz is a graph visualization software
that we've used to plot all AI generations
and it's progress changing over time.

You can download it `here <https://www.graphviz.org/>`_
just go to the "Downloads" section and follow along
with the instructions. They explain how to install
it in Windows, major linux distros and Mac.

PIP Requirements
################

Now that you have all third-party software up
and running in your computer, you'll have to
install python package dependencies. Fortunately,
we've made a PIP package listing for you.

Just open the terminal/CMD, go to the folder
where you extracted/cloned the git repo and type:

Linux/Mac:

.. code-block:: console

    pip3 install -r requirements.txt


Windows:

.. code-block:: console

    python -m pip install -r requirements.txt

You should see the PIP fetching the packages and
automatically installing it for you.

Now simply run the ``main.py`` file:

.. code-block:: console

    python3 main.py

And yay, it works! (or not, i dunno)

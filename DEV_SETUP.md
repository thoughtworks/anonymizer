# Instructions to setup dev environment

Anonymizer is written in Python, and uses `pip` to install its required packages. We also highly recommended
that you use `virtualenv` to create an isolated environment where the packages can be installed.

This document explains how to setup a developer environment.

## MacOS X

MacOS ships with Python 2.7.1, which should suffice to get up and running with everything. If you already have
pip and virtualenv setup, you can skip to the next section.

`pip` is a tool to install and manage Python packages. `virtualenv` is a tool to create isolated python environments
(similar to Ruby's `rvm`). `virtualenvwrapper` is a helper that makes it easy to setup and use `virtualenv`, creating
aliases and storing environments under `~/.virtualenvs` (similar to RVM). To install them:

   ```
   $ sudo easy_install pip
   $ sudo pip install virtualenv
   $ sudo pip install virtualenvwrapper
   ```

`virtualenvwrapper` will require you to add the following to the end of your `~/.profile` or `~/.bash_profile`:

   ```
   # virtualenv
   export WORKON_HOME=$HOME/.virtualenvs
   source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh
   ```

Once you've done that, run:

   ```
   $ source ~/.bash_profile # or ~/.profile
   ```

## Setting up a virtualenv for developing anonymizer

Clone the repository from github:

   ```
   $ git clone https://github.com/thoughtworks/anonymizer.git
   $ cd anonymizer
   ```

Create a new virtualenv for this project and install its dependencies:

   ```
   $ mkvirtualenv --no-site-packages anonymizer
   $ pip install -r requirements.txt
   ```

When you want to deactivate the anonymizer environment, simply run:

   ```
   $ deactivate
   ```

When you want to get back to work on anonymizer, run:

   ```
   $ workon anonymizer
   ```

## TODO

* How to run tests
* How to run the application


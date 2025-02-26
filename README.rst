|Icon| |title|_
===============

.. |title| replace:: linreg-helpers
.. _title: https://kunlun-wu.github.io/linreg-helpers

.. |Icon| image:: https://avatars.githubusercontent.com/kunlun-wu
        :target: https://kunlun-wu.github.io/linreg-helpers
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/kunlun-wu/linreg-helpers/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/kunlun-wu/linreg-helpers/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/kunlun-wu/linreg-helpers/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/kunlun-wu/linreg-helpers

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/linreg-helpers
        :target: https://anaconda.org/conda-forge/linreg-helpers

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/linreg-helpers
        :target: https://pypi.org/project/linreg-helpers/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/linreg-helpers
        :target: https://pypi.org/project/linreg-helpers/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/kunlun-wu/linreg-helpers/issues

Simple helper functions for linear regression

* LONGER DESCRIPTION HERE

For more information about the linreg-helpers library, please consult our `online documentation <https://kunlun-wu.github.io/linreg-helpers>`_.

Citation
--------

If you use linreg-helpers in a scientific publication, we would like you to cite this package as

        linreg-helpers Package, https://github.com/kunlun-wu/linreg-helpers

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``linreg-helpers_env`` ::

        conda create -n linreg-helpers_env linreg-helpers
        conda activate linreg-helpers_env

To confirm that the installation was successful, type ::

        python -c "import linreg_helpers; print(linreg_helpers.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``linreg-helpers_env`` environment, type ::

        pip install linreg-helpers

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/kunlun-wu/linreg-helpers/>`_. Once installed, ``cd`` into your ``linreg-helpers`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://kunlun-wu.github.io/linreg-helpers>`_ for tutorials and API references.

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of linreg-helpers. Please join the linreg-helpers users community by joining the Google group. The linreg-helpers project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/kunlun-wu/linreg-helpers/issues>`_ and/or `submit a fix as a PR <https://github.com/kunlun-wu/linreg-helpers/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_.

Feel free to fork the project and contribute. To install linreg-helpers
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/kunlun-wu/linreg-helpers/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on linreg-helpers please visit the project `web-page <https://kunlun-wu.github.io/>`_ or email Prof. Kunlun Wu at kw3037@columbia.edu.

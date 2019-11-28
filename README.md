# A Network Tour of Data Science, edition 2019

[![Binder](https://mybinder.org/badge_logo.svg)][binder]

[binder]: https://mybinder.org/v2/gh/mdeff/ntds_2019/outputs?urlpath=lab

This repository contains the material for the practical work associated with the EPFL master course [EE-558 A Network Tour of Data Science][epfl] ([moodle]), taught in fall 2019.
The content is similar to the [2017] and [2018] editions, with more emphasis on machine learning with graphs.
Compared to the [2016 edition], the course has been refocused on graph and network sciences.
The course is divided in two parts: **Network Science** and **Learning with Graphs**.
The material revolves around the following topics:

1. [Network Science](https://en.wikipedia.org/wiki/Network_science),
1. [Spectral Graph Theory](https://en.wikipedia.org/wiki/Spectral_graph_theory),
1. [Graph Signal Processing](https://arxiv.org/abs/1211.0053),
1. [Data Science](https://en.wikipedia.org/wiki/Data_science),
1. [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning).

Theoretical knowledge is taught during lectures.
Practical knowledge is taught through [tutorials](#tutorials).
Both are practiced and evaluated through [two assignments](#assignments) and a [semester project](#projects).
Below are slides about the organization of the course.

1. [Course organization][practical_info]
1. [Projects][projects]
1. Concluding remarks

[epfl]: https://edu.epfl.ch/coursebook/en/a-network-tour-of-data-science-EE-558
[moodle]: https://moodle.epfl.ch/course/view.php?id=15299
[2016 edition]: https://github.com/mdeff/ntds_2016
[2017]: https://github.com/mdeff/ntds_2017
[2018]: https://github.com/mdeff/ntds_2018

[practical_info]: https://github.com/mdeff/ntds_2019/blob/outputs/slides/ntds_info.pdf
[projects]: https://github.com/mdeff/ntds_2019/blob/outputs/slides/ntds_projects.pdf

## Tutorials

Below is the teaching material you'll find in this repository (tentative).

1. [Installation instructions](#installation)
1. [Introduction][t01]
1. [Building graphs from edge lists][t02]
1. [Building graphs from features][t03]
1. [Manipulating graphs with NetworkX][t04]
1. [Machine learning with scikit-learn][t05]
1. Learning on graphs with pytorch
1. Sparse matrices with scipy
1. Linear algebra for graphs and networkx
1. Graph signal processing with pygsp
1. Interactive graph visualization with gephi

[t01]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/tutorials/01_introduction.ipynb
[t02]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/tutorials/02_graph_from_edge_list.ipynb
[t03]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/tutorials/03_graph_from_features.ipynb
[t04]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/tutorials/04_networkx.ipynb
[t05]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/tutorials/05_scikit_learn.ipynb

For this course, you'll use the following tools:
[conda] & [anaconda], [python], [jupyter], [git], [numpy], [scipy], [matplotlib], [pandas], [networkx], [graph-tool], [pygsp], [gephi], [scikit-learn], [pytorch].

[conda]: https://conda.io
[anaconda]: https://anaconda.org
[python]: https://www.python.org
[jupyter]: https://jupyter.org
[git]: https://git-scm.com
[numpy]: https://www.numpy.org
[scipy]: https://www.scipy.org
[matplotlib]: https://matplotlib.org
[pandas]: https://pandas.pydata.org
[networkx]: https://networkx.github.io
[graph-tool]: https://graph-tool.skewed.de
[pygsp]: https://pygsp.readthedocs.io
[gephi]: https://gephi.org
[scikit-learn]: https://scikit-learn.org
[pytorch]: https://pytorch.org

## Assignments

The following assignments were designed to evaluate the theoretical understanding of students through practice.
As a Data Science course, those activities are realized on real data and networks.

1. Network science: [assignment][a1q], [solution][a1s].
1. Learning with graphs: [assignment][a2q], solution, feedback.

[a1q]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/assignments/1_network_science.ipynb
[a1s]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/assignments/1_network_science_solution.ipynb
[a2q]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/assignments/2_learning_with_graphs.ipynb

## Projects

Part of the course is evaluated by an open-ended project (see the [description][projects]), proposed and carried out by groups of four students.
We provide a list of [datasets and project ideas](projects).
Students review each other's work to receive intermediate feedback and internalize the [grading criteria](projects/grading.md).
Those data projects are meant to jointly practice and evaluate their theoretical network analysis skills and practical Data Science skills.
Below is the work of the 137 students enrolled that year.

* [report, slides, code] Project Title

As each team stored their code in a github repository, all their code can conveniently be downloaded with `git clone --recurse-submodules https://github.com/mdeff/ntds_2019`.
One folder per team will be populated in `projects/code`.

## Installation

Click the [binder badge][binder] to play with the notebooks from your browser without installing anything.

Another option is to use the EPFL's JupyterHub service, available at <https://noto.epfl.ch>.
While the default environment has most packages pre-installed, you can create different environments (e.g., for different classes).
To do so, follow the instructions contained in the notebooks supplied in the `Documentation` folder that is available on your Noto instance.

For a local installation, you will need [git], [Python], and packages from the [Python scientific stack][scipy].
If you don't know how to install those on your platform, we recommend to install [Miniconda] or [Anaconda], a distribution of the [conda] package and environment manager.
Follow the below instructions to install it and create an environment for the course.

1. Download the Python 3.x installer for Windows, macOS, or Linux from <https://conda.io/miniconda.html> and install with default settings.
   Skip this step if you have conda already installed (from [Miniconda] or [Anaconda]).
   * Windows: double-click on `Miniconda3-latest-Windows-x86_64.exe`.
   * macOS: double-click on `Miniconda3-latest-MacOSX-x86_64.pkg` or run `bash Miniconda3-latest-MacOSX-x86_64.sh` in a terminal.
   * Linux: run `bash Miniconda3-latest-Linux-x86_64.sh` in a terminal or use your package manager.
1. Open a terminal.
   Windows: open the Anaconda Prompt from the Start menu.
1. Install git with `conda install git`.
1. Navigate to the folder where you want to store the course material with `cd path/to/folder`.
1. Download this repository with `git clone https://github.com/mdeff/ntds_2019`.
1. Enter the repository with `cd ntds_2019`.
1. Create an environment with the packages required for the course with `conda env create -f environment.yml`.
1. Run the steps below to start Jupyter. You should be able to run the [`test_install.ipynb`][test_install] notebook.

[test_install]: https://nbviewer.jupyter.org/github/mdeff/ntds_2019/blob/outputs/test_install.ipynb

Every time you want to work, do the following:

1. Open a terminal.
   Windows: open the Anaconda Prompt from the Start menu.
1. Activate the environment with `conda activate ntds_2019`.
1. Navigate to the folder where you stored the course material with `cd path/to/folder/ntds_2019`.
1. Start Jupyter with `jupyter lab`.
   The command should open a new tab in your web browser.
1. Edit and run the notebooks from your browser.
1. Once done, you can run `conda deactivate` to leave the `ntds_2019` environment.

[git]: https://git-scm.com
[python]: https://www.python.org
[scipy]: https://www.scipy.org
[anaconda]: https://www.anaconda.com/download
[miniconda]: https://conda.io/miniconda.html
[conda]: https://conda.io
[conda-forge]: https://conda-forge.org

## Team

* Instructors:
[Pierre Vandergheynst](https://people.epfl.ch/pierre.vandergheynst),
[Pascal Frossard](https://people.epfl.ch/pascal.frossard),
[Andreas Loukas](https://andreasloukas.blog),
[Michaël Defferrard](https://deff.ch),
[Volodymyr Miz](http://miz.space).
* Assistants:
[Michaël Defferrard](https://deff.ch),
[Volodymyr Miz](http://miz.space),
[Effrosyni Simou](https://people.epfl.ch/effrosyni.simou),
[Eda Bayram](https://people.epfl.ch/eda.bayram),
[Benjamin Ricaud](https://github.com/bricaud),
[Nicolas Aspert](https://people.epfl.ch/nicolas.aspert),
[Clément Vignac](https://people.epfl.ch/clement.vignac),
[Guillermo Jiménez](https://gortizji.github.io),
[Nikolaos Karalias](https://people.epfl.ch/nikolaos.karalias).

## License

The content is released under the terms of the [MIT License](LICENSE.txt).

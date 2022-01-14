# slimeda

Exploratory Data Analysis is an important preparatory work to help data scientists understand and clean up data sets before machine learning begins. However, this step also involves a lot of repetitive tasks. In this context, slimeda will help data scientists quickly complete the initial work of EDA and gain a preliminary understanding of the data.

Slimeda focuses on unique value and missing value counts, as well as making graphs like histogram and correlation graphs. Also, the generated results are designed as charts or images, which will help users more flexibly reference their EDA results.

## Installation

```bash
$ pip install slimeda
```
## Functions
- Merged with Taiwo's pr.
## Usage

- To do (will complete this part in milestone2)

## Fitting in Python Ecosystem
- The packages have similar functions are:
    - [numpy](https://numpy.org/): can count unique value and missing value
    - [pandas-profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/): can generate basic eda reports.

- Slimeda's innovation points:
    - Compared with packages with massive functions, we focus on eda and simplify the code.
    - Compared with numpy, we extracted specific functions needed in eda and also optimize the output to be more clear.
    - Compared with pandas-profiling, we generate the most commonly used graphs and make possible for png outputs, which is much more flexible for users to get their eda results.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## CONTRIBUTORS

Group 4 members:
- Khalid Abdilahi (@khalidcawl)
- Anthea Chen (@anthea98)
- Simon Guo (@y248guo)
- Taiwo Owoseni (@thayeylolu)


## License

`slimeda` was created by Simon Guo. It is licensed under the terms of the MIT license.

## Credits

`slimeda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

# slimeda

Slim version of EDA processing Python package
## Function Specification

The package is under developement and includes the following functions:

- **histogram** : This function accepts a dataframe and builds histograms for all numeric columns which are returned 
as an array of chart objects. The user has the option to save the image to path.

- **corrmap** : This function accepts a dataframe and builds an heat map for all numeric columns which is returned 
as a chart object. The user has the option to save the image to path.

- **cat_unique_count** : This function accepts a dataframe and returns a table of unique value counts for all categorical columns.

- **miss_counts** : This function accepts a dataframe and returns a table of counts of missing values in all columns.

Limitations:
We only consider numeric and categorical columns in our package.
## Installation

```bash
$ pip install slimeda
```

## Usage

- TODO

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

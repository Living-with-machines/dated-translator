# dated-translator

[![All Contributors](https://img.shields.io/github/all-contributors/Living-with-machines/dated-translator?color=ee8449&style=flat-square)](#contributors)

A Python package that helps translate from one term to another, depending on a passed date, from a CSV that contains some verified information.

## Getting started

### Installation

You can install this package using `pip`:

```sh
$ pip install dated_translator
```

### First lookup

Set up the lookup object first. In this case, we have a `data_file.csv` which contains (at least) four required columns: `Term 1`, `Term 2`, `Start Date`, and `End Date`. For a more advanced setup, see below.

```py
lookup = Lookup(dataset="data_file.csv")

lookup.left_translate("Term 1", "1800-01-01") # Will return a list with the values of term 2 that exist in any given span of start and end date

lookup.right_translate("Term 2", "1800-01-01") # Will return a list with the values of term 1 that exist in any given span of start and end date
```

## Advanced setup

_This example is a real-world example from the Living with Machines project, and if you want to test it yourself (after installing the package), you can clone this repository and check out the example/`Example.ipynb` notebook._

Say that we have a list of newspaper titles with different abbreviations, and we need to check which identification number, `NLP` that each abbreviation is associated with, within a certain date range.

The file that we'd pass to the setup of the `Lookup` object, in this example called `JISC-papers.csv`, would look something like this:


| Newspaper Title                                                          | NLP | Normalised Title | Abbr | StartD | StartM | StartY | EndD | EndM | EndY |
| ------------------------------------------------------------------------ | --- | ---------------- | ---- | ------ | ------ | ------ | ---- | ---- | ---- |
| Aberdeen Journal and general advertiser for the north of Scotland, The   | 31  | Aberdeen Journal | ANJO | 1      | Jan    | 1800   | 23   | Aug  | 1876 |
| Aberdeen Weekly Journal and general advertiser for the north of Scotland | 32  | Aberdeen Journal | ANJO | 30     | Aug    | 1876   | 31   | Dec  | 1900 |

In this example, we want to get the resulting `NLP` **31** for any ANJO abbreviations (`Abbr`) between 1881-01-01 and 1876-08-23, and **32** for any of the same abbreviation between 1876-08-30 and 1900-12-31.

To set this up, we need to pass the dataset's name, and specify the names of the lookup's term 1 (`Abbr`) and term 2 (`NLP`). _Note: It doesn't matter in which order you pass them, but which one is considered term 1 and 2 will affect our `left_translate` and `right_translate` methods further down the line._

We also need to specify the particular date column format in our file. Since we're not using the standard setup here (a `Start Date` and `End Date` column respectively), we can pass a dictionary which requires three items, specifying the name of the year, month, and day columns, and their date formatting. We do so for both the start date and end date columns:

```py
lookup = Lookup(
    dataset="JISC-papers.csv",
    term_1_column = "Abbr",
    term_2_column = "NLP",
    start_date_column = {
        "StartY": "%Y",
        "StartM": "%b",
        "StartD": "%d"
    },
    end_date_column = {
        "EndY": "%Y",
        "EndM": "%b",
        "EndD": "%d"
    }
)
```

After this setup, we can run the `left_translate` method to check what the `NLP` is for the abbreviation "ANJO" on the date 1800-01-01:

```py
lookup.left_translate("ANJO", "1800-01-01")
```

This should return the value: `[31]`, that is, a list of the possible NLPs for this abbreviation on this particular date.

Similarly, we can run the `right_translate` method to check what the `Abbr` is for a given `NLP` (31) on the date 1800-01-01:

```py
lookup.right_translate(31, "1800-01-01")
```

The result should, in a reverse of the result above, be `['ANJO']`, that is, a list of the possible abbreviations for this NLP in on this particular date.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

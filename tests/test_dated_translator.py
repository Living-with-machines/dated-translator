import pytest
from dated_translator import __version__, Lookup
from dated_translator.exceptions import SetupError, MissingColumn


def test_version():
    assert __version__ == "0.1.0"


def test_Lookup_simple_setup():
    assert Lookup(dataset="tests/assets/JISC-papers-simple-format.csv")


def test_Lookup_required_args():
    with pytest.raises(SetupError) as e_info:
        Lookup()


def test_Lookup_term_1_column_format():
    with pytest.raises(SetupError) as e_info:
        Lookup(dataset="tests/assets/JISC-papers-simple-format.csv", term_1_column={})


def test_Lookup_term_2_column_format():
    with pytest.raises(SetupError) as e_info:
        Lookup(dataset="tests/assets/JISC-papers-simple-format.csv", term_2_column={})


def test_Lookup_start_date_column_format():
    with pytest.raises(SetupError) as e_info:
        Lookup(
            dataset="tests/assets/JISC-papers-simple-format.csv", start_date_column=24
        )


def test_Lookup_end_date_column_format():
    with pytest.raises(SetupError) as e_info:
        Lookup(dataset="tests/assets/JISC-papers-simple-format.csv", end_date_column=24)


def test_Lookup_missing_start_date_column():
    with pytest.raises(MissingColumn) as e_info:
        Lookup(dataset="tests/assets/JISC-papers-missing-start-date-column.csv")


def test_Lookup_missing_end_date_column():
    with pytest.raises(MissingColumn) as e_info:
        Lookup(dataset="tests/assets/JISC-papers-missing-end-date-column.csv")

import pytest

from string_calculator.string_calculator import add


def test_add_with_empty_string():
    assert add("") == 0


@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        ([1, 2, 3, 8], "The numbers of the function argument must be a string"),
        ((1, 4, 5), "The numbers of the function argument must be a string"),
    ],
)
def test_argument_data_type(input_string, expected_error):
    with pytest.raises(TypeError, match=expected_error):
        add(input_string)


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("1", 1),
        ("5", 5),
        ("9", 9),
        ("67", 67),
        ("451", 451),
    ],
)
def test_add_with_int_chars(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("1,2,4,5", 12),
        ("4,6,6", 16),
        ("1,2,3,4", 10),
        ("1\n2,3", 6),
        (
            "4,6\n6",
            16,
        ),
        ("4\n5,1", 10),
    ],
)
def test_add_with_multiple_int_chars(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("//;\n1;2", 3),
        ("//4\n142", 3),
        ("//;\n1", 1),
        ("//;\n", 0),
    ],
)
def test_add_with_custom_delimiter(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        ("//88\n18882", "ERROR: invalid input"),
        ("//5\n25553", "ERROR: invalid input"),
        ("//666\n86666699", "ERROR: invalid input"),
    ],
)
def test_add_delimiter_appears_consecutively(input_string, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        add(input_string)


@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        ("//4\n434243", "ERROR: invalid input"),
        ("//4\n342434", "ERROR: invalid input"),
        ("//4\n4342434", "ERROR: invalid input"),
    ],
)
def test_add_with_delimiter_at_start_or_end(input_string, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        add(input_string)


@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        ("-1,-2,3,4", "negatives not allowed: -1, -2"),
        ("-5,-1,-6, 9", "negatives not allowed: -5, -1, -6"),
        ("1, 5, 6, -8", "negatives not allowed: -8"),
    ],
)
def test_add_with_negative_integers(input_string, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        add(input_string)


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("//***\n1***2***3", 6),
        ("//444\n34446", 9),
        ("//####\n2####4####9", 15),
    ],
)
def test_add_with_delimiters_any_length(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("//;\n1000;1;2", 3),
        ("1001,2", 2),
        ("//***\n1000***1001***3", 3),
    ],
)
def test_add_ignoring_large_integers(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("//[:D][%]\n1:D2%3", 6),
        ("//[***][%%%]\n1***2%%%3", 6),
        ("//[(-_-')][%]\n1(-_-')2%3", 6),
        ("//[abc][777][:(]\n1abc27773:(1", 7),
    ],
)
def test_add_with_multiple_custom_delimiters(input_string, expected_result):
    assert add(input_string) == expected_result


@pytest.mark.parametrize(
    "input_string, expected_error",
    [
        ("//[\n1[2[3[4", "ERROR: invalid input"),
        ("//]\n90]11]20", "ERROR: invalid input"),
        ("//[[][[][&&]\n1[2[3&&4", "ERROR: invalid input"),
    ],
)
def test_add_with_square_bracket_delimiters(input_string, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        add(input_string)

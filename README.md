# String-calculator (266)
## Project Overview

* **Objective:** Create a string calculator that adds integer characters in a string with any custom delimetter
* **Project Instructions:** [here]( http://syllabus.africacode.net/projects/tdd/string-calculator-part-1/)
* **Package under test:** `string_calculator`
* **Test directory:** `tests`

## Prerequisites

- Python 3.x

## File Structure
```
├── string_calculator  
│   └── string_calculator.py
├── requirements.txt    
├── setup.py  
├── .gitignore          
└── tests               
    └── test_string_calculator.py
```

## Installation and Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Thxbiso-DS/string-calculator.git
    ```

2. **Navigate to the directory:**
    ```bash
    cd string-calculator/
    ```

3. **Create a virtual environment:**
    ```bash 
    python  -m venv string-env
    ```

4. **Activate the virtual environment:**
- On Windows:
  ```
  .\string-env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source string-env/bin/activate
  ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Install the `setup.py` file to import the string calculator package**
    ```bash
    pip install -e .
    ```

7. **Set the PYTHONPATH explicitly to include the root directory of the project: Include the path from your home directory to the project directory**
   ```bash
    export PYTHONPATH=/path/from/home/to/Thabiso-Mokgete-266-string-calculator-python:$PYTHONPATH

   ```

## Usage

1. Now that the package has been installed you can run the tests from the main directory:
   ```bash
   pytest tests/test_string_calculator.py
    ```
2. Once you are finished you can deactivate your virtual environment:
    ```bash
    deactivate
    ```


### Using the String Calculator Package

1. After installation, you can import the `string_calculator` package in your Python scripts or interactive sessions.

    ```python
    from string_calculator.string_calculator import add
    ```

2. Use the `add`  function on a string with integers to perform arithmetic operations:

    ```python

    add_strings_with_comma = add("4,6,6")
    print(add_strings_with_comma) # Prints 16

    add_with_semi_colon_delimeter = add("//;\n5;6")
    print(add_with_semi_colon_delimeter) # Prints 11
    ```

3. You can also use the package in interactive Python sessions or in Python scripts as needed.

## Author 
Thabiso Mokgete  
* s.mokgete@gmail.com

## License 
Copyright © 2023 [Thabiso Mokgete](https://github.com/Thxbiso-DS).<br />
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
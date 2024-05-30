# Morsil: Morse Code Converter

Morsil is a Python program that converts text between ASCII and Morse code. It also includes a simulated loading sequence and error handling for user input. This program can be useful for educational purposes or for anyone interested in learning Morse code.

## Features

- Clear the console before starting the conversion process.
- Simulate a loading sequence with delays and sound effects.
- Convert text from ASCII to Morse code and vice versa.
- Provide error messages for invalid input.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone (me)
    cd (me)
    ```

2. Ensure you have Python 3 installed. If not, download and install it from [python.org](https://www.python.org/).

### Running the Program

1. Navigate to the directory containing the script:
    ```bash
    cd (me)
    ```

2. Run the script:
    ```bash
    python morsil.py
    ```

## Code Explanation

### clear_console Function

Clears the console screen based on the operating system.

```python
def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Other systems (Linux, MacOS)
        os.system('clear')

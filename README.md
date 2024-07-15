# Password Evaluation Tool

## Overview
This tool evaluates the strength of a password and estimates the time required to crack it using brute force attacks. It demonstrates the use of Strategy, Factory, and Singleton design patterns.

## Project Structure
password_checker/
│
├── checker/
│ ├── init.py
│ ├── base_strategy.py
│ ├── strength_checker.py
│ ├── time_to_crack_calculator.py
│ └── strategy_factory.py
│
├── config/
│ ├── init.py
│ └── settings.py
│
├── main.py
└── README.md

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run the main script:
    ```
    python main.py
    ```

## Design Patterns Used
- **Singleton**: Ensures only one instance of the settings is used.
- **Strategy**: Defines different password evaluation strategies.
- **Factory**: Creates instances of the different strategies.

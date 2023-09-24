# Cron Expression Parser

# Introduction 
This project is a cron expression parser that converts a cron expression into a human-readable format. It takes cron string as input and outputs a human readable format of the cron string

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python >= 3.6


### Installation

Clone this repository:

```bash
git clone https://github.com/ManiYaswanth/cron_expression_parser
```

## Usage
1. Open a terminal and in the directory cron_expression_parser run the following command
```bash
python3 main.py "your-cron-string"
```
replace your-cron-string with a cron_string of your choice.

2. Output is printed into a human readable format

3. To run the tests written in cron_test.py file
```bash
python3 -m unittest cron_test.py
```

## Features
Takes input directly from terminal and outputs the human readable format of cron string.
Handles various cron fields (Minutes, Hours, Day of week, Day of Month, Month) and expressions(-, *, /)

## Contribute
Contributions are welcome! Feel free to open issues and pull requests.
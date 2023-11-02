[![CI](https://github.com/nogibjj/mini-project5-lisa/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/nogibjj/mini-project5-lisa/actions/workflows/cicd.yml)

[![Rust CI/CD](https://github.com/nogibjj/lisa-mini-project-8/actions/workflows/rust-cicd.yml/badge.svg)](https://github.com/nogibjj/lisa-mini-project-8/actions/workflows/rust-cicd.yml)

## Python to Rust Script Conversion Project

Welcome to the Week 8 class project repository, where I have undertaken the task of rewriting a Python script for data processing in Rust. This README file provides an overview of the project, requirements, grading criteria, findings, and future work.

### Project Overview

In this project, I aimed to take an existing Python script for data processing and rewrite it in Rust. The primary objectives were to highlight improvements in terms of speed and resource usage achieved by transitioning to Rust, a system-level programming language known for its performance and efficiency.

### Requirements

To successfully complete this project, I followed these requirements:

- **Rewrite in Rust:** I took an existing Python script and translated it into Rust.

- **Highlight Improvements:** I focused on demonstrating improvements in terms of processing speed and resource usage when comparing the Rust implementation to the original Python script.


### Data Processing Workflow

In both the Python and Rust projects, I extracted data from a dataset hosted on GitHub and followed these steps:

1. **Data Extraction:** I collected data from the GitHub dataset.

2. **Data Transformation:** The data was transformed as necessary to prepare it for further analysis.

3. **Data Loading:** I loaded the transformed data into a SQLite database table using Python's SQLite3 module for the Python project and Rusqlite for the Rust project.
   
4.  **Data Query:** SQL queries were written and executed on the SQLite database to analyze and retrieve insights from the data.

5. **Get Metrics Data:** I measure the performance of both projects.

6.  **Command-line Interface:** I provided a command-line interface for both Python and Rust, enabling the following command-line argument:

   - `--all`: If this flag is provided, the script runs all ETL (Extract, Transform, Load, Query) tasks.

### Project Structure

To maintain a well-organized project, I have structured it as follows:

#### Python
- `main.py`: Main Python code for data processing.
- `test_main.py`: Test scripts for code validation.
- `/mylib`: Library codes and utility functions.
- `test` folder: Additional test files for thorough testing.
- `MakeFile`: Configuration for building the project.
- `Requirement.txt`: A list of required packages and dependencies.

#### Rust (Under `rust_etl` Folder)
- `src`: Rust source code for data processing.
- `Cargo.toml`: Configuration for Rust's package manager, Cargo.

#### Other
- `cicd.yml`: GitHub Actions workflow for Continuous Integration and Continuous Deployment (CI/CD).
- `data` folder: A directory to store extracted data in CSV format.
- `OfferDB.db`: SQLite database file created to store processed data.

### Performance Metrics

To measure the performance of both projects, I collected the following metrics:

#### Python Metrics

- Time taken: 0.15 seconds
- Memory used: 21.79 MB
- Average CPU usage: 8.6%

#### Rust Metrics
- Time elapsed in extract, transform, and query: 29.03 seconds
- Total virtual memory used: 294 MB


### Findings

My findings showed that, surprisingly, the Rust implementation did not outperform the Python script in terms of execution time. This could be attributed to my limited familiarity with Rust, which may have led to less efficient code.

### Future Work

In future projects, I plan to address the following:

- **Improve Rust Pipeline:** I aim to make the Rust project fully functional and more accessible, possibly by addressing folder structure issues.

- **Optimize Rust Code:** I will analyze what went wrong in the Rust implementation and work on optimizing the code for better performance.

- **Create Rust Binaries:** I intend to learn how to compile Rust code into binaries, making it easier to execute from the command line.

- **Add Linting, Formatting, and Testing:** In future Rust-related projects, I will incorporate best practices such as code linting, formatting, and testing to ensure code quality and reliability.

Thank you for exploring my Python to Rust Script Conversion Project. I look forward to continued improvements and learning experiences in the realm of Rust programming.


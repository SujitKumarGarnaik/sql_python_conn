# FAQ Bot with MySQL and Python

This project implements a simple FAQ bot that uses predefined question-answer pairs. The bot retrieves answers based on user queries. The project also includes instructions for connecting Python to a MySQL database, where FAQ data can be stored and queried.

## Features
- A conversational FAQ bot implemented in Python.
- It fetches answers based on user input from a predefined set of question-answer pairs.
- The bot can be extended to pull data from a MySQL database for dynamic FAQs.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` (for MySQL connection)
- `langgraph` (for designing conversational AI flows)

## Installation and Setup

### Step 1: Install Dependencies

1. **Install MySQL** (if not already installed):
   - Download and install MySQL from [MySQL Downloads](https://dev.mysql.com/downloads/).
   - Set up a MySQL user and database. For example, create a database called `faq_db` for storing FAQ data.

2. **Install Python packages**:
   - Use the following commands to install the required libraries:

   ```bash
   pip install mysql-connector-python
   pip install langgraph

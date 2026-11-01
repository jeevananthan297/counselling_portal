# IXGVA University -- Engineering & Technology Counselling Portal

A Python-based, console-driven application that simulates an engineering
admission and counselling process. The project brings together student
registration, input validation, Excel-based data handling with Pandas,
choice filling, and a basic provisional seat-allotment simulation.

> **Project type:** Learning project / prototype\
> **Domain:** Engineering and Technology Admissions\
> **Primary language:** Python\
> **Data handling:** Pandas + Microsoft Excel

------------------------------------------------------------------------

## Table of Contents

-   [About the Project](#about-the-project)
-   [Project Objectives](#project-objectives)
-   [Application Workflow](#application-workflow)
-   [Main Features](#main-features)
-   [Registration Brochure](#registration-brochure)
-   [Choice-Filling Brochure](#choice-filling-brochure)
-   [Provisional Allotment
    Simulation](#provisional-allotment-simulation)
-   [Technology Stack](#technology-stack)
-   [Excel Dataset](#excel-dataset)
-   [Project Structure](#project-structure)
-   [Installation and Setup](#installation-and-setup)
-   [How to Run](#how-to-run)
-   [How to Use the Portal](#how-to-use-the-portal)
-   [Input Validation](#input-validation)
-   [Learning Outcomes](#learning-outcomes)
-   [Current Scope and Limitations](#current-scope-and-limitations)
-   [Responsible Use of Sample Data](#responsible-use-of-sample-data)
-   [Future Improvements](#future-improvements)
-   [Acknowledgements](#acknowledgements)

------------------------------------------------------------------------

## About the Project

**IXGVA University -- Engineering & Technology Counselling Portal** is a
console-based Python application created to explore how a student
admission and counselling workflow could be represented through
programming.

The application provides a menu-driven interface through which a student
can register, sign in, recover a password, view a dashboard, enter
engineering-course preferences, and proceed through a basic provisional
allotment simulation.

The project was developed as a hands-on programming exercise. The aim
was not simply to write isolated Python programs, but to bring together
different programming concepts and understand how they interact in a
larger application.

The application uses **Pandas** to read, filter, append, and update
student records stored in an Excel workbook.

**Important:** IXGVA University is a fictional project environment
created for this programming simulation. This application is not an
official university portal, government counselling platform, or real
admission authority.

------------------------------------------------------------------------

## Project Objectives

The project was developed to practise and explore:

-   Building a menu-driven application using Python.
-   Collecting student information through console input.
-   Applying validation rules to user-entered data.
-   Reading and processing Excel records using Pandas.
-   Searching student records using email and password details.
-   Updating an existing record during password recovery.
-   Allowing students to enter and prioritise course and campus
    preferences.
-   Demonstrating a basic cutoff-based allotment workflow.
-   Saving new student records back to an Excel workbook.

------------------------------------------------------------------------

## Application Workflow

The overall flow of the application is:

1.  The user opens the IXGVA University portal.
2.  The main menu displays the available options.
3.  A new student can choose registration and enter the requested
    information.
4.  The application validates the entered details.
5.  The student can proceed to choice filling after registration.
6.  The student enters branch and campus preferences in the prescribed
    format.
7.  The application displays the submitted preference list and asks for
    confirmation.
8.  If the user proceeds, the program runs its provisional allotment
    simulation.
9.  Student information and the available allotment result are saved to
    the Excel workbook.
10. A registered student can later log in and view the student
    dashboard.

The main menu contains these options:

  Option   Function
  -------- -----------------
  `1`      Login
  `2`      Forget Password
  `3`      Register
  `4`      Exit Portal

------------------------------------------------------------------------

## Main Features

### 1. Student Registration

The registration process collects personal, demographic, and academic
details. The program applies input checks before proceeding.

After registration and the choice-filling/allotment flow, the student's
record is appended to the Excel database and an application number is
generated from the existing records.

### 2. Input Validation

The program contains custom validation logic for several fields,
including:

-   Email address format.
-   Password length and character requirements.
-   Date-of-birth input format and an age-range check.
-   Residential address and location fields.
-   Contact number format.
-   Community/category input.
-   Academic marks.
-   Branch and campus choice codes.

These are validation checks implemented in the project code; they should
not be treated as a complete identity-verification or
eligibility-verification system.

### 3. Login System

A registered student can sign in using the email address and password
stored in the Excel workbook.

The login flow allows up to three attempts before reporting that login
has failed.

### 4. Password Recovery

The password-recovery option asks for the registered email address and
then checks the student's date of birth and contact number against the
stored record.

If the details match, the student can enter a new password that is
checked against the password rules. The updated value is written back to
the Excel workbook.

### 5. Student Dashboard

After a successful login, the application displays the student's
available profile information, including:

-   Name.
-   Application number.
-   Date of birth.
-   Community.
-   Religion.
-   Email address.
-   Contact number.
-   Address.
-   Board of education.
-   Cutoff mark.
-   Provisional branch and campus allotment status, where available.

### 6. Choice Filling

Students can enter branch and campus preferences using a short code
format, for example:

`CS_02`

The program checks the format, prevents a duplicate preference from
being added to the list, and allows the student to submit or reset the
preference list before confirmation.

### 7. Provisional Seat-Allotment Simulation

The application contains a basic allotment workflow that uses the
student's calculated mark, selected preferences, branch/campus data, and
category-related records in the Excel workbook.

The program sorts matching records by cutoff and compares the student's
mark with a cutoff value from the relevant data pool.

This is a **simplified programming simulation**. It is not an official
counselling algorithm and must not be used to predict or determine
actual admission outcomes.

------------------------------------------------------------------------

## Registration Brochure

The following is the registration information structure presented by the
application when a student selects **Register**.

### Start your Tech Career with IXGVA University!

### I. Signing In

1.  E-mail Address / ID
2.  Password

### II. Personal Information

1.  Name of the Student
2.  Date of Birth
3.  Residential Address
4.  City / Town / Village
5.  District
6.  State
7.  Country
8.  Phone Number

### III. Demographic Information

1.  Caste / Community
2.  Religion
3.  Mother Tongue

### IV. Academic Information

1.  Board of Education
2.  Medium of Education
3.  School Name
4.  Marks obtained in the Class 12 board examination:
    -   Mathematics -- out of 100
    -   Physics -- out of 100
    -   Chemistry -- out of 100

The registration flow uses these details to create a student record and
calculate the project's simulated aggregate mark.

------------------------------------------------------------------------

## Choice-Filling Brochure

The application displays a second brochure when the student proceeds to
choice filling.

### A. Branch Codes

The following branch-code names are displayed in the choice-filling
brochure:

  Code   Branch
  ------ ----------------------------------------------
  `CS`   Computer Science and Engineering
  `IT`   Information Technology
  `AD`   Artificial Intelligence and Data Science
  `AM`   Artificial Intelligence and Machine Learning
  `CB`   Cyber Security
  `BS`   Computer Science and Business Systems
  `EC`   Electronics and Communication Engineering
  `EV`   ECE -- VLSI Technology and Chip Design
  `EE`   Electrical and Electronics Engineering
  `EI`   Electronics and Instrumentation Engineering
  `MC`   Mechanical Engineering
  `ME`   Mechatronics Engineering
  `RA`   Robotics and Automation Engineering
  `AE`   Aerospace Engineering
  `MR`   Marine Engineering
  `MT`   Metallurgical Engineering
  `PR`   Printing Technology
  `CV`   Civil Engineering
  `GI`   Geoinformatics Engineering
  `CH`   Chemical Engineering
  `MS`   Material Science and Engineering
  `TF`   Textile and Fashion Technology
  `BM`   Biomedical Engineering
  `BT`   Biotechnology
  `FD`   Food Technology

The source code also contains additional branch labels/codes in its
internal lists. The brochure above reproduces the branch-code list shown
to the user in the registration/choice-filling interface; the internal
mappings should be checked and kept consistent before treating every
listed code as fully supported.

### B. Campus Codes

  Code   Campus
  ------ -----------
  `01`   Chennai
  `02`   Mumbai
  `03`   Bengaluru
  `04`   Noida
  `05`   Hyderabad
  `06`   Kolkata

### C. Choice Input Format

The expected format is:

`BRANCH_CODE_CAMPUS_CODE`

Example:

`CS_02`

This represents:

-   `CS` -- Computer Science and Engineering.
-   `02` -- Mumbai Campus.

### D. Submitting and Resetting Preferences

The choice-filling interface provides these controls:

  -----------------------------------------------------------------------
  Input                               Action
  ----------------------------------- -----------------------------------
  `0`                                 Reset the current choice list and
                                      start entering preferences again.

  `1`                                 Submit the entered choice list for
                                      review and confirmation.

  `Y`                                 Confirm the displayed choice list.

  `N`                                 Reject the displayed list and reset
                                      it for fresh entry.
  -----------------------------------------------------------------------

The application displays the entered preferences before asking for final
confirmation. The code describes a confirmed list as locked for the
current counselling flow.

------------------------------------------------------------------------

## Provisional Allotment Simulation

The allotment section is intended to demonstrate how a preference-based
counselling process can be represented in code.

The program:

1.  Reads the Excel dataset using Pandas.
2.  Goes through the student's entered preferences in order.
3.  Maps branch and campus codes to their corresponding names.
4.  Filters records for the selected branch and campus.
5.  Creates a category-specific record pool where applicable.
6.  Sorts the matching records by cutoff mark in descending order.
7.  Compares the student's calculated mark with a cutoff value from the
    selected pool.
8.  Records a provisional allotment result or a `NOT ALLOTTED` status.
9.  Saves the student's registration and allotment details to the
    workbook.

### Aggregate mark used in the code

The current source code calculates the aggregate mark using:

``` python
aggregate_mark = mathematics + ((chemistry / 100) * 50) + ((physics / 100) * 50)
```

In other words, the calculation uses:

-   Mathematics mark directly, out of 100.
-   50% of the Chemistry mark.
-   50% of the Physics mark.

This is the formula implemented in this project; it is not presented as
an official admission cutoff formula.

### Important note about allotment logic

The current allotment section is a prototype and requires further
testing and refinement. The source contains branch-group and
category-related definitions, but the actual allotment implementation
should be reviewed for correct category indexing, seat calculations,
branch coverage, boundary cases, and consistency with the dataset.

A displayed provisional result should therefore be understood only as
the output of the current program logic.

------------------------------------------------------------------------

## Technology Stack

  -----------------------------------------------------------------------
  Technology                          Use in the project
  ----------------------------------- -----------------------------------
  **Python**                          Main programming language and
                                      application logic.

  **Pandas**                          Reading, filtering, combining, and
                                      updating tabular student records.

  **Microsoft Excel**                 Workbook used as the student-data
                                      store.

  **Python `datetime` module**        Date-related operations.

  **Python standard libraries**       Supporting operations used by the
                                      script.
  -----------------------------------------------------------------------

### Python concepts explored

-   Variables and data types.
-   Strings and string methods.
-   Conditional statements.
-   `while` and `for` loops.
-   Functions.
-   Lists and dictionaries.
-   List searching and indexing.
-   Input validation.
-   Exception handling.
-   File handling through Pandas.
-   DataFrame filtering and sorting.
-   Appending records to a dataset.

------------------------------------------------------------------------

## Excel Dataset

The application uses an Excel workbook as its data source and storage
layer.

The workbook is read through Pandas using `read_excel()`. Existing
records are filtered for login and allotment-related operations. New
student records are prepared as dictionaries, converted into a
DataFrame, appended with `concat()`, and written back using
`to_excel()`.

### Data fields referenced by the application

The Python code refers to columns including:

-   `S.NO`
-   `APPLICATION NUMBER`
-   `NAME`
-   `DOB`
-   `CASTE`
-   `RELIGION`
-   `EMAIL ID`
-   `PASSWORD`
-   `CUTOFF`
-   `ADDRESS/LOCATION`
-   `CITY/VILLAGE`
-   `DISTRICT`
-   `STATE`
-   `PHONE NUMBER`
-   `BOARD OF EDUCATION`
-   `BRANCH`
-   `CAMPUS`

The workbook must contain the columns expected by the script. If the
column names differ, the code will need to be updated accordingly.

### Sample dataset

The workbook contains sample student and university-related records used
to test the application workflow. AI assistance was used to generate the
sample student dataset in Excel, which was then integrated into the
Python application using Pandas.

The dataset is for demonstration and testing only. It should not be
interpreted as an official university database or real applicant
information.

------------------------------------------------------------------------

## Project Structure

A simple local setup can be organised like this:

``` text
IXGVA-Counselling-Portal/
│
├── counselling.py
├── ixgva_university_master_updated_v2.xlsx
└── README.md
```

The Python file and Excel workbook must be available at the locations
configured in the script.

------------------------------------------------------------------------

## Installation and Setup

### 1. Install Python

Install Python 3 from the official Python website:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH** if that
option is shown.

### 2. Download or clone the project

If the project is hosted on GitHub, clone the repository:

``` bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Open the project folder

Open the extracted folder in VS Code or another Python editor.

### 4. Install the required packages

The project uses Pandas to work with Excel files. Install Pandas and the
Excel engine:

``` bash
python -m pip install pandas openpyxl
```

### 5. Place the Excel workbook

Keep the Excel workbook in the project folder, or update the workbook
path in the Python script to match its actual location.

**Important:** The current source code contains a Windows-specific
absolute path to the workbook. Before running the project on another
computer, update the path in every `pd.read_excel()` and `to_excel()`
call, or change the program to use a path relative to the project
folder.

For example, a relative-path approach can use:

``` python
excel_file = "ixgva_university_master_updated_v2.xlsx"
```

Then use `excel_file` in the Pandas read/write operations. This is a
suggested setup improvement; it is not a claim that the current source
already uses a relative path.

------------------------------------------------------------------------

## How to Run

Open a terminal in the project folder and execute:

``` bash
python counselling.py
```

If your Python file has a different name, replace `counselling.py` with
that filename.

The IXGVA University main menu should appear in the terminal.

------------------------------------------------------------------------

## How to Use the Portal

### Register a new student

1.  Select `3` from the main menu.
2.  Read the registration brochure.
3.  Enter the requested sign-in, personal, demographic, and academic
    information.
4.  Follow the validation prompts.
5.  Choose whether to continue to choice filling.

### Fill choices

1.  Read the choice-filling brochure.
2.  Enter a branch and campus preference in the required format.
3.  Continue entering preferences.
4.  Enter `1` to submit the list.
5.  Review the displayed list.
6.  Enter `Y` to confirm or `N` to reset it.

### Proceed to provisional allotment

If the program offers the option, enter `Y` to run the provisional
allotment simulation. The program displays the result and attempts to
save the record to the Excel workbook.

### Log in

1.  Select `1` from the main menu.
2.  Enter the registered email address and password.
3.  The program allows up to three login attempts.
4.  On successful login, the student dashboard is displayed.

### Recover a password

1.  Select `2` from the main menu.
2.  Enter the registered email address.
3.  Enter the date of birth and contact number requested for
    verification.
4.  If the stored details match, enter and confirm a new password.

### Exit

Select `4` to exit the portal.

------------------------------------------------------------------------

## Input Validation

The application includes custom checks intended to reduce invalid input
during registration and choice filling.

Examples include:

  -----------------------------------------------------------------------
  Field                               Validation implemented in the
                                      source
  ----------------------------------- -----------------------------------
  Email                               Checks for an `@` symbol and a
                                      basic domain pattern.

  Password                            Checks minimum length and the
                                      presence of uppercase, lowercase,
                                      numeric, and special characters.

  Date of birth                       Checks the entered date format and
                                      applies a basic age-range
                                      calculation.

  Address                             Checks a minimum text length.

  City and district                   Checks a minimum text length.

  Contact number                      Checks for a 10-character numeric
                                      input.

  Community/category                  Checks against the categories
                                      listed in the code.

  Academic marks                      Checks that entered marks are
                                      numeric and within the coded range.

  Choice code                         Checks the expected branch/campus
                                      code format and allowed values.
  -----------------------------------------------------------------------

These are project-level checks. Some are deliberately simple and would
need stronger validation for a real-world application.

------------------------------------------------------------------------

## Learning Outcomes

Working on this project provided an opportunity to practise Python
beyond small standalone exercises.

Some of the main areas explored were:

-   Writing program logic step by step.
-   Breaking a larger workflow into smaller operations.
-   Using loops to repeat input and validation steps.
-   Using conditions to control different application paths.
-   Working with lists and dictionaries to organise information.
-   Using Pandas to interact with an Excel dataset.
-   Filtering and sorting records based on multiple conditions.
-   Appending new records while preserving the workbook's column
    structure.
-   Handling file-write errors such as a workbook being open in Excel.
-   Understanding how registration, login, choice filling, and allotment
    stages connect.

------------------------------------------------------------------------

## Current Scope and Limitations

This project is a learning prototype. The following points are important
when running or reviewing the current source:

-   The application is console-based; it does not provide a graphical or
    web interface.
-   The Excel workbook acts as a simple data store. It is not a database
    server.
-   The source code currently uses a machine-specific Windows file path
    for the workbook. This must be configured on another computer.
-   Passwords are stored in the Excel workbook as plain text in the
    current implementation. This is not secure for real user accounts.
-   Password recovery relies on matching personal details stored in the
    same workbook; this is not a secure production identity-verification
    method.
-   The email and date-of-birth checks are basic custom validations, not
    comprehensive validation systems.
-   The allotment algorithm is a simplified simulation and needs further
    testing and correction before any real-world interpretation.
-   The branch/campus mappings and category/seat calculations should be
    checked for consistency and correctness.
-   The application does not connect to an official admissions authority
    or verify official eligibility, reservation rules, cutoffs, seat
    matrices, or admission results.
-   The workbook should be backed up before testing operations that
    write or update records.

------------------------------------------------------------------------

## Responsible Use of Sample Data

This project uses a sample Excel dataset for demonstration.

-   Do not use real applicants' personal information in a public
    repository.
-   Do not upload passwords, phone numbers, addresses, dates of birth,
    or other sensitive information to GitHub.
-   Use only synthetic or appropriately anonymised records when sharing
    the workbook.
-   Keep a backup copy before running code that modifies the workbook.
-   Do not present simulated allotment results as official admission
    outcomes.

If the repository is public, review the Excel workbook before uploading
it and remove any personal or sensitive data.

------------------------------------------------------------------------

## Future Improvements

Possible areas for further development include:

-   Moving from Excel storage to SQLite or MySQL.
-   Hashing passwords instead of storing them as plain text.
-   Improving email, date, phone-number, and age validation.
-   Separating the program into smaller functions and modules.
-   Making the file path configurable rather than hard-coded.
-   Improving the allotment algorithm and testing it against clearly
    defined rules.
-   Adding automated tests for registration, login, choice filling, and
    allotment.
-   Adding a graphical or web-based user interface.
-   Adding clearer error messages and recovery paths.
-   Improving data backup and record management.

These are possible future enhancements, not features claimed to be
completed in the current version.

------------------------------------------------------------------------

## Acknowledgements

This project was developed as a hands-on exercise while learning Python.

The application logic was developed step by step as part of that
learning process. AI assistance was used to generate the sample student
dataset in Excel, which was integrated into the application using
Pandas.

The project reflects an effort to move from learning individual
programming concepts to combining them in a larger, practical-style
application.

------------------------------------------------------------------------

**IXGVA University -- Engineering & Technology Counselling Portal**\
*Learning by building. Improving one step at a time.*

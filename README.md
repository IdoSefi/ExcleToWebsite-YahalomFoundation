
# Volunteer Data Automation Script

This script automates the process of entering volunteer data from an Excel spreadsheet into a website form using Selenium, BeautifulSoup, and Pandas.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Firefox browser
- geckodriver (WebDriver for Firefox)

## Installation

1. Clone this repository or download the script file.

2. Install the required Python packages using pip:

    ```bash
    pip install requests beautifulsoup4 selenium xlwt openpyxl pandas
    ```

3. Download and install [geckodriver](https://github.com/mozilla/geckodriver/releases) and make sure it is in your PATH.

## Usage

1. Prepare an Excel file named `excellVolunteers.xlsx` with the following columns:
    - First Name
    - Last Name
    - Email
    - Phone
    - Password

2. Modify the URL in the script if needed:

    ```python
    Yahalom_url = 'https://yahalomfoundation.com/yahalom-member/'
    ```

3. Run the script:

    ```bash
    python your_script_name.py
    ```

    The script will open the browser, navigate to the specified URL, and enter the volunteer data into the form fields.

## Script Details

The script performs the following steps:

1. Opens the browser and navigates to the specified URL.
2. Reads volunteer data from an Excel file using Pandas.
3. Enters the data into the web form fields.
4. Submits the form for each row of data.
5. Saves the entered data into a new Excel file named `done volunteers.xls`.

## Notes

- Ensure the Excel file `excellVolunteers.xlsx` is in the same directory as the script.
- The script uses Firefox as the browser. Make sure you have Firefox and geckodriver installed.


## Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [xlwt](https://pypi.org/project/xlwt/)
- [openpyxl](https://pypi.org/project/openpyxl/)


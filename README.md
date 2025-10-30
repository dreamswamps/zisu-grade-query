# ZISU GPA Auto-Query and Statistics Script

> A Python-based automation tool for ZISU's educational administration system, designed to query and calculate academic grades, GPA, and comprehensive assessment scores.

## ✨ Feature Description

### [√] Completed Features
- **Data Scraping** Scrapes and parses the grade data for specified academic years
- **Statistics Calculation** Calculates the credits and grade points for compulsory/elective courses, and calculate the annual GPA
- **Result Display** Output the statistics reports in the terminal

### [] Planned Features
- **Automatic Session Management** Automatically get/refresh educational administration system session information and user authentication(Cookie/Headers)

## 🚀 Quick Start

### Environment Requirements

- Python 3.8+
- Dependent library: `requests`

### Installation and Running

1. Clone the project:
    ```bash
    git clone https://github.com/dreamswamps/zisu-grade-query.git
    cd zisu-grade-query
    ```

2. Install dependencies:
    ```bash
    pip install requests
    ```

3. Configure Information:
    Before running, please configure the parameters according to the **[Usage Instructions](#configuration)** below.

4. Run the script:
    ```bash
    python ZISU.py
    ```

## 📖 Usage Instructions <a id="configuration"></a>

1. Information Configuration:
    Manually configure the authentication information for the selected script:
    - **ZISU.py** :
        ```python
        gnmkdm = "query ID field"  # From the URL path
        cookie = "user authentication"
        years = ["2022","2023"]
        ```
    - **ZISU_GPA.py** :
        Configuration items are similar to the ZISU.py.
    - **ZISU_ZC.py** :
        ```python
        headers = {
            'Authorization': '',
            'Blade-Auth': ''
            }  # From the network requests in developer tools
        years = ["2022","2023"]
        ```

    >**ℹ️ Tip:**How to get parameters? Use browser developer tools (F12), after logging in, check the network requests when accessing the grade page to get the corresponding Cookie or Header information.

2. Save and run the script, then wait and check the statistics results output in the terminal.

## 📁 Project Structure
```
zisu-grade-query/
├── ZISU.py         # Basic script: GPA statistics for specified academic years
├── ZISU_GPA.py     # Enhanced function: GPA statistics for all courses
└── ZISU_ZC.py      # Improved function: Comprehensive assessment score statistics
```

## ❓ Frequently Asked Questions

**Q: Error occurs after running the script, or the script has no response?**

**A:** Please troubleshoot according to the following steps:
1. **Expired authentication information**: Cookie or Header information is valid for about one day. Please try to log in again and get new authentication information.
2. **System maintenance**: The university's educational administration system may undergo maintenance outside the daily 7:00 - 22:00 time window. Please use it within this time period.
3. **Network issues**: Please check if the network connection is normal.
4. **Special circumstances**: During special periods such as course selection, the university's educational administration system may be at risk of crashing due to excessive requests.In such cases, please do not use the script.
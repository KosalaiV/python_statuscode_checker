# **URL Checker**
URL Checker is a Python script that checks the status of URLs listed in an Excel file and saves the failed URLs to another Excel file.

## **Prerequisites**
- Python installed (using python 3.x)
- pip installed

## **Installation**

 1. **Clone the repository:**

    ```git clone https://github.com/KosalaiV/python_statuscode_checker.git```


 2. **Install the required dependencies:**

    ```pip install pandas requests```

## **Usage**

1. Place your Excel file with URLs in the same directory. Make sure the URLs are listed in the first column.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script:

   - For Python 3.x:

     ```python3 statuscode_checker.py```

   - For Python versions less than 3.x:

     ```python statuscode_checker.py```

The script will print the total number of URLs and start processing them concurrently.

4. Once the process is complete, a new Excel file will be generated in the same directory. This file will contain the URLs that failed the status check.

## **Configuration**
You can modify the following parameters in the script according to your needs:

 - `input_file`: Specifies the name of the input Excel file containing the URLs.
- `output_file`: Specifies the name of the output Excel file to store the failed URLs.
- `num_threads`: Controls the number of concurrent threads for processing URLs. Adjust this number based on your system's capabilities.

Feel free to customize the script and adapt it to your specific requirements :) 

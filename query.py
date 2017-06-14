#! python3
"""Accesses the database with information provided by the user and returns
the singular insured account information as a list."""

import pyodbc
import os

def get_connect_info():
    """Gets login info from file and returns login credentials"""
    # Establish path to login credentials file
    login_path = os.path.dirname(__file__) # Get location of currently running script
    login_dir = os.path.split((login_path))[0] # cd ..
    file_name = "login.txt" # File name of said file
    complete_login_path = os.path.join(login_dir, file_name) # Join the file name and the path together

    with open(complete_login_path) as login:
        login_credentials = login.readlines()
    # Store login_credentials in tuple, make sure any extra spaces aren't there
    login_credentials = (x.strip() for x in login_credentials)
    return login_credentials

def connect():
    """Connects to the database and returns the cursor for getting values from the database"""
    # Unpack login credential tuple into variables
    server, user, password, database = get_connect_info()

    conn = pyodbc.connect(
        r"Driver={0};Server={1};DATABASE={2};UID={3};PWD={4};".format(
            "ODBC Driver 11 for SQL Server", server, database, user, password)
        )
    cursor = conn.cursor()
    return cursor

def get_rows(cursor, ctrlnum):
    """Uses the cursor and control number provided to query the database
    for the insured associated with the control number. Returns a list
    that consists of each item in the row
    """
    results = []

    cursor.execute("""
    select
        ControlNo, InsuredPolicyName, InsuredCorporationName,
        InsuredFirstName, InsuredMiddleName, InsuredLastName,
        InsuredAddress1, InsuredAddress2, InsuredCity,
        InsuredCounty, InsuredState, InsuredZipCode, 
        QuoteGUID
    from 
        tblQuotes
    where 
        ControlNo like '{0}'
    """.format(ctrlnum))

    for row in cursor:
        for column in row:
            results.append(column)

    return results

def search_ims(controlnumber):
    """Driver function for the query module"""
    ims_connection = connect()
    insured = get_rows(ims_connection, controlnumber)
    ims_connection.close()
    return insured
 
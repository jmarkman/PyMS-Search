#! python3
"""Accesses the database with information provided by the user and returns
the singular insured account information as a list."""

import pyodbc

# Read SQL login credentials from external file (currently on my flash drive)
with open(r'F:/Programming/Work/login.txt') as loginFile:
    CREDENTIALS = loginFile.readlines()
CREDENTIALS = (x.strip() for x in CREDENTIALS)
# Store CREDENTIALS in tuple, make sure any extra spaces aren't there

SERVER, USER, PASSWORD, DATABASE = CREDENTIALS # Unpack tuple into variables

def connect():
    """Connects to the database and returns the cursor for getting values from the database"""
    conn = pyodbc.connect(
        r"Driver={0};Server={1};DATABASE={2};UID={3};PWD={4};".format(
            "ODBC Driver 11 for SQL Server", SERVER, DATABASE, USER, PASSWORD)
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
 
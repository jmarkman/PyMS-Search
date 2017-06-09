from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import query
import pyodbc

# Search button function
def search(*args):
    """Using the query module, performs the database query to return the insured"""
    try:
        user_input = input_ctrl_num.get() # Get control number from user
        if user_input.isnumeric():
            result = query.search_ims(user_input) # Get list of values in returned row
        else:
            messagebox.showerror("Error", "That is not a valid control number!")

        # List comprehension to replace None/null values with the string "NULL"
        result = ["NULL" if x is None else x for x in result]

        # Assign to result labels
        output_ctrl_num.set(result[0])
        output_policy_name.set(result[1])
        output_corp_name.set(result[2])
        output_first_name.set(result[3])
        output_middle_name.set(result[4])
        output_last_name.set(result[5])
        output_street_1.set(result[6])
        output_street_2.set(result[7])
        output_city.set(result[8])
        output_county.set(result[9])
        output_state.set(result[10])
        output_zip.set(result[11])
        output_guid.set(result[12])
    except Exception as something_happened: # lord forgive me for i have sinned
        print(something_happened)


# Set up the tkinter window
MAINWINDOW = Tk()
WINDOWFRAME = ttk.Frame(MAINWINDOW, padding="3 3 12 12")
WINDOWFRAME.grid(column=0, row=0, sticky=(N, W, E, S))
WINDOWFRAME.columnconfigure(0, weight=1)
WINDOWFRAME.rowconfigure(0, weight=1)

# Make stringvars for the incoming control number from the user and output from DB
# pylint says these are constants, are these really constants if they're being changed?
input_ctrl_num = StringVar()
output_ctrl_num = StringVar()
output_policy_name = StringVar()
output_corp_name = StringVar()
output_first_name = StringVar()
output_middle_name = StringVar()
output_last_name = StringVar()
output_street_1 = StringVar()
output_street_2 = StringVar()
output_city = StringVar()
output_county = StringVar()
output_state = StringVar()
output_zip = StringVar()
output_guid = StringVar()

# GUI things: labels, input box, etc.
# Control Number Label
SEARCH_LABEL = ttk.Label(WINDOWFRAME, text="Input Control #")
SEARCH_LABEL.grid(column=0, row=0)

# Control Number Input Box
CTRL_NUM_ENTRY = ttk.Entry(WINDOWFRAME, width=8, textvariable=input_ctrl_num)
CTRL_NUM_ENTRY.grid(column=0, row=1)

# Search Button
LOOKUP_BUTTON = ttk.Button(WINDOWFRAME, text="Search", command=search)
LOOKUP_BUTTON.grid(column=0, row=2)

# Columns
SEP_1 = ttk.Separator(WINDOWFRAME, orient=VERTICAL)
SEP_1.grid(column=1, row=0, rowspan=13, sticky="ns")

SEP_2 = ttk.Separator(WINDOWFRAME, orient=VERTICAL)
SEP_2.grid(column=4, row=0, rowspan=13, sticky="ns")

# Labels for return values
# Control Number
CTRL_NUM_LABEL = ttk.Label(WINDOWFRAME, text="IMS Control Number:")
CTRL_NUM_LABEL.grid(column=2, row=0)
# Policy Name
POLICY_NAME_LABEL = ttk.Label(WINDOWFRAME, text="Insured Policy Name:")
POLICY_NAME_LABEL.grid(column=2, row=1)
# Corporation Name
CORP_NAME_LABEL = ttk.Label(WINDOWFRAME, text="Corporation Name")
CORP_NAME_LABEL.grid(column=2, row=2)
# First Name
FIRST_NAME_LABEL = ttk.Label(WINDOWFRAME, text="First Name:")
FIRST_NAME_LABEL.grid(column=2, row=3)
# Middle Name
MIDDLE_NAME_LABEL = ttk.Label(WINDOWFRAME, text="Middle Name:")
MIDDLE_NAME_LABEL.grid(column=2, row=4)
# Last Name
LAST_NAME_LABEL = ttk.Label(WINDOWFRAME, text="Last Name:")
LAST_NAME_LABEL.grid(column=2, row=5)
# Street 1
STREET_1_LABEL = ttk.Label(WINDOWFRAME, text="Street 1:")
STREET_1_LABEL.grid(column=2, row=6)
# Street 2
STREET_2_LABEL = ttk.Label(WINDOWFRAME, text="Street 2:")
STREET_2_LABEL.grid(column=2, row=7)
# City
CITY_LABEL = ttk.Label(WINDOWFRAME, text="City:")
CITY_LABEL.grid(column=2, row=8)
# County
COUNTY_LABEL = ttk.Label(WINDOWFRAME, text="County:")
COUNTY_LABEL.grid(column=2, row=9)
# State
STATE_LABEL = ttk.Label(WINDOWFRAME, text="State:")
STATE_LABEL.grid(column=2, row=10)
# Zip
ZIP_LABEL = ttk.Label(WINDOWFRAME, text="Zip:")
ZIP_LABEL.grid(column=2, row=11)
# GUID
GUID_LABEL = ttk.Label(WINDOWFRAME, text="Quote GUID:")
GUID_LABEL.grid(column=2, row=12)

# The results as labels
RESULT_CTRL_NUM = ttk.Label(WINDOWFRAME, textvariable=output_ctrl_num)
RESULT_CTRL_NUM.grid(column=3, row=0)

RESULT_POLICY_NAME = ttk.Label(WINDOWFRAME, textvariable=output_policy_name)
RESULT_POLICY_NAME.grid(column=3, row=1)

RESULT_CORP_NAME = ttk.Label(WINDOWFRAME, textvariable=output_corp_name)
RESULT_CORP_NAME.grid(column=3, row=2)

RESULT_FIRST_NAME = ttk.Label(WINDOWFRAME, textvariable=output_first_name)
RESULT_FIRST_NAME.grid(column=3, row=3)

RESULT_MIDDLE_NAME = ttk.Label(WINDOWFRAME, textvariable=output_middle_name)
RESULT_MIDDLE_NAME.grid(column=3, row=4)

RESULT_LAST_NAME = ttk.Label(WINDOWFRAME, textvariable=output_last_name)
RESULT_LAST_NAME.grid(column=3, row=5)

RESULT_STREET_1 = ttk.Label(WINDOWFRAME, textvariable=output_street_1)
RESULT_STREET_1.grid(column=3, row=6)

RESULT_STREET_2 = ttk.Label(WINDOWFRAME, textvariable=output_street_2)
RESULT_STREET_2.grid(column=3, row=7)

RESULT_CITY = ttk.Label(WINDOWFRAME, textvariable=output_city)
RESULT_CITY.grid(column=3, row=8)

RESULT_COUNTY = ttk.Label(WINDOWFRAME, textvariable=output_county)
RESULT_COUNTY.grid(column=3, row=9)

RESULT_STATE = ttk.Label(WINDOWFRAME, textvariable=output_state)
RESULT_STATE.grid(column=3, row=10)

RESULT_ZIP = ttk.Label(WINDOWFRAME, textvariable=output_zip)
RESULT_ZIP.grid(column=3, row=11)

RESULT_GUID = ttk.Label(WINDOWFRAME, textvariable=output_guid)
RESULT_GUID.grid(column=3, row=12)

# Add padding
for child in WINDOWFRAME.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind search button to enter key for friendly usage
CTRL_NUM_ENTRY.focus()
MAINWINDOW.bind('<Return>', search)

# Launch window
MAINWINDOW.mainloop()

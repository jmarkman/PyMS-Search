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

        # Assign to result labels, the list indecies should match up 1:1 with the query
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
        messagebox.showerror("Error", something_happened)


# Set up the tkinter window
main_window = Tk()
main_window.title("PyMS Search")
window_frame = ttk.Frame(main_window, padding="3 3 12 12")
window_frame.grid(column=0, row=0, sticky=(N, W, E, S))
window_frame.columnconfigure(0, weight=1)
window_frame.rowconfigure(0, weight=1)

# Make stringvars for the incoming control number from the user and output from DB
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
search_label = ttk.Label(window_frame, text="Input Control #")
search_label.grid(column=0, row=0)

# Control Number Input Box
ctrl_num_entry = ttk.Entry(window_frame, width=8, textvariable=input_ctrl_num)
ctrl_num_entry.grid(column=0, row=1)

# Search Button
lookup_button = ttk.Button(window_frame, text="Search", command=search)
lookup_button.grid(column=0, row=2)

# Columns
sep_1 = ttk.Separator(window_frame, orient=VERTICAL)
sep_1.grid(column=1, row=0, rowspan=13, sticky="ns")

# Labels for return values
# Control Number
ctrl_num_label = ttk.Label(window_frame, text="IMS Control Number:")
ctrl_num_label.grid(column=2, row=0)
# Policy Name
policy_name_label = ttk.Label(window_frame, text="Insured Policy Name:")
policy_name_label.grid(column=2, row=1)
# Corporation Name
corp_name_label = ttk.Label(window_frame, text="Corporation Name")
corp_name_label.grid(column=2, row=2)
# First Name
first_name_label = ttk.Label(window_frame, text="First Name:")
first_name_label.grid(column=2, row=3)
# Middle Name
middle_name_label = ttk.Label(window_frame, text="Middle Name:")
middle_name_label.grid(column=2, row=4)
# Last Name
last_name_label = ttk.Label(window_frame, text="Last Name:")
last_name_label.grid(column=2, row=5)
# Street 1
street_1_label = ttk.Label(window_frame, text="Street 1:")
street_1_label.grid(column=2, row=6)
# Street 2
street_2_label = ttk.Label(window_frame, text="Street 2:")
street_2_label.grid(column=2, row=7)
# City
city_label = ttk.Label(window_frame, text="City:")
city_label.grid(column=2, row=8)
# County
county_label = ttk.Label(window_frame, text="County:")
county_label.grid(column=2, row=9)
# State
state_label = ttk.Label(window_frame, text="State:")
state_label.grid(column=2, row=10)
# Zip
zip_label = ttk.Label(window_frame, text="Zip:")
zip_label.grid(column=2, row=11)
# GUID
guid_label = ttk.Label(window_frame, text="Quote GUID:")
guid_label.grid(column=2, row=12)

# The results as labels
result_ctrl_num = ttk.Label(window_frame, textvariable=output_ctrl_num)
result_ctrl_num.grid(column=3, row=0)

result_policy_name = ttk.Label(window_frame, textvariable=output_policy_name)
result_policy_name.grid(column=3, row=1)

result_corp_name = ttk.Label(window_frame, textvariable=output_corp_name)
result_corp_name.grid(column=3, row=2)

result_first_name = ttk.Label(window_frame, textvariable=output_first_name)
result_first_name.grid(column=3, row=3)

result_middle_name = ttk.Label(window_frame, textvariable=output_middle_name)
result_middle_name.grid(column=3, row=4)

result_last_name = ttk.Label(window_frame, textvariable=output_last_name)
result_last_name.grid(column=3, row=5)

result_street_1 = ttk.Label(window_frame, textvariable=output_street_1)
result_street_1.grid(column=3, row=6)

result_street_2 = ttk.Label(window_frame, textvariable=output_street_2)
result_street_2.grid(column=3, row=7)

result_city = ttk.Label(window_frame, textvariable=output_city)
result_city.grid(column=3, row=8)

result_county = ttk.Label(window_frame, textvariable=output_county)
result_county.grid(column=3, row=9)

result_state = ttk.Label(window_frame, textvariable=output_state)
result_state.grid(column=3, row=10)

result_zip = ttk.Label(window_frame, textvariable=output_zip)
result_zip.grid(column=3, row=11)

result_guid = ttk.Label(window_frame, textvariable=output_guid)
result_guid.grid(column=3, row=12)

# Add padding
for child in window_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind search button to enter key for friendly usage
ctrl_num_entry.focus()
main_window.bind('<Return>', search)

# Launch window
main_window.mainloop()

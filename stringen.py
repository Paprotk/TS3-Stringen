import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
from base64 import b64decode
small_icon_data = "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"

def list_cs_files(folder):
    cs_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.cs'):
                cs_files.append(os.path.join(root, file))
    return cs_files

def extract_localized_strings(file_path, exclude_gameplay, exclude_ui):
    localized_strings = []  # Use a list to maintain order
    seen_strings = set()  # Use a set to avoid duplicates
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'Localization.LocalizeString' in line:
                start_index = line.find('Localization.LocalizeString') + len('Localization.LocalizeString')
                first_quote_index = line.find('"', start_index)
                if first_quote_index != -1:
                    second_quote_index = line.find('"', first_quote_index + 1)
                    if second_quote_index != -1:
                        localized_string = line[first_quote_index + 1:second_quote_index]
                        if (exclude_gameplay and localized_string.startswith("Gameplay")) or \
                           (exclude_ui and localized_string.startswith("Ui")):
                            continue
                        if localized_string not in seen_strings:
                            localized_strings.append(localized_string)  # Add to list
                            seen_strings.add(localized_string)  # Track seen strings
    return localized_strings

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        global cs_files  # Make cs_files global to access it later
        cs_files = list_cs_files(folder_path)
        folder_name_label.config(text=f"Selected folder: {os.path.basename(folder_path)}")
        folder_name_label.pack()
        refresh_text_widget()

def refresh_text_widget():
    text_widget.delete('1.0', tk.END)
    if cs_files:
        exclude_gameplay = exclude_gameplay_var.get()
        exclude_ui = exclude_ui_var.get()
        all_strings = []  # Use a list to collect all unique strings in order
        seen_strings = set()  # Use a set to track seen strings
        for file in cs_files:
            localized_strings = extract_localized_strings(file, exclude_gameplay, exclude_ui)
            for string in localized_strings:
                if string not in seen_strings:
                    all_strings.append(string)
                    seen_strings.add(string)
        for string in all_strings:
            text_widget.insert(tk.END, string + '\n')
        toggle_save_button()
        update_line_count()

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            text_content = text_widget.get('1.0', tk.END).strip()
            lines = text_content.split('\n')
            
            file.write('<?xml version="1.0" ?>\n')
            file.write('<TEXT>\n')
            for line in lines:
                if line:  # Check if the line is not empty
                    file.write(f'    <KEY>{line}</KEY>\n')
                    file.write('    <STR></STR>\n')
            file.write('</TEXT>\n')

def toggle_save_button():
    text_content = text_widget.get('1.0', tk.END).strip()
    if text_content:
        save_button.config(state=tk.NORMAL)
    else:
        save_button.config(state=tk.DISABLED)

def update_line_count():
    # Get the number of lines in the text widget
    text_content = text_widget.get('1.0', tk.END).strip()  # Get all text and strip extra newlines
    if text_content:
        line_count = text_content.count('\n') + 1  # Number of lines is the count of newlines plus 1
    else:
        line_count = 0
    line_count_label.config(text=f"Number of lines: {line_count}")

def open_blacklist_window():
    # Create a new window for blacklist settings    
    blacklist_window = tk.Toplevel(root)
    blacklist_window.iconphoto(False, small_icon)
    blacklist_window.title("Blacklist Settings")
    blacklist_window.geometry("260x120")
    
    # Create checkboxes for "Gameplay" and "Ui"
    tk.Checkbutton(blacklist_window, text="Gameplay", variable=exclude_gameplay_var).pack(anchor=tk.W, padx=10, pady=5)
    tk.Checkbutton(blacklist_window, text="Ui", variable=exclude_ui_var).pack(anchor=tk.W, padx=10, pady=5)
    
    # Add a button to close the settings window
    tk.Button(blacklist_window, text="Close", command=lambda: close_blacklist_window(blacklist_window)).pack(pady=10)

def close_blacklist_window(blacklist_window):
    blacklist_window.destroy()
    refresh_text_widget()  # Refresh text widget to apply blacklist settings

# Set up the main application window
root = tk.Tk()
root.title("Select folder with .cs files to generate strings")
root.geometry("600x400")

# Set up the icon
small_icon = tk.PhotoImage(data=b64decode(small_icon_data))
root.iconphoto(False, small_icon)

# Set up a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20, fill='x')

# Set up a button to open the blacklist settings window
blacklist_button = tk.Button(button_frame, text="Blacklist Settings", command=open_blacklist_window)
blacklist_button.pack(side=tk.LEFT, padx=10)

# Set up a button to select the folder
select_button = tk.Button(button_frame, text="Select Folder", command=select_folder)
select_button.pack(side=tk.LEFT, padx=10)

# Set up a button to save the text to a file
save_button = tk.Button(button_frame, text="Save to File", command=save_to_file, state=tk.DISABLED)
save_button.pack(side=tk.LEFT, padx=10)

# Set up a frame for the folder name label
folder_name_frame = tk.Frame(root)
folder_name_frame.pack(pady=0, fill='x')

# Add a label to display the selected folder name
folder_name_label = tk.Label(folder_name_frame, text="")
folder_name_label.pack_forget()  # Initially hide the label

# Set up a frame for the line count label
line_count_frame = tk.Frame(root)
line_count_frame.pack(pady=0, fill='x')

# Add a label to display the number of lines
line_count_label = tk.Label(line_count_frame, text="Number of lines: 0")
line_count_label.pack()

# Set up a scrolled text widget to display the localized strings
text_widget = scrolledtext.ScrolledText(root, wrap='word', undo=True)
text_widget.pack(expand=1, fill='both')
text_widget.bind('<<Modified>>', lambda e: update_line_count())

# Initialize BooleanVars for blacklist settings
exclude_gameplay_var = tk.BooleanVar()
exclude_ui_var = tk.BooleanVar()

# Initialize global variable for cs_files
cs_files = []

# Start the Tkinter main loop
root.mainloop()

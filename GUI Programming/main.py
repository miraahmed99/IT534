import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from json_gui import save_settings, load_settings

class App:
    """
    Class for the server application 

    Attributes

    threads: number of threads (1,2,4)
    log: path for event log
    root: window for root app
    types: select events to log
    file_types: holds files
    debug_mode: enabled or disabled debug mode
    server_port: server port value

    Methods

    browse_file: opens file to select the log file
    save_to_json: saves settings 
    load_from_json: loads settings and updates GUI
    """
    def __init__(self, root):
        """
        Creates attributes for app

        Args:
            root (tkinter.Tk): window for app
        """
        self.root = root #assigms root window
        self.root.title("Server Configuration")

        self.threads_label = ttk.Label(root, text= "Threads:") #configures threads
        self.threads_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W) #place label in grid
        self.threads = tk.IntVar(value=1) # default value
        self.threads_menu = ttk.Combobox(root, textvariable=self.threads, values=[1 , 2 , 4])
        self.threads_menu.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W) #place menu dropbox

        self.log_label = ttk.Label(root, text="Event Log File Location: ") # configures log file location
        self.log_label.grid(row=1,column=0, padx=10,pady=10,sticky=tk.W)#place label in grid
        self.log = tk.StringVar()
        self.log_entry = ttk.Entry(root, textvariable= self.log, width=40)
        self.log_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.browse_button = ttk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=10,pady=10,sticky=tk.W)#place menu button

        self.types_label = ttk.Label(root, text= "Types of Events to Log:") # types of events
        self.types_label.grid(row=2,column=10,padx=10,pady=10,sticky=tk.W)#place label in grid
        self.types = {}
        options = ["application", "security", "error", "input/output"]
        for i, event in enumerate(options):
            self.types[event] = tk.BooleanVar()
            cb = ttk.Checkbutton(root, text = event, variable= self.types[event])
            cb.grid(row=2+i, column=1, padx=10, pady=5, sticky=tk.W) #place checkbox grid
            
        self.file_types_label = ttk.Label(root, text = "Supported File Types:") # files supported
        self.file_types_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)#place label in grid
        self.file_types = {}
        file_options = [".doc", "docx", ".ppt", ".pptx", ".xls", ".xlsx", ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif", ".xml", ".html", ".zip", ".mp4", ".mov"]
        for i, file_type in enumerate(file_options):
            self.file_types[file_type] = tk.BooleanVar()
            cb = ttk.Checkbutton(root, text=file_type, variable=self.file_types[file_type])
            cb.grid(row=6+(i//8), column=1+(i%8), padx=10, pady=5, sticky=tk.W)#place checkbox grid

        self.debug_label = ttk.Label(root, text="Debug Mode: ") #debugging mode
        self.debug_label.grid(row=8,column=0, padx=10,pady=10, sticky=tk.W)#place label in grid
        self.debug_mode = tk.BooleanVar()
        self.debug_checkbox = ttk.Checkbutton(root, text="Enable Debug", variable=self.debug_mode )
        self.debug_checkbox.grid(row=8,column=1, padx=10,pady=10,sticky=tk.W) #place menu checkbox grid

        self.port_label = ttk.Label(root, text="Server Port: ") #server port
        self.port_label.grid(row=9, column=0, padx=10,pady=10, sticky=tk.W)#place label in grid
        self.server_port = tk.IntVar(value=50000)
        self.port_spinbox = ttk.Spinbox(root, from_=50000, to=50500, textvariable=self.server_port)
        self.port_spinbox.grid(row=9,column=1,padx=10,pady=10,sticky=tk.W) #place menu spinbox
        self.save_button = ttk.Button(root, text = "Save Settings", command= self.save_to_json) #save and load
        self.save_button.grid(row=10,column=0,padx=10,pady=20,sticky=tk.W)#place save button in grid
        self.load_button = ttk.Button(root, text="Load Settings", command=self.load_from_json)
        self.load_button.grid(row=10,column=1,padx=10,pady=20,sticky=tk.W) #place load button on grid

    def browse_file(self):
        """
        Opens file to select log file location
        """
        file_path = filedialog.askopenfilename(title="Select Event Log File")#open file dialog
        if file_path:
            self.log.set(file_path) #set log variable to file path

    def save_to_json(self):
        """
        saves configuration settings to json

        Uses all settings in GUI
        """
        settings = { #settings dictionary 
            "threads": self.threads.get(),
            "log": self.log.get(),
            "types": {k: v.get() for k,v in self.types.items()},
            "file_types": {k: v.get() for k,v in self.file_types.items()},
            "debug_mode": self.debug_mode.get(),
            "server_port": self.server_port.get()
        }
        file_path = filedialog.asksaveasfilename(title="Save Settings As", defaultextension=".json") 
        if file_path:
            save_settings(settings,file_path)
            messagebox.showinfo("Success", "Settings saved")

    def load_from_json(self):
        """
        Loads config settings for JSON and GUI settings
        """
        file_path = filedialog.askopenfilename(title="Open Setting File", filetypes=[("JSON Files", "*.json")])# open dialog file to chose json file
        if file_path:
            settings = load_settings(file_path) #load settings
            if settings: #if success
                self.threads.set(settings.get("threads", 1))#set threads
                self.log.set(settings.get("log", "")) #set path
                for key, var in self.types.items():#set event types
                    var.set(settings.get("types",{}).get(key,False))
                for key, var in self.file_types.items(): #set file types
                    var.set(settings.get("file_types", {}).get(key, False))
                self.debug_mode.set(settings.get("debug_mode", False)) #set debug mode
                self.server_port.set(settings.get("server_port", 50000)) #set server port 
                messagebox.showinfo("Success", "Settings loaded")
            else:
                messagebox.showerror("Error", "Failed to load settings")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


import os
import tkinter as tk
from main import App
from json_gui import save_settings, load_settings

def run_test():
    root = tk.Tk()
    app = App(root)
    app.threads.set(4)
    app.log.set("C:/example/path/to/event.log")
    app.types['application'].set(True)
    app.types['security'].set(False)
    app.types['error'].set(True)
    app.file_types['.doc'].set(True)
    app.file_types['.pdf'].set(True)
    app.debug_mode.set(True)
    app.server_port.set(50210)

    test_file_path = "test_settings.json"
    settings = {
        "threads": app.threads.get(),
        "log": app.log.get(),
        "types": {k: v.get() for k,v in app.types.items()},
        "file_types": {k: v.get() for k,v in app.file_types.items()},
        "debug_mode": app.debug_mode.get(),
        "server_port": app.server_port.get()
    }

    save_settings(settings, test_file_path)
    print(f"Settings saved to {test_file_path}")
    loaded_settings = load_settings(test_file_path)
    if load_settings:
        print("Success")
        print(loaded_settings)
    else:
        print("Failed")

    app.load_from_json()
    assert app.threads.get() == 4, "Values do not match for threads"
    assert app.log.get() == "C:/example/path/to/event.log", "Log location did nnot match"
    assert app.types['application'].get() == True, " event type application did not match"
    app.types['security'].get() == False, " event type security did not match"
    app.types['error'].get() == True, " event type error did not match"
    app.file_types['.doc'].get() == True, ".doc did not match"
    app.file_types['.pdf'].get() == True, " .pdf did not match"
    app.debug_mode.get() == True, "Debug mode did not match"
    app.server_port.get() == 50210, "Server port value did not match"

    print("All tests successful")

    if os.path.exists(test_file_path):
        os.remove(test_file_path)
        print(f"Test file {test_file_path} removed")

    root.destroy()

if __name__ == "__main__":
    run_test()
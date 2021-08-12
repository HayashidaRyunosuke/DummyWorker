import tkinter as tk
import tkinter.ttk as ttk
import random
import subprocess
subprocess.Popen("work.bat")
root=tk.Tk()
root.iconbitmap(default="favicon.ico")
root.title("Main System")
dummy_dirs = ["main","dist","dll","lib","bin","dev","files"]
dummy_files = ["windows","index","config","style","main"]
dummy_extensions = ["dll","bat","exe","html","ini",".py"]
progressbar=ttk.Progressbar(root,orient="horizontal",length=300,mode="determinate")
progressbar.pack()
maximum_bar=1000
value_bar=0
div_bar=1
progressbar.configure(maximum=maximum_bar,value=value_bar)
def var_start(value_bar):
    progressbar.configure(value=value_bar)
def start_progress():
    global value_bar,div_bar,text_label
    for i in range(maximum_bar):
        value_bar+=div_bar
        text_label.set("c:"+dummy_dirs[random.randint(0,len(dummy_dirs)-1)]+"/"+dummy_files[random.randint(0,len(dummy_files)-1)]+"."+dummy_extensions[random.randint(0,len(dummy_extensions)-1)])
        if value_bar==maximum_bar:
            progressbar.after(1000,var_start(value_bar))
            value_bar = 0
            start_progress()
        else:
            progressbar.after(1000,var_start(value_bar))
            progressbar.update()
text_label=tk.StringVar()
text_label.set("0")
label=tk.Label(textvariable=text_label)
label.pack()
start_progress()
root.mainloop()
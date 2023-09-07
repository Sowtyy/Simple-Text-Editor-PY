import tkinter
import tkinter.filedialog
import tkinter.scrolledtext


VERSION = "1.0.0"
VERSION_DATE = "07.09.2023"
NAME = "Sowtyy's Simple Text Editor PY"


def writeFile(path : str, data : str):
  with open(path, "w", encoding = "utf-8") as file:
    file.write(data)
  
  print(f"Wrote file: Path: {path}.")
  return

def readFile(path : str):
  with open(path, "r", encoding = "utf-8") as file:
    data = file.read()
  
  print(f"Read file: Path: {path}.")
  return data

def replaceTextValue(textObj : tkinter.Text, newValue : str):
  textObj.delete(1.0, tkinter.END)
  textObj.insert(tkinter.END, newValue)

  print("Replaced text value.")
  return

def askOpenFileAndReplaceTextValue(textObj : tkinter.Text):
  filePath = tkinter.filedialog.askopenfilename()
  if not filePath:
    return
  replaceTextValue(textObj, readFile(filePath))
  return

def askOpenFileAndWriteTextValue(textObj : tkinter.Text):
  filePath = tkinter.filedialog.askopenfilename()
  if not filePath:
    return
  writeFile(filePath, textObj.get(1.0, "end-1c"))
  return


def main():
  rootWindow = tkinter.Tk()
  rootWindow.title(f"{NAME}  {VERSION}")

  #textBox = tkinter.Text(rootWindow)
  textBox = tkinter.scrolledtext.ScrolledText(rootWindow)
  textBox.pack(fill = tkinter.BOTH, expand = True)

  menuBar = tkinter.Menu(rootWindow)
  rootWindow.config(menu = menuBar)

  fileMenu = tkinter.Menu(menuBar, tearoff = False)
  fileMenu.add_command(label = "Open...", command = lambda: askOpenFileAndReplaceTextValue(textBox))
  fileMenu.add_command(label = "Save as...", command = lambda: askOpenFileAndWriteTextValue(textBox))
  fileMenu.add_separator()
  fileMenu.add_command(label = "Exit", command = rootWindow.destroy)

  menuBar.add_cascade(label = "File", menu = fileMenu)

  rootWindow.bind("<Control-o>", lambda *args: askOpenFileAndReplaceTextValue(textBox))
  rootWindow.bind("<Control-s>", lambda *args: askOpenFileAndWriteTextValue(textBox))

  rootWindow.mainloop()
  return

if __name__ == "__main__":
  main()

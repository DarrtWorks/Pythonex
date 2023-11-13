import subprocess
import webbrowser


n = input("App:")


if n=="notepad":
    subprocess.call('notepad.exe')
    
elif n=="youtube":
  webbrowser.open('https://youtube.com')

elif n =="vscode":
  subprocess.Popen('C:\\Users\\Darsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
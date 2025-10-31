import platform

if platform.system() == "Windows":
    print ("Winget")
elif platform.system() == "Linux":
    print ("apt")
elif platform.system() == "macOS" or platform.system == "Darwin":
    print ("brew")
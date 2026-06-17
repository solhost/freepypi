from colorama import Fore, init
import urllib.request
import sys
import os
import shutil
import tomllib
init(autoreset=True)

VERSION = "0.1.0"

if len(sys.argv) == 1:
    print(Fore.LIGHTYELLOW_EX + "freePyPI " + Fore.WHITE + VERSION)
elif len(sys.argv) > 1:
    if sys.argv[1] == "install":
        if len(sys.argv) > 2:
            print(Fore.LIGHTYELLOW_EX + "freePyPI " + Fore.WHITE + VERSION)
            confirm = input(f"Install package {sys.argv[2]}? (y/N) ")
            if confirm.lower() == "y":
                print(Fore.GREEN + "[- - -] " + Fore.WHITE + "Installing package...")
                if not os.path.exists("py_modules"):
                    os.mkdir("py_modules")
                if not os.path.exists("py_modules/packages.lock"):
                    with open("py_modules/packages.lock", "w") as f:
                        f.write("")
                urllib.request.urlretrieve(f"https://solhost.github.io/freepypi/archive/{sys.argv[2]}.whl", "out.whl")
                print(Fore.GREEN + "[- - -] " + Fore.WHITE + "Fetched package...")
                shutil.unpack_archive("out.whl", "py_modules", "zip")
                with open("py_modules/pyproject.toml", "rb") as f:
                    data = tomllib.load(f)
                print(Fore.CYAN + "[/] " + Fore.WHITE + f"Installed package {data['name']} by {data['author']}.")
                os.remove("py_modules/pyproject.toml")
                os.remove("out.whl")
                with open("py_modules/packages.lock", "a") as f:
                    f.write(data["name"] + "\n")
            else:
                print(Fore.RED + "Abort installation.")
        else:
            print(Fore.RED + "ERROR: Please provide a subcommand as an argument.")
    elif sys.argv[1] == "list":
        with open("py_modules/packages.lock") as f:
            print(f.read())
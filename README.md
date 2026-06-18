<img src="md-assets/freePyPI.png">

# What is freePyPI?
FreePyPI is the open-source, non-bureaucratic Python package index, designed for a simple build system, simple publishing and a overall easy workflow.
# How to install freePyPI?
It is quite unified across both Windows and *nix systems, Firstly do this:
```bash
pip install colorama
mkdir freepypi
cd freepypi
curl -O https://solhost.github.io/freepypi/src/core.py
cd ..
```
Voila! freePyPI is installed on your system.
# How do I use freePyPI
freePyPI has 2 commands:
- install <pkg> - install a package from the freePyPI registry
- list - list all installed packages that exist in `./py_modules/`
Examples:
Install a package:
```bash
python3 freepypi/core.py install chudprogram@0.1.0
```
List all installed packages in `./py_modules/`:
```bash
python3 freepypi/core.py list
```
## For people wishing to publish a package:
You need a wheel building system, we recommend the official `build` package *run in your project directory*. This command works on both Windows and *nix systems:
```bash
python3 freepypi/core.py install build@0.1.0
```
Now in your project directory, you need:
- pyproject.toml
*pyproject.toml structure:*
```toml
name = "mypackage@x.y.z"
author = "StrangeOwl69"
```
- <yourproject>@x.y.z.py
*Your project can contain everything, from a library, to a complete cli tool*

You have successfully created your project, Now let's build it! *in your project directory*

works on both Windows and *nix systems
```bash
python3 py_modules/build.py mk <your-project-file.py>
```
Voila! A .whl file should have appeared in a dist/ folder in your project directory.

# Publishing it:

Fork this repository on GitHub, add your .whl file into the archive/ folder, Open a pull request and expect your package to be up within 42 hours!

## Test it:

After you publish it and you are sure that it is up, you can install your own package with this command:
```bash
python3 freepypi/core.py install <yourproject@x.y.z>
```
*Note that your packages live in a ./py_modules/ directory*

## Thanks for using freePyPI!
freePyPI would not have been possible without you and community authors, we thank you for contributing!

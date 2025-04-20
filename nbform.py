import nbformat

with open("code.ipynb", "r", encoding="utf-8") as f:
    notebook = nbformat.read(f, as_version=4)

with open("fixed.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(notebook, f)
#!/usr/bin/env python

import nbformat as nb

notebook = nb.v4.new_notebook()
code = nb.v4.new_code_cell(
    """name = "Jeff"
print(f"Hello, {name}")"""
)

notebook.cells.append(code)

with open("template.ipynb", "w") as f:
    nb.write(notebook, f)
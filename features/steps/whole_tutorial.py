from databaker.framework import *
from pathlib import Path
from os import listdir
import pandas as pd

#### "Given" functions

@given(u'code to complete a data transformation from folder "{foldername}"')
def step_impl(context, foldername):
    context.path = Path(".") / "databaker" / "bdd_tests" / foldername
    context.script = Path(".") / "databaker" / "bdd_tests" / foldername / "main.py"

    import subprocess
    import sys
    #print(context.script)
    transform = [sys.executable, "main.py"]
    subprocess.call(transform, cwd=context.path)
    #assert subprocess.call(transform, cwd=context.path) == 0
    

@given(u'a resulting CSV file is produced "{filename}"')
def step_impl(context, filename):
    csv_path = Path(".") / context.path / "out"
    if filename in os.listdir(csv_path):
        #print(True)
        context.df = pd.read_csv(Path(".") / csv_path / filename)
        #print(context.df)
    else:
        raise NotImplementedError(u'a resulting CSV file is produced "{filename}"') #Not sure which error to throw here.





#### "Then" functions

@then(u'a resulting CSV file is produced "{filename}"')
def step_impl(context, filename):
    csv_path = Path(".") / context.path / "out"
    if filename in os.listdir(csv_path):
        #print(True)
        context.df = pd.read_csv(Path(".") / csv_path / filename)
        #print(context.df)
    else:
        raise NotImplementedError(u'a resulting CSV file is produced "{filename}"') #Not sure which error to throw here.

@then(u'check that the number of rows = {rows}')
def step_impl(context, rows):
    #print(len(context.df))
    #print(type(rows))
    if len(context.df) == int(rows):
        print(True)
        #print(len(context.df))
    
    else:
        raise NotImplementedError(u'check that the number of rows = {rows}') #Not sure which error to throw here.
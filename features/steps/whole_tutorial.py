from databaker.framework import *
from pathlib import Path
import subprocess
import sys
import pandas as pd

#### "Given" functions

@given(u'code to complete a data transformation from folder "{foldername}"')
def step_impl(context, foldername):
    # foldername taken from the senario outline in the feature file which in turn takes
    # the name from the examples table associated with each scenario outline.

    # Define the path to the whole folder containing the transform code (main.py)
    # info.json and the "out" folder.
    # Added to context so that this path can be reused later in the scenario.   

    # The transform of the associated folder in the examples table is executed.
    # This will re-write the out folder - including CSV
    # So the new properties of the CSV can be used in comparisions.

    # Current working directory (cwd=) is changed because main.py needs to be
    # executed in the same directory as info.json
    
    context.path = Path(".") / "databaker" / "bdd_tests" / foldername

    transform = [sys.executable, "main.py"]
    subprocess.call(transform, cwd=context.path)
    #assert subprocess.call(transform, cwd=context.path) == 0
    
# Check if there is a CSV file in the expeced location. If so, then create
# a pandas dataframe and add it to context to be used in the "then" portion
# of the scenario.
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

# This is identical to the @given but is needed in the first scenario in which
# this step is the final result of the test.
@then(u'a resulting CSV file is produced "{filename}"')
def step_impl(context, filename):
    csv_path = Path(".") / context.path / "out"
    if filename in os.listdir(csv_path):
        #print(True)
        context.df = pd.read_csv(Path(".") / csv_path / filename)
        #print(context.df)
    else:
        raise NotImplementedError(u'a resulting CSV file is produced "{filename}"') #Not sure which error to throw here.

# Actually checking the property/attribute of the outputted CSV file is as expected.
@then(u'check that the number of rows = {rows}')
def step_impl(context, rows):
    #print(len(context.df))
    #print(type(rows))
    if len(context.df) == int(rows):
        print(True)
        #print(len(context.df))
    
    else:
        raise NotImplementedError(u'check that the number of rows = {rows}') #Not sure which error to throw here.
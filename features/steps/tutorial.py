from databaker.framework import *
from pathlib import Path

@given(u'an Excel file "{filename}"')
def step_impl(context, filename):
    context.databaker = loadxlstabs(Path(".") / "databaker" / "tutorial" / filename, sheetids="*", verbose=True)


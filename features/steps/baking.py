import json
import os

from behave import *
from pathlib import Path
from databaker.framework import loadxlstabs
from databaker.jupybakeutils import *
from databaker.structure_csv_default import *
from databaker.constants import *

def get_fixture(file_name):
    """Helper to get specific files out of the fixtures dir"""
    feature_path = Path(os.path.dirname(os.path.abspath(__file__))).parent
    fixture_file_path = Path(feature_path, "fixtures", file_name)
    return fixture_file_path

@given(u'we define the dimensions and observations:')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we define the dimensions and observations:')
    context.tab = context.tabs[0]

    context.year = context.tab.excel_ref("A13")
    context.month = context.tab.excel_ref("B6:B25").is_not_blank()
    context.day = context.tab.excel_ref("C6:C25")
    context.top_dims = context.tab.excel_ref("D5:I5")
    context.over_dim = context.tab.excel_ref("D4")
    context.bottom_dims = context.tab.excel_ref("D26:I26")
    context.under_dim = context.tab.excel_ref("D27")
    context.county = context.tab.excel_ref("J6:J25")
    context.country = context.tab.excel_ref("K6:K25").is_not_blank()
    context.unit = context.tab.excel_ref("M13")

    context.observations = context.tab.excel_ref("D6:I25")


@given(u'we create a list of dimensions (HDim objects) with their relation to observations.')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we create a list of dimensions (HDim objects) with their relation to observations.')
    context.dimensions = [
        HDim(context.year, "Year", CLOSEST, LEFT),
        HDim(context.month, "Month", CLOSEST, ABOVE),
        HDim(context.day, "Day", DIRECTLY, LEFT),
        HDim(context.top_dims, "Top Dims", DIRECTLY, ABOVE),
        HDim(context.over_dim, "Over Dim", CLOSEST, ABOVE),
        HDim(context.bottom_dims, "Bottom Dims", DIRECTLY, BELOW),
        HDim(context.under_dim, "Under Dim", CLOSEST, BELOW),
        HDim(context.county, "County", DIRECTLY, RIGHT),
        HDim(context.country, "Country", CLOSEST, ABOVE),
        HDim(context.unit, "Unit", CLOSEST, RIGHT)
    ]


@given(u'we create a ConversionSegment object.')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we create a ConversionSegment object.')
    context.tidy_sheet = ConversionSegment(context.tab, context.dimensions, context.observations)


@given(u'we convert the ConversionSegment object into a pandas dataframe.')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we convert the ConversionSegment object into a pandas dataframe.')
    context.df = context.tidy_sheet.topandas()


@given(u'we have the file "{expected_csv}" transformed back into a pandas dataframe.')
def step_impl(context, expected_csv):
    #raise NotImplementedError(u'STEP: Given we have the expected CSV file transformed back into a pandas dataframe.')
    path_to_csv = get_fixture(expected_csv)
    context.expected_df = pandas.read_csv(path_to_csv, dtype = {"Day": object})


@then(u'the two dataframes should be identical.')
def step_impl(context):
    #pandas.set_option("display.max_rows", None, "display.max_columns", None)
    #print(context.df)
    #print("")
    #print(context.expected_df)
    #print("")
    #print("difference")
    #print(context.df.equals(context.expected_df))
    #print("")

    #print(context.df.dtypes)
    #print("")
    #print(context.expected_df.dtypes)


    #comp_df = context.df.merge(context.expected_df, indicator = True)
    #print(comp_df)

    #new_df = pandas.concat([context.df, context.expected_df])
    #new_df = new_df.reset_index(drop=True)
    #df_gpby = new_df.groupby(list(new_df.columns))
    #idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]
    #new_df.reindex(idx)
    #print(new_df)
    #print("!")

    
    if context.df.equals(context.expected_df):
        step = "Success"

    else:
        raise NotImplementedError(u'STEP: Then the two dataframes should be identical.')
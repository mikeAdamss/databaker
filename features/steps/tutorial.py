from databaker.framework import *
from pathlib import Path

@given(u'an Excel file "{filename}"')
def step_impl(context, filename):
    context.tabs = loadxlstabs(Path(".") / "databaker" / "tutorial" / filename, sheetids="*", verbose=True)

@given(u'tab_1 = tabs[0]')
def step_impl(context):
    context.tab_1 = context.tabs[0]

@given(u'names = tab.excel_ref("A4").expand(DOWN).is_not_blank()')
def step_impl(context):
    context.names = context.tab_1.excel_ref("A4").expand(DOWN).is_not_blank()

@given(u'measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()')
def step_impl(context):
    context.measure_types = context.tab_1.excel_ref("B3").expand(RIGHT).is_not_blank()
    #print(savepreviewhtml(context.measure_types))

@given(u'unit = "Count"')
def step_impl(context):
    context.unit = "Count"

@given(u'obs = names.waffle(measure_types)')
def step_impl(context):
    context.obs = context.names.waffle(context.measure_types)

@given(u'dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]')
def step_impl(context):
    context.dimensions = [HDim(context.names, "Name", DIRECTLY, LEFT), HDim(context.measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", context.unit)]





@then(u'names = tab.excel_ref("A4").expand(DOWN).is_not_blank()')
def step_impl(context):
    context.names = context.tab_1.excel_ref("A4").expand(DOWN).is_not_blank()

@then(u'measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()')
def step_impl(context):
    context.measure_types = context.tab_1.excel_ref("B3").expand(RIGHT).is_not_blank()
    #print(savepreviewhtml(context.measure_types))

@then(u'unit = "Count"')
def step_impl(context):
    context.unit = "Count"

@then(u'obs = names.waffle(measure_types)')
def step_impl(context):
    context.obs = context.names.waffle(context.measure_types)

@then(u'dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]')
def step_impl(context):
    context.dimensions = [HDim(context.names, "Name", DIRECTLY, LEFT), HDim(context.measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", context.unit)]


#@then(u'dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]')
#def after_scenario(context, senario):
#    context.dimensions = [HDim(context.names, "Name", DIRECTLY, LEFT), HDim(context.measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", context.unit)]

@then(u'tidy_sheet = ConversionSegment(tab, dimensions, obs)')
def step_impl(context):
    context.tidy_sheet = ConversionSegment(context.tab_1, context.dimensions, context.obs)
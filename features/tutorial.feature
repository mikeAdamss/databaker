Feature: Tutorial
  We want to capture the features from the Databaker tutorial so that we can
  check that expectations are met.

  Scenario: load Excel file
    Given an Excel file "example1.xls"

  Scenario: get tab
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]

  Scenario: define/locate name dimension
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    # When name dimension is being defined/located
    Then names = tab.excel_ref("A4").expand(DOWN).is_not_blank()

  Scenario: define/locate measure_types dimension
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    Then measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()

  Scenario: define unit dimension
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    Then unit = "Count"

  Scenario: define/locate observations
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    And names = tab.excel_ref("A4").expand(DOWN).is_not_blank()
    And measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()
    Then obs = names.waffle(measure_types)

  Scenario: Define dimensions in relation to observations
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    And names = tab.excel_ref("A4").expand(DOWN).is_not_blank()
    And measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()
    And unit = "Count"
    And obs = names.waffle(measure_types)
    Then dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]

  #Scenario: get dimensions list in relation to observations
  #  Given all dimension have been defined/located
  #  And observations have been defined/located
  #  When dimensions list is being populated
  #  Then dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]

  Scenario: use conversion segment to define the new sheet.
    Given an Excel file "example1.xls"
    And tab_1 = tabs[0]
    And names = tab.excel_ref("A4").expand(DOWN).is_not_blank()
    And measure_types = tab.excel_ref("B3").expand(RIGHT).is_not_blank()
    And unit = "Count"
    And obs = names.waffle(measure_types)
    And dimensions = [HDim(names, "Name", DIRECTLY, LEFT), HDim(measure_types, "Measure Type", DIRECTLY, ABOVE), HDimConst("Unit", unit))]
    Then tidy_sheet = ConversionSegment(tab, dimensions, obs)
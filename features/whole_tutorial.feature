Feature: Whole tutorial
    We want to capture our databaker uses across a whole transform so that we
    can compare expected properties of the resulting CSV file to the ones
    produced after any databaker edits.

    Scenario Outline: CSV output from a completed transformation
        Given code to complete a data transformation from folder <folder>
        Then a resulting CSV file is produced <CSV name>

        Examples: Transforms
            | folder     | CSV name   | attribute   |
            | "BEIS-Lower-and-Middle-Super-Output-Areas-electricity-consumption"    | "lsoa_observations.csv"   | 375535    |

    Scenario Outline: Output CSV contains the expected number of rows
        Given code to complete a data transformation from folder <folder>
        Then a resulting CSV file is produced <CSV name>
        Then check that the number of rows = <attribute>

        Examples: Transforms
            | folder     | CSV name   | attribute   |
            | "BEIS-Lower-and-Middle-Super-Output-Areas-electricity-consumption"    | "lsoa_observations.csv"   | 375535    |


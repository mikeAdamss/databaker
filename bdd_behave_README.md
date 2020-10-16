# BDD Behave Tests for Databaker
 
BDD behave test suite scaffolding for the databaker library. Tests work by
comparing known/expected values, attributes and properties of the resulting
CSV files produced by each transform to those produced after any future
Databaker refactoring is completed.

## Starting Up

### Requirements:

pipenv requirements.txt

-i https://pypi.org/simple
airtable-python-wrapper==0.15.0
argon2-cffi==20.1.0
async-generator==1.10
attrs==20.2.0
backcall==0.2.0
beautifulsoup4==4.9.1
behave==1.2.6
bleach==3.1.5
cachecontrol[filecache]==0.12.6
certifi==2020.6.20
cffi==1.14.2
chardet==3.0.4
cycler==0.10.0
decorator==4.4.2
defusedxml==0.6.0
entrypoints==0.3
et-xmlfile==1.0.1
fingertips-py==0.2.2
git+https://github.com/GSS-Cogs/databaker.git@15f2c18a6864476eca075b270da201e3adb2e757#egg=databaker
git+https://github.com/GSS-Cogs/gss-utils.git@5148696f44a020af15900832440bd904a7b82c42#egg=gss-utils
html2text==2020.1.16
idna==2.10
importlib-metadata==1.7.0 ; python_version < '3.8'
ipykernel==5.3.4
ipython-genutils==0.2.0
ipython==7.18.1 ; python_version >= '3.3'
ipywidgets==7.5.1
isodate==0.6.0
jdcal==1.4.1
jedi==0.17.2
jinja2==2.11.2
json5==0.9.5
jsonschema==3.2.0
jupyter-client==6.1.7
jupyter-console==6.2.0
jupyter-core==4.6.3
jupyter==1.0.0
jupyterlab-pygments==0.1.1
jupyterlab-server==1.2.0
jupyterlab==2.2.7
jupytext==1.6.0
kiwisolver==1.2.0
lml==0.0.9
lockfile==0.12.2
lxml==4.5.2
markdown-it-py==0.5.4
markupsafe==1.1.1
matplotlib==3.3.1
mistune==0.8.4
msgpack==1.0.0
multi-key-dict==2.0.3
nbclient==0.5.0
nbconvert==6.0.1
nbformat==5.0.7
nest-asyncio==1.4.0
notebook==6.1.4
numpy==1.19.2
odfpy==1.4.1
openpyxl==3.0.5
packaging==20.4
pandas==0.25.3
pandocfilters==1.4.2
parse-type==0.5.2
parse==1.18.0
parso==0.7.1
pbr==5.5.0
pexpect==4.8.0 ; sys_platform != 'win32'
pickleshare==0.7.5
pillow==7.2.0
prometheus-client==0.8.0
prompt-toolkit==3.0.7
ptyprocess==0.6.0 ; os_name != 'nt'
pycparser==2.20
pyexcel-io==0.5.20
pyexcel-ods==0.5.6
pyexcel-odsr==0.5.2
pyexcel-text==0.2.7.1
pyexcel==0.6.4
pygments==2.6.1
pyparsing==2.4.7
pyrsistent==0.17.2
python-box==5.1.1
python-dateutil==2.8.1
python-jenkins==1.7.0
pytz==2020.1
pyyaml==5.3.1
pyzmq==19.0.2
qtconsole==4.7.7
qtpy==1.9.0
rdflib==4.2.2
regex==2020.7.14
requests==2.24.0
send2trash==1.5.0
six==1.15.0
soupsieve==2.0.1
sparqlwrapper==1.8.5
tabulate==0.8.7
terminado==0.8.3
testpath==0.4.4
texttable==1.6.3
titlecase==1.1.1
toml==0.10.1
tornado==6.0.4
traitlets==5.0.4
urllib3==1.25.10
wcwidth==0.2.5
webencodings==0.5.1
widgetsnbextension==3.5.1
zipp==3.1.0


### Quick Start

In a virtual environment with the same requirements as above - should be the
same as the environment used to complete Databaker transforms.
Use:
    pipenv install --dev

then:
    run behave

## Feature Files

In the folder named "features" there will be two .feature files and a folder "steps".
The first feature file (tutorial.feature) has been kept as a reminder to an
alternative approach to BDD testing. But as such it does not follow the same structure
as the second file (whole_tutorial.feature) which is the main basis for this test
suite.

Each scenario in the feature file follows the same template for the convenience of
adding new tests in the future:

Scenario Outline: Output CSV contains the expected *value/attribute/property for current test*
    Given code to complete a data transformation from folder <folder>
    Then a resulting CSV file is produced <CSV name>
    Then check that the *value/attribute/property* = <attribute>

    Examples: Transforms
        | folder     | CSV name   | attribute   |
        | "Example1"    | "example1_observations.csv"   | some value    |
        | "Example2"    | "example2_observations.csv"   | another value    |

**Note : Folder containing the entire transform (main.py, info.json, "out" 
folder/observations csv) must be a copy placed in the folder "bdd_tests"
found at databaker/databaker/bbd_tests

## Steps

Each feature file needs an associated steps script. Similarly to the feature
files, ignore tutorial.py as whole_tutorial.py contains the correct structure.

whole_tutorial.py already contains the step functions for the "given" portions
of each scenario - execute the transform and check for the resulting csv.

New "then" functions will have to be added in accordance to their inclusion in
the feature file.

E.g. Step to check the length of the CSV is the same:

@then(u'check that the number of rows = {rows}')
def step_impl(context, rows):
    if len(context.df) == int(rows):
        print(True)

    else:
        raise NotImplementedError(u'check that the number of rows = {rows}')

**Notes : I'd recommend reading the comments in whole_tutorial.py to understand
        from where certain values are comming. E.g. context.df is defined in
        a previous step.

        Raising the error is more of a placeholder and should be changed to
        something more suitable but fulfills the need to break the test.

## Typical Workflow:

1) Identify a suitable transform for inclusion in the test suite. The collection
    of transforms should cover most of our Databaker uses.

2) Place a copy of the entire folder containing the transform (main.py, info.json,
    "out" folder/observations csv) in the folder called "bdd_tests" found at:
    databaker/databaker/bdd_tests

3) Append to the feature file (it can be a new one or whole_tutorial.features can 
    be used as long as there is a corresponding steps script). New scenarios must
    have a new examples table. Where appropriate include transforms from other
    scenarios and find their expected values for each test.

4) Any new scenarios created must have corresponding steps. This should be a new
    "then" function for each senario with python code to verify the correctness
    of the supplied/known value.

    A shortcut for a step template is to run behave after adding the scenario 
    outline to the feature file. This will give a suggestion for a function
    with a not implemented error.

6) Run behave

## Next Steps

To make this a more functional/expansive test suite, we need to identify a list
of complete transforms which cover a wide variety of our Databaker uses.

We also need to identify a list of useful attributes/values/properties which
can be taken from the resulting CSV files. These can then be used to implement
scenario outlines.

Finally, I am aware of scenario backgrounds which could be used to avoid executing
the common two steps in each scenario (execute transform and check for CSV file).
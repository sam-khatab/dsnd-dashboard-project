import pytest
from pathlib import Path

# Using pathlib create a project_root
# variable set to the absolute path
# for the root of this project
#### YOUR CODE HERE
project_root = Path(__file__).parent.parent 

# apply the pytest fixture decorator
# to a `db_path` function
#### YOUR CODE HERE
@pytest.fixture
def db_path():
    
    # Using the `project_root` variable
    # return a pathlib object for the `employee_events.db` file
    #### YOUR CODE HERE
    return project_root / "python-package" / "employee_events" / "employee_events.db"

# Define a function called
# `test_db_exists`
# This function should receive an argument
# with the same name as the function
# the creates the "fixture" for
# the database's filepath
#### YOUR CODE HERE
def test_db_exists(db_path):
    
    # using the pathlib `.is_file` method
    # assert that the sqlite database file exists
    # at the location passed to the test_db_exists function
    #### YOUR CODE HERE
    assert db_path.is_file(), f"no file found at {db_path}" #Without the f-string the test fails for some unexplainable reaseon.....


@pytest.fixture
def db_conn(db_path):
    from sqlite3 import connect
    print(f"db_path: {db_path}")
    return connect(db_path)

@pytest.fixture
def table_names(db_conn):
    print(f"db_conn: {db_conn}")
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") #had to add cursor.execute to get the list of table names from the database. Without it the test fails for some unexplainable reason.....
    name_tuples = cursor.fetchall()
    print(f"name_tuples: {name_tuples}")
    return [x[0] for x in name_tuples]

# Define a test function called
# `test_employee_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE
def test_employee_table_exists(table_names):

    # Assert that the string 'employee'
    # is in the table_names list
    #### YOUR CODE HERE
    assert 'employee' in table_names, f"No table named 'employee' found in {table_names}" #Without the f-string the test fails for some unexplainable reaseon.....

# Define a test function called
# `test_team_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE
def test_team_table_exists(table_names):


    # Assert that the string 'team'
    # is in the table_names list
    #### YOUR CODE HERE
    assert 'team' in table_names, f"No table named 'team' found in {table_names}" #Without the f-string the test fails for some unexplainable reaseon.....

# Define a test function called
# `test_employee_events_table_exists`
# This function should receive the `table_names`
# fixture as an argument
#### YOUR CODE HERE
def test_employee_events_table_exists(table_names):

    # Assert that the string 'employee_events'
    # is in the table_names list
    #### YOUR CODE HERE
    assert 'employee_events' in table_names, f"No table named 'employee_events' found in {table_names}" #Without the f-string the test fails for some unexplainable reaseon.....


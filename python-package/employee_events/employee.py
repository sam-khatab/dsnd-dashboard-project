'''
Module: employee_events.employee
This module defines the Employee class, which inherits from QueryBase
and provides methods for querying the employee table in the employee_events database.
The Employee class includes methods for retrieving employee names, usernames, and model
data related to positive and negative events. The module also imports necessary dependencies
 for SQL execution.
'''
# Import the QueryBase class
from .query_base import QueryBase
from .sql_execution import execute


# Import dependencies needed for sql execution
# from the `sql_execution` module

# Define a subclass of query_base.QueryBase
# called Employee
class Employee(QueryBase):
    '''
    A class that inherits from QueryBase and adds methods
    for querying the employee table in the employee_events database.'''

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        '''
        A method that returns a list of tuples
        containing the full names and employee ids
        '''

        # Query 3
        # Write an SQL query
        # that selects two columns
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        sql_query = f"SELECT full_name, employee_id FROM {self.name}"
        #sql_excution.execute(sql_query) return a list of tuples from an sql execution
        return execute(sql_query) #execute is imported from sql_execution.py

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, employee_id):
        '''
        A method that returns a list of tuples
        containing the full name of an employee'''

        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        sql_query = f"SELECT full_name FROM {self.name} WHERE employee_id = {employee_id}"
        #sql_excution.execute(sql_query) return a list of tuples from an sql execution
        return execute(sql_query)


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, employee_id):
        '''
        A method that returns a pandas dataframe
        containing the sum of positive and negative events'''

        sql_query = f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {employee_id}
                """
        return execute(sql_query) #execute is imported from sql_execution.py
    
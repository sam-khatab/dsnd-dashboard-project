'''
Module: employee_events.team
This module defines the Team class, which inherits from QueryBase and provides methods for querying
the team table in the employee_events database. The Team class includes methods for retrieving team
names, usernames, and model data related to positive and negative events.
The module also imports necessary dependencies
for SQL execution.
'''
# Import the QueryBase class
# YOUR CODE HERE
from .query_base import QueryBase

# Import dependencies for sql execution
#### YOUR CODE HERE
from .sql_execution import execute

# Create a subclass of QueryBase
# called  `Team`
#### YOUR CODE HERE
class Team(QueryBase):
    '''
    A class that inherits from QueryBase and adds methods
    for querying the team table in the employee_events database.'''
    # Set the class attribute `name`
    # to the string "team"
    #### YOUR CODE HERE
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        '''
        A method that returns a list of tuples
        containing the team names and team ids'''
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        sql_query = f"SELECT team_name, team_id FROM {self.name}"
        #sql_excution.execute(sql_query) return a list of tuples from an sql execution
        return execute(sql_query) #execute is imported from sql_execution.py

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, user_id):
        '''
        A method that returns a list of tuples
        containing the team name of a team'''
        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        #### YOUR CODE HERE
        sql_query = f"SELECT team_name FROM {self.name} WHERE team_id = {user_id}"
        return execute(sql_query) #execute is imported from sql_execution.py

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
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {employee_id}
                    GROUP BY employee_id
                   )
                """
        return execute(sql_query) #execute is imported from sql_execution.py

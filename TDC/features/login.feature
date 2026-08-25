Feature: Login
    Identify the visitor and store their data

Scenario: Successful Login
    Given username 'user' and password 'pwd'
    When Log In button clicked
    Then show welcome message

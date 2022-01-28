Feature: sendEmail
  Scenario: Send a message via internal mail (3a)
    Given that the user is logged into the course platform#3
    When the user selects the “Internal Mail” option
    And fill in the necessary fields to send a message
    Then a new message is sent
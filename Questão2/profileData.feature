Feature: profileData
  Scenario: Change some profile data. For example, the marital status (4a)
    Given that the user is logged into the course platform#4
    When the user clicks on your profile and the option to “edit profile”
    And makes changes to the “marital status” field
    Then the changes are saved
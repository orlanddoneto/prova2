Feature: accessClass

  Scenario: access a class (1a)
    Given that the user is logged into the course platform
    When you select the option “My Courses” and choose your course
    And choose a lesson
    Then the user can access the lessons
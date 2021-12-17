Feature: Test

  Scenario: Test sum_cost
    Given  I have sum = 0
    When I sum the cost
    Then I expect to get result = 150000
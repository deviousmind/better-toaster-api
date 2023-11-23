# Created by xdanm at 11/23/2023
Feature: Smart Toaster
  # Enter feature description here

  Scenario: Start Toasting
    Given the toaster is online
    When it receives a request for wheat bread at level 3
    Then the toaster is in wait mode

  Scenario: Toasting in progress
    Given the toaster is online
    And the toaster is in wait mode
    When it receives a request for wheat bread at level 3
    Then a wait response is sent

  Scenario: Finish Toasting
    Given the toaster is online
    And it receives a request for wheat bread at level 3
    When it completes toasting
    Then a toast ready response is sent

  Scenario: Toaster offline
    Given the toaster is offline
    When it receives a request for wheat bread at level 3
    Then an offline response is sent

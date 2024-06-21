Feature: Login capability

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button

    @smoke
  Scenario: I login with valid credentials
    When login: I login with user "proms2023" and pasword "Betuna22@"
    Then books: I should land om books page

     @smoke
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pasword "<pasword>"
    Then login: I validate that error mesage is displayed

  Examples:
       | user      | pasword |
       | proms2023 | Betuna22  |
       | proms     | Betuna22@ |






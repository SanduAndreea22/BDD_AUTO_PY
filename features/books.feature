Feature: Login capability

  @smoke
  Scenario:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with valid credentials
    Then books: I should land om books page

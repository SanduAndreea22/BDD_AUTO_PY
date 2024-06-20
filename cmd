pip install -U selenium
pip install behave
pip install behave-html-formatter

run test
behave -f html -o behave.report.html --tags=smoke

# given - seteaza situatia initiala
# when - actiunile intermediare
# them - verificarea finala

'''
Given I am a user on home page
When I click bookstore application card
When I click login button
When I login with valid credentials
Then I should land om books page
'''
from survey import AnonymousSurvey

# Define a question
question = "What language you like most?"
my_survey = AnonymousSurvey(question)

# Show the question
my_survey.show_question()
print('\nEnter "q" at any time to "quit"')
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the results
print("Thank you for participating in the survey.")
my_survey.show_results()
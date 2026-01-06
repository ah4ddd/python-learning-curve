from survey import AnonymousSurvey

quest = AnonymousSurvey("Why i like boobs so much")

quest.show_question()
quest.store_response("Cos they warm soft and fucking awesome")

quest.show_results()

question = "What makes money so filthy and amazing? "

srv = AnonymousSurvey(question)

srv.show_question()
print("Enter 'q' at anytime to quit")

while True:
    response = input("What u say? ")
    if response == 'q':
        break
    srv.store_response(response)

print("\nThanks, forever in debt to your precious..")
srv.show_results()

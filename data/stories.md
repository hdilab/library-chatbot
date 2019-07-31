## greet path 1
* greet
  - utter_greet
> check_greeting

## provide_nursing_librarian_email path 2
* greet
  - utter_greet
* nursing_librarians_email
  - utter_nursing_librarians_email
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - action_restart

## news path 3
* greet
  - utter_greet
* difference_between_qualitative_quantative_articles
  - utter_difference_between_qualitative_quantative_articles
  - utter_did_that_help
* affirm
  - utter_gratitude
  - utter_goodbye
  - action_restart

## news path 4
* greet
  - utter_greet
* difference_between_qualitative_quantative_articles
  - utter_difference_between_qualitative_quantative_articles
  - utter_did_that_help
* deny
  - utter_ask_again
* how_to_know_type_of_articles
  - utter_article_type_from_articles
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - utter_gratitude
  - action_restart

## goodbye path 5
* goodbye
  - utter_goodbye

## goodbye path 6
> check_greeting
* goodbye
  - utter_goodbye

## provide_CINAHL_link path 7
> check_greeting
* access_CINAHL_database
  - utter_access_CINAHL_database
  - utter_input_in_CINAHL
* thanks
  - utter_anymore_questions
* deny
  - utter_goodbye
  - action_restart

## find_a_research_article path 8
* greet
    - utter_greet
* quantitative_research_article
    - utter_happy_to_help
    - utter_ask_article_for_research_or_project
* affirm
    - utter_ask_field_of_study
* choose{"area_of_study": "Nursing"}
    - slot{"area_of_study": "Nursing"}
    - action_database_link
    - utter_did_that_help
* affirm
    - utter_more_help_librarian_email
* goodbye
    - utter_goodbye
    - action_restart

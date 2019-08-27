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
  - utter_start_chat_again_button
  - action_restart

## provide_articles_from_pubmed
> check_greeting
* articles_from_pubmed
 - utter_open_pubmed_website
 - utter_did_that_help
* affirm
 - utter_gratitude
 - utter_goodbye
 - utter_start_chat_again_button
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
  - utter_start_chat_again_button
  - action_restart

## cite_an_article_using_apa_path
> check_greeting
* cite_an_article_using_apa
  - utter_cite_an_article_using_apa_partA
  - utter_cite_an_article_using_apa_partB
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## difference_between_qualitative_quantative_articles path 4
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
  - utter_start_chat_again_button
  - action_restart

## goodbye path 5
* goodbye
  - utter_goodbye

## goodbye path 6
> check_greeting
* goodbye
  - utter_goodbye

## if_an_article_is_peer_reviewed_path
> check_greeting
* article_is_peer_reviewed
  - utter_article_is_peer_reviewed
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart


## provide_CINAHL_link path 7
> check_greeting
* access_CINAHL_database
  - utter_access_CINAHL_database
  - utter_input_in_CINAHL
* thanks
  - utter_anymore_questions
* deny
  - utter_goodbye
  - utter_start_chat_again_button
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
    - utter_start_chat_again_button
    - action_restart

## find_authors_education_background_path
> check_greeting
* find_authors_education_background
  - utter_find_authors_education_background_i
  - utter_find_authors_education_background_ii
  - utter_find_authors_education_background_iii
  - utter_find_authors_education_background_iv
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## provide_RN_to_BSN_homepage_link path 9
> check_greeting
* find_RN_to_BSN_program_homepage
  - utter_provide_RN_to_BSN_homepage_link
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## deny_research_article_path 10
* greet
    - utter_greet
* quantitative_research_article
    - utter_happy_to_help
    - utter_ask_article_for_research_or_project
* deny
    - utter_start_chat_again_button
    - action_restart

## provide_plagiarism_guide_link_path
> check_greeting
* plagiarism_tutorial_in
  - utter_plagiarism_tutorial_link
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## provide_link_for_the_apa_exposed
> check_greeting
* link_for_apa_exposed
  - utter_link_for_apa_exposed
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## resource_guide_for_nursing_path
> check_greeting
* resource_guide_for_nursing
  - utter_resource_guide_for_nursing
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## title_page_for_uta_nursing_department
> check_greeting
* title_page_for_uta_nursing_department
  - utter_title_page_for_nursing_department
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

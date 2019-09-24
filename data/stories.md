## greet path 1
* greet
  - utter_greet
> check_greeting

## add_money_to_print_quota_path_17
> check_greeting
*  add_money_to_print_quota
  - utter_add_money_to_print_quota_i
  - utter_add_money_to_print_quota_ii
  - utter_add_money_to_print_quota_iii
  - utter_add_money_to_print_quota_iv
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## colors_and_sizes_of_poster_path_24
> check_greeting
* colors_and_sizes_of_poster
  - utter_colors_and_sizes_of_poster
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## file_type_to_print_poster_path_26
> check_greeting
* file_type_to_print_poster
  - utter_file_type_to_print_poster
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## hours_of_dining_services_path_29
> check_greeting
* hours_of_dining_services
  - utter_hours_of_dining_services
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## poster_pickup_location_path_27
> check_greeting
* poster_pickup_location
  - utter_poster_pickup_location
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart
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

## guest_visitor_alumni_library_access_path_18
> check_greeting
* guest_visitor_alumni_library_access
  - utter_guest_visitor_alumni_library_access
  - utter_acceptable_id
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## guest_visitor_alumni_wireless_internet_path_19
> check_greeting
* guest_visitor_alumni_wireless_internet
  - utter_guest_visitor_alumni_wireless_internet
  - utter_guest_computer_account
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## if_an_article_is_peer_reviewed_path
> check_greeting
* article_is_peer_reviewed
  - utter_article_is_peer_reviewed
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## pay_for_the_poster_path_22
> check_greeting
* pay_for_the_poster
  - utter_pay_for_the_poster_i
  - utter_pay_for_the_poster_ii
  - utter_pay_for_the_poster_iii
  - utter_pay_for_the_poster_iv
  - utter_pay_for_the_poster_v
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## plotter_printer_location_path_20
> check_greeting
* plotter_printer_location
  - utter_plotter_printer_location_i
  - utter_plotter_printer_location_ii
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## cost_to_print_the_plotter_path_21
> check_greeting
* cost_to_print_the_plotter
  - utter_cost_to_print_the_plotter
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

## reserve_study_room_path_28
> check_greeting
* reserve_study_room
  - utter_study_room_reserve_i
  - utter_study_room_reserve_ii
  - utter_study_room_reserve_iii
  - utter_study_room_reserve_iv
  - utter_study_room_reserve_v
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## submit_poster_order_online_path_23
> check_greeting
* submit_poster_order_online
  - utter_can_i_submit_poster_order_online
  - utter_did_that_help
* affirm
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart

## time_to_print_poster_path_25
> check_greeting
* time_to_print_poster
  - utter_time_to_print_poster
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

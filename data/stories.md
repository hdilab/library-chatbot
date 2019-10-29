## greet path
* greet
- utter_greet
> check_greeting

## find research article 1
> check_greeting
* quantitative_research_article
    - utter_ask_article_for_research_or_project
* affirm
    - utter_ask_field_of_study
* choose{"area_of_study": "Nursing"}
    - slot{"area_of_study": "Nursing"}
    - action_database_link
> check_find_research_article


## cite an article using APA path 4
> check_greeting
* cite_an_article_using_apa
  - utter_cite_an_article_using_apa
> check_cite_an_article_using_apa_path

## RN to BSN homepage link 5
> check_greeting
* find_RN_to_BSN_program_homepage
  - utter_provide_RN_to_BSN_homepage_link
> RN_to_BSN_homepage_link

## authors education background 6
> check_greeting
* find_authors_education_background
  - utter_find_authors_education_background
> check_author_education_background

## resource guide for nursing 7
> check_greeting
* resource_guide_for_nursing
  - utter_resource_guide_for_nursing
> check_resource_guide_for_nursing


## plagiarism guide 8
> check_greeting
* plagiarism_tutorial_in
  - utter_plagiarism_tutorial_link
> check_plagiarism_guide

## uta nursing title page 9
> check_greeting
* title_page_for_uta_nursing_department
  - utter_title_page_for_nursing_department
> check_uta_nursing_title_page

## nursing librarian email 10
> check_greeting
* nursing_librarians_email
  - utter_nursing_librarians_email
> check_nursing_librarian_email

## provide pubmed articles 11
> check_greeting
* articles_from_pubmed
 - utter_open_pubmed_website
> check_pubmed_articles

## check difference between qq articles 12
> check_greeting
* difference_between_qualitative_quantative_articles
  - utter_difference_between_qualitative_quantative_articles
> check_difference_between_qq_articles

## link for the apa exposed 14
> check_greeting
* link_for_apa_exposed
  - utter_link_for_apa_exposed
> check_link_for_the_apa_exposed

## tell if article is peer reviewed 15
> check_greeting
* article_is_peer_reviewed
  - utter_article_is_peer_reviewed
> check_tell_if_article_is_peer_reviewed


## add money 17
> check_greeting
* add_money_to_print_quota
  - utter_add_money_to_print_quota
> check_add_money

## add money cash 17
> check_add_money
> check_poster_payment_load_money
* cash
  - utter_pay_by_cash_response
> check_add_money_cash

## add money credit 17
> check_add_money
> check_poster_payment_load_money
* credit
  - utter_pay_by_credit_response
> check_add_money_credit

## check library alumni visitor access 18
> check_greeting``
* guest_visitor_alumni_library_access
  - utter_guest_visitor_alumni_library_access
> check_library_alumni_visitor_access

## check library alumni visitor wireless internet access 19
> check_greeting
* guest_visitor_alumni_wireless_internet
  - utter_guest_visitor_alumni_wireless_internet
> check_library_alumni_visitor_wireless_internet_access

## plotter printer location 20
> check_greeting
* plotter_printer_location
  - utter_plotter_printer_location
> check_plotter_printer_location 

## plotter cost 21
> check_greeting
* cost_to_print_the_plotter
  - utter_cost_to_print_the_plotter
> check_plotter_cost

## poster payment 22 sub
> check_greeting
* pay_for_the_poster
  - utter_pay_for_the_poster
* add_money_to_print_quota
  - utter_add_money_to_print_quota
> check_poster_payment_load_money

## poster payment 22 sub
> check_greeting
* pay_for_the_poster
  - utter_pay_for_the_poster
* get_temporary_card
  - utter_get_temporary_card
> check_poster_payment_temp_card

## poster online order 23
> check_greeting
* submit_poster_order_online
  - utter_can_i_submit_poster_order_online
> check_poster_online_order

## poster details 24
> check_greeting
* colors_and_sizes_of_poster
  - utter_colors_and_sizes_of_poster
> check_poster_details

## poster pickup time 25
> check_greeting
* time_to_print_poster
  - utter_time_to_print_poster
> poster_pickup_time

## poster file type 26
> check_greeting
* file_type_to_print_poster
  - utter_file_type_to_print_poster
> poster_file_type

## poster pickup location 27
> check_greeting
* poster_pickup_location
  - utter_poster_pickup_location
> poster_pickup_location

## reserve study room 28
> check_greeting
* reserve_study_room
  - utter_study_room_reserve
> check_reserve_study_room

## dining services hours 29
> check_greeting
* hours_of_dining_services
  - utter_hours_of_dining_services
> check_dining_services_hours

## provide CINAHL link
> check_greeting
* access_CINAHL_database
  - utter_access_CINAHL_database
  - utter_input_in_CINAHL
> provide_CINAHL_link

## guest library comuter access
> check_greeting
* can_a_guest_use_library_computers
  - utter_guest_library_computer_access
> guest_library_comuter_access

## good bye path
> check_find_research_article
> check_cite_an_article_using_apa_path
> RN_to_BSN_homepage_link
> check_author_education_background
> check_resource_guide_for_nursing
> check_plagiarism_guide
> check_uta_nursing_title_page
> check_nursing_librarian_email
> check_pubmed_articles
> check_difference_between_qq_articles
> check_link_for_the_apa_exposed
> check_tell_if_article_is_peer_reviewed
> check_add_money_cash
> check_add_money_credit
> check_library_alumni_visitor_access
> check_library_alumni_visitor_wireless_internet_access
> check_plotter_printer_location
> check_plotter_cost
> check_poster_payment
> check_poster_online_order
> check_poster_details
> poster_pickup_time
> poster_file_type
> poster_pickup_location
> check_reserve_study_room
> check_dining_services_hours
> provide_CINAHL_link
> guest_library_comuter_access
> check_poster_payment_temp_card
- utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye
  - utter_start_chat_again_button
  - action_restart
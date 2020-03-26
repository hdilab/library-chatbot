## find research article 1
* research_article
    - utter_ask_article_for_research_or_project
* affirm
    - utter_ask_field_of_study
* choose{"area_of_study": "Nursing"}
    - slot{"area_of_study": "Nursing"}
    - action_database_link

## find research article 1 deny path 1
* research_article
    - utter_ask_article_for_research_or_project
* deny
    - utter_ask_article_type
* class_writing_assignment
    - utter_ask_field_of_study
* choose{"area_of_study": "Nursing"}
    - slot{"area_of_study": "Nursing"}
    - action_database_link
    
## find research article 1 deny path 2
* research_article
    - utter_ask_article_for_research_or_project
* deny
    - utter_ask_article_type
* research_project
    - utter_class_writing_response

## find research article 1 deny path 3
* research_article
    - utter_ask_article_for_research_or_project
* deny
    - utter_ask_article_type
* other
    - utter_other_articles

## cite an article using APA path 4
* cite_an_article_using_apa
  - utter_cite_an_article_using_apa

## RN to BSN homepage link 5
* find_RN_to_BSN_program_homepage
  - utter_provide_RN_to_BSN_homepage_link

## authors education background 6
* find_authors_education_background
  - utter_find_authors_education_background

## resource guide for nursing 7
* resource_guide_for_nursing
  - utter_resource_guide_for_nursing

## plagiarism guide 8
* plagiarism_tutorial_in
  - utter_plagiarism_tutorial_link

## uta nursing title page 9
* title_page_for_uta_nursing_department
  - utter_title_page_for_nursing_department

## nursing librarian email 10
* nursing_librarians_email OR librarian_information
  - utter_nursing_librarians_email

## provide pubmed articles 11
* articles_from_pubmed
 - utter_open_pubmed_website

## check difference between qq articles 12
* difference_between_qualitative_quantative_articles
  - utter_difference_between_qualitative_quantative_articles

## link for the apa exposed 14
* link_for_apa_exposed
  - utter_link_for_apa_exposed

## tell if article is peer reviewed 15
* article_is_peer_reviewed
  - utter_article_is_peer_reviewed


## add money 17
* add_money_to_print_quota
  - utter_add_money_to_print_quota

## add money cash 17
* cash
  - utter_pay_by_cash_response

## add money credit 17
* credit
  - utter_pay_by_credit_response

## check library alumni visitor access 18
* guest_visitor_alumni_library_access
  - utter_guest_visitor_alumni_library_access

## check library alumni visitor wireless internet access 19
* guest_visitor_alumni_wireless_internet
  - utter_guest_visitor_alumni_wireless_internet

## plotter printer location 20
* plotter_printer_location
  - utter_plotter_printer_location 

## plotter cost 21
* cost_to_print_the_plotter
  - utter_cost_to_print_the_plotter

## poster payment 22 sub
* pay_for_the_poster
  - utter_pay_for_the_poster
* add_money_to_print_quota
  - utter_add_money_to_print_quota

## poster payment 22 sub
* pay_for_the_poster
  - utter_pay_for_the_poster
* get_temporary_card
  - utter_get_temporary_card

## poster online order 23
* submit_poster_order_online
  - utter_can_i_submit_poster_order_online

## poster details 24
* colors_and_sizes_of_poster
  - utter_colors_and_sizes_of_poster

## poster pickup time 25
* time_to_print_poster
  - utter_time_to_print_poster

## poster file type 26
* file_type_to_print_poster
  - utter_file_type_to_print_poster

## poster pickup location 27
* poster_pickup_location
  - utter_poster_pickup_location

## reserve study room 28
* reserve_study_room
  - utter_study_room_reserve

## dining services hours 29
* hours_of_dining_services
  - utter_hours_of_dining_services

## provide CINAHL link
* access_CINAHL_database
  - utter_access_CINAHL_database
  - utter_input_in_CINAHL

## guest library comuter access
* can_a_guest_use_library_computers
  - utter_guest_library_computer_access

## thank you path deny
* thanks OR acknowledge
  - utter_handle_affirmation
* deny
  - utter_have_a_great_day
  
## thank you path affirm
* thanks OR acknowledge
  - utter_handle_affirmation
* affirm
  - utter_what_can_i_help_you_with  

## check out books
* check_out_book
  - utter_check_out_books
  
## printing documents
* library_printing
  - utter_library_printing
  
## get to databases
* get_to_databases
  - utter_get_to_databases
  
## printing personal machine
* printing_personal_machine
  - utter_printing_personal_machine 
  
## netid username
* netid_username
  - utter_netid_username
  
## netid plus
* netid_plus
  - utter_netid_plus
  
## vpn
* vpn
  - utter_vpn
  
## alma
* alma
  - utter_alma
  
## search cinahl
* search_cinahl
  - utter_search_cinahl  

## course reserves
* course_reserves
  - utter_course_reserves
  
## etd
* etd
  - utter_etd
  
## ezproxy url
* ezproxy_url
  - utter_ezproxy_url

## inter library loan
* inter_library_loan
  - utter_inter_library_loan
  
## interview room
* interview_room
  - utter_interview_room
  
## journal search
* journal_search
  - utter_journal_search
  
## mymav
* mymav
  - utter_mymav
  
## offcampus
* off_campus_access
  - utter_off_campus_access
  
## oit chat
* oit_chat
  - utter_oit_chat
  
## oit help desk
* oit_help_desk
  - utter_oit_help_desk
  
## silent sign in
* silent_sign_in
  - utter_silent_sign_in
  
## writing help
* writing_help
  - utter_writing_help
  
## find quantitative research article
* quantitative_research_article
    - utter_quantitative_research_article
    
## plagiarism
* plagiarism
    - utter_plagiarism
    
## book_location
* book_location
    - utter_book_location
        
## location_directions
* location_directions
    - action_google_map_api
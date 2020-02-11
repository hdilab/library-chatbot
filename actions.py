# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, ActionReverted


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_database_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        area_of_study_student = tracker.get_slot('area_of_study')

        if area_of_study_student == "nursing":
            utter_database_link = "In that case, I recommend searching CINAHL database at https://libguides.uta.edu/cinahl. \
                                    Off-campus? Log in using your NetID username\
                                    and password."
        elif area_of_study_student == "social_work":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/SocialWork. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "business":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/Business. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "history":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/History. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "english":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/English. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        elif area_of_study_student == "chemistry":
            utter_database_link = "In that case, I recommend opening this link: https://libguides.uta.edu/chemistry. Once you open the link, \
            click on the Databases tab, and you may select one of the database  with the Best Bets. Additional database \
            are also listed here."
        else:
            utter_database_link = "In that case, I recommend opening the link: https://libguides.uta.edu/sb.php. \
            Please select a subject from the dropdown, and you will be guided to the homepage of the subject. Click on the database tab, and \
            you may select one of the database  with the Best Bets. Additional database are also listed here."
        dispatcher.utter_message(utter_database_link)

        return []


class ActionIsBot(Action):
    """Revertible mapped action for utter_is_bot"""

    def name(self):
        return "action_insult"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_respond_insult", tracker)
        return [UserUtteranceReverted()]


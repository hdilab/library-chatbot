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
import urllib.parse
import psycopg2
from rasa_sdk.events import SlotSet

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


class ActionGoogleMap(Action):

    def name(self) -> Text:
        return "action_google_map_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            if len(tracker.latest_message['entities']) > 1:
                from_place = tracker.latest_message['entities'][0]['value']
                to_place = tracker.latest_message['entities'][1]['value']
                from_place = "UTA " + from_place
                to_place = "UTA " + to_place
                dispatcher.utter_message(attachment={"type": "video", "payload": {
                    "src": "https://www.google.com/maps/embed/v1/directions?key=AIzaSyB5boK0YWtedGIQmU4diY3pVBCSW6web9s&origin=" + urllib.parse.quote_plus(
                        from_place) + "&destination=" + urllib.parse.quote_plus(
                        to_place) + "&mode=walking"}})
            else:
                to_place = tracker.latest_message['entities'][0]['value']
                to_place = "UTA " + to_place
                dispatcher.utter_message(attachment={"type": "video", "payload": {
                    "src": "https://www.google.com/maps/embed/v1/place?key=AIzaSyB5boK0YWtedGIQmU4diY3pVBCSW6web9s&q=" + urllib.parse.quote_plus(
                        to_place)}})
        except Exception as ex:
            pass
        return []


class ActionInsult(Action):
    def name(self):
        return "action_insult"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_respond_insult", tracker)
        return [UserUtteranceReverted()]


class ActionFallback(Action):
    """Revertible mapped action for utter_is_bot"""

    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):
        number_failures = tracker.get_slot("number_failures")
        print(number_failures)
        if number_failures is None:
            number_failures = 0.0
        number_failures += 1.0
        if number_failures == 2.0:
            number_failures = 0.0
            dispatcher.utter_message("I'm having difficulty understanding your question. If you would like to speak to person please click on the link https://libraries.uta.edu/live-help")
        else:
            dispatcher.utter_message("Sorry, I did not understand you. Please rephrase your question.")
        return [UserUtteranceReverted(), SlotSet("number_failures", number_failures)]


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_database_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        area_of_study_student = tracker.get_slot('area_of_study')
        var = area_of_study_student + "Hi"
        # print(area_of_study_student)

        if area_of_study_student in ("nursing","kinesiology"):
            utter_database_link = "In that case, I recommend searching CINAHL database at https://libguides.uta.edu/cinahl \
                                    If you are off-campus, you will be prompted to log in using your NetID username\
                                    and password."
        elif area_of_study_student == "data":
            utter_database_link = "In that case, I recommend searching https://libguides.uta.edu/az.php?s=9568 "

        else:
            utter_database_link = "In that case, I recommend searching at https://libguides.uta.edu/az.php using basic keywords."

        dispatcher.utter_message(utter_database_link)

        return []

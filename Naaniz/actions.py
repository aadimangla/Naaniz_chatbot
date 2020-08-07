# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "info_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        print("required_slots(tracker: Tracker)")

        return["name","email","phone"]


    @staticmethod
    def msg() -> List[Text]:
        return ["back","previous"]

    def validate_email(
        self,
        value: Text,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value.lower() not in self.msg():
            return {"email": value}
        else:
            dispatcher.utter_message(text="Enter your name?")
            return {"email": None, "name": None}

    def validate_phone(
        self,
        value: Text,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value.lower() not in self.msg():
            return {"phone": value}
        else:
            dispatcher.utter_message(text="Enter your email?")
            return {"phone": None,"email": None}

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message(template=utter_info)
        return []

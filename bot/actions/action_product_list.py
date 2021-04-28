# Este arquivo contém uma custom action que utiliza código python
# para executar ações no diálogo.
#
# Veja o guia na documentação do RASA em:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import os

class ActionProductList(Action):
    def name(self) -> Text:
        return "action_product_list"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # TODO: query VTEX's product list database to match the products
        # with what the user has ordered

        vtex_store = os.getenv('VTEX_STORE')
        vtex_store_api_key = os.environ.get('VTEX_STORE_API_KEY')
        vtex_store_api_token = os.environ.get('VTEX_STORE_API_TOKEN')

        user_product_list = tracker.get_slot("product_list")
        print(user_product_list)

        # Get product list from VTEX store
        # match against user provided input
        # try best we can to find the most likely candidate
        # We need to give back a list of items that didn't quite match
        # the user intent and ask them to provide more information or just forget about it

        try:
            dispatcher.utter_message("A orderm do seu product é {}?".format(product_list))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet("telefone", telefone)]

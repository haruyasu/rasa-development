# from rasa_sdk import Action


# class ActionCheckPlaceTime(Action):
#     def name(self):
#         return "action_check_PandT"

#     def run(self, dispatcher, tracker, domain):
#         time = tracker.get_slot("play_time")
#         place = tracker.get_slot("play_place")
#         dispatcher.utter_message(text=f"おーけー！じゃぁ、{place}で{time}くらいに待ってるからな！")

#         return []

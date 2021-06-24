# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
import pandas as pd



###############Method Defination

# finds shortest path between 2 nodes of a graph using BFS
def get_bfs_shortest_path(start, goal):
	 
	
	direction = {1: 'Climb UpStairs', 2: 'Climb Downstairs'}
	place={'ECE':1,'IT':2,'CSE':3}
	
	data = [[0,1,0],[2,0,1],[0,2,0]]

	
	graph = {'IT': ['CSE', 'ECE'],
         'CSE': ['IT'],
         'ECE': ['IT']}
	
	explored = []
	queue = [[start]]
	if start == goal:
		return "That was easy! Start = goal"
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				if neighbour == goal:
					length = len(new_path)
					str1 = ""
					for i in range(length-1):
						st=place[new_path[i]]
						de=place[new_path[i+1]]
						print(st)
						print(de)
						print(direction[data[st-1][de-1]])
						str2 = direction[data[st-1][de-1]]
						strs = new_path[i]
						strd = new_path[i+1]
						str1= str1 + "From " + strs + " " + str2 + " to " + strd +"\n"
					return (str1)
					
			explored.append(node)
			
	return "So sorry, but a connecting path doesn't exist :("		
			
    
 
###############Action Area####################



class ActionGivePath(Action):

     def name(self) -> Text:
         return "action_give_path"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
				 
			 

         #dispatcher.utter_message(text="Hello World!")
         splace = tracker.get_slot("splace")
         dplace = tracker.get_slot("dplace")
         mess="I am finding the path from {} to {}".format(splace,dplace)
         route = get_bfs_shortest_path(splace,dplace)
         dispatcher.utter_message(text=mess)
         message="I am finding the path from {} to {} : {}".format(splace,dplace,route)
         print(message)
         dispatcher.utter_message(text=message)

         return []

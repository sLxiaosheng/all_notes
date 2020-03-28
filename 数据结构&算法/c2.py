
from collections import deque


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "Orange"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

#创建一个队列
search_queue = deque()
#将邻居加入队列
search_queue += graph["you"]

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    # deque可以创建一个双端队列
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            if person not in searched:
                print(person + " is a mango seller!")
                return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return False

search("you")
import json

with open("data.json", "r") as file:
    data = json.load(file)

while True:
  command = input("> ")
  
  #track command
  if command.startswith("track "):
    topic = command.replace("track ", "")
  
    if topic in data["topics"]:
          print("You are already tracking this topic.")
  
    else:
      data["topics"].append(topic)
  
      with open("data.json", "w") as file:
          json.dump(data, file, indent=2)
  
      print("Tracking:", topic)
       
    #untrack command
  elif command.startswith("untrack "):
     topic = command.replace("untrack ", "")

     if topic in data["topics"]:
        data["topics"].remove(topic)

        with open("data.json", "w") as file:
           json.dump(data, file, indent=2)

        print("You are no longer tracking", topic)

     else:
        print(f"You are not tracking  {topic}  \nType 'list' to see a list of all the topics you're tracking.")

    #list command
  elif command == "list":
      if not data["topics"]:
        print("You are not tracking any topic")
  
      else:
       for topic in data["topics"]:
        print("-", topic)

  elif command == "help":
     print(f"Available commands:\ntrack <topic> - add a topic to track\nuntrack <topic> - add a topic to untrack\nlist - list all tracked topics\nhelp - show this help menu\nexit - close command")
        
  else:
      print("unknown command")
       
  
  if command == "exit": 
   break



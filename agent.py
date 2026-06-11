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
       
    #list command
  elif command == "list":
      if not data["topics"]:
        print("You are not tracking any topic")
  
      else:
       for topic in data["topics"]:
        print("-", topic)
  
        
  else:
      print("unknown command")
       
  
  if command == "exit":
    break



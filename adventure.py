__author__ = 'lbattaglioli'

prompt = "> "
inventory = []

# For those who are reading this.
# There are multiple easter eggs throughout this game.
# If you enter them, you will encounter bazaar ways to die.
# Look through the code and find all of them!

def enterCabin(inventory):
    print("You are now in the cabin.")
    print("On the other side of the cabin there is a chest. You attempt to open it but it's locked.")
    print("There is a key on the shelf above the chest. 1 Key has been added to inventory.")
    inventory.append("key")
    print("Here is your inventory: " + str(inventory))
    print("You may 'leave' or 'open chest'.")
    action = input(prompt).lower()
    if action == "open chest":
        inventory.remove("key")
        print("You have found a map, it appears as if part of the map has been torn off.")
        inventory.append("map")
        print("You look around the cabin and find a two additional items. You find a bottle of water and "
              "a bit of fire starter. You find nothing else and return outside.")
        inventory += ("fire starter", "water bottle")
        print("You are now back outside of the cabin. Since you gave been in the cabin already, 'follow trail'.")
        action = input(prompt).lower()
        if action == "follow trail":
            followTrail()
        while action != 'follow trail':
            print("Please 'follow trail'")
            action = input(prompt).lower()
            if action == "follow trail":
                followTrail()
    if action == "leave":
        print("You are now back outside of the cabin. If you'd like you can 'enter cabin' or 'follow trail'.")
        action = input(prompt).lower()
        if action == "enter cabin":
            enterCabin()
        if action == "follow trail":
            followTrail()

def followTrail():
    print("You are walking down the path. You are heading south towards Raquette River..")
    print("The path is very thick and overgrown.")
    print("After walking for multiple miles, you encounter two lean-to's.")
    print("At the lean-to, there is a group of religious children camping there. You attempt to speak to them, but "
          "they have taken a vow of silence.")
    print("The sun is beginning to set, would you like to 'sleep at lean-to' or 'keep walking'?")
    action = input(prompt).lower()
    if action == "sleep at lean-to":
        sleepAtLeanto()
    if action == "keep walking":
        keepWalking()
    if action == "talk to jesus kids":
        print("The Jesus kids have taken great offense to you speaking to them. They kill you in your sleep.")
        print("You die.")

def keepWalking():
    print("After walking for another mile, you encounter a tombstone.")
    print("The name engraved on the tombstone was partially eroded. The last name Seger was all that could be made out.")
    print("At the base of the tombstone is a ferrel cat. The cat appears to be playing with a coin. The cat seems to "
          "paw the coin in your direction, signaling you to pick it up.")
    print("1 coin added to your inventory.")
    inventory.append("coin")
    print("The cat begins to rub against your leg. You decide to keep the cat.")
    inventory.append("cat")
    print("You walk a little ways. The path has a slight incline. Your reach the top and see that the path diverges in "
          "two different directions.")
    print("You may go 'left' or 'right'.")
    action == input(prompt).lower()
    if action == "left":
        left()
    if action == "right":
        right()

def sleepAtLeanto():
    print("You set up your sleeping bag in the lean-to.")
    print("You set up your portable stove and begin to cook a bag of freeze dried food.")
    print("You've eaten your dinner and turn in for the night.")
    print("Later...")
    print("It is 1:00 in the morning. You have to get up to pee, you get out of the sleeping bag. The air is freezing")
    print("You grab a flashlight and walk into the woods a bit. You hear a owl and shine the light in the tree. "
          "You noticed what appears to be a red canoe hanging in the trees.")
    print("You can either leave the canoe and 'return to camp' or 'take the canoe' and leave.")
    action = input(prompt).lower()
    if action == "return to camp":
        returnToCamp()
    if action == "take the canoe":
        takeCanoe()

def returnToCamp():
    print("You have done your business and head back to camp.")
    print("You crawl back in your sleeping bag and go back to sleep.")
    print("The next morning...")
    print("You unzip your sleeping bag and feel the cold morning air against you skin. You want to get back in your "
          "sleeping bag but you must make breakfast.")
    print("You setup your portable stove and cook a bag of freeze dried food.")
    print("You eat your breakfast, and wave goodbye to the silent children. You continue on your adventure.")
    keepWalking()

def takeCanoe():
    print("You have taken the canoe.")
    print("You put the canoe in the water, gather your belongings and you head out on the lake.")
    print("You begin paddling up the incoming Raquette River towards Buttermilk Falls.")
    print("After paddling up the river for about two miles, you reach Buttermilk Falls.")
    print("From here, you can 'continue on foot' or stop and 'portage' around the falls.")
    action = input(prompt).lower()
    if action == "continue on foot":
        continueOnFoot()
    if action == "portage":
        portage()

def continueOnFoot():
    print("You have gathered all of your belongings and hide your canoe.")
    print("You use your rope to hang your canoe in the tree so nobody steals is.")
    inventory.remove("rope")
    print("You begin walking out, there are a few tourists there, you say hello to them.")
    print("After talking to the tourist, you walk a little ways and end up on the road.")

def portage():
    print("You have pulled the canoe out of the water and begun pulling it up to the top of the falls to continue "
          "by canoe.")
    print("You've reached the top of the waterfall. You put the canoe in the water and put our belongings back "
          "in the canoe. You set the cat in the front canoe.")
    print("You then enter the canoe and begin paddling up the stream.")

def left():
    # towards long lake
    print("The path continues to head b")

def right():
    # towards forked lake

print("Welcome to Adventure.")
print("To play you must enter commands to the computer. All available commands "
      "will be in 'quotes'. To exit the game, simply enter 'exit'.")
print("Press enter to begin your adventure.")

start = input(prompt)

while start == "help":
    print("To play you must enter commands to the computer, available commands will be in 'quotes'. "
          "To exit the game, simply enter 'exit'.")
    print("Press enter to begin.")
    start = input(prompt)
    if start == "":
        break

if start == "":
    print("You have just gotten off of a sea plane. You are on a lake in the Adirondacks called Long Lake.")
    print("You smell the clean, fresh air, much different than the air of the city.")
    print("You pause for a moment to take in the beautiful scene. You then begin to unload your gear for the adventure "
          "that lies ahead of you.")
    inventory += ("freeze dried food", "medicine kit", "water filter", "rifle", "bullets", "sleeping bag", "tent",
                  "hatchet", "knife", "rope", "camera", "portable stove")
    print("You now have the following items in your inventory: " + str(inventory))
    print("You walk up a short trail to a cabin in the woods.")
    print("You observe that there is a cabin and there is also a trail that continues into the woods.")
    print("You may 'enter cabin' or 'follow trail'.")

    action = input(prompt).lower()

    if action == "enter cabin":
        enterCabin(inventory)
    elif action == "follow trail":
        followTrail()
    elif action == "bear":
        print("A bear has attacked you. You die.")
    elif action == "exit":
        print("Goodbye.")

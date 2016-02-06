def takeCanoe():
    print("hi")

def keepWalking():
    print("After walking for another mile, you encounter a tombstone.")
    print("At the base of the tombstone, there is a ferrel cat playing with a coin.")
    print("The cat paws the coin in your direction, almost telling you to look at the coin.")
    print("You look at the coin and notice it's not a real coin. It appears as if there is a map engraved "
          "on it.")
    print("")

def sleepAtLeanto():
    print("You set up your sleeping bag in the lean-to.")
    print("You set up your portable stove and begin to cook a bag of freeze dried food.")
    print("You've eaten your dinner and turn in for the night.")
    print("Later...")
    print("It is 1:00 in the morning. You have to get up to pee, you get out of the sleeping bag. The air is freezing")
    print("You grab a flashlight and walk into the woods a bit. You hear a owl and shine the light in the tree. "
          "You noticed what appears to be a red canoe hanging in the trees.")
    print("You can either leave the canoe and 'return to camp' or 'take the canoe' and leave.")

def enterCabin():
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
        print("There is nothing more in here, let's return outside.")
        print("You are now back outside of the cabin. To begin you adventure, 'follow trail'.")
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
    print("You are walking down the path. You are heading south towards Forked Lake.")
    print("The path is very thick and overgrown.")
    print("After walking for multiple miles, you encounter two lean-to's.")
    print("At the lean-to, there is a group of religious children camping there. You attempt to speak to them, but"
          "they have taken a vow of silence.")
    print("The sun is beginning to set, would you like to 'sleep at lean-to' or 'keep walking'?")
    action = input(prompt).lower()
    if action == "sleep at lean-to":
        print("You set up your sleeping bag in the lean-to.")
        print("You set up your portable stove and begin to cook a bag of freeze dried food.")
        print("You've eaten your dinner and turn in for the night.")
        print("Later...")
        print("It is 1:00 in the morning. You have to get up to pee, you get out of the sleeping bag. The air is freezing")
        print("You grab a flashlight and walk into the woods a bit. You hear a owl and shine the light in the tree. "
              "You noticed what appears to be a red canoe hanging in the trees.")
        print("You can either leave the canoe and 'return to camp' or 'take the canoe' and leave.")
        if action == "take the canoe":
            takeCanoe()
        if action == "return to camp":
            print("You do your business in the woods and walk back to camp.")
            print("You crawl back in your sleeping bag and go back to bed. ")
    if action == "keep walking":
        keepWalking()

__author__ = 'lbattaglioli'

print("Welcome to Adventure.")
print("To play you must enter commands to the computer. All available commands "
      "will be in 'quotes'. To exit the game, simply enter 'exit'.")
print("Press enter to begin your adventure.")

prompt = "> "
inventory = []

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
    print("You now have the following items in your inventory: ")
    inventory += ("freeze dried food", "medicine kit", "water filter", "rifle", "bullets", "sleeping bag", "tent",
                  "hatchet", "knife", "rope", "camera", "flashlight")
    print(inventory)
    print("Inventory updated.")
    print("You walk up a short trail to a cabin in the woods.")
    print("You observe that the trail breaks off.")
    print("You may 'enter cabin' or 'follow trail'.")

    action = input(prompt).lower()

    if action == "enter cabin":
        enterCabin()
        action = input(prompt).lower()
    elif action == "follow trail":
        followTrail()
        action = input(prompt).lower()
    elif action == "bear":
        print("A bear has attacked you. You die.")
    if action == "exit":
        print("Goodbye.")

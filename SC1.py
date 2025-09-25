#Name:Aaden hampton
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:

#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
Rustcardict={
    "enemy1":{

        "Name": "willjum",
        "height": "6'3",
        "health": "150",
        "damage": 75

    },
    "enemy2": {

        "Name": "Jorque",
        "height": "5'4",
        "health": "300",
        "damage": 67

    },
    "enemy3": {

        "Name": "Aaden",
        "height": "6'6",
        "health": "175",
        "damage": 140

    },
    "enemy4": {

        "Name": "Blooprint",
        "height": "6'8",
        "health": "150",
        "damage": 85


    },
    "enemy5": {

        "Name": "Caleb",
        "height": "5'10",
        "health": "200",
        "damage": 100
    }
}
Rustcardict["enemy1"]["damage"]=int(input())
print(Rustcardict["enemy1"])
Rustcardict["enemy2"]["damage"]=int(input())
print(Rustcardict["enemy2"])
Rustcardict["enemy3"]["damage"]=int(input())
print(Rustcardict["enemy3"])
Rustcardict["enemy4"]["damage"]=int(input())
print(Rustcardict["enemy4"])
Rustcardict["enemy5"]["damage"]=int(input())
print(Rustcardict["enemy5"])
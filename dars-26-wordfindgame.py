#Asilbek Asqarov
#Mohirdev python-darslari
#dars-26
import random 
#word guessing game

words = [
    "apple", "bird", "clock", "desk", "fish", "game", "house", "iron", "jump", "kite",
    "lamp", "moon", "nest", "ocean", "park", "quiz", "rain", "star", "tree", "unit",
    "view", "wolf", "yard", "zeus", "boat", "cold", "door", "east", "fire", "gold",
    "bridge", "camera", "dragon", "energy", "forest", "garden", "helmet", "island",
    "jungle", "knight", "laptop", "magnet", "nature", "orange", "planet", "rocket",
    "silver", "target", "unique", "valley", "window", "yellow", "zenith", "anchor",
    "button", "desert", "fabric", "galaxy", "hammer", "jacket", "adventure", "blizzard",
    "champion", "dinosaur", "elephant", "fountain", "graphite", "horizon", "infinity",
    "keyboard", "labyrinth", "mountain", "notebook", "obstacle", "parallel", "question",
    "resource", "skeleton", "triangle", "umbrella", "vacation", "waterfall", "yesterday",
    "astronaut", "butterfly", "computer", "fireworks", "greenhouse", "moonlight", "nightmare",
    "abyss", "echo", "icy", "jazz", "lynx", "myth", "onyx", "quartz", "rhythm", "sphinx"
]

def guess_word():
    print("Let's play word guess game! ")
    word = random.choice(words)
    guesses = 0
    entered_letters = []
    print("Word Guessed with ",'_'*len(word)  )
    while True:
        guesses+=1
        display = ""
        letter = str(input("Enter letter: ").lower()[:1])
        if letter in word:
            print(f"{letter} is in word")
        else:
            print("No such a letter")
        entered_letters.append(letter)
        for xarf in word:
            if xarf in entered_letters:
                display += xarf
            else:
                display += "_"
        print(display)
        print(entered_letters)
        if '_' not in display:
            print(f"You won with {guesses} guesses! ")
            break

guess_word()        
        
        
        
    
    

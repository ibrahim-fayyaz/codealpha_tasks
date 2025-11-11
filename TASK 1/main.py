import random

categories = {
     "Animals" : [
         'dog', 'cat', 'lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'kangaroo', 'panda', 'leopard',
     'cheetah', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'camel', 'horse', 'rhino', 'hippo'],

    "Fruits":[
        'apple', 'banana', 'grape', 'orange', 'mango', 'kiwi', 'pear', 'peach', 'cherry', 'melon',
     'pineapple', 'plum', 'strawberry', 'blueberry', 'raspberry', 'papaya', 'guava', 'apricot', 'fig', 'pomegranate'],

    "Things": [
        'chair', 'table', 'laptop', 'bottle', 'phone', 'remote', 'lamp', 'pen', 'pencil', 'notebook',
     'clock', 'mirror', 'bag', 'wallet', 'key', 'mug', 'plate', 'cushion', 'scissors', 'brush'],

    "Actors": [
        'bradpitt', 'leonardodicaprio', 'tomhanks', 'johnnydepp', 'robertdowneyjr', 'morganfreeman',
     'chrishemsworth', 'ryanreynolds', 'willsmith', 'keanureeves', 'christianbale', 'hughjackman',
     'jakegyllenhaal', 'benaffleck', 'mattdamon', 'markwahlberg', 'tomhardy', 'dwaynejohnson', 'zendaya', 'emmastone'],

     "Technology": ['internet', 'laptop', 'smartphone', 'bluetooth', 'wifi', 'router', 'server', 'cloud', 'ai',
     'blockchain', 'keyboard', 'monitor', 'usb', 'python', 'java', 'android', 'ios', 'email', 'drone', 'robot'],

    "Car Brands": [
        'toyota', 'honda', 'ford', 'chevrolet', 'bmw', 'mercedes', 'audi', 'tesla', 'nissan', 'hyundai',
     'kia', 'volkswagen', 'mazda', 'jaguar', 'porsche', 'ferrari', 'lamborghini', 'rollsroyce', 'bentley', 'subaru'],

     "Hobbies": [
    'reading', 'writing', 'painting', 'dancing', 'singing', 'cycling', 'hiking', 'swimming', 'gaming',
     'gardening', 'fishing', 'drawing', 'cooking', 'baking', 'skating', 'yoga', 'knitting', 'traveling', 'photography', 'jogging'],

    "Countries": [
     'pakistan', 'india', 'china', 'usa', 'canada', 'germany', 'france', 'italy', 'japan', 'brazil',
     'russia', 'mexico', 'egypt', 'turkey', 'spain', 'australia', 'argentina', 'indonesia', 'sweden', 'norway'],

    "Sports": [
        'football', 'cricket', 'tennis', 'badminton', 'hockey', 'basketball', 'baseball', 'rugby',
     'golf', 'cycling', 'swimming', 'boxing', 'wrestling', 'skating', 'skiing', 'karate', 'judo', 'fencing', 'surfing', 'volleyball'],

    "School Subjects" :[
        'math', 'english', 'physics', 'chemistry', 'biology', 'history', 'geography', 'computer',
     'economics', 'psychology', 'sociology', 'philosophy', 'urdu', 'islamiyat', 'art', 'music', 'pe', 'literature', 'business', 'law']
}


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

negative_responses = ["N" , "NO" , "NOPE" , "NAH"]
attempt = 1
total_score = 0

while True:
    chosen_list = random.choice(list(categories.keys()))
    chosen_word = random.choice(categories[chosen_list])

    print(f"Attempt No. {attempt}")
    print(f"\nThe Word is from Category: {chosen_list.upper()} \n")

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + ' '.join(placeholder))
    game_over = False
    lives = 6

    correct_letters = []
    guessed_words = []

    while not game_over:
        print(f"**************************** {lives}/6 LIVES LEFT ****************************")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_words:
            print(f"You have already guessed '{guess}', Try Again!") 
            print(stages[lives]) 
            continue
        else:
            guessed_words.append(guess)  

        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + ' '.join(display))

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

            if lives == 0:
                game_over = True
                print(f"*********************** IT WAS '{chosen_word.upper()}'❗️ YOU LOSE ☹️ **********************")

        if "_" not in display:
            game_over = True
            print(f"**************************** YOU WIN 🥳 IT WAS '{chosen_word.upper()}' ****************************")
        
        print(stages[lives])
    attempt += 1
    score = lives * 10
    total_score += score
    print(f"Your scored {score} Points | Total Score: {total_score}")
    choice = input(("\nDo you want to continue the game? (Enter NO to quit): ")).upper() 
    if choice in negative_responses:
        print("Thank you for Playing!! ")
        break   

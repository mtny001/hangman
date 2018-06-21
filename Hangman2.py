import random

def hangman():
    word_list = ["Python","Java","computer","painter"]
    number = random.randint(0,3)
    word = word_list[number]
    wrong =0    
    stages=["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    reletters = list(word)
    board =["_"]*len(word)
    win = False
    print("ハングマンにようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        guess = input("言葉を予想してね")
        if guess in reletters:
            cind = reletters.index(guess)
            board[cind] = guess
            reletters[cind]='$'
        else:
            wrong += 1
        print(" ".join(board))
        e= wrong +1
        print("\n".join(stages[0:e]))
        if"_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))                         

hangman()           

        
            
            
        

    

    


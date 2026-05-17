import random
moves = ["rock","paper", "scissor"]
player_moves = []
def ai_move():
    if not player_moves:
        return random.choice(moves)
    most_common = max(set(player_moves), key=player_moves.count)
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"
def winner(player,ai):
    if player==ai:
        return "draw"
    elif (player == "rock" and ai == "scissors") or\
         (player == "paper" and ai == "rock") or\
         (player == "scissors" and ai == "paper"):
        return "player"
    else:
        return "ai"
print("Welcome to Rock, Paper, Scissors!")
print("Enter rock,paper or scissors or enter quit to stop playing!")
player_score = 0
ai_score = 0
while True:
    player = input("Enter your move: ").lower()
    if player == "quit":
        break
    if player not in moves:
        print("Invalid answer, try again")
        continue
    ai = ai_move()
    print(f"AI chose: {ai}")
    result = winner(player,ai)
    if result == "player":
        print("You win!")
        player_score +=1
    elif result == "ai":
        print("AI wins this round!")
        ai_score += 1
    else:
        print("It's a draw!")
    player_moves.append(player)
    print(f"AI score: {ai_score} Your score: {player_score}")
print(f"Final score:\n AI: {ai_score}\n Your score: {player_score}")
print("Thanks for playing!")

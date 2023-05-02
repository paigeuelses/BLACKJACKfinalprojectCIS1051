#BlackJack try 5
import random
import pygame
pygame.init()

#Setup

window_size = (960,540)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Final Project - BlackJack")

black = (0,0,0)
white = (255, 255, 255)
titleFont = pygame.font.Font(None,60)
lostFont = pygame.font.Font(None, 90)
welcomeText = titleFont.render("Welcome to Blackjack!", True, white)
otherFont = pygame.font.Font(None,30)

#For other texts: otherFont.render("...", True, white)

screen.fill("dark green")
screen.blit(welcomeText, (250,50))


#Buttons

buttonFont = pygame.font.Font(None,40)

hitButton = buttonFont.render("Hit", True, white)
hitRect = pygame.Rect(300, 450, 100, 50)

standButton = buttonFont.render("Stand", True, white)
standRect = pygame.Rect(500, 450, 100, 50)

startButton = buttonFont.render("Click to Start", True, white)
startRect = pygame.Rect(350,200,150,75)
screen.blit(startButton,startRect)
pygame.display.update()

def showButtons():
    screen.blit(hitButton, hitRect)
    screen.blit(standButton, standRect)
    pygame.display.update()
    

#Functions

deck = []
suits = ["hearts", "spades", "diamonds", "clubs"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
for suit in suits:
    for rank in ranks:
        deck += [f"{rank} of {suit}"]

playerHand = []
dealerHand = []


def deal(turn):
    random.shuffle(deck)
    card = deck.pop()
    turn.append(card)

for _ in range(2):
    deal(playerHand)
    deal(dealerHand)


def calculateTotal(turn):
    
    newHand = []
    for item in turn:
        newHand.append(item.split(" "))
        
    turnTotal = 0
    for i in newHand:
        if i[0] == "2":
            turnTotal += 2
        if i[0] == "3":
            turnTotal += 3
        if i[0] == "4":
            turnTotal += 4
        if i[0] == "5":
            turnTotal += 5
        if i[0] == "6":
            turnTotal += 6
        if i[0] == "7":
            turnTotal += 7
        if i[0] == "8":
            turnTotal += 8
        if i[0] == "9":
            turnTotal += 9
        if i[0] == "10":
            turnTotal += 10
        elif i[0] == "jack" or i[0] == "queen" or i[0] == "king":
            turnTotal += 10
        elif i[0] == "ace":
            if turnTotal <= 10:
                turnTotal += 11
            else:
                turnTotal += 1        
    return turnTotal
        
def showCards(turn, position):
        turnTotal = calculateTotal(turn)
        displayTotalText = otherFont.render(f"Total: {turnTotal}", True, white)
        bustText = lostFont.render("Bust! Dealer wins", True, white)

        if turnTotal > 21:
            screen.fill("dark green")
            pygame.display.update()
            screen.blit(bustText, (250, 50))
            screen.blit(displayTotalText,(position[0], position[1]+150))
        else:
            screen.blit(displayTotalText,(position[0], position[1]+150)) 
        
        newHand = []
        for item in turn:
            newHand.append(item.split(" "))


        for i in newHand:
            rank = i[0]
            suit = i[2]

            filename = f"{rank}_of_{suit}.png"
            card_image = pygame.image.load(filename)
            scaled_image = pygame.transform.scale(card_image, (100,144))
            screen.blit(scaled_image, position)
            position[0] += 115


def showDealerCard(turn, position):
    
    turnTotal = calculateTotal(turn)
    card1 = turn[0]
    displayTotalText =  otherFont.render(f"Dealer's Total:{card1} and ??", True, white)
    screen.blit(displayTotalText, (position[0], position[1]+150)) 
    
    newHand = []
    for item in turn:
        newHand.append(item.split(" "))

    for i, card in enumerate(newHand):
        rank = card[0]
        suit = card[2]

        if i == 0:
            filename = f"{rank}_of_{suit}.png"
        else:
            filename = "back.png" 
            
        card_image = pygame.image.load(filename)
        scaled_image = pygame.transform.scale(card_image, (100,144))
        screen.blit(scaled_image, position)
        position[0] += 115

def playerWinsbyHighNum(turn, dealer):
    playerTotal = calculateTotal(turn)
    dealerTotal = calculateTotal(dealer)
    if playerTotal > dealerTotal:
        return True
    else:
        return False

def resultPush(turn, dealer):
    playerTotal = calculateTotal(turn)
    dealerTotal = calculateTotal(dealer)
    if playerTotal == dealerTotal:
        return True
    else:
        return False
    

def showAllDealerCards(turn, position):
        screen.fill("dark green")
        winText = lostFont.render("You win!", True, white)
        screen.blit(winText, (250, 50))
        
        newHand = []
        for item in turn:
            newHand.append(item.split(" "))


        for i in newHand:
            rank = i[0]
            suit = i[2]

            filename = f"{rank}_of_{suit}.png"
            card_image = pygame.image.load(filename)
            scaled_image = pygame.transform.scale(card_image, (100,144))
            screen.blit(scaled_image, position)
            position[0] += 115


def revealDealerCard(player, turn, position):
    turnTotal = calculateTotal(turn)
    displayTotalText = otherFont.render(f"Total: {turnTotal}", True, white)
    screen.blit(displayTotalText,(position[0], position[1]+150))
    winText = lostFont.render("You win!", True, white)
    pushText = lostFont.render("Push", True, white)

    playerTotal = calculateTotal(player)
    
    if turnTotal > playerTotal or playerWinsbyHighNum(playerHand, dealerHand) == True:
        screen.fill("dark green")
        pygame.display.update()
        showAllDealerCards(dealerHand,[500, 200]) 
        screen.blit(winText, (250, 50))
    elif resultPush(playerHand, dealerHand) == True:
        screen.fill("dark green")
        pygame.display.update()
        showAllDealerCards(dealerHand,[500, 200])
        screen.blit(pushText, (250, 50))       
    else:
        screen.blit(displayTotalText,(position[0], position[1]+150)) 
        
    
    newHand = []
    for item in turn:
        newHand.append(item.split(" "))


    for i in newHand:
        rank = i[0]
        suit = i[2]

        if i == len(newHand) - 1:
            filename = "back_of_card.png"
        else:
            filename = f"{rank}_of_{suit}.png"

        filename = f"{rank}_of_{suit}.png"
        card_image = pygame.image.load(filename)
        scaled_image = pygame.transform.scale(card_image, (100,144))
        screen.blit(scaled_image, position)
        position[0] += 115

    
    
     

#Game

def play():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startRect.collidepoint(event.pos):
                    screen.fill("dark green")
                    screen.blit(welcomeText, (250,50))
                    showCards(playerHand, [100, 200])
                    showDealerCard(dealerHand, [500, 200])
                    showButtons()
                    pygame.display.update()
                if hitRect.collidepoint(event.pos):
                        screen.fill("dark green")
                        screen.blit(welcomeText, (250,50))
                        deal(playerHand)
                        showCards(playerHand, [100, 200])
                        deal(dealerHand)
                        showDealerCard(dealerHand, [500, 200])
                        showButtons()
                        pygame.display.update()
                elif standRect.collidepoint(event.pos):
                    screen.fill("dark green")
                    screen.blit(welcomeText, (250,50))
                    showCards(playerHand, [100, 200])
                    revealDealerCard(playerHand, dealerHand, [500, 200])
                    pygame.display.update()



        

play()

import cards
import random

allCards = []
allCards.extend(cards.townCards)
allCards.extend(cards.mafiaCards)
allCards.extend(cards.werewolfCards)
allCards.extend(cards.alienCards)
random.shuffle(allCards)

discardedCards = []

#numPlayers = input("How many players? ")
numPlayers = 1

initialDeals = {}
tempHand = []
count = 0
for x in range(1, int(numPlayers) + 1):
   for y in range(3):
      tempHand.append(allCards[count]) # if I want to put the entire card object in each list, remove the .name here
      count += 1
   initialDeals["player{0}".format(x)] = []
   for y in range(3):
      initialDeals["player{0}".format(x)].append(tempHand.pop(0))

print(initialDeals["player1"][0].name)
print(initialDeals["player1"][1].name)
print(initialDeals["player1"][2].name)
alignment = int(input("Which card do you want to take the alignment from? "))
alignmentCard = initialDeals["player1"].pop(alignment - 1)
print(initialDeals["player1"][0].name)
print(initialDeals["player1"][1].name)
ability = int(input("Which card do you want to take the ability from? "))
abilityCard = initialDeals["player1"].pop(ability - 1)
discardCard = initialDeals["player1"][0]

print("Chosen alignment is from: " + alignmentCard.name)
print("Chosen ability is from: " + abilityCard.name)
print("Discarded card is: " + discardCard.name)
discardedCards.extend(discardCard.name)
name = alignmentCard.alignment + " " + abilityCard.ability


print("\nYou are a " + name + ".\n\n" + alignmentCard.factional + "\n" + abilityCard.abilityDesc + abilityCard.modifierDesc + "\n" + alignmentCard.wincon)

# Next up is figuring out how to incorporate this into a GUI with options for num players
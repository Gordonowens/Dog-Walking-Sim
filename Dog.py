from Animal import *
from config import *

class Dog(Animal):

    def __init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters):

        Animal.__init__(self, row, col, width, total_rows, grid, spriteSheet, spriteGroup, characters)

        self.recordTime = 0
        self.coolDown = 5
        self.coolDownTimer = 5
        self.goal = None
        self.items = []
        self.characters = characters

    def stateReset(self):
        '''resets path and player command when transfering between states'''

        self.path = []
        self.playerCommand = ''


    def stayState(self):
        if self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()


        elif self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

    def fleeState(self):
        # change state if appropriote
        if self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        # else if animal is far enough from player change state to flee sniff
        elif (h(self.get_pos(), self.characters.get('Player').get_pos()) > 5):
            self.animalState = 'flee sniff'
            self.stateReset()

        # else if animal still has places to move move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:

            self.movement()
            self.coolDownTimer = self.coolDown

        # else if player is too close find a place to move to
        elif (h(self.get_pos(), self.characters.get('Player').get_pos()) < 5) and len(self.path) <= 0:
            self.runAway()

    def fleeSniffState(self):
        # if player is less than 5 blocks away change state to flee
        if (h(self.get_pos(), self.characters.get('Player').get_pos()) < 5):
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'follow':

            self.animalState = 'follow'

            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        elif self.coolDownTimer <= 0:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def followState(self):
        # change state if appropriote
        if self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        # change state if appropriote
        elif self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        # if player is within 4 spaces of animal change state to follow sniff
        elif h(self.get_pos(), self.characters.get('Player').get_pos()) < 4:
            self.animalState = 'follow sniff'
            self.stateReset()

        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        elif len(self.path) <= 0:
            self.come(self.characters.get('Player'))

    def followSniffState(self):
        # if player is over 4 spaces away from animal then create a path to player
        if self.playerCommand == 'follow':
            self.animalState = 'follow'
            self.stateReset()

        elif self.playerCommand == 'stay':
            self.animalState = 'stay'
            self.stateReset()

        elif self.playerCommand == 'flee':
            self.animalState = 'flee'
            self.stateReset()

        elif self.playerCommand == 'fetch':
            self.animalState = 'fetch'
            self.stateReset()

        # if player is more than 4 spaces from dog change state to follow
        elif h(self.get_pos(), self.characters.get('Player').get_pos()) > 4:
            self.animalState = 'follow'
            self.stateReset()

        elif self.coolDownTimer <= 0:
            self.randomMove()
            self.movement()
            self.coolDownTimer = self.coolDown

    def fetchState(self):
        #get location of ball

        if self.goal not in self.characters.get('Items'):
            self.animalState = 'follow'
            self.stateReset()
            self.goal = None

        elif len(self.path) <= 0:
            self.come(self.goal)
            pass

        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        elif self.get_pos() == self.goal.get_pos():
            self.pickUp()
            self.animalState = 'return ball'
            self.stateReset()

    def returnBallState(self):

        #if dog is near player drop ball and change state to follow
        if h(self.get_pos(), self.characters.get('Player').get_pos()) <=1:
            self.dropItem(self, self.items[0])
            self.animalState = 'follow'
            self.stateReset()
            self.items = []


        # if there are still spaces to move in the path - then move
        elif len(self.path) > 0 and self.coolDownTimer <= 0:
            self.coolDownTimer = self.coolDown
            self.movement()

        #create path
        elif len(self.path) <= 0:
            self.come(self.characters.get('Player'))

    def update(self):
        '''
        this function handles moving the dog between states
        no other function can change the dog's state
        '''

        self.coolDownTimer = self.coolDownTimer - 1

        #do nothing if in stay state
        if self.animalState == 'stay':
            self.stayState()

        elif self.animalState == 'flee':
            self.fleeState()

        elif self.animalState =='flee sniff':
            self.fleeSniffState()

        elif self.animalState == 'follow':
            self.followState()

        elif self.animalState == 'follow sniff':
            self.followSniffState()

        elif self.animalState == 'fetch':
            self.fetchState()

        elif self.animalState == 'return ball':
            self.returnBallState()

        #update rectangle of sprite, x,y refers to upper left corner of sprite box
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def randomMove(self):


        self.direction = randrange(4)

        if self.direction == 0:
            nextNode = self.grid.getGrid()[self.get_pos()[0]][self.get_pos()[1] - 1]
            if nextNode not in self.characters.get('Barriers'):
                self.path.append(nextNode)

        elif self.direction == 1:
            nextNode = self.grid.getGrid()[self.get_pos()[0]][self.get_pos()[1] + 1]

            if nextNode not in self.characters.get('Barriers'):
                self.path.append(nextNode)

        elif self.direction == 2:

            nextNode = self.grid.getGrid()[self.get_pos()[0] - 1][self.get_pos()[1]]

            if nextNode not in self.characters.get('Barriers'):
                self.path.append(nextNode)

        elif self.direction == 3:
            nextNode = self.grid.getGrid()[self.get_pos()[0] + 1][self.get_pos()[1]]

            if nextNode not in self.characters.get('Barriers'):
                self.path.append(nextNode)

    def pickUp(self):
        for i, item in enumerate(self.characters.get('Items')):
            if item.get_pos() == self.get_pos():
                #add item to dictionary
                self.items.append(item)

                # remove from interactive characters item list
                self.removeCharacter('Items', i)
                # remove item sprite from sprite group
                item.kill()

    def dropItem(self, node, item):
        #update items position
        item.updatePosition(node.get_pos())
        self.spriteGroup.add(item)

        # add item sprite back into the game
        self.spriteGroup.add(item)

        # add the character back into the game
        self.addCharcter('Items', item)

    def removeCharacter(self, characterType, position):
        tempArray = self.characters.get(characterType)
        tempArray.pop(position)
        self.characters.update({characterType: tempArray})



    def addCharcter(self, characterType, character):
        #get the specific array from the interactive characters dictionary
        tempArray = self.characters.get(characterType)

        #add character to array
        tempArray.append(character)
        #update characters dictionary
        self.characters.update({characterType: tempArray})
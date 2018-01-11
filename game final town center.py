#! python3
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80


R = {
    'Town_Center': {
        DESC: 'The Town_Center is a large open space with a fountain in the center. Streets lead in all directions.',
        NORTH: 'North_Street',
        EAST: 'East_Street',
        SOUTH: 'South_Street',
        WEST: 'West_Street',
        GROUND: ['Welcome Sign', 'Fountain']},
    'North_Street': {
        DESC: 'The northern end of Y Street has really gone down hill. Pot holes are everywhere, as are stray cats, rats, and wombats.',
        WEST: 'Thief Guild',
        EAST: 'Bakery',
        SOUTH: 'Town_Center',
        GROUND: ['Do Not Take Sign Sign']},
    'Thief Guild': {
        DESC: 'The Thief Guild is a dark den of unprincipled types. You clutch your purse (though several other people here would like to clutch your purse as well).',
        SOUTH: 'West_Street',
        EAST: 'North_Street',
        GROUND: ['Lock Picks', 'Silly Glasses']},
    'Bakery': {
        DESC: 'The delightful smell of meat pies fills the air, making you hungry. The baker flashes a grin, as he slides a box marked "Not Human Organs" under a table with his foot.',
        WEST: 'North_Street',
        SOUTH: 'East_Street',
        SHOP: ['Meat Pie', 'Donut', 'Bagel'],
        GROUND: ['Shop Howto']},
    'West_Street': {
        DESC: 'West_Street is the rich section of town. So rich, they paved the streets with gold. This probably was not a good idea. The thief guild opened up the next day.',
        NORTH: 'Thief Guild',
        EAST: 'Town_Center',
        SOUTH: 'Weapon_Master',
        WEST: 'Empty Weapon Store',
        GROUND: []},
    'Empty Weapon Store': {
        DESC: 'The anvil store has anvils of all types and sizes, each previously-owned but still in servicable condition. However, due to a bug in the way this game is designed, you can buy anvils like any other item and walk around, but if you drop them they cannot be picked up since their TAKEABLE value is set to False. The code should be changed so that it\'s not possible for shops to sell items with TAKEABLE set to False.',
        EAST: 'West_Street',
        SHOP: ['Anvil'],
        GROUND: ['Anvil', 'Anvil', 'Anvil', 'Anvil']},
    'East_Street': {
        DESC: 'East_Street. It\'s like X Street, except East.',
        NORTH: 'Bakery',
        WEST: 'Town_Center',
        SOUTH: 'Magic_Tower',
        GROUND: []},
    'Weapon_Master': {
        DESC: 'The Weapon_Master loudly hammers a new sword over her anvil. Swords, axes, butter knives all line the walls of her workshop, available for a price.',
        NORTH: 'West_Street',
        EAST: 'South_Street',
        SHOP: ['Sword', 'War Axe', 'Chainmail T-Shirt'],
        GROUND: ['Anvil', 'Shop Howto']},
    'South_Street': {
        DESC: 'The Christmas Carolers of South_Street are famous for all legally changing their name to Carol. They are also famous for singing year-round, in heavy fur coats and wool mittens, even in the summer. That\'s dedication to their craft!',
        NORTH: 'Town_Center',
        WEST: 'Weapon_Master',
        GROUND: []},
    'Magic_Tower': {
        DESC: 'Zanny magical antics are afoot in the world-famous Magic_Tower. Cauldrons bubble, rats talk, and books float midair in this center of magical discovery.',
        NORTH: 'East_Street',
        UP: 'View_Deck',
        GROUND: ['Crystal Ball', 'Floating Book', 'Floating Book']},
    'View_Deck': {
        DESC: 'You can see the entire town from the top of the Magic_Tower. Everybody looks like ants, especially the people transformed into ants by the wizards of the tower!',
        DOWN: 'Magic_Tower',
        UP: 'Magical Escalator to Nowhere',
        GROUND: ['Telescope']},
    'Magical Escalator to Nowhere': {
        DESC: 'No matter how much you climb the escalator, it doesn\'t seem to be getting you anywhere.',
        UP: 'Magical Escalator to Nowhere',
        DOWN: 'View_Deck',
        GROUND: []},
    }

worldItems = {
    'Welcome Sign': {
        GROUNDDESC: 'A welcome sign stands here.',
        SHORTDESC: 'a welcome sign',
        LONGDESC: 'The welcome sign reads, "Welcome to the land of adventure. If you need any help, type "help" for a list of commands to use.',
        TAKEABLE: False,
        DESCWORDS: ['welcome', 'sign']},
    'Do Not Take Sign Sign': {
        GROUNDDESC: 'A sign stands here, not bolted to the ground.',
        SHORTDESC: 'a sign',
        LONGDESC: 'The sign reads, "Do Not Take This Sign"',
        DESCWORDS: ['sign']},
    'Fountain': {
        GROUNDDESC: 'A bubbling fountain of green water.',
        SHORTDESC: 'a fountain',
        LONGDESC: 'The water in the fountain is a bright green color. Is that... gatorade?',
        TAKEABLE: False,
        DESCWORDS: ['fountain']},
    'Sword': {
        GROUNDDESC: 'A sword lies on the ground.',
        SHORTDESC: 'a sword',
        LONGDESC: 'A longsword, engraved with the word, "Exkaleber"',
        DESCWORDS: ['sword', 'exkaleber', 'longsword']},
    'War Axe': {
        GROUNDDESC: 'A mighty war axe lies on the ground.',
        SHORTDESC: 'a war axe',
        LONGDESC: 'The mighty war axe is made with antimony impurities from a fallen star, rendering it surpassingly brittle.',
        DESCWORDS: ['axe', 'war', 'mighty']},
    'Chainmail T-Shirt': {
        GROUNDDESC: 'A chainmail t-shirt lies wadded up on the ground.',
        SHORTDESC: 'a chainmail t-shirt',
        LONGDESC: 'The chainmail t-shirt has a slogan and arrow engraved on the front: "I\'m with Stupid"',
        DESCWORDS: ['chainmail', 'chain', 'mail', 't-shirt', 'tshirt', 'stupid']},
    'Anvil': {
        GROUNDDESC: 'The Weapon_Master\'s anvil, far too heavy to pick up, rests in the corner.',
        SHORTDESC: 'an anvil',
        LONGDESC: 'The black anvil has the word "ACME" engraved on the side.',
        TAKEABLE: False,
        DESCWORDS: ['anvil']},
    'Lock Picks': {
        GROUNDDESC: 'A set of lock picks lies on the ground.',
        SHORTDESC: 'a set of lock picks',
        LONGDESC: 'A set of fine picks for picking locks.',
        DESCWORDS: ['lockpicks', 'picks', 'set']},
    'Silly Glasses': {
        GROUNDDESC: 'A pair of those silly gag glasses with the nose and fake mustache rest on the ground.',
        SHORTDESC: 'a pair of silly fake mustache glasses',
        LONGDESC: 'These glasses have a fake nose and mustache attached to them. The perfect disguise!',
        DESCWORDS: ['glasses', 'silly', 'fake', 'mustache']},
    'Meat Pie': {
        GROUNDDESC: 'A suspicious meat pie rests on the ground.',
        SHORTDESC: 'a meat pie',
        LONGDESC: 'A meat pie. It tastes like chicken.',
        EDIBLE: True,
        DESCWORDS: ['pie', 'meat']},
    'Bagel': {
        GROUNDDESC: 'A bagel rests on the ground. (Gross.)',
        SHORTDESC: 'a bagel',
        LONGDESC: 'It is a donut-shaped bagel.',
        EDIBLE: True,
        DESCWORDS: ['bagel']},
    'Donut': {
        GROUNDDESC: 'A donut rests on the ground. (Gross.)',
        SHORTDESC: 'a donut',
        LONGDESC: 'It is a bagel-shaped donut.',
        EDIBLE: True,
        DESCWORDS: ['donut']},
    'Crystal Ball': {
        GROUNDDESC: 'A glowing crystal ball rests on a small pillow.',
        SHORTDESC: 'a crystal ball',
        LONGDESC: 'The crystal ball swirls with mystical energy, forming the words "Answer Unclear. Check Again Later."',
        DESCWORDS: ['crystal', 'ball']},
    'Floating Book': {
        GROUNDDESC: 'A magical book floats here.',
        SHORTDESC: 'a floating book',
        LONGDESC: 'This magical tomb doesn\'t have a lot of pictures in it. Boring!',
        DESCWORDS: ['book', 'floating']},
    'Telescope': {
        GROUNDDESC: 'A telescope is bolted to the ground.',
        SHORTDESC: 'a telescope',
        LONGDESC: 'Using the telescope, you can see your house from here!',
        TAKEABLE: False,
        DESCWORDS: ['telescope']},
    'README Note': {
        GROUNDDESC: 'A note titled "README" rests on the ground.',
        SHORTDESC: 'a README note',
        LONGDESC: 'The README note reads, "Welcome to the text adventure demo. Be sure to check out the source code to see how this game is put together."',
        EDIBLE: True,
        DESCWORDS: ['readme', 'note']},
    'Shop Howto': {
        GROUNDDESC: 'A "Shopping HOWTO" note rests on the ground.',
        SHORTDESC: 'a shopping howto',
        LONGDESC: 'The note reads, "When you are at a shop, you can type "list" to show what is for sale. "buy <item>" will add it to your inventory, or you can sell an item in your inventory with "sell <item>". (Currently, money is not implemented in this program.)',
        EDIBLE: True,
        DESCWORDS: ['howto', 'note', 'shop']},
    }

location = 'Town_Center' # start in Town_Center
inventory = ['README Note', 'Sword', 'Donut'] # start with blank inventory
showFullExits = True

import cmd, textwrap

def displayLocation(loc):
    print(loc)
    print('=' * len(loc))

    print('\n'.join(textwrap.wrap(R[loc][DESC], SCREEN_WIDTH)))

    if len(R[loc][GROUND]) > 0:
        print()
        for item in R[loc][GROUND]:
            print(worldItems[item][GROUNDDESC])

    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in R[loc].keys():
            exits.append(direction.title())
    print()
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction in R[location]:
                print('%s: %s' % (direction.title(), R[location][direction]))
    else:
        print('Exits: %s' % ' '.join(exits))


def moveDirection(direction):

    global location

    if direction in R[location]:
        print('You move to the %s.' % direction)
        location = R[location][direction]
        displayLocation(location)
    else:
        print('You cannot move in that direction')


def getAllDescWords(itemList):
    descWords = []
    for item in itemList:
        descWords.extend(worldItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    itemList = list(set(itemList))
    descWords = []
    for item in itemList:
        descWords.append(worldItems[item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList))
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList))
    matchingItems = []
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        return True

    def help_combat(self):
        print('Combat is not implemented in this program.')

    def do_north(self, arg):
        moveDirection('north')

    def do_south(self, arg):
        moveDirection('south')

    def do_east(self, arg):
        moveDirection('east')

    def do_west(self, arg):
        moveDirection('west')

    def do_up(self, arg):
        moveDirection('up')

    def do_down(self, arg):
        moveDirection('down')

    do_n = do_north
    do_s = do_south
    do_e = do_east
    do_w = do_west
    do_u = do_up
    do_d = do_down

    def do_exits(self, arg):
        global showFullExits
        showFullExits = not showFullExits
        if showFullExits:
            print('Showing full exit descriptions.')
        else:
            print('Showing brief exit descriptions.')


    def do_take(self, arg):
        itemToTake = arg.lower()

        if itemToTake == '':
            print('Take what? Type "look" the items on the ground here.')
            return

        cantTake = False

        for item in getAllItemsMatchingDesc(itemToTake, R[location][GROUND]):
            if worldItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue
            print('You take %s.' % (worldItems[item][SHORTDESC]))
            R[location][GROUND].remove(item)
            inventory.append(item)
            return

        if cantTake:
            print('You cannot take "%s".' % (itemToTake))
        else:
            print('That is not on the ground.')


    def do_use(self, arg):
        itemToUse = arg.lower()

        invDesccWords = getAllDescWords(inventory)

        if itemToUse not in invDesccWords:
            print('You do not have "%s" in your inventory.' % (itemToUse))
            return

        item = getFirstItemMatchingDesc(itemToUse, inventory)
        if item != None:
            print('You used %s.' % (worldItems[item][SHORTDESC]))
            #print (worldItems[item][SHORTDESC])
            #R[location][GROUND].append(item)
            return

    def do_drop(self, arg):
        itemToDrop = arg.lower()

        invDescWords = getAllDescWords(inventory)

        if itemToDrop not in invDescWords:
            print('You do not have "%s" in your inventory.' % (itemToDrop))
            return

        item = getFirstItemMatchingDesc(itemToDrop, inventory)
        if item != None:
            print('You drop %s.' % (worldItems[item][SHORTDESC]))
            inventory.remove(item)
            R[location][GROUND].append(item)
            return


    def complete_take(self, text, line, begidx, endidx):
        possibleItems = []
        text = text.lower()

        if not text:
            return getAllFirstDescWords(R[location][GROUND])

        for item in list(set(R[location][GROUND])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(TAKEABLE, True):
                    possibleItems.append(descWord)

        return list(set(possibleItems))


    def complete_drop(self, text, line, begidx, endidx):
        possibleItems = []
        itemToDrop = text.lower()

        invDescWords = getAllDescWords(inventory)

        for descWord in invDescWords:
            if line.startswith('drop %s' % (descWord)):
                return []

        if itemToDrop == '':
            return getAllFirstDescWords(inventory)

        for descWord in invDescWords:
            if descWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems))

    def complete_use(self, text, line, begidx, endidx):
        possibleItems = []
        itemToUse = text.lower()

        invDesccWords = getAllDescWords(inventory)

        for descWord in invDesccWords:
            if line.startswith('use %s' % (descWord)):
                return []

        if itemToUse == '':
            return getAllFirstDescWords(inventory)

        for descWord in invDescWords:
            if desccWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems))

    def do_look(self, arg):

        lookingAt = arg.lower()
        if lookingAt == '':
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in R[location]:
                    print('%s: %s' % (direction.title(), R[location][direction]))
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
            if lookingAt.startswith('n') and NORTH in R[location]:
                print(R[location][NORTH])
            elif lookingAt.startswith('w') and WEST in R[location]:
                print(R[location][WEST])
            elif lookingAt.startswith('e') and EAST in R[location]:
                print(R[location][EAST])
            elif lookingAt.startswith('s') and SOUTH in R[location]:
                print(R[location][SOUTH])
            elif lookingAt.startswith('u') and UP in R[location]:
                print(R[location][UP])
            elif lookingAt.startswith('d') and DOWN in R[location]:
                print(R[location][DOWN])
            else:
                print('There is nothing in that direction.')
            return

        item = getFirstItemMatchingDesc(lookingAt, R[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        item = getFirstItemMatchingDesc(lookingAt, inventory)
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    def complete_look(self, text, line, begidx, endidx):
        possibleItems = []
        lookingAt = text.lower()

        invDescWords = getAllDescWords(inventory)
        groundDescWords = getAllDescWords(R[location][GROUND])
        shopDescWords = getAllDescWords(R[location].get(SHOP, []))

        for descWord in invDescWords + groundDescWords + shopDescWords + [NORTH, SOUTH, EAST, WEST, UP, DOWN]:
            if line.startswith('look %s' % (descWord)):
                return []

        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(R[location][GROUND]))
            possibleItems.extend(getAllFirstDescWords(R[location].get(SHOP, [])))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in R[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems))

        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        for descWord in shopDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)

        for descWord in invDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        return list(set(possibleItems))


if __name__ == '__main__':
    print('Town Center Adventure!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')

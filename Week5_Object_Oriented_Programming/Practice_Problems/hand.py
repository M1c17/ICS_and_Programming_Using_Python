import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        #make a copy of the hand and try updating     
        new_hand = self.hand.copy()
        
        for letter in word:
            if letter not in new_hand:
                return False
            new_hand[letter] -=1
            
        for letter in new_hand.keys():
            if new_hand[letter] < 0:
                return False
        self.hand = new_hand
        return True
  
myHand = Hand(7)
print(myHand)
print(myHand.calculateLen())

myHand.setDummyHand('saabanz')
print(myHand)
print(myHand.calculateLen())

print(myHand.update('bananas'))
print(myHand)

myHand = Hand(11)
myHand.setDummyHand('eecoferdozz')
myHand.update('coffee')
print(myHand)



#        for letter in word:
#            try:
#               new_hand[letter] -= 1
#            except:
#                #if letter isn't in the hand, we cant make the word from this hand
#                return False
#            
#        for letter in new_hand.keys():
#            #if any of the letter counts of the new hand are less than zero
#            #after the update, then we can't make the word from this hand 
#            if new_hand[letter] < 0:
#                return False
#        # If we've gotten to here, we must be able to make the word from this hand.
#        # Set self.hand to the new, updated hand and return True.
#        self.hand = new_hand
#        return True 




## Count each letter in the word and confirm that they are >= the letter count in the hand
## Using hand.get() will return 0 instead of an error if that letter isn't in the hand
## If all of those pass the >= check, continue
#
#if all(self.hand.get(c, 0) >= word.count(c) for c in word):
#
#    # For each key c in hand, subtract from the value the corresponding value in hand
#
#    self.hand = {c: self.hand[c] - word.count(c) for c in self.hand}
#    return True
#
## Return False if the conditional is not met
#
#return False


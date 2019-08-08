import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        ''' 
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)
        upper_values = list(string.ascii_uppercase)
        shift_upper_values = upper_values[shift:] + upper_values[:shift]
        
        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + shift_upper_values
        
        self.dic_shift = dict(zip(full_keys, full_values))
        
        return self.dic_shift 
    
#p1 = Message('banana') 
#print(p1.build_shift_dict(3))

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #call a method from your instance 
        d = self.build_shift_dict(shift)
        new_encrypt = []
        to_encrypt = self.get_message_text()
        for c in to_encrypt:
            if c in d.keys():
                to_encrypt = d[c]
                new_encrypt.append(to_encrypt)
            else:
                new_encrypt.append(c)
        return(''.join(new_encrypt))

#p1 = Message('banana9,/;"')
#p2 = Message('hello there') 
#print(p2.apply_shift(3))
    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.change_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        #update other attributes
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
#        return self.message_text_encrypted #Test
#
#p2 = PlaintextMessage("9,?banana", 2) #Test
#print(p2.change_shift(4))         #Test


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
#       counter to know which is my max num 
        
        max_count_words, best_shift = 0, 0
        valid_words = self.get_valid_words()
        #tries each shift and maximizes the number of English words
        for shift in range(1, 27): 
            words_count = 0
            to_decrypt = self.apply_shift(shift).split(" ")
            for word in to_decrypt:
                if is_word(valid_words, word):
                    words_count += 1

            if words_count > max_count_words:
                max_count_words = words_count
                best_shift = shift
                
        decrypt = ''.join(self.apply_shift(best_shift)).strip(" 1234567890!@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        return (best_shift, decrypt)

#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('jgnnq')
#print('Expected Output:', (19, 'hello'))
#print('Actual Output:', ciphertext.decrypt_message())


plaintext = PlaintextMessage('separate succeed ash above stripe door strengthen royal down dollar \
                            collector extensive operate loss pad good brother ancient product yes \
                            way mouth expense rejoice sharp pain introduction sheet various whip place\
                            educator prefer introduce bush', 2)
print('Expected Output: ugrctcvg uweeggf cuj cdqxg uvtkrg fqqt uvtgpivjgp tqacn fqyp fqnnct \
      eqnngevqt gzvgpukxg qrgtcvg nquu rcf iqqf dtqvjgt cpekgpv rtqfwev agu \
      yca oqwvj gzrgpug tglqkeg ujctr rckp kpvtqfwevkqp ujggv xctkqwu yjkr rnceg \
      gfwecvqt rtghgt kpvtqfweg dwuj')
print()
print('Actual Output:', plaintext.get_message_text_encrypted())
print()
   
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('ugrctcvg uweeggf cuj cdqxg uvtkrg fqqt uvtgpivjgp tqacn fqyp fqnnct \
                               eqnngevqt gzvgpukxg qrgtcvg nquu rcf iqqf dtqvjgt cpekgpv rtqfwev agu \
                               yca oqwvj gzrgpug tglqkeg ujctr rckp kpvtqfwevkqp ujggv xctkqwu yjkr rnceg\
                               gfwecvqt rtghgt kpvtqfweg dwuj')

print('Expected Output:', (24, 'separate succeed ash above stripe door strengthen royal down dollar \
                             collector extensive operate loss pad good brother ancient product yes \
                             way mouth expense rejoice sharp pain introduction sheet various whip place\
                             educator prefer introduce bush'))
print()
print('Actual Output:', ciphertext.decrypt_message())
print()

plaintext = PlaintextMessage('aghdy', 1)
print('Expected Output: bhiez')
print()
print('Actual Output:', plaintext.get_message_text_encrypted())
print()

ciphertext = CiphertextMessage('bhiez')
print('Expected Output:', (25, 'aghdy'))
print()
print('Actual Output:', ciphertext.decrypt_message())
print()


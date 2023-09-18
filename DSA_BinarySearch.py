def locate_cards(cards, query):
    #make position 0
    position = 0

    #while loop used to repeat
    while True:

        #Check if current position is the same as query
        if cards[position] == query:

            return position

        #if current position is not same as query move to the next position
        position += 1

        
        #check if end of the list is reached
        if position == len(cards):

            return -1


#test cases
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

tests = []

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
        },
    'output': 3
    }
locate_cards(test['input']['cards'], test['input']['query']) == test['output']

#query is in middle
tests.append(test)
tests.append({

    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
        },
        'output': 6

    })

#query is the first element in the list
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 13
        },
    'output': 0
    })

#query is last element
tests.append({
    'input': {
        'cards': [3,-1,-9,-127],
        'query': -127
        },
    'output': 3
    })

#the only element in cards is the query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
        },
    'output': 0
    })

#cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
        },
    'output': -1
    })

#list of cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 4
        },
    'output': -1
    })

#there are repeats on numbers in cards list
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
        },
    'output': 2 #if query occurs multiple times then function will return first occurence of query
    
    })

print(tests)

#test function by passing the inputs into function and comparing with expected output

result = locate_cards(cards, query)
print(result)


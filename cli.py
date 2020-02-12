import random
import math


# array with the words
first = 'A '
adj = ['two headed ', 'nuclear ', 'angry ', 'lonely ','crazy ','glowing ','smelly ','slow ','old ' ]
noun = ['jogger ','racoon ','dog ', 'merchant ', 'driver ', 'comedian ', 'pinecone ']
action = ['took my ', 'threw my ', 'yelled at my ' , 'kicked my ', 'stole my ', 'burned my ', 'bit my ', 'hit my ']
possetion = ['toe ', 'car ', 'watch ', 'shoe ', 'wallet ', 'shirt ', 'keys ', 'computer ', 'phone ', 'sandwich ']
where = ['on the street','in my house','in my driveway', 'in front of the office', 'near the mall', 'near the toilet', 'at the bus station']

# declaring random variables
rdm1 = int(math.floor(random.randint(1, len(adj))))
rdm2 = int(math.floor(random.randint(1, len(noun))))
rdm3 = int(math.floor(random.randint(1, len(action))))
rdm4 = int(math.floor(random.randint(1, len(possetion))))
rdm5 = int(math.floor(random.randint(1, len(where))))

# creating a sentence (the excuse)
print(first + adj[rdm1 - 1] + noun[rdm2 - 1] + action[rdm3 - 1] + possetion[rdm4 - 1] + where[rdm5 - 1])

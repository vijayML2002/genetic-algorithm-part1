#importing the lib

import numpy as np
import itertools

possible = []

test_list = ['0','1']
d ={'1':test_list, '2':test_list, '3':test_list, '4':test_list, '5':test_list}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    possible.append(''.join(combo))

#printing all the possible population

for pop in possible:
  print(pop)

#preprocessing the population

population = []

for pop in possible:
  single = []
  for letter in pop:
    single.append(int(letter))
  population.append(single)


#printing out some value

for pop in population:
  print(pop)

#def the fitness function

def check_fitness(person):
  life = 0
  for pop in person:
    life += pop
  return life
  
life = check_fitness(population[len(population)-1]) #checking the function

print('The lifetime of the person -- {}'.format(life))

#intializing random population

random_pop = [] #matting pool

for i in range(700000):
  ind = np.random.randint(0,17)
  random_pop.append(population[ind])

#def the process of selection

def selection(intial):
  fit = []
  for pop in intial:
    fitness = check_fitness(pop)
    if fitness>=3: #here 3 is the low fitness score considered
      fit.append(pop)

  return fit

#for pairing 

def pairing(people):
  pair = []
  for i in range(len(people)-1):
    paired = [people[i],people[i+1]]
    pair.append(paired)

  return pair

#probability of producing offspring
prob_off = 0.8

#def for producing the offspring

def produce_offspring(pairs):
  offspring = []
  
  for parents in pairs:
    for i in range(np.random.randint(0,1000)): #this for loops makes the required next gen population
      if prob_off > 0:
        parent1 = parents[0]
        parent2 = parents[1]

        rand_pos = np.random.randint(0,4)

        gene1 = parent1[rand_pos] #this the process of crossover
        gene2 = parent2[rand_pos]

        parent2[rand_pos] = gene1
        parent1[rand_pos] = gene2

        offspring1 = parent2
        offspring2 = parent1

        offspring.append(offspring1)
        offspring.append(offspring2)
      
      else:
        offspring1 = parents[0]
        offspring2 = parents[1]

        offspring.append(offspring1)
        offspring.append(offspring2)

    return offspring

#def the mutation

def mutate(people):
  if np.random.uniform(0,1)>0.92:
    rand_pop = np.random.randint(0,len(people))
    person = people[rand_pop]
    
    pos_gene1 = np.random.randint(0,len(person))
    pos_gene2 = np.random.randint(0,len(person))

    val_gene1 = person[pos_gene1]
    val_gene2 = person[pos_gene2]

    person[pos_gene1] = val_gene2
    person[pos_gene2] = val_gene1

    people[rand_pop] = person

  return people

#check the perfectness:

def perfect_being(people):
  for pop in people:
    if check_fitness(pop)>=5:
      print('THE BEST HUMAN FOUND IN THIS WORLD - {}'.format(pop))
      return 1
  return 0

#create the evolution function

def evolve():
  fit_people = selection(random_pop)
  evolution = 0
  while True:
    if evolution%1000==0:
      print('EVOLUTION - {}   POPULATION - {}'.format(evolution,len(fit_people)))
    paired = pairing(fit_people)
    offspring = produce_offspring(paired)
    offspring = mutate(offspring)
    if not offspring:
      print('EVOLUTION FAILED AT EVOLUTION - {}   POPULATION - {}'.format(evolution,len(offspring)))
      break
    if perfect_being(offspring):
      print('PERFECT HUMAN FOUND !!! - {}   POPULATION - {}'.format(evolution,len(offspring)))
      break
    fit_people = offspring
    evolution += 1


evolve() #this is the main evolution function




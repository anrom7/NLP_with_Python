#presented by Volkov Mark PRLc 11
# Chapter 10, Ex.3

#Translate the following sentences into quantified formulas of first-order logic.

a.  Angus likes someone and someone likes Julia.

∃ Adam.(person(Adam) & y.(person(y) & Julia.(person(Julia)  => like(Angus,y) & like (y,Julia)))

∃ x.y.z.(person(x,y,z))  => like(x,y) & like (y,z)))

   b. Angus loves a dog who loves him.

∃ Adam.(person(Adam) & y.(dox(y)  => love(Angus,y) & love (y,Angus)))

∃ x.(person(x) & y.(dog(y)  => love(x,y) & love (y,x)))

c. Nobody smiles at Pat.

¬∀x.(person(x) & ∃ Pat.(person(Pat) => smile(x,Pat))))

¬∀x.(person(x) & ∃ y.(person(y) => smile(x,y))))


d. Somebody coughs and sneezes.

∃ x.(person(x) => cough(x) & sneeze (x)))	

e. Nobody coughed or sneezed.

¬∀ x.(person(x) => cough(x) & sneeze (x)))	

f. Bruce loves somebody other than Bruce.

∃ Bruce.(person(Bruce) & y.(person(y)  => love(Bruce,y) &¬ (Bruce, Bruce)))

∃ x.(person(x) & y.(person(y)  => love(x,y) & ¬ love (x, x)))

g. Nobody other than Matthew loves Pat.

¬∀x.(person(x) & ∃ Matthew.(person(Matthew) & ∃ Pat.(person(Pat) => love(Matthew,Pat) & love(x,Pat)))

¬∀x.(person(x) & ∃ y.(person(y) & ∃ z.(person(z) => love(y,z) & love(x,z)))

h. Cyril likes everyone except for Irene.

∃ Cyril.(person(Cyril) & ∀y.(person(y) ∃ Irene.(person(Irene)  => like(Cyril,y) & ¬ like (Cyril, Irene)))

∃ x.(person(x) & ∀y.(person(y) ∃ z.(person(z)  => like(x,y) & ¬ like (x, z)))

i. Exactly one person is asleep.

∃ x.(person(x) => sleep(x))



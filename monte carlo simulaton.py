import random
courses = 13 
reussite = 10
nbr_simulation = 10000

#mon profil comme etudiante 

taux_presence = 0.3
range_concentration_en_classe = (0.2,0.9)
taux_clarte_prof = (0.2,0.6)
range_comprendre_seule_maison = (0.4,1.0)
nbr_reussite = 0


# Uniform(a,b) return a random number between a and b
# the * inside the uniform just unpack the tuple so instad of of range_concentration_en_classe[0] et range_concentration_en_classe[1]
for simulation in (nbr_simulation):
    
    concentration = random.uniform(*range_concentration_en_classe)
    clarte = random.uniform(*taux_clarte_prof)
    comprendre_seule = random.uniform(*range_comprendre_seule_maison)

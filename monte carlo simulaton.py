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
for simulation in range(nbr_simulation):
    moyenne = 0
    
    for cour in range(courses):
        knowledge_gained_course = 0
        
        ma_presence = random.uniform(0, 1)
        concentration = random.uniform(*range_concentration_en_classe)
        clarte = random.uniform(*taux_clarte_prof)
        comprendre_seule = random.uniform(*range_comprendre_seule_maison)
        
        #this logic right here needs to be updated why abir ?
        # well cuz presence and concentration are related and clarte and comprendre_seule are too ; so u need to add like a link or sth
        
        
        if ma_presence <= taux_presence:
            knowledge_gained_course += 3  
            
        if concentration >= 0.5  :
            knowledge_gained_course += 5  
            
        if clarte >= 0.5:
            knowledge_gained_course += 5  
        
        if comprendre_seule >= 0.5:
            knowledge_gained_course += 7 
        
        moyenne += knowledge_gained_course
    
    moyenne = moyenne /courses
          

    if moyenne >= reussite:
        nbr_reussite += 1 

taux_reussite = nbr_reussite / nbr_simulation
print(f"Taux de réussite estimé : {taux_reussite * 100:.2f}%")
        

População_A = 80000
População_B = 200000
Taxa_De_Crescimento_A = 0.03
Taxa_De_Crescimento_B = 0.015

Anos_Necessários = 0

while População_A < População_B:
    População_A += População_A * Taxa_De_Crescimento_A
    População_B += População_B * Taxa_De_Crescimento_B
    Anos_Necessários += 1
print (Anos_Necessários)




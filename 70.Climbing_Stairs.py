#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

#Example 1:

#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:

#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
 

#Constraints:

#1 <= n <= 45
# dostal jsem  že je potřeba vylézt N schodů, třeba 5
# pokaždé když se hýbu tedy call it h, můžu udělat 1, nebo 2 kroky
# kolika způsoby můžu vylézt nahorů
# abych se dostal na 45 schod, co mohli být mé předchozí kroky (mysli na velikosti kroků)
# sudé liché +1, 1 
# mohl jsem to udělat minimalne od 45 // 2 + 1 kroku a maximalne 45 kroku
# kombinatorika
# na prvni misto muzu dat dve veci a to stejne plati az do pateho mista kde jen jednu
# pocet kolikrat cisla pridavam se mi meni podle toho co za cisla vyberu priklad 10 schodu muzu udelat peti az 10 kroky
# oukej toto hodne pomohlo taze 10 schodu muzu vylezt>
# 5k 1m
# 6k 
# 7k 
# 8k 
# 9k 
# 10k 
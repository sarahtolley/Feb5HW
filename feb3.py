#! /usr/bin/python

from __future__ import division

print("Hello world")

def bradysRevenge(bro):
    bigbro = bro.upper()
    print "You mad, " + bigbro + "?"

#add sig_figs to variable list 
def get_at_content(dna, sig_figs):
	#remove any "N"'s from sequence
	dena = dna.replace('N','')
	length = len(dna)
	#fix lower case problem by converting the sequence to upper case
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	#use round() to limit the number of significant figures in the result
	return round(at_content, sig_figs)


my_at_content = get_at_content("ATGCGCGATCGATCGAATCG", 1)
print(str(my_at_content))
print(get_at_content("ATGCGCGATCGATCGAATCG", 2))
print(get_at_content("aactgtagctagctacgagcgta", 3))


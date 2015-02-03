#! /usr/bin/python

from __future__ import division

print("Hello world")

def bradysRevenge(bro):
    bigbro = bro.upper()
    print "You mad, " + bigbro + "?"

def get_at_content(dna):
	length = len(dna)
	#fix lower case problem by converting the sequence to upper case
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count) / length
	#use round() to limit the number of significant figures in the result
	return round(at_content, 2)


my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
print(str(my_at_content))
print(get_at_content("ATGCGCGATCGATCGAATCG"))
print(get_at_content("aactgtagctagctacgagcgta"))


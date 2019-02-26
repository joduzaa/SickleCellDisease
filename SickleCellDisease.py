# =============== Task 25 ===============

# *************** Task 1 ***************
# Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html
# Note the 'SLC' code for each Amino Acid. 
# Create a program called SickleCellDisease.py. You will simulate the effects of the  
# Single Nucleotide Polymorphism that leads to this genetic disease.  
# Write a function called 'translate' that when given a DNA sequence of arbitrary length,  
# the program identifies and returns the amino acid sequence of the DNA using the  
# amino acid SLC code found in that table. 
# E.g  DNA Input: ATTATTATT  
# Output: III 
# There are many different amino acids so this may get a bit repetitive. Just do the first  
# five Amino Acids (i.e I L V F M) and make any other codon be printed as the amino acid 'X'. 
# So basically, you would use an if - elif - elif .... else structure to translate each codon  
# of DNA into the correct Amino Acid. 
# Note that the program must be able to handle DNA sequences that are not of a length  
# divisible by 3.  
# Hint: 
# len(DNA) - (Will return the length of a String) 
# DNA[0:3] - (Will get the first 3 characters of the string stored in DNA num = 3) 
# DNA[0:num] - (This will work too!) 

# Based on the website: http://www.cbs.dtu.dk/courses/27619/codon.html
# Amino Acid - SLC - DNA codons
# Isoleucine - I - ATT, ATC, ATA
# Leucine - L - CTT, CTC, CTA, CTG, TTA, TTG
# Valine - V - GTT, GTC, GTA, GTG
# Phenylalanine - F - TTT, TTC
# Methionine - M - ATG

# The function to translate DNA into Amino acids >>>>>
def translate(DNA):

	lenght_DNA = len(DNA)
	num_codon = lenght_DNA/3
	DNA_codon = DNA[0:num_codon*3]
	Amino = []

	for i in range(0,num_codon):
		a = i*3
		b = i*3+3
		if DNA_codon[a:b] == "ATT":
			Amino.append('I')
		elif DNA_codon[a:b] == "ATC":
			Amino.append('I')
		elif DNA_codon[a:b] == "ATA":
			Amino.append('I')
		elif DNA_codon[a:b] == "CTT":
			Amino.append('L')
		elif DNA_codon[a:b] == "CTC":
			Amino.append('L')
		elif DNA_codon[a:b] == "CTA":
			Amino.append('L')
		elif DNA_codon[a:b] == "CTG":
			Amino.append('L')
		elif DNA_codon[a:b] == "TTA":
			Amino.append('L')
		elif DNA_codon[a:b] == "TTG":
			Amino.append('L')
		elif DNA_codon[a:b] == "GTT":
			Amino.append('V')
		elif DNA_codon[a:b] == "GTC":
			Amino.append('V')
		elif DNA_codon[a:b] == "GTA":
			Amino.append('V')
		elif DNA_codon[a:b] == "GTG":
			Amino.append('V')
		elif DNA_codon[a:b] == "TTT":
			Amino.append('F')
		elif DNA_codon[a:b] == "TTC":
			Amino.append('F')
		elif DNA_codon[a:b] == "ATG":
			Amino.append('M')
		else:
			Amino.append('X')
	
	Amino = ''.join(Amino)

	return Amino

# To test the function; Output should be : IIIXLLLLLLXVVVVXFFXM
# DNA = "ATTATCATAXXXCTTCTCCTACTGTTATTGXXXGTTGTCGTAGTGXXXTTTTTCXXXATGX"
# Amino = translate(DNA)
# print DNA
# print Amino

# *************** Task 2 ***************
# Add another function to the program SickleCellDisease.py called 'mutate'. This function  
# must read in the contents of the text file named 'DNA.txt'. It must then identify the first  
# occurrence of the lowercase letter 'a' in 'DNA.txt'. 
# You must then write two new text files, one named normalDNA.txt and the other  
# named mutatedDNA.txt. 
# The normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a'  
# changed to an 'A'. 
# The mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a'  
# changed to a 'T'. 
# Now create a new function, 'txtTranslate', that calls the translate function that you  
# wrote in Task 1, to take in textfile input. 
# Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid  
# sequences to the user.

# The function to find a letter, change that letter and then save the results >>>>>
def mutate(letter_find,letter_change,file_name):

	f = open('DNA.txt','r')
	contents = []
	for line in f:
		contents.append(line.strip())
	f.close()
	
	DNA = list(''.join(contents))
	First_Inst = DNA.index(letter_find)
	
	DNA[First_Inst] = letter_change
	changed_DNA = ''.join(DNA)
	
	f = file(file_name,'w')
	f.write(changed_DNA)
	f.close()
		
	return ()

# The function to read in a DNA text file and change the DNA sequence to an Amino sequence >>>>
def txtTranslate(txt_file):
	
	f = open(txt_file,'r')
	contents = []
	for line in f:
		contents.append(line.strip())
	f.close()
	
	DNA = ''.join(contents)
	Amino = translate(DNA)
	
	return Amino

# Output to the user using the functions mutate and txtTranslate
print "A programme to simulate the effects of Single Nucleotide Polymorphism >>>>>"
print ""

mutate('a','A','normalDNA.txt')
mutate('a','T','mutatedDNA.txt')
normal_Amino = txtTranslate('normalDNA.txt')
mutated_Amino = txtTranslate('mutatedDNA.txt')

print "The Normal Amino Acid Sequence >>>>>"
print normal_Amino
print ""
print "The Mutated Amino Acid Sequence >>>>>"
print mutated_Amino
print ""
print "The results are saved to file : results.txt"

# Output to file: results.txt
f = file('results.txt','w')
f.write("The Normal Amino Acid Sequence >>>>> \n")
f.write(normal_Amino)
f.write("\n")
f.write("\n")
f.write("The Mutated Amino Acid Sequence >>>>> \n")
f.write(mutated_Amino)
f.close()

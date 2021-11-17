boolean = [True, False]

for A in boolean :
	for B in boolean :
		for C in boolean :
			for D in boolean :
				print(f'A={A}, B={B}, C={C}, D={D}')
				print(f'(A+B)(B+C+D)(A+C)={(A or B) and (B or C or D) and (A or C)}')
				print(f'A(B+C+D)+BC={(A and (B or C or D)) or (B and C)}')
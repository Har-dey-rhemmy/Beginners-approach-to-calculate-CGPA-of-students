runs = 1
while runs <= 3:
	print("Enter Marks Obtained in the Subjects: ")
	English_Language = int(input("English Language: "))
	Mathematics = int(input("Mathematics: "))
	physics = int(input("Physics: ")) 
	chemistry = int(input("Chemistry: ")) 
	biology = int(input("Biology: "))
	total = English_Language + Mathematics + physics + chemistry + biology 
	avg = total/5
	print("Your average is: ", avg)
	if avg>=70 and avg<=100:
		print("Your Grade is A")
	elif avg>=50 and avg<70:
		print("Your Grade is B")
	elif avg>=0 and avg<50:
		print("Your Grade is E ")
	else:
	   print("Invalid Input!")    
	A = 5
	B = 4
	E = 1
	unit_for_mathematics = 3
	unit_for_english_language = 5
	unit_for_physics = 4
	unit_for_biology = 4
	unit_for_chemistry = 4
	#TCP = Total Credit Point
	if English_Language>=70 and English_Language<=100:
		print("Your TCP for English Language is: ", unit_for_english_language*A)
	elif English_Language>=50 and English_Language<70:
		print("Your TCP for English Language is: ", unit_for_english_language*B)
	elif English_Language>=0 and English_Language<50:
		print("Your TCP for English Language is: ", unit_for_english_language*E)
	else:
		print("We are still working on it!")
	if Mathematics>=70 and Mathematics <=100:
		print("Your TCP for mathematics is: ", unit_for_mathematics*A)
	elif Mathematics>=50 and Mathematics<70:
		print("Your TCP for mathematics is: ", unit_for_mathematics*B)
	elif Mathematics>=0 and Mathematics<50:
		print("Your TCP for mathematics is: ",  unit_for_mathematics*E)
	else:
		print("we are still working on it!")		
	if physics>=70 and physics<=100:
	   print("Your TCP for physics is: ", unit_for_physics *A)
	elif physics>=50 and physics<70:
	   	print("Your TCP for physics is: ", unit_for_physics*B)
	elif physics>=0 and physics<50:
	 print("Your TCP for physics is: ", unit_for_physics*E)
	else:
	 print("we are still working on it!")
	if biology>=70 and biology<=100:
	  print("Your TCP for biology is: ", unit_for_biology *A)
	elif biology>=50 and biology<70:
	 	print("Your TCP for biology is: ", unit_for_biology*B)
	elif biology>=0 and biology<50:
	 	print("Your TCP for biology is: ", unit_for_biology*E)
	else:
	    print("we are still working on it!")
	if chemistry>=70 and physics<=100:
	    	print("Your TCP for chemistry is: ", unit_for_chemistry *A)
	elif chemistry>=60 and chemistry<70:
	    	print("Your TCP for chemistry is: ", unit_for_chemistry*B)
	elif chemistry>=0 and chemistry<50:
	    	print("Your TCP for chemistry is: ", unit_for_chemistry*E)
	else:
	    	print("we are still working on it!")
	  
	TCP_for_English_Language = int(input("Your TCP for English Language above: "))
	TCP_for_Mathematics = int(input("Your TCP for Mathematics above: ")) 	
	TCP_for_physics = int(input("your TCP for physics above: "))
	TCP_for_biology = int(input("your TCP for chemistry above: "))
	TCP_for_chemistry = int(input("your TCP for biology above: "))
	CTCP = TCP_for_chemistry + TCP_for_physics + TCP_for_biology
	    	
	    	#TNU = Total Number of Units
	TNU = unit_for_chemistry + unit_for_physics + unit_for_biology + unit_for_mathematics + unit_for_english_language
	    #GPA = Grade Point Average
	GPA = CTCP/TNU
	print("Your CGPA is: ", GPA)
	runs += 1
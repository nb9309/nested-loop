# nested-loop

						Inner OR Nested Loops
				====================================================
>The Process of Defining One Loop inside of another Loop is called Inner OR Nested Loop.
=>The Execution Process of Outer and Inner Loops is that "For Every Value of Outer Loop, inner loop repeated for Finite 
     Number of Times until Inner Loop Test Condition becomes False".
=>In Python Programming we can Inner Loops Concept in 4 Possible Ways. They are
------------------------------------------------------------------------------------------------------------------------------------------------------------		
possibility-1:    for loop in for loop
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:     for varname1 in Iterable-object1:
			------------------------------------
			------------------------------------
			for varname2 in Iterable-object2:
				--------------------------------------
				--------------------------------------
			else:
				---------------------------------------
		  else:
			-------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------
Possibility-2:    while loop in while loop
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:		while(Test Cond1):
				-------------------------------
				-------------------------------
				while(Test Cond2):
					-----------------------------
					-----------------------------
				else:
					-----------------------------
			else:
				----------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------
Possibility-3:    for loop in while loop
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:		while(Test Cond1):
				-------------------------------
				-------------------------------
				for varname2 in Iterable-object2:
					--------------------------------------
					--------------------------------------
				else:
					---------------------------------------
			else:
				----------------------------------------


------------------------------------------------------------------------------------------------------------------------------------------------------------
Possibility-4:    while loop in for loop
------------------------------------------------------------------------------------------------------------------------------------------------------------
Syntax:     for varname1 in Iterable-object1:
			------------------------------------
			------------------------------------
			while(Test Cond2):
					-----------------------------
					-----------------------------
				else:
					-----------------------------
		  else:
			-------------------------------------------------

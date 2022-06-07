.data 
	multiplicand: .asciiz "\nEnter the multiplicand: "
	multiplier: .asciiz "\nEnter the multiplier: "
	result: .asciiz "\nResult of Multiplication: "
	overflow: .asciiz "\nMultiplication Overflowed!!"
	newline: .asciiz "\n"

.text

		### ..................PART - 1: TAKING USER INPUT....................... ###

	# show prompt 1 (Enter the multiplicand: )
	li $v0, 4
	la $a0, multiplicand
	syscall
	
	# take user input of multiplicand
	li $v0, 5
	syscall
	
	# save the entered multiplicand
 	# move $t0, $v0 (storing a value method 1)
	add $t0, $zero, $v0 # (storing a value method 2)
	
	
	
	# show prompt 2 (Enter the multiplier: )
	li $v0, 4
	la $a0, multiplier
	syscall
		
	# take user input of multiplier
	li $v0, 5
	syscall
	
	# save the entered multiplier
	move $t1, $v0
	
	
		### ..................PART - 2: CALCULATION AND OVERFLOW HANDLING....................... ###
	
	
	# calculation
	mul $t3, $t0, $t1
	mfhi $s1
	mflo $s2
	

	# NO OVERFLOW - 
	# if the result fits into 32 bit then (hi, lo) = (-1,-1) or (hi, lo) = (0, 0) 
	# that means we have to compare if  both of the hi and lo are EQUAL in terms of BOTH SIGN and VALUE
	# ELSE - The result will be OVERFLOWED


	# make the lo = -1 (if number is negative) else lo = 0 using shift right arithmatic 
	sra $s2, $s2, 31
	
	# check if hi, lo are both equal or not. If equal then goto NO_OVERFLOW_DETECTED label		
	beq $s1, $s2, NO_OVERFLOW_DETECTED
	
	
		### ..................PART - 3: DISPLAY THE OUTPUT...................... ###
	
	
	# if result overflows then execute these 4 lines and exit
	li $v0, 4
	la $a0, overflow
	syscall
	j EXIT
	
	
	NO_OVERFLOW_DETECTED:
	
		# show prompt 3
		li $v0, 4
		la $a0, result
		syscall
		
		
		# multiplication value
		li $v0, 1
		move $a0, $t3
		syscall
		j EXIT
	
	EXIT:
	
		# print a newline
		li $v0, 4
		la $a0, newline
		syscall
		
		# exit
		li $v0, 10
		syscall
	
	

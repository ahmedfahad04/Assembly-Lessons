.data
	dividend: .asciiz "\nEnter the dividend: "
	divisor: .asciiz "\nEnter the divisor: "
	msg1: .asciiz "\nResult of division: Quotient = "
	msg2: .asciiz " Reminder = "	
	warning: .asciiz "\nDivisor Can't be 0. Enter a non zero value\n"
	newline: .asciiz "\n"
	
.text	
		### ..................PART - 1: TAKING USER INPUT....................... ###
	
	
	# show prompt 1 (Enter the dividend: )
	li $v0, 4
	la $a0, dividend
	syscall
	
	# take user input of dividend
	li $v0, 5
	syscall
	
	# save the entered dividend
	move $s0, $v0
	
	
	TRY_AGAIN:
	# show prompt 2 (Enter the divisor: )
	li $v0, 4
	la $a0, divisor
	syscall
		
	# take user input of divisor
	li $v0, 5
	syscall
	
	# save the entered dividend
	move $s1, $v0
	
	
		### ..................PART - 2: CALCULATION....................... ###
	
	
	# check if the divisor is zero or not
	bnez $s1, CALCULATION
	
	# show warning message if divisor = 0
	li $v0, 4
	la $a0, warning
	syscall	
	j TRY_AGAIN	
		
	
	CALCULATION:
	# division
	div $s0, $s1
	
	# move from low (Quotient)
	mflo $t1
	
	# move from high (Reminder)
	mfhi $t2
	

	
		### ..................PART - 3: DISPLAY THE OUTPUT...................... ###
		
		
	# print the message 1
	li $v0, 4
	la $a0, msg1
	syscall
	
	# print the quotiant
	li $v0, 1
	move $a0, $t1
	syscall
	
	# print the message 2
	li $v0, 4
	la $a0, msg2
	syscall
	
	# print the reminder
	li $v0, 1
	move $a0, $t2
	syscall
	
	# print newline
	li $v0, 4
	la $a0, newline
	syscall
	
	
	# exit
	li $v0, 10
	syscall
	

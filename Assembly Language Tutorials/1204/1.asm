.data
	rows: .asciiz "Enter number of rows in the array: "
	cols: .asciiz "\nEnter number of columns in the array: "
	
	exchangeRow1: .asciiz "Enter a row number: "
	exchangeRow2: .asciiz "\nEnter another row number: "
	
	msgP1: .asciiz "\nEnter an array of "
	msgP2: .asciiz " characters:\n"
	msgP3: .asciiz "\n\nThe entered "
	msgP4: .asciiz " array is:\n"
	msgP5: .asciiz "\nThe array after exchanging Row "
	msgP6: .asciiz " and Row "
	msgP7: .asciiz " is:\n"
	
	array: .space 1200
	newline: .asciiz "\n"
	space: .ascii " "
	
	# register listing
	#
	# $t0 = row number
	# $t1 = col number
	# $t2 = array index
	# $t3 = exchange row number 1
	# $t4 = exchange row number 2
	# $s1 = array size (based on row * col)
	
.text
	
		### ..................PART - 1: ENTER ELEMENTS IN THE CHARACTER ARRAY....................... ###
	
	# input 1 (row) - $t0
	
	# show prompt 1
	li $v0, 4
	la $a0, rows
	syscall
	
	# ask user input
	li $v0, 5
	syscall
	
	# save the entered data 
	move $t0, $v0
	
	
	
	# input 2 (col) - $t1
	
	# show prompt 1
	li $v0, 4
	la $a0, cols
	syscall
	
	# ask the user input
	li $v0, 5
	syscall
	
	# save the entered data
	move $t1, $v0
	
	
	
	# display headline 1
	li $v0, 4
	la $a0, msgP1
	syscall
	
	li $v0, 1
	move $a0, $t0 	# row value
	syscall
	
	
	li $t2, 'x'
	li $v0, 11
	move $a0, $t2	# print a character 'x'
	syscall
	
	
	li $v0, 1
	move $a0, $t1 	# col value
	syscall
	
	li $v0, 4
	la $a0, msgP2
	syscall 
	
	
	# calculate array size (n)
	mulu $s1, $t0, $t1
	addi $s1, $s1, -1	# As indexing starts from 0, we decrease total count($s1) by 1, {s1 = s1 - 1}
	
	
	#index = $t0 (i = 0)
	addi $t2, $zero, 0
	
	
	# store the values into the array
	WHILE:
	
		li $v0, 12		# enter your character
		syscall
	
		blt $v0, 48, WHILE 	# skip characters like space, carriage return....all which ascii is less than 48 
	
		move $s0, $v0 		# save it to $s0 
	
		sb $s0, array($t2)	# assign value to the array, array[i] = $s0
		addi $t2, $t2, 1	# increase the array index (i+=1)
	
	
		bgt $t2, $s1, LOOPEXIT	# check terminating condition (i>n)	
		j WHILE
	
	LOOPEXIT:
	
	
		### ..................PART - 2: DISPLAY THE ARRAY IN MATRIX FORM....................... ###
	
	
	# display headline 2
	li $v0, 4
	la $a0, msgP3
	syscall
	
	li $v0, 1
	move $a0, $t0	# row value
	syscall
	
	
	li $t2, 'x'
	li $v0, 11
	move $a0, $t2	# print a character 'x'
	syscall
	
	
	li $v0, 1
	move $a0, $t1 	# col value
	syscall
	
	li $v0, 4
	la $a0, msgP4
	syscall 
	
	
	# decrease the row and col count by 1
	# its because the index starts from 0
	# so to match the index count, we need to decrease it
	addi $t0, $t0, -1	# row count
	addi $t1, $t1, -1	# col count
	
	
	# reset the index to 0 (i=0)
	addi $t2, $zero, 0
	# reset second index to 0 (j=0)
	addi $t3, $zero, 0
	# assume a variable to keep track of row count, initialize at 0 (elem = 0)
	addi $t4, $zero, 0
	# assume the increament of row count, initialize at 0 (constvalue = 0)
	addi $t5, $zero, 0
	add $t5, $t5, $t1
	# assume the array_new_index, initialize at 0 (id = 0)
	addi $t6, $zero, 0
	
	
	
	# display array values
	OUTERLOOP:
	
		INNERLOOP:
	
			# id($t6) = elem + i + j
	
			addu $t7, $t2, $t3	# x = i + j
			addu $t6, $t4, $t7	# id = elem + x = elem + i + j
		
			lb $s0, array($t6)	# load the characters from memory (char[id])
			addi $t3, $t3, 1	# increase the index (j += 1)
		
			li $v0, 11		# print the value
			addi $a0, $s0 , 0	
			syscall
	
			li $v0, 4		# print a space
			la $a0, space
			syscall		


			bgt $t3, $t1, INNERLOOPEXIT	# check terminating condition (j>col)
			j INNERLOOP
			
		INNERLOOPEXIT:
		
		# print a new line
		li $v0, 4
		la $a0, newline
		syscall
		
		addu $t4, $t4, $t5	# elem = elem + constvalue
		addi $t2, $t2, 1	# i++
		addi $t3, $zero, 0	# j = 0
		
		
		bgt $t2, $t0, OUTERLOOPEXIT	# check terminating condition (i>row)
		j OUTERLOOP
	
	OUTERLOOPEXIT:
	
	
	# print a new line
	li $v0, 4
	la $a0, newline
	syscall
	
	
	
		### ..................PART - 3: EXHANGE TOW ROWS AS PER USER INPUT....................... ###
	
	
	
	# add 1 to utilize the initially entered row and col value 
	addi $t0, $t0, 1	# row value
	addi $t1, $t1, 1	# col value
	
	
	
	# initialize exchangeRow1 to 0(r1=0)
	addi $t3, $zero, 0
	# initialize exchangeRow2 to 0(r2=0)
	addi $t4, $zero, 0
	
	
	
	# input of r1
	li $v0, 4
	la $a0, exchangeRow1
	syscall
	
	li $v0, 5
	syscall
	
	move $t3, $v0
	
	
	
	# input of r2
	li $v0, 4
	la $a0, exchangeRow2
	syscall
	
	li $v0, 5
	syscall
	
	move $t4, $v0
	
	
	
	# display headline 3
	li $v0, 4
	la $a0, msgP5
	syscall
	
	li $v0, 1
	move $a0, $t3	# r1 value
	syscall	
		
	li $v0, 4
	la $a0, msgP6
	syscall 
	
	li $v0, 1
	move $a0, $t4 	# r2 value
	syscall
	
	li $v0, 4
	la $a0, msgP7
	syscall 
	
	
	
	# modified r1 to traverse the character array
	mulu $t3, $t3, $t1	# r1 = r1*col(modr1)
	mulu $t4, $t4, $t1	# r2 = r2*col(modr2)
	
	# reset traverse index to 0 (j=0)
	addi $t5, $zero, 0
	
	
	# exchange the entered exchangeRow1 with excahngeRow2 (swap r1, r2)
	LOOPSTART:
		
		lb $s0, array($t3)	# temp = char[modr1], $s0 = array[0]
		lb $s2, array($t4)	# temp2 = char[modr2], $s2 = array[1]
		sb $s2, array($t3)	# char[modr1] = temp2, array[0] = $s2
		sb $s0, array($t4)	# char[modr2] = temp, array[1] = $s0
		
		addi $t3, $t3, 1	# increase the index (modr1 += 1)
		addi $t4, $t4, 1	# increase the index (modr2 += 1)
		addi $t5, $t5, 1	# increase the index (j += 1)
		
		bge $t5, $t1, LOOPEND	# check terminating condition (j>col)
		j LOOPSTART
		
	LOOPEND:
	
	
	
		### ..................PART - 4: DISPLAY THE FINAL OUTPUT....................... ###
	
	
	# decrease the row and col count by 1
	# its because the index starts from 0
	# so to match the index count, we need to decrease it
	addi $t0, $t0, -1	# row count
	addi $t1, $t1, -1	# col count
	
	
	# reset the index to 0 (i=0)
	addi $t2, $zero, 0
	# reset second index to 0 (j=0)
	addi $t3, $zero, 0
	# assume a pointer variable, initialize at 0 (elem = 0)
	addi $t4, $zero, 0
	# assume the increament, initialize at 0 (constvalue = 0)
	addi $t5, $zero, 0
	add $t5, $t5, $t1
	# assume the array_new_index, initialize at 0 (id = 0)
	addi $t6, $zero, 0
	
	
	
	# display the finally exchanged array values
	OUTERLOOP2:
	
		INNERLOOP2:
	
			# id($t6) = elem + i + j
	
			addu $t7, $t2, $t3	# x = i + j
			addu $t6, $t4, $t7	# id = elem + x = elem = i + j
		
			lb $s0, array($t6)	# load the characters from ram (char[id])
			addi $t3, $t3, 1	# increase the index ( i += 1)
		
			li $v0, 11		# print the value
			addi $a0, $s0 , 0	
			syscall
	
			li $v0, 4		# print a space
			la $a0, space
			syscall		


			bgt $t3, $t1, INNERLOOPEXIT2	# check terminating condition (j>col)
			j INNERLOOP2
			
		INNERLOOPEXIT2:
		
		# print a new line
		li $v0, 4
		la $a0, newline
		syscall
		
		addu $t4, $t4, $t5	# elem = elem + constvalue
		addi $t2, $t2, 1	# i++
		addi $t3, $zero, 0	# j = 0
		
		
		bgt $t2, $t0, OUTERLOOPEXIT2	# check terminating condition (i>row)
		j OUTERLOOP2
	
	OUTERLOOPEXIT2:
	
		# exit 
		li $v0, 10
		syscall
	
	

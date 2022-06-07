.data
	array: .space 2212 	#CHANGE
	size: .word 400
	promptRow: .asciiz "Enter total row number: "
	promptCol: .asciiz "\nEnter total column number: "
	promptArr: .asciiz "\nEnter the array: \n"
	promptRowSwap1: .asciiz "\nEnter the first row number you want to swap: "
	promptRowSwap2: .asciiz "\nEnter the second row number you want to swap: "
	showArray: .asciiz "Array after swapping rows :\n"
	.eqv DATA_SIZE 4

.text
	main:
	
	#take input row number
	li $v0, 4
	la $a0, promptRow 
	syscall
	
	li $v0, 5
	syscall
	
	move $s0,$v0
	 
	#take input column number
	li $v0, 4
	la $a0, promptRow 
	syscall
	
	li $v0, 5
	syscall
	
	move $s1,$v0		
	
	#store the total size required to hold the array as intended by user
	mult $s0, $s1
	mflo $s3	#CHANGE
	mul $s2, $s3, $s1

		
	#take input whole array
	li $v0, 4       	
    	la $a0, promptArr        
    	syscall
    	
	
   	addi $t0,$zero,0		#set counter to 0
   	
	while1:
		
    		li $v0, 12		#DID A CHANGE HERE
    		syscall 
    		
    		sb $v0, array($t0)       #store input in array #CHANGE (sw ->  sb)
    		
    		addi  $t0, $t0, 1  	#DID A CHANGE HERE 	#increase by 4 to to get to next integer
    		
    		beq $t0, $s2, exit
    		j while1
    	
    	
    	#COntinue taking inputs for exchanging row
    	exit:
    	
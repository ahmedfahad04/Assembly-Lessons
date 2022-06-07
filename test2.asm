.data

	msg: .asciiz "Summation is: "
	
.text

	li $v0, 4
	la $a0, msg
	syscall
	
	li $s0, 5
	li $s1, 10
	
	add $s2, $s1, $s0
	
	li $v0, 1
	move $a0, $s2	
	syscall
	
	
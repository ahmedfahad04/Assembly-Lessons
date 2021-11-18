.data

	msg: .asciiz "Summation is: "
	
.text

	li $v0, 4
	la $a0, msg
	syscall
	
	add $s0, $zero, 5
	add $s1, $zero, 10
	
	add $s2, $s1, $s0
	
	li $v0, 1
	move $a0, $s2	
	syscall
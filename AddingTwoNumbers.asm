.data

    # these are the functions arguments
    n1: .asciiz "enter your first number: "
    n2: .asciiz "enter your second number: "
    result: .asciiz "result is "

.text
    #getting first input.
    la $a0, n1 
    li $v0, 4  # system call to print_str
    syscall    
    
    li $v0, 5  # system call to read_int
    syscall
    move $s0, $v0

    #getting second input.
    la $a0, n2
    li $v0, 4
    syscall
    
    li $v0, 5
    syscall
    move $s1, $v0

    #calculate and print out the result.
    la $a0, result
    li $v0, 4
    syscall
    
    add $s3, $s0, $s1
    move $a0, $s3
    
    li $v0, 1  # system call for print_int
    syscall

    #end program.
    #li $v0, 10
    #syscall
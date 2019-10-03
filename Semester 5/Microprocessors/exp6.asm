.model small

.data
    m1 db 10,13, "Negative Count: $"
    m2 db 10,13, "Negative numbers: $"
    Array db 10h, 20h, 0f0h, 0abh, 0b0h
    n_array db 5 DUP(0)
    n_count db ?

.code
    Disp MACRO xx
        mov ah, 09h
        lea dx, xx
        int 21h
    endm
    
    .startup
        mov bl, 0
        mov cl, 5
        lea si, Array
        lea di, n_array
        
        back:
            mov bh, [si]
            ; anding with 1000 0000 gives msb as 1 
            ; else msb = 0
            ; so we know the number is -ve or +ve
            ; then save that number in n_array
            and bh, 80h
            jz aa; +ve number
            ; -ve number
            mov bh, [si]
            mov [di],  bh
            inc di
            inc bl
            
            aa:
                inc si
                dec cl
  
        jnz back
            
        ;display count
        Disp m1
        mov n_count, bl
        mov dl, bl
        add dl, 30h
        mov ah, 02h
        int 21h
        
        ;first digit
        Disp m2
        lea di, n_array
        
        back1:
            mov bh, [di]
            and bh, 0f0h
            mov cl, 4
            shr bh, cl
            cmp bh, 9
            JG aa1
            add bh, 30h
            jmp aa2
            
            aa1:
                add bh, 37h; for numbers greater than 9    
            
            aa2: ; display tens place digit
                mov dl, bh
                mov ah, 02h
                int 21h
            
            ; units place digit
            mov bh, [di]
            and bh, 0fh
            cmp bh , 9
            JG aa3
            add bh, 30h
            jmp aa4
            
            aa3:
                add bh, 37h
            
            aa4:
                mov dl,bh
                mov ah, 02
                int 21h
                inc di
                dec n_count
            
        jnz back1
    .exit
end
            
        
        
        
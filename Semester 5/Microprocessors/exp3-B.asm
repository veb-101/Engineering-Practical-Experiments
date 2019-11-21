;HEX to BCD
.model small
.data
    m1 db 10, 13, "Equivalent BCD no. is: $"
    no dw 0ffffh

.code
    Disp macro xx
        mov ah, 09
        lea dx, xx
        int 21h
        endm
    
    .startup
        Disp m1
        mov cl, 0
        mov ax, no
        
        mov bx, 0ah
        back:
            mov dx, 0
            div bx
            push dx
            inc cl
            cmp ax, 0
            jnz back
        
        back1:
            pop dx
            add dl, 30h
            mov ah, 02
            int 21h
            dec cl
        jnz back1
    .exit
end

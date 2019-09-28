.model small
.data
    m0 db 10,13, "Enter choice: $"
    m1 db 10,13, "Addition is: $";
    m2 db 10,13, "Subtraction is: $";
    m3 db 10,13, "exit$"
    
    number1 dw 2345h;
    number2 dw 1234h;
    res dw ?
.code
    Disp MACRO xx
        mov ah, 09h
        lea dx, xx
        int 21h
    endm
    
    .startup
        CHOICE: Disp m0
                mov ah, 01h; take user choice
                int 21h
                sub al, 30h ;retrieving number from ascii
                cmp al, 01h
                je ADDITION; Jump if equal
                cmp al, 02h; compare two numbers
                je SUBTRACTION
                cmp al, 03h
                je EXIT
                
                
                ; cannot access 2 locations at the same time so we use register
                
      ADDITION: Disp m1
                mov ax, number1
                add ax, number2
                mov res, ax
                call pprint
                jmp CHOICE
   
   SUBTRACTION: Disp m2
                mov ax, number1
                sub ax, number2
                mov res, ax
                call pprint
                jmp choice
                
    pprint PROC
           mov bx, res
           and bh, 0f0h
           mov cl, 4
           shr bh, cl
           add bh, 30h
           mov dl, bh
           mov ah,  02h; print a single digit, works only with dl register
           int 21h
           
           mov bx, res
           and bh, 0fh
           add bh, 30h
           mov dl, bh
           mov ah, 02
           int 21h
           ;-------------------------
           mov bx, res
           and bl, 0f0h
           mov cl, 4
           shr bl, cl
           add bl, 30h
           mov dl, bl
           mov ah, 02h
           int 21h
           
           mov bx, res
           and bl, 0fh
           add bl, 30h
           mov dl, bl
           mov ah, 02
           int 21h
           ret
           
    pprint endp
    
    EXIT: .exit
    
end
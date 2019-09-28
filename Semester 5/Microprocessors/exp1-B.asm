.model small
.data

        m1 db 10, 13, "Enter 16-bit no.:$"
        m2 db 10, 13, "Display 16-bit no.:$"
        no dw(?)
.code
    .startup
        mov ah, 09
        lea dx, m1
        int 21h
        
        ; --------------INPUT-------------
        ;number: 1234
        ;for higher byte
        ;we use the bx register for saving the number
        mov ah, 01
        int 21h
        sub al, 30h
        mov cl, 4
        shl al, cl
        mov dh, al
        
        mov ah, 01h
        int 21h
        sub al, 30h
        add dh, al
        
        mov bh, dh ;storing MSB(8bit) no. in bh -> 12
        
        ;for lower byte
        mov ah, 01
        int 21h
        sub al, 30h
        mov cl, 4
        shl al, cl
        mov dh, al
        
        mov ah, 01h
        int 21h
        sub al, 30h
        add dh, al
        
        mov bl, dh ;storing LSB(8bit) no. in bl -> 34
        
        ; -----------DISPLAY-----------
        
        mov no, bx
        
        mov ah, 09
        lea dx, m2
        int 21h
        ;for 12
        ;for 1
        mov dx, no
        mov dl, dh
        
        and dl, 0f0h
        mov cl, 4
        shr dl, cl
        add dl, 30h
        mov ah, 02
        int 21h
        ;for 1
        mov dx, no
        mov dl, dh
        and dl, 0fh
        add dl, 30h
        mov ah, 02
        int 21h
       
        ;for 34
        ;for 3
        
        mov dx, no
        and dl, 0f0h
        mov cl, 4
        shr dl, cl
        add dl, 30h
        mov ah, 02
        int 21h
        
        ;for 4
        mov dx, no
        and dl, 0fh
        add dl, 30h
        mov ah, 02
        int 21h
    .exit
end
; ACCEPT, DISPlAY, CONCAT, COMPARE
.model small
.data
    m1 db 10, 13, "Accept string 1: $" 
    m2 db 10, 13, "Length of string: $"
    m3 db 10, 13, "Displat 1st string: $"
    
    m4 db 10, 13, "Accept string 2: $" 
    m5 db 10, 13, "Length of string: $"
    m6 db 10, 13, "Displat 2nd string: $"
    
    m7 db 10, 13, "Concat: $"
    m8 db 10, 13, "String are equal.$"
    m9 db 10, 13, "String are not equal.$"
    
    str1 db 80, ?, 80 DUP(?)
    str2 db 80, ?, 80 DUP(?)

.code
    Disp MACRO xx
        mov ah, 09
        lea dx, xx
        int 21h
    endm
    
    .startup
        Disp m1
        mov ah, 0ah
        lea dx, str1
        int 21h
        
        ;display length of string 1
        Disp m2
        lea si, str1 + 1
        mov cl, [si]
        mov dl, cl
        add dl, 30h
        mov ah, 02
        int 21h
   
        ;display string 1
        Disp m3
        lea si, str1 + 2
        BACK1:   
            mov dl, [si]
            mov ah, 02h
            int 21h
            inc si
            dec cl
            jnz BACK1
        ;========================
            
        Disp m4
        mov ah, 0ah
        lea dx, str2
        int 21h
        
        ;display length of string 2
        Disp m5
        lea si, str2 + 1
        mov cl, [si]
        mov dl, cl
        add dl, 30h
        mov ah, 02
        int 21h
   
        ;display string 2
        Disp m6
        lea si, str2 + 2
        BACK2:   
            mov dl, [si]
            mov ah, 02h
            int 21h
            inc si
            dec cl
            jnz BACK2
            
        ;concat --------------------
        Disp m7
        lea si, str1 + 1      
        mov cl, [si]
        mov bl, cl
        lea di, str2 + 1
        mov ch, [di]
        mov bh, ch
        
        lea si, str1 + 2
        back3:
            inc si
            dec cl
            jnz back3
            
        lea di, str2+2
        
        back4:
            mov cl, [di]
            mov [si], cl
            inc si
            inc di
            dec ch
            jnz back4
            
        add bl, bh
        lea si, str1 + 2
        
        back5:
            mov dl, [si]
            mov ah, 02
            int 21h
            inc si
            dec bl
            jnz back5
       ;----------------------
       ;compare
       lea si, str1+1
       lea di, str2+1
       mov cl, [si]
       mov ch, [di]
       cmp cl, ch
       jnz aa
       lea si, str1+2
       lea di, str2+2
       back6:
            mov dl, [si]
            mov dh, [di]
            cmp dl, dh
            jnz aa
            inc si
            inc di
            dec cl
            jnz back6
       Disp m8
       jmp bb
       
       aa: Disp m9
       
       bb: 
            .exit  
end
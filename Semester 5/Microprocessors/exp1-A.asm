.model small
.data

        m1 db 10, 13, "Enter 8-bit no.:$"
        m2 db 10, 13, "Display 8-bit no.:$"
        no db(?)

.code
    .startup
                mov ah, 09
                lea dx, m1
                int 21h
                ; --------------INPUT----------------
                mov ah, 01
                int 21h

                sub al, 30h
                ;default entered number is saved in al reg. 
                ;while converting 8 bit no, 
                ;conversion of ascii to binary is done
                ;ASCII -> binary
        
                mov cl, 4
                ;moving the first number to tens place
                shl al, cl
                mov bl, al
        
                mov ah, 01
                int 21h
                sub al, 30h
                add bl, al
                int 21h
                
                ; -------------DISPLAY---------------
                ;we need to convert from binary-> ASCII
                ;First extract the tens place number
                ;eg. 56H5
                ;we need 5H, anding(&) the number with F0H
                ;we need 6H, anding(&) the number with 0FH
                ;we get 50H and 6H
                ;shift 05H to units place by shifting left
                ;add 30 to 05H and 06H,then display
                
                ;for tens place no. eg. 5
                mov no, bl
                mov ah, 09
                lea dx, m2
                int 21h
                
                mov bh, no
                and bh, 0f0H ;so processor understands its a number, append 0
                mov cl, 4
                shr bh, cl
                add bh, 30h
                mov dl, bh
                mov ah, 02h; works only if the content is saved in dl register
                int 21h
                
                ;for units place no. eg.6
                mov bh, no
                and bh, 0fh
                add bh, 30h
                mov dl, bh
                mov ah, 02h
                int 21h
        .exit
end

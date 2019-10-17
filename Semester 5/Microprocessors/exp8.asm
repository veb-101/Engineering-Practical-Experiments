;------------ Basic mouse commands
;1) ax = 0000 -> mouse driver present or not
;  int 21h

; return ax = 0000, mouse driver not present
;        ax = FFFF, mouse driver present

;2) ax = 0001 -> show mouse cursor
;   int 33h 

;3) ax =0011h -> set graphics mode
;   int 10h

;4) ax = 000 -> text mode
;   int 10h

;5) ax = 0003 -> get mouse button status
;   int 33h

; return bx = 0000, centre button
;        bx = 0001, left button
;        bx = 0002, right button

;6) ax = 0004h -> set mouse cursor
;   cx = x co-ordinate
;   dx = y co-ordinate

;7) ax = 0007h -> set horizontal limit
;   cx = min x co-ordinate
;   dx = max x co-ordinate

;8) ax = 0008h -> set vertical limit
;   cx = min y co-ordinate
;   dx = max y co-ordinate

;------------

.model small
.data
    m1 db 10, 13, "Mouse driver is present$"

.code
    disp macro xx
        mov ah, 09
        lea dx, xx
        int 21h
    endm
   
    .startup
        mov ax, 0000
        int 33h
        cmp ax, 0000
        je exit1
        
        disp m1
        
        mov ax, 0004h
        mov cx, 0
        mov dx, 0
        int 33h
        
        mov ax,0007h
        mov cx, 0
        mov dx, 0fffh
        int 33h
        
        mov ax,008h
        mov cx, 0
        mov dx, 0
        int 33h
        
        back:
            mov ax, 0001
            int 33h
            mov ax, 0003
            int 33h
            cmp bx, 0001
            je next
            jmp next1
            
            next:
                mov ax, 0011h
                int 10h
                mov ah, 0ch; pixel printing
                int 10h
            
            next1:
                mov ax, 0003h
                int 33h
                cmp bx, 0002
                je exit1
        jmp back
        
        exit1:
            mov ah, 00h; going to text mode
            int 10h
            
            mov ah, 31h; terminate
            int 21h
        .exit
end 

; BCD TO HEX

.model small
.stack
.data
    m1 DB 10,13, "hex equivalent is: $"
    number DW 14
.code
    Disp MACRO xx
        MOV AH, 09
        LEA DX, XX
        INT 21H
    ENDM
    
    .startup
        MOV DX, 0
        MOV AX, number
        MOV BX, 16
        MOV CL, 0

        LOOP1:
            MOV DX, 0
            DIV BX
            PUSH DX
            INC CL
            CMP AX, 0
            JNZ LOOP1
        
        Disp m1
        BACK:
            POP dx
            cmp dx,09h
            jg logic
            ADD DL, 30H
            logic:
                add dl,37h 
                MOV AH, 02
                INT 21H
                DEC CL
             JNZ BACK
    .exit
end

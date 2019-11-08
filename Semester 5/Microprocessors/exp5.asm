; Reverse String, Palindrome
.model small
.stack
.data
    M1 DB 10,13,"Accept String: $"
    M2 DB 10,13,"Length of String: $"
    M3 DB 10,13,"Display String: $"
    M4 DB 10,13,"Reverse of String: $"
    M5 DB 10,13,"String is Palindrome. $"
    M6 DB 10,13,"String is Not Palindrome. $"
    str1 DB 80,?,80 DUP(?)
    str2 DB 80,?,80 DUP(?)
.code
    
    Disp MACRO xx
        MOV AH,09H
        LEA DX,xx
        INT 21H
    ENDM
    
    .startup
        Disp M1     ;Accept the string
        MOV AH,0AH
        LEA DX,str1
        INT 21H

        Disp M2     ;Display Length of String 1
        LEA SI,str1+1
        MOV CL,[SI]
        MOV DL,CL
        ADD DL,30H
        MOV AH,02H
        INT 21H

        Disp M3     ;Display String 1
        LEA SI,str1+2
        bk1:
            MOV DL,[SI]
            MOV AH,02H
            INT 21H
            INC SI
            DEC CL
            JNZ bk1

        Disp M4    ;Reverse String
        LEA DI,str2+2
        LEA SI,str1+1
        MOV CL,[SI]
        MOV CH,CL    
        MOV BH,CL
        LEA SI,str1+2
        
        bk2:
            INC SI
            DEC CL
            JNZ bk2
        
        DEC SI

        bk3:
            MOV DL,[SI]
            MOV [DI],DL
            INC DI
            DEC SI
            DEC CH
            JNZ bk3
    
        LEA DI,str2+2
        
        bk4:
            MOV DL,[DI]
            MOV AH,02
            INT 21H
            INC DI
            DEC BH
            JNZ bk4
    
        LEA SI,str1+2     ;Palindrome or not
        LEA DI,str2+2
        MOV CL,str1+1

        bk5:
            MOV DL,[SI]
            MOV DH,[DI]
            CMP DL,DH
            JNZ aa
            INC SI
            INC DI
            DEC CL
            JNZ bk5
        
        Disp M5
        JMP ext
    
        aa:
            Disp M6

        ext:
            .exit
end


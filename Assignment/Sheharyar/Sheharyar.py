# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 01:25:03 2022

@author: walee
"""

def generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    machineCode = ""
    if len(inst) == 3:        
        if inst == 'MOV':
            if (operand1 in registerNames and operand2 in registerNames) or (operand1 in registerLower and operand2 in registerLower) or (operand1 in registerHigher and operand2 in registerHigher):
                machineCode = "000000 11 11 xxx yyy"
                if (operand1 == "AX"):
                    machineCode = machineCode.replace("xxx","000") 
                elif (operand1 == "BX"):
                    machineCode = machineCode.replace("xxx","001")
                elif (operand1 == "CX"):
                    machineCode = machineCode.replace("xxx","010")
                elif (operand1 == "DX"):
                    machineCode = machineCode.replace("xxx","011")
                elif (operand1 == "EX"):
                    machineCode = machineCode.replace("xxx","100")
                elif (operand1 == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                    
                if (operand2 == "AX"):
                    machineCode = machineCode.replace("yyy","000") 
                elif (operand2 == "BX"):
                    machineCode = machineCode.replace("yyy","001")
                elif (operand2 == "CX"):
                    machineCode = machineCode.replace("yyy","010")
                elif (operand2 == "DX"):
                    machineCode = machineCode.replace("yyy","011")
                elif (operand2 == "EX"):
                    machineCode = machineCode.replace("yyy","100")
                elif (operand2 == "FX"):
                    machineCode = machineCode.replace("yyy","101")
            elif (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 not in registerNames or operand2 not in registerLower or operand2 not in registerHigher) and operand2[0] != '[':
                machineCode = "000000 11 00 xxx 000 00000000 00000000 aaaaaaaa bbbbbbbb"
                if (operand1 == "AX"):
                    machineCode = machineCode.replace("xxx","000") 
                elif (operand1 == "BX"):
                    machineCode = machineCode.replace("xxx","001")
                elif (operand1 == "CX"):
                    machineCode = machineCode.replace("xxx","010")
                elif (operand1 == "DX"):
                    machineCode = machineCode.replace("xxx","011")
                elif (operand1 == "EX"):
                    machineCode = machineCode.replace("xxx","100")
                elif (operand1 == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                operand2 = int(operand2)
                operand2 = bin(operand2)
                operand2 = operand2[2:]
                higher, lower = binaryDirect(operand2)
                machineCode = machineCode.replace("aaaaaaaa",higher) 
                machineCode = machineCode.replace("bbbbbbbb",lower) 
                
            elif operand1 in registerNames and operand2[0] == '[' and operand2[1:3] in registerNames and operand2[3] != '+':
                operand2 = operand2[1:3]
                machineCode = "000000 11 00 xxx yyy"
                machineCode = "000000 11 11 xxx yyy"
                if (operand1 == "AX"):
                    machineCode = machineCode.replace("xxx","000") 
                elif (operand1 == "BX"):
                    machineCode = machineCode.replace("xxx","001")
                elif (operand1 == "CX"):
                    machineCode = machineCode.replace("xxx","010")
                elif (operand1 == "DX"):
                    machineCode = machineCode.replace("xxx","011")
                elif (operand1 == "EX"):
                    machineCode = machineCode.replace("xxx","100")
                elif (operand1 == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                    
                if (operand2 == "AX"):
                    machineCode = machineCode.replace("yyy","000") 
                elif (operand2 == "BX"):
                    machineCode = machineCode.replace("yyy","001")
                elif (operand2 == "CX"):
                    machineCode = machineCode.replace("yyy","010")
                elif (operand2 == "DX"):
                    machineCode = machineCode.replace("yyy","011")
                elif (operand2 == "EX"):
                    machineCode = machineCode.replace("yyy","100")
                elif (operand2 == "FX"):
                    machineCode = machineCode.replace("yyy","101")

            elif operand1[0] == '[' and operand1[1:3] in registerNames and operand2 in registerNames:
                operand1 = operand1[1:3]
                machineCode = "000000 01 00 xxx yyy"
                machineCode = "000000 11 11 xxx yyy"
                if (operand1 == "AX"):
                    machineCode = machineCode.replace("xxx","000") 
                elif (operand1 == "BX"):
                    machineCode = machineCode.replace("xxx","001")
                elif (operand1 == "CX"):
                    machineCode = machineCode.replace("xxx","010")
                elif (operand1 == "DX"):
                    machineCode = machineCode.replace("xxx","011")
                elif (operand1 == "EX"):
                    machineCode = machineCode.replace("xxx","100")
                elif (operand1 == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                    
                if (operand2 == "AX"):
                    machineCode = machineCode.replace("yyy","000") 
                elif (operand2 == "BX"):
                    machineCode = machineCode.replace("yyy","001")
                elif (operand2 == "CX"):
                    machineCode = machineCode.replace("yyy","010")
                elif (operand2 == "DX"):
                    machineCode = machineCode.replace("yyy","011")
                elif (operand2 == "EX"):
                    machineCode = machineCode.replace("yyy","100")
                elif (operand2 == "FX"):
                    machineCode = machineCode.replace("yyy","101")

            elif operand1[0] == '[' and operand1[1:3] not in registerNames and operand2 in registerNames:
                operand1 = operand1[1:len(operand1)]
                machineCode = "000000 11 10 xxx 000 aaaaaaaa bbbbbbbb"
                if (operand2 == "AX"):
                    machineCode[18:21] = "000" 
                elif (operand2 == "BX"):
                    machineCode[18:21] = "001"
                elif (operand2 == "BX"):
                    machineCode[18:21] = "010"
                elif (operand2 == "BX"):
                    machineCode[18:21] = "011"
                elif (operand2 == "BX"):
                    machineCode[18:21] = "100"
                elif (operand2 == "BX"):
                    machineCode[18:21] = "101"
                operand1 = int(operand1)
                operand1 = bin(operand1)
                operand1 = operand2[2:]
                higher, lower = binaryDirect(operand1)
                machineCode = machineCode.replace("aaaaaaaa",higher) 
                machineCode = machineCode.replace("bbbbbbbb",lower) 
            
            elif operand1 in registerNames and operand2[0] == '[' and operand2[3] == '+':
                machineCode = "000000 11 10 xxx yyy aaaaaaaa bbbbbbbb"
                if (operand1 == "AX"):
                    machineCode = machineCode.replace("xxx","000") 
                elif (operand1 == "BX"):
                    machineCode = machineCode.replace("xxx","001")
                elif (operand1 == "CX"):
                    machineCode = machineCode.replace("xxx","010")
                elif (operand1 == "DX"):
                    machineCode = machineCode.replace("xxx","011")
                elif (operand1 == "EX"):
                    machineCode = machineCode.replace("xxx","100")
                elif (operand1 == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                    
                if (operand2[1:3] == "AX"):
                    machineCode = machineCode.replace("yyy","000") 
                elif (operand2[1:3] == "BX"):
                    machineCode = machineCode.replace("yyy","001")
                elif (operand2[1:3] == "CX"):
                    machineCode = machineCode.replace("yyy","010")
                elif (operand2[1:3] == "DX"):
                    machineCode = machineCode.replace("yyy","011")
                elif (operand2[1:3] == "EX"):
                    machineCode = machineCode.replace("yyy","100")
                elif (operand2[1:3] == "FX"):
                    machineCode = machineCode.replace("xxx","101")
                operand1 = int(operand1[4:len(operand1)])
                operand1 = bin(operand1)
                operand1 = operand2[2:]
                higher, lower = binaryDirect(operand1)
                machineCode = machineCode.replace("aaaaaaaa",higher) 
                machineCode = machineCode.replace("bbbbbbbb",lower) 
            
        elif inst == 'ADD':
            machineCode = "000011 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == 'SUB':
            machineCode = "000100 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "ROR":
            machineCode = "001010 11 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == "ROL":
            machineCode = "001010 11 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == "MUL":
            machineCode = "001100 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "DIV":
            machineCode = "001101 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "AND":
            machineCode = "001110 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "XOR":
            machineCode = "010000 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "NOT":
            machineCode = "010001 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        elif inst == "JMP":
            machineCode = "010010 11 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == "CMP":
            machineCode = "010011 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
        if inst == 'DEC':
            machineCode = "000110 01 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
        elif inst == 'INC':
            machineCode = "000101 01 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == 'SHR':
            machineCode = "000010 01 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == 'SHL':
            machineCode = "000001 01 00 xxx"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
        elif inst == 'POP':
            machineCode = "001001"
    elif len(inst) == 4:
        if inst == 'SHRD':
            machineCode = "000010 01 00 xxx 000 00000000 00000000 aaaaaaaa bbbbbbbb"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            operand2 = int(operand2)
            operand2 = bin(operand2)
            operand2 = operand2[2:]
            higher, lower = binaryDirect(operand2)
            machineCode = machineCode.replace("aaaaaaaa",higher) 
            machineCode = machineCode.replace("bbbbbbbb",lower) 
        elif inst == 'SHLD':
            machineCode = "000001 01 00 xxx 000 00000000 00000000 aaaaaaaa bbbbbbbb"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
            operand2 = int(operand2)
            operand2 = bin(operand2)
            operand2 = operand2[2:]
            higher, lower = binaryDirect(operand2)
            machineCode = machineCode.replace("aaaaaaaa",higher) 
            machineCode = machineCode.replace("bbbbbbbb",lower) 
            
        elif inst == 'XCHG':
            machineCode = "000111 01 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
            elif inst == 'PUSH':
                machineCode = "001000"
                
    elif len(inst) == 2:
        if inst == "OR":
            machineCode = "001111 11 11 xxx yyy"
            if (operand1 == "AX"):
                machineCode = machineCode.replace("xxx","000") 
            elif (operand1 == "BX"):
                machineCode = machineCode.replace("xxx","001")
            elif (operand1 == "CX"):
                machineCode = machineCode.replace("xxx","010")
            elif (operand1 == "DX"):
                machineCode = machineCode.replace("xxx","011")
            elif (operand1 == "EX"):
                machineCode = machineCode.replace("xxx","100")
            elif (operand1 == "FX"):
                machineCode = machineCode.replace("xxx","101")
                
            if (operand2 == "AX"):
                machineCode = machineCode.replace("yyy","000") 
            elif (operand2 == "BX"):
                machineCode = machineCode.replace("yyy","001")
            elif (operand2 == "CX"):
                machineCode = machineCode.replace("yyy","010")
            elif (operand2 == "DX"):
                machineCode = machineCode.replace("yyy","011")
            elif (operand2 == "EX"):
                machineCode = machineCode.replace("yyy","100")
            elif (operand2 == "FX"):
                machineCode = machineCode.replace("yyy","101")
                
    return machineCode 
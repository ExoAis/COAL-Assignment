# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 01:22:38 2022

@author: walee
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python
# coding: utf-8

def inc(inst, operand1, registers, registerNames, instructions):
    inst = 'INC'
    check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    reg1 = str(reg1)
    left = ''
    value = registers[reg1]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left, 2)
    resultT = left + 1
    print(resultT)
    if resultT > 65535:
        return check
    check = True
    resultT = bin(resultT)
    resultT = resultT[2:]
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    return check


# In[ ]:


def dec(inst, operand1, registers, registerNames, instructions):
    inst = 'DEC'
    check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    reg1 = str(reg1)
    left = ''
    value = registers[reg1]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left, 2)
    resultT = left - 1
    print(resultT)
    if resultT < 0:
        return check
    check = True
    resultT = bin(resultT)
    resultT = resultT[2:]
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    return check


# In[ ]:


def sub(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'SUB'
    check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left, 2)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right, 2)
    resultT = left - right
    if resultT < -65535:
        return check
    check = True
    resultT = bin(abs(resultT))
    resultT = resultT[2:]
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    if int(resultT,2) >= -65535 and int(resultT,2) < 0:
        registers['FR'][0] = 1 
    return check


# In[ ]:


def push(inst, registers, registerNames, instructions, memoryLocations):
    inst = 'PUSH'
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        mem = bin(i+8)
        mem = str(mem)
        mem = mem[2:]
        reg = bin(i)
        reg = str(reg)
        reg = reg[2:]
        for j in range(len(registers[reg])):
             memoryLocations[mem][j] = registers[reg][j]  #copy values from registers to memory locations
            #last 8 memory locations are used for stack operations i.e storing registers on stack
    #return machineCode


# In[ ]:


def pop(inst, registers, registerNames, instructions, memoryLocations):
    inst = 'POP'
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        mem = bin(i+8)
        mem = str(mem)
        mem = mem[2:]
        reg = bin(i)
        reg = str(reg)
        reg = reg[2:]
        for j in range(len(registers[reg])):
             registers[reg][j] = memoryLocations[mem][j] #copy values from registers to memory locations
            #last 8 memory locations are used for stack operations i.e storing registers on stack
    #return machineCode


# In[ ]:


def shift_right(inst, operand1, registers, registerNames, instructions):
    inst = 'SHR'
    #displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    registers[reg1] = [registers[reg1][-1]] + registers[reg1][:-1]
    registers[reg1][0] = 0
    #return machineCode


# In[ ]:


def shift_right_by_displacement(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'SHRD'
    check = False
    displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    if int(displacement) > 15:
        return check
    check = True
    for i in range(int(displacement)):
        registers[reg1] = [registers[reg1][-1]] + registers[reg1][:-1]
        registers[reg1][0] = 0
    return check


# In[ ]:


def shift_left(inst, operand1, registers, registerNames, instructions):
    inst = 'SHL'
    #check = False
    #displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    registers[reg1] =  registers[reg1][1:] + [registers[reg1][0]]
    registers[reg1][15] = 0
    #return machineCode


# In[ ]:


def shift_left_by_displacement(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'SHLD'
    check = False
    displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    if int(displacement) > 15:
        return check
    check = True
    for i in range(int(displacement)):
        registers[reg1] =  registers[reg1][1:] + [registers[reg1][0]]
        registers[reg1][15] = 0
    return check


# In[ ]:

def rotate_left(inst, operand1, registers, registerNames, instructions):
    inst = 'ROL'
    #check = False
    #displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    temp = registers[reg1][0]
    registers[reg1] =  registers[reg1][1:] + [registers[reg1][0]]
    registers[reg1][15] = temp

def rotate_right(inst, operand1, registers, registerNames, instructions):
    inst = 'ROR'
    #check = False
    #displacement = operand2
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    temp = registers[reg1][15]
    registers[reg1] =  registers[reg1][1:] + [registers[reg1][0]]
    registers[reg1][0] = temp



def exchange(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'ROL'
    #check = False
    machineCode = ''
    
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    temp = registers[reg1]
    registers[reg1] = registers[reg2]
    registers[reg2] = temp
    #return machineCode


# In[12]:

def bitwise_and(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'AND'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    print("left")
    print(left)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right,2)
    
    print(right)
    resultT = left & right
    resultT = bin(resultT)
    print(resultT)

    resultT = str(resultT)
    resultT = resultT[2:]
    
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result

def bitwise_or(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'OR'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    print("left")
    print(left)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right,2)
    
    print(right)
    resultT = left | right
    resultT = bin(resultT)
    print(resultT)

    resultT = str(resultT)
    resultT = resultT[2:]
    
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    
    
def bitwise_xor(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'XOR'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    print("left")
    print(left)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right,2)
    
    print(right)
    resultT = left ^ right
    resultT = bin(resultT)
    print(resultT)

    resultT = str(resultT)
    resultT = resultT[2:]
    
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result


def bitwise_not(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'NOT'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    
    left = ''
    value = registers[reg1]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    resultT = ~left
    resultT = bin(resultT)
    print(resultT)
    resultT = str(resultT)
    resultT = resultT[3:]
    print(resultT)
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    
def multiply(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'MUL'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    print("left")
    print(left)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right,2)
    
    print(right)
    resultT = left * right
    resultT = bin(resultT)
    print(resultT)

    resultT = str(resultT)
    resultT = resultT[2:]
    
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    
def divide(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'DIV'
    #check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg1]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left,2)
    print("left")
    print(left)
    value = registers[reg2]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right,2)
    
    print(right)
    resultT = left // right
    print(resultT)
    resultT = bin(resultT)
    print(resultT)

    resultT = str(resultT)
    resultT = resultT[2:]
    
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers[reg1] = result
    
def compare(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'CMP'
    check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand2:
            reg2 = bin(i)
            reg2 = reg2[2:]
            if len(reg2) == 1:
                machineCode += '00' + reg2
            elif len(reg2) == 2:
                machineCode += '0' + reg2
            else:
                machineCode += reg2
                break
    machineCode += ' '
    left = ''
    right = ''
    value = registers[reg2]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left, 2)
    value = registers[reg1]
    for i in range(len(value)):
        right += str(value[i])
    right = int(right, 2)
    #FR = [OF, CF, ZF, SF]
    if (left == right):
        registers['111'][1] = 0
        registers['111'][2] = 1
        registers['111'][3] = 0
    elif ( left < right):
        registers['111'][1] = 1
        registers['111'][2] = 0
        registers['111'][3] = 1
    else:
        registers['111'][1] = 0
        registers['111'][2] = 0
        registers['111'][3] = 0
    return check

def jump(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'JMP'
    check = False
    machineCode = ''
    for instruction in instructions:
        if instruction == inst:
            a = instructions[instruction]
            if len(a) == 1:
                machineCode = '000' + str(a)
            elif len(a) == 2:
                machineCode = '00' + str(a)
            elif len(a) == 3:
                machineCode = '0' + str(a)
            else:
                machineCode = str(a)
            break
    machineCode += ' '
    for i in range(len(registerNames)):
        if registerNames[i] == operand1:
            reg1 = bin(i)
            reg1 = reg1[2:]
            if len(reg1) == 1:
                machineCode += '00' + reg1
            elif len(reg1) == 2:
                machineCode += '0' + reg1
            else:
                machineCode += reg1
                break
    machineCode += ' '
    left = ''
    value = registers[reg1]
    for i in range(len(value)):
        left += str(value[i])
    left = int(left, 2)
    resultT = bin(left)
    resultT = resultT[2:]
    result = []
    for i in range(len(resultT)):
        num = int(resultT[i])
        result.append(num)
    while len(result) < 16:
        result.insert(0,0)
    registers['110'] = result
    return check


        
def main():
    machineCode = ''
    registers = {}
    memoryLocations = {}
    instructions = {}
    registerLower = ['AL', 'BL', 'CL', 'DL', 'EL', 'FL', 'GL']
    registerHigher = ['AH', 'BH', 'CH', 'DH', 'EH', 'FH', 'GH']
    registerNames = ['AX', 'BX', 'CX', 'DX', 'EX', 'FX', 'IP', 'FR']
    registersInit(registers)
    memoryInit(memoryLocations)
    instructionsInit(instructions)
    memoryLocations['1111'] = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    while True:
        instruction = input('Enter Assembly Instruction With Space In Between Each Word')
        instruction = instruction.split(' ')
        if len(instruction) == 3:
            inst = instruction[0]
            operand1 = instruction[1]
            operand2 = instruction[2]
            if inst == 'MOV':
                if (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 in registerLower or operand2 in registerHigher or operand2 in registerNames):
                    if (operand1 in registerNames and operand2 in registerNames) or (operand1 in registerLower and operand2 in registerLower) or (operand1 in registerHigher and operand2 in registerHigher):
                        registerDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                        machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    else:
                        print("operand donot match")
                elif (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 not in registerNames or operand2 not in registerLower or operand2 not in registerHigher) and operand2[0] != '[':
                    check = immediate(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    if check == False:
                        print("Operand is out of range")
                    else:
                       machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                elif operand1 in registerNames and operand2[0] == '[' and operand2[1:3] in registerNames and operand2[3] != '+':
                    operand2 = operand2[1:3]
                    registerIndirectMemToReg(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    operand2 = '[' + operand2 + ']'
                elif operand1[0] == '[' and operand1[1:3] in registerNames and operand2 in registerNames:
                    operand1 = operand1[1:3]
                    registerIndirectRegToMem(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    operand1 = '[' + operand1 + ']'
                elif operand1[0] == '[' and operand1[1:3] not in registerNames and operand2 in registerNames:
                    check = memoryDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    if check == False:
                        print("memory address is out of range")
                    else:
                        machineCode  = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                elif operand1 in registerNames and operand2[0] == '[' and operand2[3] == '+':
                    check = memoryRelative(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    if check == False:
                        print('Enter Valid Relative Address')
                        continue
                    else:
                        machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'ADD':
                check = add(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    print("The Value is greater than 16 bits")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "CMP":
                compare(inst, operand1, operand2, registers, registerNames, instructions)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "MUL":
                multiply(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "DIV":
                divide(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "AND":
                bitwise_and(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "OR":
                bitwise_or(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "XOR":
                bitwise_xor(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SUB':
                check = sub(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    print("The Value is out of the allowed range")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SHRD':
                check = shift_right_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    print("The Displacement Value is greater than 16 bits")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SHLD':
                check = shift_left_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    print("The Displacement Value is greater than 16 bits")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'XCHG':
                if (operand1 in registerNames and operand2 in registerNames): 
                    exchange(inst, operand1, operand2, registers, registerNames, instructions)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                else:
                    print("Operands donot match")
        elif len(instruction) == 2:
            inst = instruction[0]
            operand1 = instruction[1]
            if inst == 'DEC':
                check = dec(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    print("The Value is less than zero ")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'INC':
                check = inc(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    print("The Value is greater than 16 bits")
                    continue
                else:
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SHR':
                    shift_right(inst, operand1, registers, registerNames, instructions)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SHL':
                    shift_left(inst, operand1, registers, registerNames, instructions)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'NOT':
                    bitwise_not(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'JMP':
                jump(inst, operand1, operand2, registers, registerNames, instructions)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
        elif len(instruction) == 1:
            inst = instruction[0]
            if inst == 'PUSH':
                push(inst, registers, registerNames, instructions, memoryLocations)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'POP':
                pop(inst, registers, registerNames, instructions, memoryLocations)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
        print(inst, operand1, operand2)
        print(machineCode)
        displayContents(registerNames, registers, memoryLocations)
        choice = input('Do you want to continue? Press Y or N')
        if choice == 'N' or choice == 'n':
            break


# In[4]:


main()

#16 registers AX, BX, CX, DX, EX, FX and their 8 bit counterparts and 1 flag register FR and IP regitser
#16 Memory Locations
#All outputs in Binary
#Currently 6 Mov Instructions
#MOV Rm Rn 
#MOV Rm #Imme 
#MOV Rm [Rn] 
#MOV [Rm] Rn 
#MOV [#DecValue] Rm
#MOV Rm [Rn+#DecValue]
#PUSH 
#POP
#SHL Rm
#SHR Rm 
#SHRD Rm #displacement
#SHLD Rm #displacement
#ADD Rm Rn
#SUB Rm Rn
#INC Rm
#DEC Rm
#XCHG Rm Rn
#MUL Rm Rn
#DIV Rm Rn
#ROR Rm
#ROL Rm
#AND Rm
#OR Rm
#XOR Rm
#NOT Rm
#JMP Rm
#CMP Rm Rn



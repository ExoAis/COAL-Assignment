from tkinter import *
from tkinter import messagebox

memory = 0
registers = 0
ALU = 0
count = 0

def registersInit(registers):
    for i in range(0, 7):
        reg = bin(i)
        reg = str(reg)
        reg = reg[2:]
        li = []
        if i == 1:
            registers[reg] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            continue
        for j in range(0, 16):
            li.append(0)
        registers[reg] = li
    registers['111'] = [0, 1, 1, 0]

def memoryInit(memoryLocations):
    for i in range(0, 16):
        mem = bin(i)
        mem = str(mem)
        mem = mem[2:]
        li = []
        for i in range(0, 16):
            li.append(0)
        memoryLocations[mem] = li

def instructionsInit(instructions):
    for i in range(0, 16):
        ins = bin(i)
        ins = ins[2:]
        if i < 6:
            instructions['MOV' + str(i)] = ins
        elif i == 7:
            instructions['ADD'] = ins
        elif i == 8:
            instructions['SUB'] = ins
        elif i == 9:
            instructions['INC'] = ins
        elif i == 10:
            instructions['DEC'] = ins
        elif i == 11:
            instructions['POP'] = ins
        elif i == 12:
            instructions['PUSH'] = ins
        elif i == 13:
            instructions['SHR'] = ins
        elif i == 14:
            instructions['SHL'] = ins
        elif i == 15:
            instructions['SHRD'] = ins
        elif i == 16:
            instructions['SHLD'] = ins
        elif i == 16:
            instructions['XCHG'] = ins

def registerDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'MOV0'
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
    if operand1 in registerNames and operand2 in registerNames:
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
        value = registers[reg2]
        registers[reg1] = value
    elif operand1 in registerLower and operand2 in registerLower:
        for i in range(len(registerLower)):
            if registerLower[i] == operand1:
                idx1 = i
            elif registerLower[i] == operand2:
                idx2 = i
        operand1 = registerNames[idx1]
        operand2 = registerNames[idx2]
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
        value = registers[reg2]
        value = value[8:]
        registers[reg1][8:] = value.copy()
    elif operand1 in registerHigher and operand2 in registerHigher:
        for i in range(len(registerHigher)):
            if registerHigher[i] == operand1:
                idx1 = i
            elif registerHigher[i] == operand2:
                idx2 = i
        operand1 = registerNames[idx1]
        operand2 = registerNames[idx2]
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
        value = registers[reg2]
        value = value[0:8]
        registers[reg1][0:8] = value.copy()
    #return machineCode

def immediate(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'MOV1'
    machineCode = ''
    check = False
    operand2 = int(operand2)
    #print(operand2)
    operand2 = bin(operand2)
   #print(operand2)
    operand2 = operand2[2:]
   #print(operand2)
    if len(operand2) > 16:
       return check
    higher, lower = binaryDirect(operand2)
   #print(higher)
   #print(lower)
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
    if operand1 in registerNames and len(operand2) <= 16:
        for i in range(len(registerNames)):
            if registerNames[i] == operand1:
                idx1 = i
                break
        operand1 = registerNames[idx1]
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
        machineCode += higher + ' ' + lower
        immediate = higher + lower
        immediate = list(immediate)
       #print(immediate)
        immediate = [eval(i) for i in immediate]
       #print(immediate)
        registers[reg1] = immediate.copy()
        check = True
    elif operand1 in registerLower and len(operand2) < 9:
        for i in range(len(registerLower)):
            if registerLower[i] == operand1:
                idx1 = i
                break
        operand1 = registerNames[idx1]
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
        machineCode += higher + ' ' + lower
        immediate = lower
        immediate = list(immediate)
        immediate = [eval(i) for i in immediate]
        registers[reg1][8:] = immediate.copy()
        check = True
    elif operand1 in registerHigher and len(operand2) < 9:
        for i in range(len(registerHigher)):
            if registerHigher[i] == operand1:
                idx1 = i
                break
        operand1 = registerNames[idx1]
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
        machineCode += higher + ' ' + lower
        immediate = lower
        immediate = list(immediate)
        immediate = [eval(i) for i in immediate]
        registers[reg1][0:8] = immediate.copy()
        check = True
    return check

def registerIndirectMemToReg(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames):
    inst = 'MOV2'
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
    value = str(registers[reg2][12]) + str(registers[reg2][13]) + str(registers[reg2][14]) + str(registers[reg2][15])
    value = int(value)
    value = str(value)
    value = memoryLocations[value]
    registers[reg1] = value
    #return machineCode

def registerIndirectRegToMem(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames):
    inst = 'MOV3'
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
    value = registers[reg2]
    mem = str(registers[reg1][12]) + str(registers[reg1][13]) + str(registers[reg1][14]) + str(registers[reg1][15])
    mem = int(mem)
    mem = str(mem)
    memoryLocations[mem] = value
    #return machineCode

def memoryDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames):
    check = False
    machineCode = ''
    if len(operand1) == 3:
        operand1 = operand1[1]
    elif len(operand1) == 4:
        operand1 = operand1[1:3]
    operand1 = int(operand1)
    operand1 = bin(operand1)
    operand1 = operand1[2:]
    if len(operand1) > 4:
        return check
    inst = 'MOV4'
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
    machineCode += ' ' + operand1 + ' '
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
    value = registers[reg2]
    memoryLocations[operand1] = value
    check = True
    return check

def memoryRelative(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames):
    check = False
    inst = 'MOV5'
    machineCode = ''
    relative = operand2[4:len(operand2) - 1]
    relative = int(relative)
    operand2 = operand2[1:3]
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
    value = str(registers[reg2][12]) + str(registers[reg2][13]) + str(registers[reg2][14]) + str(registers[reg2][15])
    value = int(value, 2)
    if value + relative > 15:
        return check
    check = True
    mem = value + relative
    mem = bin(mem)
    mem = mem[2:]
    value = memoryLocations[mem]
    registers[reg1] = value
    return check

def add(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'ADD'
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
    resultT = left + right
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

def binaryDirect(operand2):
    if len(operand2) == 1:
        higher = '00000000'
        lower = '0000000' + operand2
    elif len(operand2) == 2:
        higher = '00000000'
        lower = '000000' + operand2
    elif len(operand2) == 3:
        higher = '00000000'
        lower = '00000' + operand2
    elif len(operand2) == 4:
        higher = '00000000'
        lower = '0000' + operand2
    elif len(operand2) == 5:
        higher = '00000000'
        lower = '000' + operand2
    elif len(operand2) == 6:
        higher = '00000000'
        lower = '00' + operand2
    elif len(operand2) == 7:
        higher = '00000000'
        lower = '0' + operand2
    elif len(operand2) == 8:
        higher = '00000000'
        lower = operand2
    elif len(operand2) == 9:
        higher = '0000000' + operand2[0]
        lower = operand2[1:]
    elif len(operand2) == 10:
        higher = '000000' + operand2[0:2]
        lower = operand2[2:]
    elif len(operand2) == 11:
        higher = '00000' + operand2[0:3]
        lower = operand2[3:]
    elif len(operand2) == 12:
        higher = '0000' + operand2[0:4]
        lower = operand2[4:]
    elif len(operand2) == 13:
        higher = '000' + operand2[0:5]
        lower = operand2[5:]
    elif len(operand2) == 14:
        higher = '00' + operand2[0:6]
        lower = operand2[6:]
    elif len(operand2) == 15:
        higher = '0' + operand2[0:7]
        lower = operand2[7:]
    else:
        higher = operand2[0:8]
        lower = operand2[8:]
    return higher, lower

def displayContents(registerNames, registers, memoryLocations):
    for i in range(8):
        reg = bin(i)
        print(registerNames[i], ':', registers[reg[2:]])
    for i in range(16):
        reg = bin(i)
        print(i, ':', memoryLocations[reg[2:]])

def generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher, instruction):
    machineCode = ""
    if len(instruction) == 3:        
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
                operand2 = int(operand2[4:len(operand2) - 1])
                operand2 = bin(operand2)
                operand2 = operand2[2:]
                higher, lower = binaryDirect(operand2)
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
        elif inst == "AND":
            print("and")
    elif len(instruction) == 4:
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
                
    elif len(instruction) == 2:
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
    elif len(instruction) == 1:
        inst = inst[0]
        if inst == 'PUSH':
            machineCode = "001000"
        elif inst == 'POP':
            machineCode = "001001"
            
    return machineCode 

def calculateCycles(instruction, registerLower, registerHigher, registerNames):
    globals()['registers'] = 0
    globals()['memory'] = 0
    globals()['ALU'] = 0
    instructionNames = ''
    if len(instruction) == 3:
        inst = instruction[0]
        op1 = instruction[1]
        op2 = instruction[2]
        if instruction[0] == 'MOV':
            if (instruction[1] in registerNames and instruction[2] in registerNames) or (instruction[1] in registerLower and instruction[2] in registerLower) or (instruction[1] in registerHigher and instruction[2] in registerHigher):
                instructionNames = 'Fetch, Decode'
                return 2, instructionNames
            elif (instruction[1] in registerNames or instruction[1] in registerLower or instruction[1] in registerHigher) and (op2 not in registerNames or op2 not in registerLower or op2 not in registerHigher) and (op2[0] != '['):
                instructionNames = 'Fetch, Decode'
                return 2, instructionNames
            elif (instruction[1] in registerNames) and (op2[1:3] in registerNames) and (op2[0] == '[') and (op2[3] != '+'):
                globals()['registers'] = 1
                instructionNames = 'Fetch, Decode, Load'
                return 3, instructionNames
            elif (op1[0] == '[') and (op1[1:3] in registerNames) and (op2 in registerNames):
                globals()['memory'] = 1
                instructionNames = 'Fetch, Decode, Store'
                return 3, instructionNames
            elif (op1[0] == '[') and (op1[1:3] not in registerNames) and (op2 in registerNames):
                globals()['memory'] = 1
                instructionNames = 'Fetch, Decode, Store'
                return 3, instructionNames
            elif op1 in registerNames and op2[0] == '[' and op2[3] == '+':
                globals()['memory'] = 1
                globals()['ALU'] = 1
                instructionNames = 'Fetch, Decode, Execute, Load'
                return 4, instructionNames
        elif instruction[0] == 'ADD' or instruction[0] == 'SUB':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'XCHG':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'SHRD' or instruction[0] == 'SHLD':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'MUL' or instruction[0] == 'DIV' or instruction[0] == 'AND' or instruction[0] == 'OR' or instruction[0] == 'XOR' or instruction[0] == 'NOT' or instruction[0] == 'CMP':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
    elif len(instruction) == 2:
        inst = instruction[0]
        op1 = instruction[1]
        if instruction[0] == 'INC' or instruction[0] == 'DEC' or instruction[0] == 'SHR' or instruction[0] == 'SHL':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'JMP' or instruction[0] == 'ROR' or instruction[0] == 'ROL':
            globals()['ALU'] = 1
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
    elif len(instruction) == 1:
        inst = instruction[0]
        if instruction[0] == 'POP':
            globals()['memory'] = 1
            instructionNames = 'Fetch, Decode, Store'
            return 3, instructionNames
        elif instruction[0] == 'PUSH':
            globals()['registers'] = 1
            instructionNames = 'Fetch, Decode, Load'
            return 3, instructionNames

def displayContents(cycles, instructionNames, instruction, machineCode, registerNames, registers, memoryLocations, operand1 = 'None', operand2 = 'None', ):
    global root2
    root2 = Tk()
    root2.title('Outputs')
    if globals()['registers'] == 0 and globals()['memory'] == 0 and globals()['ALU'] == 0:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold')) .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold')).grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold')).grid(row = 2, column = 2, sticky = W)
    elif globals()['memory'] == 0 and globals()['ALU'] == 0:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold'), bg = 'red') .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold')).grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold')).grid(row = 2, column = 2, sticky = W)
    elif globals()['memory'] == 0 and globals()['registers'] == 0:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold')) .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold')).grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 2, column = 2, sticky = W)
    elif globals()['ALU'] == 0 and globals()['registers'] == 0:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold')) .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold')).grid(row = 2, column = 2, sticky = W)
    elif globals()['memory'] == 1 and globals()['ALU'] == 1:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold')) .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 2, column = 2, sticky = W)
    elif globals()['memory'] == 1 and globals()['registers'] == 1:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold'), bg = 'red') .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold')).grid(row = 2, column = 2, sticky = W)
    elif globals()['ALU'] == 1 and globals()['registers'] == 1:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold'), bg = 'red') .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold')).grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 2, column = 2, sticky = W)
    elif globals()['registers'] == 1 and globals()['memory'] == 1 and globals()['ALU'] == 1:
        label = Label(root2, text ='Registers', font=('Times New Roman',13,'bold'), bg = 'red') .grid(row = 0, column = 2, sticky = W)
        label = Label(root2, text ='Memory', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 1, column = 2, sticky = W)
        label = Label(root2, text ='ALU', font=('Times New Roman',13,'bold'), bg = 'red').grid(row = 2, column = 2, sticky = W)
    if operand2 != 'None' and operand1 != 'None':
        label = Label(root2, text = 'Instruction: ' + str(instruction[0]) + " " + str(instruction[1]) + " " + str(instruction[2]), font=('Times New Roman',13,'bold')).grid(row = 0, column = 0, sticky = W)
    elif operand1 != 'None' and operand2 == 'None':
        label = Label(root2, text ='Instruction: ' +  str(instruction[0]) + " " + str(instruction[1]), font=('Times New Roman',13,'bold')).grid(row = 0, column = 0, sticky = W)
    elif operand1 == 'None' and operand2 == 'None':
        label = Label(root2, text ='Instruction: ' +  str(instruction[0]), font=('Times New Roman',13,'bold')).grid(row = 0, column = 0, sticky = W)
    label = Label(root2, text ='Machine Code: ' +  machineCode, font=('Times New Roman',13,'bold')).grid(row = 1, column = 0, sticky = W)
    label = Label(root2, text ='Instructions Used: ' +  instructionNames, font=('Times New Roman',13,'bold')).grid(row = 0, column = 1, sticky = W)
    label = Label(root2, text ='Number of Instruction Cycles: ' +  str(cycles), font=('Times New Roman',13,'bold')).grid(row = 1, column = 1, sticky = W)
    label = Label(root2, text = 'REGISTERS:', font=('Times New Roman',13,'bold')).grid(row = 2, column = 0, sticky = W)
    for i in range(8):
        reg = bin(i)
        label1 = Label(root2, text = registerNames[i] + ':', font=('Times New Roman',13,'bold')).grid(row = i + 3, column = 0, sticky = W)
        label2 = Label(root2, text = str(registers[reg[2:]]), font=('Times New Roman',13,'bold')).grid(row = i + 3, column = 1, sticky = W)
    label = Label(root2, text = ' ', font=('Times New Roman',13,'bold')).grid(row = 10, column = 0, sticky = W)
    label = Label(root2, text = 'MEMORY LOCATIONS:', font=('Times New Roman',13,'bold')).grid(row = 11, column = 0, sticky = W)
    for i in range(16):
        reg = bin(i)
        label1 = Label(root2, text = str(i) + ':', font=('Times New Roman',13,'bold')).grid(row = 12 + i, column = 0, sticky = W)
        label2 = Label(root2, text = str(memoryLocations[reg[2:]]), font=('Times New Roman',13,'bold')).grid(row = 12 + i, column = 1, sticky = W)
    mainloop()

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
        instruction = str(e1.get())
        instruction = instruction.split(' ')
        cycles, instructionNames = calculateCycles(instruction, registerLower, registerHigher, registerNames)
        if len(instruction) == 3:
            inst = instruction[0]
            operand1 = instruction[1]
            operand2 = instruction[2]
            if inst == 'MOV':
                if (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 in registerLower or operand2 in registerHigher or operand2 in registerNames):
                    if (operand1 in registerNames and operand2 in registerNames) or (operand1 in registerLower and operand2 in registerLower) or (operand1 in registerHigher and operand2 in registerHigher):
                        registerDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    else:
                        msg = messagebox.showinfo("ERROR","Enter Valid Relative Address!")
                        root1.destroy()
                        mainMenu()
                        continue
                elif (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 not in registerNames or operand2 not in registerLower or operand2 not in registerHigher) and operand2[0] != '[':
                    check = immediate(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                    if check == False:
                        msg = messagebox.showinfo("ERROR","Operand is out of range")
                        root1.destroy()
                        mainMenu()
                        continue
                elif operand1 in registerNames and operand2[0] == '[' and operand2[1:3] in registerNames and operand2[3] != '+':
                    operand2 = operand2[1:3]
                    registerIndirectMemToReg(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    operand2 = '[' + operand2 + ']'
                elif operand1[0] == '[' and operand1[1:3] in registerNames and operand2 in registerNames:
                    operand1 = operand1[1:3]
                    registerIndirectRegToMem(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    operand1 = '[' + operand1 + ']'
                elif operand1[0] == '[' and operand1[1:3] not in registerNames and operand2 in registerNames:
                    check = memoryDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    if check == False:
                        msg = messagebox.showinfo("ERROR","memory address is out of range")
                        root1.destroy()
                        mainMenu()
                        continue
                elif operand1 in registerNames and operand2[0] == '[' and operand2[3] == '+':
                    check = memoryRelative(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    if check == False:
                        msg = messagebox.showinfo("ERROR","Enter Valid Relative Address")
                        root1.destroy()
                        mainMenu()
                        continue
            elif inst == 'ADD':
                check = add(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is greater than 16 bits")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == "CMP":
                compare(inst, operand1, operand2, registers, registerNames, instructions)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "MUL":
                multiply(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "DIV":
                divide(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "AND":
                bitwise_and(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "OR":
                bitwise_or(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == "XOR":
                bitwise_xor(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'SUB':
                check = sub(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is out of the allowed range")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHRD':
                check = shift_right_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Displacement Value is greater than 16 bits")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHLD':
                check = shift_left_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Displacement Value is greater than 16 bits")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'XCHG':
                if (operand1 in registerNames and operand2 in registerNames): 
                    exchange(inst, operand1, operand2, registers, registerNames, instructions)
                else:
                    print("")
                    msg = messagebox.showinfo("ERROR","Operands do not match")
                    root1.destroy()
                    mainMenu()
                    continue
            root1.destroy()
            machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher, instruction)
            displayContents(cycles, instructionNames, instruction, machineCode, registerNames, registers, memoryLocations)
        elif len(instruction) == 2:
            inst = instruction[0]
            operand1 = instruction[1]
            if inst == 'DEC':
                check = dec(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is less than zero")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'INC':
                check = inc(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is greater than 16 bits")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHR':
                    shift_right(inst, operand1, registers, registerNames, instructions)
            elif inst == 'SHL':
                    shift_left(inst, operand1, registers, registerNames, instructions)
            elif inst == 'NOT':
                    bitwise_not(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            elif inst == 'JMP':
                jump(inst, operand1, operand2, registers, registerNames, instructions)
            elif inst == 'JMP':
                jump(inst, operand1, operand2, registers, registerNames, instructions)
                machineCode = generateMachineCode(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
            root1.destroy()
            machineCode = generateMachineCode(inst, operand1, -1, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher, instruction)
            displayContents(cycles, instructionNames, instruction, machineCode, registerNames, registers, memoryLocations)
        elif len(instruction) == 1:
            inst = instruction[0]
            if inst == 'PUSH':
                push(inst, registers, registerNames, instructions, memoryLocations)
            elif inst == 'POP':
                pop(inst, registers, registerNames, instructions, memoryLocations)
            root1.destroy()
            machineCode = generateMachineCode(inst, -1, -1, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher, instruction)
            displayContents(cycles, instructionNames, instruction, machineCode, registerNames, registers, memoryLocations)
        mainMenu()

def mainMenu():
    global root1
    global e1
    root1 = Tk()
    root1.title("8086 Simulator")
    label = Label(root1,text="Enter an Instruction:", font=('Times New Roman',17,'bold')).grid(row=0,column=0)
    e1 = Entry(root1, bg = 'Black', fg = 'white', font=('Times New Roman',17,'bold'))
    e1.grid(row=0,column=1)
    button = Button(root1,text="Enter", width = 12, height = 3, font=('Times New Roman',17,'bold'), command = main).grid(row=3,column=0,columnspan=3, sticky = W + E)
    exit = Button(root1, text = "Exit", width = 12, height = 3, font=('Times New Roman',17,'bold'), command = root1.destroy).grid(row = 5, column = 0, columnspan = 4, sticky = W + E)
    mainloop()

mainMenu()

#16 registers AX, BX, CX, DX, EX, FX, GX and their 8 bit counterparts and 1 flag register FR
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



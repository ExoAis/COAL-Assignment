from tkinter import *
from tkinter import messagebox

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
    return machineCode
def immediate(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher):
    inst = 'MOV1'
    machineCode = ''
    operand2 = int(operand2)
    operand2 = bin(operand2)
    operand2 = operand2[2:]
    higher, lower = binaryDirect(operand2)
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
    if operand1 in registerNames and len(operand2) < 16:
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
        immediate = [eval(i) for i in immediate]
        registers[reg1] = immediate.copy()
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
    return machineCode
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
    return machineCode
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
    return machineCode
def memoryDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames):
    if len(operand1) == 3:
        operand1 = operand1[1]
    elif len(operand1) == 4:
        operand1 = operand1[1:3]
    operand1 = int(operand1)
    operand1 = bin(operand1)
    operand1 = operand1[2:]
    inst = 'MOV4'
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
    return machineCode
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
        return machineCode, check
    check = True
    mem = value + relative
    mem = bin(mem)
    mem = mem[2:]
    value = memoryLocations[mem]
    registers[reg1] = value
    return machineCode, check
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
        return machineCode, check
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
    return machineCode, check
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
        return machineCode, check
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
    return machineCode, check
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
        return machineCode, check
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
    return machineCode, check
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
        return machineCode, check
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
    return machineCode, check
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
    return machineCode
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
    return machineCode
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
    return machineCode
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
        return machineCode, check
    check = True
    for i in range(int(displacement)):
        registers[reg1] = [registers[reg1][-1]] + registers[reg1][:-1]
        registers[reg1][0] = 0
    return machineCode, check
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
    return machineCode
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
        return machineCode, check
    check = True
    for i in range(int(displacement)):
        registers[reg1] =  registers[reg1][1:] + [registers[reg1][0]]
        registers[reg1][15] = 0
    return machineCode, check
def exchange(inst, operand1, operand2, registers, registerNames, instructions):
    inst = 'XCHG'
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
    return machineCode
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
        higher = '000000' + operand2[0:1]
        lower = operand2[2:]
    elif len(operand2) == 11:
        higher = '00000' + operand2[0:2]
        lower = operand2[3:]
    elif len(operand2) == 12:
        higher = '0000' + operand2[0:3]
        lower = operand2[4:]
    elif len(operand2) == 13:
        higher = '000' + operand2[0:4]
        lower = operand2[5:]
    elif len(operand2) == 14:
        higher = '00' + operand2[0:5]
        lower = operand2[6:]
    elif len(operand2) == 15:
        higher = '0' + operand2[0:6]
        lower = operand2[7:]
    else:
        higher = operand2[0:7]
        lower = operand2[8:]
    return higher, lower

def calculateCycles(instruction, registerLower, registerHigher, registerNames):
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
                instructionNames = 'Fetch, Decode, Load'
                return 3, instructionNames
            elif (op1[0] == '[') and (op1[1:3] in registerNames) and (op2 in registerNames):
                instructionNames = 'Fetch, Decode, Store'
                return 3, instructionNames
            elif (op1[0] == '[') and (op1[1:3] not in registerNames) and (op2 in registerNames):
                instructionNames = 'Fetch, Decode, Store'
                return 3, instructionNames
            elif op1 in registerNames and op2[0] == '[' and op2[3] == '+':
                instructionNames = 'Fetch, Decode, Execute, Load'
                return 4, instructionNames
        elif instruction[0] == 'ADD' or instruction[0] == 'SUB':
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'XCHG':
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
        elif instruction[0] == 'SHRD' or instruction[0] == 'SHLD':
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
    elif len(instruction) == 2:
        if instruction[0] == 'INC' or instruction[0] == 'DEC' or instruction[0] == 'SHR' or instruction[0] == 'SHL':
            instructionNames = 'Fetch, Decode, Execute'
            return 3, instructionNames
    elif len(instruction) == 1:
        if instruction[0] == 'POP':
            instructionNames = 'Fetch, Decode, Store'
            return 3, instructionNames
        elif instruction[0] == 'PUSH':
            instructionNames = 'Fetch, Decode, Load'
            return 3, instructionNames
def displayContents(cycles, instructionNames, instruction, machineCode, registerNames, registers, memoryLocations, operand1 = 'None', operand2 = 'None', ):
    global root2
    root2 = Tk()
    root2.title('Outputs')
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
    registerNames = ['AX', 'BX', 'CX', 'DX', 'EX', 'FX', 'GX', 'FR']
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
                if (operand1 in registerNames and operand2 in registerNames) or (operand1 in registerLower and operand2 in registerLower) or (operand1 in registerHigher and operand2 in registerHigher):
                    machineCode = registerDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                elif (operand1 in registerNames or operand1 in registerLower or operand1 in registerHigher) and (operand2 not in registerNames or operand2 not in registerLower or operand2 not in registerHigher) and operand2[0] != '[':
                    machineCode = immediate(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames, registerLower, registerHigher)
                elif operand1 in registerNames and operand2[0] == '[' and operand2[1:3] in registerNames and operand2[3] != '+':
                    operand2 = operand2[1:3]
                    machineCode = registerIndirectMemToReg(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    operand2 = '[' + operand2 + ']'
                elif operand1[0] == '[' and operand1[1:3] in registerNames and operand2 in registerNames:
                    operand1 = operand1[1:3]
                    machineCode = registerIndirectRegToMem(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    operand1 = '[' + operand1 + ']'
                elif operand1[0] == '[' and operand1[1:3] not in registerNames and operand2 in registerNames:
                    machineCode = memoryDirect(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                elif operand1 in registerNames and operand2[0] == '[' and operand2[3] == '+':
                    machineCode, check = memoryRelative(inst, operand1, operand2, registers, memoryLocations, instructions, registerNames)
                    if check == False:
                        msg = messagebox.showinfo("ERROR","Enter Valid Relative Address!")
                        root1.destroy()
                        mainMenu()
                        continue
            elif inst == 'ADD':
                machineCode, check = add(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is greater than 16 bits!")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SUB':
                machineCode, check = sub(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is out of the allowed range!")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHRD':
                machineCode, check = shift_right_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Displacement Value is greater than 16 bits!")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHLD':
                machineCode, check = shift_left_by_displacement(inst, operand1, operand2, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Displacement Value is greater than 16 bits!")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'XCHG':
                machineCode = exchange(inst, operand1, operand2, registers, registerNames, instructions)
            root1.destroy()
            displayContents(cycles, instructionNames, instruction, machineCode,  registerNames, registers, memoryLocations, operand1, operand2)
        elif len(instruction) == 2:
            inst = instruction[0]
            operand1 = instruction[1]
            if inst == 'DEC':
                machineCode, check = dec(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is less than zero!")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'INC':
                machineCode, check = inc(inst, operand1, registers, registerNames, instructions)
                if check == False:
                    msg = messagebox.showinfo("ERROR","The Value is greater than 16 bits")
                    root1.destroy()
                    mainMenu()
                    continue
            elif inst == 'SHR':
                    machineCode = shift_right(inst, operand1, registers, registerNames, instructions)
            elif inst == 'SHL':
                    machineCode = shift_left(inst, operand1, registers, registerNames, instructions)
            root1.destroy()
            displayContents(cycles, instructionNames, instruction, machineCode,  registerNames, registers, memoryLocations, operand1)
        elif len(instruction) == 1:
            inst = instruction[0]
            if inst == 'PUSH':
                machineCode = push(inst, registers, registerNames, instructions, memoryLocations)
            elif inst == 'POP':
                machineCode = pop(inst, registers, registerNames, instructions, memoryLocations)
            root1.destroy()
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


# 6 registers AX, BX, CX, DX, EX, FX, GX and their 8 bit counterparts and 1 flag register FR<br>
# 6 Memory Locations<br>
# ll outputs in Binary<br>
# Currently 6 Mov Instructions<br>
# MOV Rm Rn <br>
# MOV Rm #Imme <br>
# MOV Rm [Rn] <br>
# MOV [Rm] Rn <br>
# MOV [#DecValue] Rm<br>
# MOV Rm [Rn+#DecValue]<br>
# PUSH <br>
# POP<br>
# SHL Rm<br>
# SHR Rm <br>
# SHRD Rm #displacement<br>
# SHLD Rm #displacement<br>
# ADD Rm Rn<br>
# SUB Rm Rn<br>
# INC Rm<br>
# DEC Rm<br>
# XCHG Rm Rn

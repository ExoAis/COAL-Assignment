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

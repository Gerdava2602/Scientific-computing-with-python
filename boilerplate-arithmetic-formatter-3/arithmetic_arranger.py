def arithmetic_arranger(problems, result=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  operations = dict()
  i = 0
  for problem in problems:
    operands = problem.split()
    if len(operands[0]) > 4 or len(operands[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if not operands[0].isdigit() or not operands[2].isdigit():
      return "Error: Numbers must only contain digits."
    
    if operands[1] != "+" and operands[1] != "-":
      return "Error: Operator must be '+' or '-'."
    
    actual_problem = list()
    actual_problem.append(operands)
    actual_problem.append(max(len(operands[0]), len(operands[2])))
    actual_problem.append(answer(operands))
    operations[i] = actual_problem
    i += 1

  lines = list()
  for i in range(3):
      lines.append("")

  if result:
    lines.append("")

  for operation in operations.values():
    i = 0
    for operand in operation[0]:
      if i == 0:
        lines[i] += " "*(operation[1]- len(operand)+2)+operand
        lines[i] += " "*4
      elif i == 1:
        lines[i] += operand
      else:
        lines[i-1] +=" "*(operation[1]- len(operand)+1)+operand
        lines[i-1] += " "*4
      i += 1
    lines[i-1] += "-"*(operation[1]+2) + " "*4
    if result:
      lines[i] += " "*(operation[1] - len(str(operation[2])) + 2) + str(operation[2]) + " "*4
  
  return "\n".join(line.rstrip() for line in lines)

def answer(operands):
  if operands[1] == "+":
    return int(operands[0]) + int(operands[2])
  else:
    return int(operands[0]) - int(operands[2])

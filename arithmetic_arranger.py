import operator

ops = {"+": operator.add, "-": operator.sub}


def print_space(limit):
  string = ""
  for i in range(0, limit):
    string += " "
  return string


def print_bar(limit):
  string = ""
  for i in range(0, limit):
    string += "-"
  return string


def find_operator(string):
  if (string.find('+') != -1):
    operator = "+"
  elif (string.find('-') != -1):
    operator = "-"
  else:
    operator = ""
  return operator


def arithmetic_arranger(problems, solution=False):
  # string result
  arranged_problems = ""
  # top numbers
  top = []
  # bottom numbers
  bot = []
  # max lengths of problems
  max_length = []
  # operator of problems
  operator = []
  # checking whether there is multiplication or divison
  y = 0
  has_multiplication_or_division = False
  is_not_digit = False
  has_more_than_five = False
  is_more_than_four_digits = False
  for x in problems:
    if "*" in x or "/" in x:
      has_multiplication_or_division = True
      break
    operator.append(find_operator(problems[y]))
    number = problems[y].split(operator[y])
    if (not (number[0].replace(" ", "").isdigit()
             and number[1].replace(" ", "").isdigit())):
      is_not_digit = True
      break
    if len(problems) > 5:
      has_more_than_five = True
      break
    if (len(str(int(number[0]))) > 4 or len(str(int(number[1]))) > 4):
      is_more_than_four_digits = True
      break
    # print(find_operator(problems[y]))
    y += 1
  if (has_multiplication_or_division):
    arranged_problems += "Error: Operator must be '+' or '-'."
  elif (is_not_digit):
    arranged_problems += "Error: Numbers must only contain digits."
  elif (has_more_than_five):
    arranged_problems += "Error: Too many problems."
  elif (is_more_than_four_digits):
    arranged_problems += "Error: Numbers cannot be more than four digits."
  else:
    # iterating top numbers
    for i in range(0, len(problems)):
      operator.append(find_operator(problems[i]))
      number = problems[i].split(operator[i])
      # top number
      top.append(int(number[0]))
      # bottom number
      bot.append(int(number[1]))
      # get max length of both numbers
      max_length.append(max(len(str(top[i])), len(str(bot[i]))) + 2)
      # print space for number
      arranged_problems += print_space(max_length[i] - len(str(top[i])))
      # print number
      arranged_problems += str(top[i])
      # print space between problems
      if not (i == len(problems) - 1):
        arranged_problems += print_space(4)

    arranged_problems += "\n"

    # iterating bottom numbers
    for i in range(0, len(problems)):
      # print problem operators
      arranged_problems += operator[i]
      # print space for number (accounts for operator)
      arranged_problems += print_space(max_length[i] - len(str(bot[i])) - 1)
      # print number
      arranged_problems += str(bot[i])
      # print space between problems
      if not (i == len(problems) - 1):
        arranged_problems += print_space(4)

    arranged_problems += "\n"

    # iterating bars
    for i in range(0, len(problems)):
      # print bars
      arranged_problems += print_bar(max_length[i])
      # print space between problems
      if not (i == len(problems) - 1):
        arranged_problems += print_space(4)

    if solution:
      arranged_problems += "\n"

      # iterating results
      for i in range(0, len(problems)):
        # calculating problem results
        result = ops[operator[i]](top[i], bot[i])
        # print space for result
        arranged_problems += print_space(max_length[i] - len(str(result)))
        # print result number
        arranged_problems += str(result)
        # print space between problems
        if not (i == len(problems) - 1):
          arranged_problems += print_space(4)

  return arranged_problems

# =========================
# AHAD LANGUAGE INTERPRETER
# =========================


# CREATE DEFAULT FILE

default_code = """

store a = 10

store b = 20

store c = add(a,b)

show(c)

show(c + 100)

"""


# CREATE program.ahad FILE

file = open("program.ahad", "w")

file.write(default_code)

file.close()



# =========================
# OPEN FILE
# =========================

file = open("program.ahad", "r")

lines = file.readlines()



# =========================
# VARIABLES
# =========================

variables = {}



# =========================
# PROCESS EACH LINE
# =========================

for i in range(len(lines)):

    line = lines[i].strip()



    # IGNORE EMPTY LINE

    if line == "":

        continue



    # =========================
    # STORE COMMAND
    # =========================

    if line.startswith("store"):

        line = line.replace("store", "").strip()

        parts = line.split("=")

        var_name = parts[0].strip()

        value_part = parts[1].strip()



        # =========================
        # ADD FUNCTION SUPPORT
        # =========================

        if value_part.startswith("add"):

            content = value_part[4:-1]

            nums = content.split(",")

            a = eval(nums[0], {}, variables)

            b = eval(nums[1], {}, variables)

            value = a + b



        else:

            value = eval(value_part, {}, variables)



        variables[var_name] = value



    # =========================
    # SHOW COMMAND
    # =========================

    elif line.startswith("show"):

        content = line[5:-1]

        result = eval(content, {}, variables)

        print(result)



    # =========================
    # ADD COMMAND DIRECT OUTPUT
    # =========================

    elif line.startswith("add"):

        content = line[4:-1]

        nums = content.split(",")

        a = eval(nums[0], {}, variables)

        b = eval(nums[1], {}, variables)

        print(a + b)



    # =========================
    # ROUND COMMAND
    # =========================

    elif line.startswith("round"):

        count = int(line[6:-1])

        next_line = lines[i + 1].strip()



        for j in range(count):

            if next_line.startswith("show"):

                content = next_line[5:-1]

                result = eval(content, {}, variables)

                print(result)



    # =========================
    # CHECK COMMAND
    # =========================

    elif line.startswith("check"):

        condition = line[6:-1]

        next_line = lines[i + 1].strip()



        if eval(condition, {}, variables):

            if next_line.startswith("show"):

                content = next_line[5:-1]

                result = eval(content, {}, variables)

                print(result)



    # =========================
    # ASK COMMAND
    # =========================

    elif line.startswith("ask"):

        var_name = line[4:-1]

        value = input(f"{var_name}: ")

        variables[var_name] = value



    # =========================
    # UNKNOWN COMMAND
    # =========================

    else:

        print("Unknown Command:", line)

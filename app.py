import streamlit as st


# PAGE CONFIG

st.set_page_config(

    page_title="Ahad Browser IDE",

    page_icon="🚀",

    layout="wide"
)



# TITLE

st.title("🚀 Ahad Browser IDE")

st.markdown("### Write and Run Your Own Programming Language")



# COMMANDS

commands = [

    "store",
    "show()",
    "add()",
    "round()",
    "check()"

]



# SIDEBAR

st.sidebar.title("📚 Ahad Commands")

for cmd in commands:

    st.sidebar.write(cmd)



# DEFAULT CODE

default_code = """

store health = 100

store damage = 20

show(health)

show(health - damage)

add(10,20)

round(3)
show("Attack")

check(health > 50)
show("Strong")

"""



# CODE EDITOR

code = st.text_area(

    "📝 Write Ahad Code",

    value=default_code,

    height=400

)



# RUN BUTTON

if st.button("▶ Run Ahad Code"):



    # SAVE FILE

    file = open("program.ahad", "w")

    file.write(code)

    file.close()



    # READ FILE

    file = open("program.ahad", "r")

    lines = file.readlines()



    # VARIABLES

    variables = {}



    # OUTPUT

    output = []



    # INTERPRETER

    for i in range(len(lines)):

        line = lines[i].strip()



        # IGNORE EMPTY LINES

        if line == "":

            continue



        # =========================
# STORE COMMAND
# =========================

if line.startswith("store"):

    line = line.replace("store", "").strip()

    parts = line.split("=")

    var_name = parts[0].strip()

    value_part = "=".join(parts[1:]).strip()



    # =========================
    # ADD FUNCTION
    # =========================

    if value_part.startswith("add"):

        content = value_part[4:-1]

        nums = content.split(",")

        a = eval(nums[0].strip(), {}, variables)

        b = eval(nums[1].strip(), {}, variables)

        value = a + b



    else:

        try:

            value = eval(value_part, {}, variables)

        except:

            value = value_part



    variables[var_name] = value


        # =========================
        # SHOW
        # =========================

        elif line.startswith("show"):

            content = line[5:-1]

            result = eval(content, {}, variables)

            output.append(str(result))



        # =========================
        # ADD
        # =========================

        elif line.startswith("add"):

            content = line[4:-1]

            nums = content.split(",")

            a = eval(nums[0], {}, variables)

            b = eval(nums[1], {}, variables)

            output.append(str(a + b))



        # =========================
        # ROUND
        # =========================

        elif line.startswith("round"):

            count = int(line[6:-1])

            next_line = lines[i + 1].strip()



            for j in range(count):

                if next_line.startswith("show"):

                    content = next_line[5:-1]

                    result = eval(content, {}, variables)

                    output.append(str(result))



        # =========================
        # CHECK
        # =========================

        elif line.startswith("check"):

            condition = line[6:-1]

            next_line = lines[i + 1].strip()



            if eval(condition, {}, variables):

                if next_line.startswith("show"):

                    content = next_line[5:-1]

                    result = eval(content, {}, variables)

                    output.append(str(result))



        # =========================
        # UNKNOWN COMMAND
        # =========================

        else:

            output.append("Unknown Command: " + line)



    # SHOW OUTPUT

    st.subheader("⚡ Output")


    for item in output:

        st.code(item)

#!/usr/bin/env python3

import os
import random


# get a list of all global variables and generate GDB commands to get values
def get_global(candidate_code):
    print("GET GLOBAL VARIABLE INFO")
    test = iter(candidate_code.splitlines())
    line_counter = 0
    global_definitions = False
    global_variables = []
    for code_line in test:
        # start global variable definitions
        if(code_line == "/* --- GLOBAL VARIABLES --- */"):
            global_definitions = True
        # end global variable definitions
        if(code_line == "/* --- FORWARD DECLARATIONS --- */"):
            break
        # check global definition
        if(global_definitions):
            tokens = code_line.split()
            if not (tokens == []) and not (tokens[2] == "GLOBAL"):
                # check that variable is not a pointer
                if(not (tokens[2][0] == "*")):
                    # add to the variables list
                    global_variables.append(tokens[2])
    

    # print list of global variables
    gdb_global = ""
    for var in global_variables:
        gdb_global = gdb_global + "\nprint " + var
    return gdb_global, global_variables
            



# take code. transform to compile ready. keep track of DCEMarkers
# PRECONDITION: The markers are numbered continuously
def precompute(candidate_code):
    print("PRECOMPUTE FOR COMPILATION")
    os.system("rm tmp/gdb_log.txt tmp/candidate.c tmp/command_file.txt")
    counter = 0
    x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    gdb_commands = ""
    # get global variable info
    gdb_global, global_variables = get_global(candidate_code)
    
    # interate through all markers
    while(not x == -1):
        # complete DCEMarker to a explicit function definition
        candidate_code = candidate_code.replace("void DCEMarker{}_(void);".format(counter), "void DCEMarker{}_(void){{}}".format(counter))
        # add the marker as breakpoint
        gdb_commands = gdb_commands + "break DCEMarker{}_\n".format(counter)
        # next iteration
        counter += 1
        x = candidate_code.find("void DCEMarker{}_(void);".format(counter))
    
    # store candidate as .c file to compile
    new_candidate = open('tmp/candidate.c', 'w+')
    new_candidate.write(candidate_code)
    new_candidate.close()
    # complete gdb_commands to automatically run and log the program. \ninfo locals

    gdb_commands = gdb_commands + "set logging file gdb_log.txt\nset logging on\nr\nwhile 1\ns\ninfo locals" + gdb_global + "\ncontinue\nend"

    # store gdb_commands as .txt file to run in a gdb session
    command_file = open('tmp/command_file.txt', 'w+')
    command_file.write(gdb_commands)
    command_file.close()
    return global_variables
    


def run_gdb():
    print("COMPILE AND EXECUTE GDB AND GET LOCAL VARIABLE INFO")
    os.system("./gdb_script.sh")


def eval_log(global_variables):
    print("START: EVALUTATE LOG FILE")
    global_count = len(global_variables)
    curr_break = ""
    var_vals = {}
    
    with open("tmp/gdb_log.txt", "r") as log_file:
        # iterate through each line in the log file
        for line in log_file:
            stripped_line = line.strip()
            # split lines into list of tokens
            tokens = stripped_line.split()

            # catch breakpoint and update the current active marker
            if (len(tokens) > 0 and tokens[0] == "Breakpoint"):
                curr_break = tokens[2]
                if not (curr_break in var_vals):
                    var_vals[curr_break] = {}

            # catch variable values
            if(len(tokens) > 0 and tokens[1] == "="):
                var = tokens[0]
                val = tokens[2]
                # check if var is a global variable
                if var[0] == '$':
                    global_number = var[1:]
                    global_number = (int(global_number) - 1) % global_count
                    var = global_variables[global_number]
                
                # add new variable to dictionary
                if not (var in var_vals[curr_break]):
                    var_vals[curr_break][var] = []
                # bring value to int format
                val = int(val, 0)
                if not (val in var_vals[curr_break][var]):
                    var_vals[curr_break][var].append(val)
                
    print("END: EVALUATED LOG FILE")
    return var_vals
    
    
def unsatConditionGenerator(var_vals):
    print("GENERATE UNSATISFIABLE CONDITION WITH HELP OF VARIABLE VALUES")
    conditions = {}
    # iterate through markers; create a condition for a new marker
    for marker, variables in var_vals.items():
        conditions[marker] = ""
        # iterate through variables of the marker
        for var, vals in variables.items():
            # generate random value
            new_var = random.randint(0, 2147483647)
            # check if variable obtains value during runtime
            if not (new_var in vals):
                # check if it is the first variable and create condition string
                if conditions[marker] == "":
                    conditions[marker] = str(new_var) + " == " + var
                else:
                    conditions[marker] = conditions[marker] + " || " + str(new_var) + " == " + var

    print("CONDITION GENERATED")
    # return generated conditions
    return conditions

def instrument_code(conditions, code):
    print("INSTRUMENT CODE")
    # iterate through each marker with its unsat condition
    for marker, condition in conditions.items():
        # look for the maker call
        marker_call = marker + "();"
        # create replacement code for the marker call (one line)
        replacement = "if (" + condition + "){" + marker_call + "}"
        # replace the marker call with replacement putting it into dead code
        code = code.replace(marker_call, replacement)
    print("CODE INSTRUMENTED")
    return code
    
# enter program from generator.py
def entrance(candidate_code):
    # store program in tmp/
    program_txt = open('tmp/candidate.txt', 'w+')
    program_txt.write(candidate_code)
    program_txt.close()
    global_variables = precompute(candidate_code)
    run_gdb()
    var_vals = eval_log(global_variables)
    conditions = unsatConditionGenerator(var_vals)
    new_candidate = instrument_code(conditions, candidate_code)
    new_program_txt = open('tmp/candidate_new.txt', 'w+')
    new_program_txt.write(new_candidate)
    new_program_txt.close()


# enter program standalone
def main():
    text_file = open("tmp/candidate.txt", "r")
    candidate_code = text_file.read()
    text_file.close()
    global_variables = precompute(candidate_code)
    run_gdb()
    var_vals = eval_log(global_variables)
    conditions = unsatConditionGenerator(var_vals)
    new_candidate = instrument_code(conditions, candidate_code)
    new_program_txt = open('tmp/candidate_new.txt', 'w+')
    new_program_txt.write(new_candidate)
    new_program_txt.close()
    

if __name__ == "__main__":
    main()



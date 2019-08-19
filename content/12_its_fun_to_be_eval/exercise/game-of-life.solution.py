def apply_custom_rules(custom_rules, grid, i, j, total_neighbours):
    ###
    ### TODO:
    ### 1. go through the custom_rules one by one
    ###   a. create a safe 'globals' and 'locals' environment for each rule that has the relevant information
    ###   b. exec the fule
    ###   c. check if the rule has a result. if it does, return the result
    ### 2. if no rule had a resultm, return grid[i, j] 
    for rule in custom_rules:
        globals_ = {} #{'__builtins__' : {}}
        locals_ = {
            'grid' : grid.copy(),
            'i': i,
            'j': j,
            'total_neighbours' : total_neighbours,
            'ON' : ON,
            'OFF' : OFF,
            }
    
        exec(rule, globals_, locals_)
        if 'result' in locals_:
            return locals_['result']
            
    return grid[i, j]


def read_custom_rules(custom_rules):
    ###
    ### TODO
    ### 1. use the glob module to search for rule files with the file pattern "rule-*.txt"
    ### 2. read each file as a string 
    ### 3. use the `compile` function to compile the string
    ### 4. append the compiled code into the custom_rules list
    for rule_file in glob.glob('rule-*.txt'):
        with open(rule_file) as f:
            source = f.read()
            rule = compile(source, rule_file, 'exec')
            custom_rules.append(rule)


""" 
# Save this as rule-1.txt

if grid[i, j]  == ON:
    if (total_neighbours < 2) or (total_neighbours > 3):
        result = OFF
"""

"""
# Save this as rule-2.txt
if grid[i, j]  == OFF:
    if total_neighbours == 3:
        result = ON
"""

class Facts(): 
    def __init__(self, input_text, output_text) -> None:
        self.input_text = input_text
        self.output_text = output_text

    def get_fact(self): 
        with open(self.input_text, 'r') as f: 
            line = f.readline()
            rest_lines = f.readlines()
        with open(self.input_text, 'w') as f: 
            f.writelines(rest_lines)
        with open(self.output_text, 'w') as f: 
            print(line, file=f)
        return line

    def get_fact_count(self): 
        with open(self.input_text, 'r') as f: 
            all_lines = f.readlines()
        if len(all_lines) == 1: 
            print("There is " + str(len(all_lines)) + " fact left.")
        else: 
            print("There are " + str(len(all_lines)) + " facts left.")
        return

class Facts(): 
    def __init__(self, input_text, output_text) -> None:
        self.input_text = input_text
        self.output_text = output_text

    def get_first_fact(self): 
        with open(self.input_text, 'r') as f: 
            line = f.readline()
            rest_lines = f.readlines()
        with open(self.input_text, 'w') as f: 
            f.writelines(rest_lines)
        with open(self.output_text, 'w') as f: 
            print(line, file=f)
        return line

    def get_random_fact(self): 
        with open(self.input_text, 'r') as f: 
            line = f.readlines()
            
        


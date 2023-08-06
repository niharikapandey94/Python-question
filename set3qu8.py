def count_words(input_file, output_file):
    try:
      
        with open(input_file, 'r') as file:
            content = file.read()
        
       
        word_count = len(content.split())

        
        with open(output_file, 'w') as file:
            file.write(str(word_count))
        
        print("Word count written to", output_file)
    
    except FileNotFoundError:
        print("Input file not found")

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'

count_words(input_file, output_file)

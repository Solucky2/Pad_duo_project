from bs4 import BeautifulSoup
import csv

class Parser:

    def __init__(self, source, parser_type):
        self.source = source
        self.type = parser_type
        self.soup = BeautifulSoup(source, parser_type)

    def find_all(self, elem_type, class_name):
        elements = self.soup.find_all(elem_type, class_=class_name)
        return [[element.text.strip()] for element in elements]

    @staticmethod
    def parse_to_csv(output_file, *values):
        transposed_values = zip(*values)
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in transposed_values:
                formatted_row = [", ".join(str(item) for item in col if item is not None) for col in row]
                writer.writerow(formatted_row)

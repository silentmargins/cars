def generate_report(filename, title, additional_info):
    column_of_paragraphs = []
    description_directory = '~/supplier-data/descriptions'
    for file in os.listdir(description_directory):
        with open(description_directory + '/' + file, 'r') as description_file:
            description_list = []
            for line in description_file:
                description_list.append(line)
            report_name= Paragraph('name: ' + description_list[0] + '\n')
            column_of_paragraphs.append(report_name)
            report_weight = Paragraph('weight: ' + description_list[1] + '\n')
            column_of_paragraphs.append(report_weight)
            empty_line = Spacer(1,20)
            column_of_paragraphs.append(empty_line)

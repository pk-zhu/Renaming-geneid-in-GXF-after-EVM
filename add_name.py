import argparse

def add_name_attribute_to_gff(input_path, output_path):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        for line in input_file:
            # 如果行以 "#" 开头，将注释行直接写入输出文件
            if line.startswith("#"):
                output_file.write(line)
                continue

            line = line.rstrip()
            fields = line.split('\t')
            # 确保行至少包含9个字段，以避免 "list index out of range" 错误
            if len(fields) >= 9:
                if fields[2] in ('gene', 'mRNA'):
                    attributes = fields[8].split(';')
                    id_attribute = [attr for attr in attributes if attr.startswith('ID=')]
                    if id_attribute:
                        id_value = id_attribute[0].split('=')[1]
                        # 将"name"属性的值与之前的内容以分号分隔开，保持原有属性不变
                        fields[8] = ';'.join(attributes + [f'name={id_value}'])
                output_file.write('\t'.join(fields) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add 'name' attribute to GFF lines with 'gene' or 'mRNA' in the third column.")
    parser.add_argument("-i", "--input", help="Input GFF file path", required=True)
    parser.add_argument("-o", "--output", help="Output GFF file path", required=True)
    args = parser.parse_args()

    add_name_attribute_to_gff(args.input, args.output)

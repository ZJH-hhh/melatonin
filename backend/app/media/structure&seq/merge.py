import csv
import glob

# 定义输入和输出路径
input_folder = 'Gene_expression'  # 替换为包含 .txt 文件的目录路径
output_file = 'merged_output.csv'   # 输出的 CSV 文件名

# 第一步：提取所有文件的表头字段
all_columns = set()  # 使用集合来存储所有不同的字段

txt_files = glob.glob(f"{input_folder}/*.txt")

for file_path in txt_files:
    with open(file_path, mode='r', encoding='utf-8') as txt_file:
        # 跳过前三行，第四行为表头
        for _ in range(3):
            next(txt_file)
        headers = next(csv.reader(txt_file, delimiter='\t'))
        all_columns.update(headers)  # 添加字段到集合中

# 将集合转换为列表并排序，确保字段顺序一致
all_columns = sorted(all_columns)

# 第二步：写入到 CSV 文件中
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=all_columns)
    csv_writer.writeheader()  # 写入表头

    # 遍历每个文件，将数据写入 CSV
    for file_path in txt_files:
        with open(file_path, mode='r', encoding='utf-8') as txt_file:
            # 跳过前三行，然后读取数据
            for _ in range(3):
                next(txt_file)
            txt_reader = csv.DictReader(txt_file, delimiter='\t')

            # 对于每一行，缺失的字段将自动填充为空值
            for row in txt_reader:
                csv_writer.writerow(row)

print("所有文件已成功合并到 CSV 文件中！")

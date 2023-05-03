import os
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO


def extract_pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        # 使用PdfReader获取文档页数
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # 使用pdfminer提取带格式的文本
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page in range(num_pages):
                output_string = StringIO()
                extract_text_to_fp(pdf_file, output_string, laparams=LAParams(), codec='utf-8', page_numbers=[page])
                txt_file.write(output_string.getvalue())

    print(f"文本已成功提取到 {txt_path}")


def process_pdf_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            txt_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + '.txt')
            extract_pdf_to_txt(pdf_path, txt_path)


if __name__ == '__main__':
    folder_path = 'B:/train_MEGA/MarxEngelsGesamtausgabe'  # 将此处替换为您的PDF文件夹路径
    process_pdf_files_in_folder(folder_path)

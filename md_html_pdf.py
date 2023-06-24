import os
import pdfkit

# 將Markdown轉換為HTML
def markdown_to_html(markdown_text):
    # 在這裡使用你喜歡的Markdown庫將Markdown轉換為HTML
    # 這裡以示例使用python-markdown作為Markdown庫
    import markdown
    html_text = markdown.markdown(markdown_text)
    return html_text

# 將HTML轉換為PDF
def html_to_pdf(html_text, output_path):
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8'
    }
    pdfkit.from_string(html_text, output_path, options=options, configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'))

# 資料夾路徑
folder_path = r'C:\Users\P65\Documents\vscode\markdown轉\md檔'

# 輸出資料夾路徑
output_folder_path = r'C:\Users\P65\Documents\vscode\markdown轉\html_pdf檔'

# 建立輸出資料夾
os.makedirs(output_folder_path, exist_ok=True)

# 讀取資料夾中的Markdown檔案
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        md_file_path = os.path.join(folder_path, filename)
        
        # 讀取Markdown文件
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # 取得輸入的Markdown檔案名稱
        md_filename = os.path.basename(md_file_path)

        # 移除副檔名，並用於生成輸出檔案名稱
        filename_without_extension = os.path.splitext(md_filename)[0]

        # 將Markdown轉換為HTML
        html_text = markdown_to_html(md_text)

        # 生成輸出的HTML檔案名稱
        html_filename = f"{filename_without_extension}.html"
        html_path = os.path.join(output_folder_path, html_filename)

        # 保存HTML檔案
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_text)

        # 生成輸出的PDF檔案名稱
        pdf_filename = f"{filename_without_extension}.pdf"
        pdf_path = os.path.join(output_folder_path, pdf_filename)

        # 將HTML轉換為PDF
        html_to_pdf(html_text, pdf_path)

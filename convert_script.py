import os
import nbformat
from nbconvert import PythonExporter

# Caminho da pasta onde estão os arquivos .ipynb
input_folder = './notebooks'
output_folder = './'

# Criar a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Listar todos os arquivos .ipynb na pasta
notebooks = [f for f in os.listdir(input_folder) if f.endswith('.ipynb')]

# Converter cada arquivo .ipynb para .py
for notebook_filename in notebooks:
    input_path = os.path.join(input_folder, notebook_filename)
    output_path = os.path.join(output_folder, notebook_filename.replace('.ipynb', '.py'))

    # Ler o conteúdo do notebook
    with open(input_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Converter para script Python
    python_exporter = PythonExporter()
    python_code, _ = python_exporter.from_notebook_node(notebook_content)

    # Salvar como .py
    with open(output_path, 'w', encoding='utf-8') as python_file:
        python_file.write(python_code)

print(f"Conversão concluída! Arquivos salvos em: {output_folder}")

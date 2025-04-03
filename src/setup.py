from cx_Freeze import setup, Executable
import os


build_options = {
    "packages": ["customtkinter", "openpyxl", "darkdetect", "et_xmlfile"],
    "excludes": [],  # Excluir pacotes desnecessários (opcional)
    "include_files": [],  # Incluir arquivos adicionais (ex: .json, .txt)
}


executables = [
    Executable(
        script="src/app.py",
        base="Win32GUI" if os.name == "nt" else None,  # Oculta o console no Windows (GUI)
        # icon="icone.ico"  # Opcional: caminho para um ícone personalizado
        target_name="RegistroDeVendas.exe"
    )
]

setup(
    name="Registro de Vendas",
    version="1.0",
    description="Interface gráfica para inserir registros numa planilha",
    options={"build_exe": build_options},
    executables=executables,
)
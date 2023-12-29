from PIL import Image
import os


diretorio_entrada = r"xx"
diretorio_saida = r"xx"


if not os.path.exists(diretorio_saida):
    os.makedirs(diretorio_saida)


def is_jpg(arquivo):
    return arquivo.lower().endswith((".jpg", ".jpeg"))


for diretorio_raiz, diretorios, arquivos in os.walk(diretorio_entrada):
    for nome_arquivo in arquivos:
        if is_jpg(nome_arquivo):
            caminho_entrada = os.path.join(diretorio_raiz, nome_arquivo)

            caminho_saida = os.path.join(diretorio_saida, os.path.relpath(
                caminho_entrada, diretorio_entrada))

            with Image.open(caminho_entrada) as imagem:
                if imagem.width > imagem.height:
                    imagem = imagem.transpose(Image.Transpose.ROTATE_90)
                imagem = imagem.resize((300, 400), Image.ANTIALIAS)
                imagem.save(caminho_saida)

print("Todas as imagens foram redimensionadas e salvas em orientação vertical em", diretorio_saida)

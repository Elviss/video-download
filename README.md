# Video Download

Este scriot busca no youtube as midias disponíveis para a URL do video especificado e faz o download da melhor resolução, e do audio do video. Após fazer o download de ambos, executa a operação de merge dos dois arquivos para gerar um arquivo único com audio e vídeo.

Dependencias:
- pytube
- moviepy

Antes de rodar:

- Alterar `VIDEO_URL` na linha 6 do arquivo `main.py` para colocar a url do video que quer baixar

- Alterar `PATH_TO_DOWNLOAD` na linha 9 do arquivo `main.py` para colocar o caminho onde ficará o arquivo baixado
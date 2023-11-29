# JHM MOTORES CATALOGO
#### Vídeo Demo:  <https://youtu.be/TjzcWTo9NyI>
#### Descrição:

Bem-vindo ao Portal de Catálogo da JHM Motores! Este projeto, resultado da minha jornada em Harvard, é uma plataforma desenvolvida com HTML, CSS, Flask e Python, proporcionando aos usuários acesso ao catálogo de motores oferecidos pela JHM Motores Elétricos. A combinação de uma interface intuitiva e um backend eficiente garante uma experiência envolvente para os usuários.

## Estrutura do Projeto

### Arquivos Estáticos (static)
Na pasta "static", encontram-se os arquivos estáticos que não sofrem alterações durante a execução do código. Esta seção está subdividida em duas pastas principais:

- **img:** Contém as imagens utilizadas ao longo do projeto.
- **css:** Dividido em cinco arquivos, cada um dedicado a diferentes blocos, incluindo navegação, reset, rodapé, página de motores e página de produtos.

### Arquivos de Templates (templates)
A pasta "templates" abriga os arquivos HTML do projeto, organizados da seguinte forma:

- **base.html:** Arquivo base compartilhado por todas as páginas, promovendo consistência no design.
- **produtos.html:** Página destinada à visualização de todos os motores da JHM Motores.
- **motores.html:** Página específica para visualização do motor selecionado anteriormente.

A utilização do Flask permitiu simplificar o desenvolvimento, eliminando a necessidade de criar diversas páginas específicas para cada tipo de motor.

### Código Principal (app.py)
O arquivo "app.py" desempenha um papel central, contendo a implementação dos códigos necessários para o funcionamento eficiente do catálogo. É nele que linka tudo e exibe ao usuário o determinado motor ou a pagina dos produtos.

### Banco de Dados (bd.py)
Ao lado do "app.py", encontra-se o arquivo "bd.py", que serve como o banco de dados fundamental para facilitar a manipulação das informações. Este banco de dados foi criado para simplificar a integração e implementação no Flask, contribuindo para a eficiência do sistema.

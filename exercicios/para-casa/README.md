# Exercício de Casa 🏠 

## Nome do Exercicio
Agora que já sabem como fazer o processo de ETL com pandas, é hora de brincar com a lista dos artistas mais ouvidos do SPOTIFY!
O que preciso que faça:

- Use o arquivo `mais_ouvidas_2024.csv` para análise. Lembre-se de garantir que o carregamento foi feito com sucesso.
- Indentifique as colunas que contêm números, como 'Spotify Streams', 'YouTube Views', etc., e converta essas colunas para o tipo numérico se estiverem em outro formato. (Use replace() e astype())
- Corrija a coluna 'Release Date' para o formato datetime.
- Crie uma nova coluna chamada 'Streaming Popularity', que seja a média da popularidade nas plataformas 'Spotify Popularity', 'YouTube Views', 'TikTok Likes', e 'Shazam Counts'. (lembrem-se que só é possível calcular médias e fazer operações matemáticas com tipos númericos)
- Crie uma coluna 'Total Streams', somando os valores de 'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', e 'Soundcloud Streams'.
- Filtre apenas as faixas onde a popularidade do Spotify ('Spotify Popularity') é maior que 80 e que tenham mais de 1 milhão de streams totais ('Total Streams').
- Salve o DataFrame resultante em um novo arquivo JSON chamado 'faixas_filtradas.json'.
- Garanta que o arquivo foi salvo corretamente
---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).

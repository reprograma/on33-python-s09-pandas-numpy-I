# Exercício de Sala 🏫  

## Nome do Exercicio
Usando a biblioteca PANDAS , vamos aprender ETL na prática.

- Extract:
    - Carregue o arquivo CSV usando pandas.
    - Exiba as primeiras 5 linhas para garantir que os dados foram carregados corretamente.
- Transform:
  - Limpeza de Dados:
      - Verifique se há valores nulos ou ausentes nas colunas e, se houver, trate-os adequadamente (por exemplo, substituindo por uma média ou removendo as linhas).
      - Corrija a coluna 'Date' para o formato datetime.
  - Criação de Novas Colunas:
      - Crie uma nova coluna chamada 'Total Sales Value', que seja o produto de 'Price' e 'UnitsSold'.
      - Crie uma coluna 'Profit Margin', assumindo que o custo de fabricação é 70% do preço ('Price'), a margem de lucro pode ser calculada como (Price * 0.30) * UnitsSold.
  - Filtragem:
      - Filtre as transações onde o 'Total Sales Value' é maior que 100,000 e a margem de lucro ('Profit Margin') é maior que 20,000.
- Load:
    - Salve o DataFrame resultante em um novo arquivo CSV chamado 'vendas_filtradas.csv'.
    - Carregue este arquivo salvo e exiba as primeiras 5 linhas para verificar.

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)

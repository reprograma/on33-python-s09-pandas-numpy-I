<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online ON33 | Semana 09 | 2024 | Professora Manuelly Suzik

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]

### Resumo
O que veremos na aula de hoje?
* [Dados x informação](#dadosxinformacao)
* [ETL ou ELT](#ETLouELT)
* [PANDAS e NUMPY](#PANDAS)

## Conteúdo
### Dados x Informação
1. [Conceitos e definições](#topico1)
### ETL ou ELT
1. [Extract](#topico3)
2. [Transform](#topico3)
3. [Load](#topico3)
### PANDAS e Numpy
1. [Importando dados](#topico3)
2. [Tranformando dados em informação](#topico3)
    - Dataset
    - Dados tabulares
    - Funções nativas
    - Visualização

### Dados x Informação
A coisa mais importante que uma cientista de dados precisa saber são os significados e diferenças entre dados, informação e conhecimento. Para elucidar o que significa esses termos temos que levar em conta o processo que os dados levam desde sua coleta até sua utilização e por fim a transformação em informação, com a qual você pode criar conhecimento sobre um certo tema.

Para isso, vamos imaginar que temos dados de todos os brasileiros: onde mora, seu gênero, sua classe econômica e outras informações relevantes que estão armazenadas em um banco de dados do governo federal. Pois bem, esses dados por si só mostram a quantidade de brasileiros. Agora imagine que também temos um banco de dados que os registros dos imóveis no Brasil e seus respectivos proprietários.Esse dado, também, não nos daria muitas informações além de quantas casas no brasil tem proprietários.

Esses DADOS são importante porque eles QUANTIFICAM algo, mas sozinhos não tem muito valor já que não podemos extrair muitas informações QUALITATIVAS deles. Agora, se eu utilizar esses dados para fazer um levantamento de quantos brasileiros tem casa própria, seria possível transforma-los em INFORMAÇÃO.

Veja o que o próprio dicionário diz sobre esses dois termos:

> **DADOS**: Plural de dado, do latim dátus.a.um 'apresentado, entregue'.: Conhecimento que se tem sobre algo, usado para solucionar uma questão, fazer um julgamento, criar ou colocar em prática um pensamento, uma opinião;

> **INFORMAÇÃO**: Do latim informatio.onis.: Reunião dos conhecimentos, dos dados sobre um assunto ou pessoa.

Embora sejam parecidos em suas definições acadêmicas, na prática perceberão que os dados sozinhos não podem explorar todo o poder que a informação tem a oferecer. Mesmo assim, são essenciais já que a informação não pode ser construída sem eles.

### ETL x ELT
Outros conceitos também devem ser conhecidos para as pessoas que pretendem trabalhar com dados, alguns desses conceitos são muito importantes de serem compreendidos principalmente quando se trata do ciclo de vida dos dados. Dentre eles, um que considero importante para se conhecer no começo de sua jornada é o ETL. Vamos abordar o que é e quando deve ser usado, sem nos aprofundarmos muito em detalhes técnicos desnecessários que possam confundi-las. A intenção é que saibam o que é e a importancia no seu trabalho.

Extract-Transform-Load ou ETL, é um padrão que normalmente é utilizado em serviços para garantir a integridade e armazenamento dos dados.

Explicarei brevemente sobre o que cada uma dessas etapas significa.

#### Extract
Descreve o processo de extração dos dados de um banco de dados, uma planilha, um dataframe ou basicamente qualquer coisa que registre valores.Além disso, como eles serão compartilhados para quaisquer fins que o detentor desses dados sinta que é necessário.

Nessa etapa, é necessário que uma base de dados esteja pronta para receber conexões ou que sejam capazes de serem compartilhadas, de preferência nos formatos mais compatíveis, e que a integridade desses dados seja confiável.

#### Transform
A etapa de transformação dos dados consiste em reforçar a qualidade dos dados, excluindo registros duplicados ou nulos, ou às vezes os convertendo para outros formatos para que sejam lidos mais facilmente pelo sistema de destino.

Durante a transformação dos dados é comum que haja cruzamento de dados entre diferentes fontes, seja para criar outros conjunto de dados mais consistentes, atender uma regra específica do negócio ( cliente ) ou até aplicar modificações diretas através de algoritmos de tratamento de dados.

#### Load
Após os dados serem transformados corretamente, é necessário garantir que esses dados estejam em um lugar específico onde poderão ser consultados sempre que necessário. Essa é a etapa de carregamento, que consiste em enviar os dados tratados ( ou quase ) a um sistema capaz de processa-los e acessa-los rapidamente independente da quantidade de registros que existam.

O lugar em que esses dados são enviados são chamados de **data warehouse** ou **data lakes**, e embora não seja muito aconselhado, também podem ser carregados a outros sistemas de armazenamentos de dados como banco de dados de alta perfomance.

### ELT
Como já conhecemos o que significa cada uma das letras do ETL ficará fácil falar sobre o ELT. Como podemos presumir, nesse formato os dados são carregados antes de serem transformados, isso pode acontecer por diversas razões e a escolha entre os dois formatos depende muito de como seus dados foram extraídos e para qual fim você precisa utiliza-los.

O que precisamos saber sobre o processo de ELT é que como os dados não são previamente tratados, costumam consumir muito espaço e tempo para que as informações sejam encontradas, aumentando custo e complexidade. Isso é tão ruim quanto parece ser, mas como cientistas de dados serão capazes de indentificar em qual momento ele deverá ser usado.

### Pandas
**O que é:** Uma biblioteca que pode ser usada na linguagem de programação python, usada no processo tanto de extração quanto de transformação de dados. Devido a sua capacidade de carregar diversas extensões de arquivos diferentes ( CSV, XLSX, XLS...) e também a velocidade em que consegue ler esses arquivos e tranforma-los em **Dataframes**.

**Como usa-la**
```Python
pip install pandas
```
```Python
import pandas as pd
```

#### ETL com Pandas
- Extraindo: Utilizando as funções de leitura como o `read_csv()` conseguimos extrair os dados de um dataset e tranforma-los em um dataframe, que é um tipo com o qual o pandas consegue ler e manipular.
- Transformando: Através de funções como `replace()`, `drop_duplicates()` e etc., conseguimos consultar, alterar, visualizar e **normalizar** os dados da nossa tabela. Também conseguimos converter os valores de uma coluna utilizando `astype()`
- Carregando: Por fim, funções como `to_json` conseguem criar arquivos a partir de um dataframe.

### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)


### Links Úteis
- [Documentação oficial PANDAS (EN)](https://pandas.pydata.org/docs/getting_started)
- [Documentação oficinal NUMPY(EN)](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [ETL conceitos](https://www.ibm.com/br-pt/topics/etl)


<p align="center">
Desenvolvido com :purple_heart:  
</p>


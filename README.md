# housepricing

  Projeto de Ciência de Dados ao qual prevê o preço de aluguel da imóveis na cidade de São Paulo, utilizando técnicas de Machine Learning. Foi feito nesse projeto uma preparação dos dados, em que analisei a qualidade dos dados, análise de dados para entender a distribuição dos dados, análise das features para saber qual o impacto das mesmas no valor do aluguel, e por fim selecionar quais features vão para o treinamento do modelo. Ao final fiz o deploy do modelo num app local utilizando uma API para acessar o app, em que o usuário possa passar as informações do imóvel e ter uma previsão do aluguel. Além disso, ainda construí um banco de dados local para armazenar os inputs do usuário, quando foi iniciado e finalizado o processo, e o tempo de processamento da previsão.

  Neste projeto utilizei Flask e sqlite3 para criar o app e o banco de dados local, também utilizei RandomForestRegressor para treinar o modelo de para ver previsão do aluguel. Pandas para análise, limpeza e qualidade dos dados.
  
  ### Features utilizadas no treinamento do modelo: 
  <ul>
    <li>area - tamanho do imóvel em m².</li>
    <li>quartos - quantidade de quartos do imóvel.</li>
    <li>banheiro - quantidade de banheiros do imóvel.</li>
    <li>vagas_garagem - quantidade de vagas na garagem.</li>
    <li>andar - andar que se encontra o imóvel.</li>
    <li>animal - se aceita ou não animais de estimação (variável categórica).</li>
    <li>mobilhado - se o imóvel está ou não mobilhado (variável categórica).</li>
    <li>condominio - valor do condimínio em R$.</li>
    <li>iptu - valor do IPTU do imóvel em R$.</li>
  </ul>
  
  ### Target:
  <ul><li>aluguel - valor do aluguel do imóvel em R$</li></ul>

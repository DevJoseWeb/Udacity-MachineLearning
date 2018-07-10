Projeto Final de Aprendizado de Máquina: Identificar Fraude
Resuma para nós o objetivo deste projeto e como o aprendizado de máquina é útil na tentativa de realizá-lo. Como parte de sua resposta, dê um panorama sobre o conjunto de dados e como ele pode ser usado para responder à pergunta do projeto. Houve algum valor discrepante nos dados quando você os obteve e como você lidou com eles? [rubricas relevantes: "exploração de dados", "investigação outlier"]

Introdução:

O escândalo da Enron por volta de 2000 foi tão grave que até mesmo a maioria dos alemães (onde eu moro) já ouviu falar sobre isso. Muitos executivos da Enron foram indiciados por estarem fortemente entrelaçados no escândalo devido a esconder dívidas e / ou manipular saldos financeiros.

O conjunto de dados disponível é um subconjunto de funcionários da Enron, sendo que alguns deles fazem parte do escândalo. O objetivo é identificar esses suspeitos. Tem:

um total de 146 funcionários (ou seja, linhas / observações) no conjunto de dados
com 21 recursos (incl. POI)
o recurso poi (Person of Interest) é um booleano e classifica os funcionários se uma investigação adicional contra fraudes for necessária ou não.
os outros 20 recursos são de natureza financeira (por exemplo, salário) ou comunicacional (por exemplo, e-mails enviados from_this_person_to_poi)
há 18 'POI' e 128 'não-POI'
20 de 21 recursos contêm valores ausentes
Aqui está a lista completa dos detalhes do projeto da Udacity:

características financeiras : ['salário', 'deferral_payments', 'total_payments', 'loan_advances', 'bônus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'despesas', 'exercitado_stock_options', 'outro', 'long_term_incentive ',' restricted_stock ',' director_fees '] (todas as unidades estão em dólares americanos)

características de email : ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi'] (as unidades são geralmente o número de mensagens de emails; a exceção notável é 'email_address', que é uma cadeia de texto)

Rótulo de POI : ['poi'] (booleano, representado por inteiro)

Outliers:

Através de uma breve análise exploratória de dados e uma dupla checagem com o arquivo enron61702insiderpay.pdf (fornecido por Udacity), os seguintes outliers foram detectados:

TOTAL
A AGÊNCIA DE VIAGENS NO PARQUE
Ambas são observações agregadas e, portanto, nenhum funcionário. Além disso,

LOCKHART, EUGENE E
pode ser considerado como um outlier foi removido como todos os seus valores foram NaN.

Quais recursos você usou no seu identificador de POI e que processo de seleção você usou para selecioná-los? Você teve que fazer algum escalonamento? Por que ou por que não? Como parte da tarefa, você deve tentar projetar seu próprio recurso que não vem pronto no conjunto de dados - explique qual recurso você tentou fazer e a lógica por trás dele. (Você não precisa necessariamente usá-lo na análise final, apenas o engenheie e teste.) Em sua etapa de seleção de recursos, se você usou um algoritmo como uma árvore de decisão, forneça também as importâncias de recursos dos recursos que você usa, e se você usou uma função de seleção de recursos automatizada como o SelectKBest, por favor, informe as pontuações dos recursos e as razões para a sua escolha de valores de parâmetros. [rubricas relevantes: "criar novas funcionalidades", "selecionar de forma inteligente funcionalidades", "

Novas características

Eu experimentei dois novos recursos, que são proporções (financeiras e comunicacionais):

ratio_tsv_salary: definir o valor total das ações para o salário anual pode fornecer algumas informações se o bônus em ações for desproporcional em relação ao salário-base.
poi_messages_ratio: configurar todas as mensagens relacionadas a poi para a soma de todas as mensagens pode fornecer algumas dicas se um funcionário tiver contato contínuo com os POIs.
Processo de seleção

Eu classifiquei todos os recursos disponíveis (incl. E excl. Os dois que criei, exceto o e-mail do recurso) via select k-best o método feature_importances_ para Decision Trees e Random Forest. Estes foram os TOP-10 classificados por kBest:

Característica	Ponto
exercised_stock_options	24.815079733218194
total_stock_value	24.182898678566872
bônus	20,792252047181538
salário	18.289684043404513
deferred_income	11.458476579280697
long_term_incentive	9,9221860131898385
restricted_stock	9.212810621977086
total_payments	8,7727777300916809
shared_receipt_with_poi	8,5894207316823774
loan_advances	7,1840556582887247
O 10º lugar, 'loan_advances', foi descartado, já que tinha apenas 3 (!) Valores não NaN. Além disso, sua pontuação é 15% menor do que no local acima, o que pareceu um bom corte arbitrário. Então, optei por trabalhar apenas com o TOP 9. Exceto o shared_receipt_with_poi , todos os recursos eram financeiros.

Eventualmente, shared_receipt_with_poi foi substituído pelo meu próprio recurso de proporção poi_messages_ratio . O mesmo vale para os recursos salário e total_stock_value , que fazem parte do meu índice financeiro. No entanto, meu índice financeiro não foi bem-sucedido, então o removi e adicionei novamente o salário e o total_stock_value à lista de recursos.

Escala

O escalonamento não foi necessário para todos os algoritmos testados (por exemplo, Floresta aleatória e Árvore de decisão). No entanto, ainda era usado como as escalas para recursos financeiros ofuscados os comunicacionais. Se nenhum dimensionamento ocorresse, os recursos financeiros receberiam mais peso.

Qual algoritmo você acabou usando? Que outro (s) você tentou? Como o desempenho do modelo diferiu entre os algoritmos? [rubrica de rubrica relevante: "escolha um algoritmo"]

Eu tentei os seguintes algoritmos, com os seguintes resultados finais:

GaussianNB: Precisão: 0,84100 Precisão: 0,38355 Lembre-se: 0,31700
Árvore de decisão: Precisão: 0,81000 Precisão: 0,25686 Lembre-se: 0,22450
* Kmeans: Precisão: 0.85593 Precisão: 0.31663 Lembre-se: 0.06950
* (Isso foi por curiosidade, já que o Kmeans é projetado principalmente para clustering)

RandomForest: Precisão: 0.85407 Precisão: 0.39936 Lembre-se: 0.18750
SVM: "Tenho uma divisão por zero ao experimentar", presumo que nenhum funcionário tenha sido rotulado como um POI
Estes são os resultados sem meu próprio recurso poi_messages_ratio , mas apenas pegando os melhores recursos classificados acima:

GaussianNB: Precisão: 0,84067 Precisão: 0,37611 Lembre-se: 0,31400
Árvore de decisão: Precisão: 0,80920 Precisão: 0,28535 Lembre-se: 0,2850
* Kmeans: Precisão: 0.84807 Precisão: 0.32963 Lembre-se: 0.10450
* (Isso foi por curiosidade, já que o Kmeans é projetado principalmente para clustering)

RandomForest: Precisão: 0.85620 Precisão: 0.37025 Recuperar: 0.15050
SVM: "Tenho uma divisão por zero ao experimentar", presumo que nenhum funcionário tenha sido rotulado como um POI
Então, no final, minha seleção de recursos não funcionou para o algoritmo de árvore, mas fez com que o classificador GaussianN B passasse no teste.

O que significa ajustar os parâmetros de um algoritmo e o que pode acontecer se você não fizer isso bem? Como você ajustou os parâmetros do seu algoritmo particular? Quais parâmetros você ajustou? (Alguns algoritmos não possuem parâmetros que você precisa ajustar - se este for o caso daquele que você escolheu, identifique e explique brevemente como você teria feito isso para o modelo que não foi sua escolha final ou um modelo diferente que faz utilizar o ajuste de parâmetros, por exemplo, um classificador da árvore de decisão). [rubricas relevantes: "discutir o ajuste dos parâmetros", "ajustar o algoritmo"]

O objetivo do ajuste de parâmetro é melhorar o desempenho do algoritmo escolhido. Hyperparameters são parâmetros cujos valores são definidos antes do início do aprendizado. A otimização dos hiperparâmetros pode ser feita manualmente ou com o GridSearchCV do sklearn. Se não for bem feito, o desempenho do classificador escolhido pode estar abaixo das expectativas na prática.

Embora eu eventualmente tenha usado o GaussianNB, experimentei ajustar os outros classificadores para obter alguma experiência. Os hiperparâmetros para dois classificadores são dados aqui como exemplo:

Floresta Aleatória
critério = Existem as opções 'gini' e 'entropy' para medir como dividir
bootstrap = Se as amostras de bootstrap são usadas ao construir árvores.
max_depth = A profundidade máxima da árvore. Se for muito profundo, você pode se sobrepor.
min_samples_split = O número mínimo de amostras necessárias para dividir um nó interno. Se definido muito baixo, você pode overfit.

SVM
C: valor baixo é para limite de decisão suave, limite complexo de alto valor (ressalva: overfitting),
Gama: se o gama é muito grande, você também pode acabar se superdimensionando

O que é validação e qual é um erro clássico que você pode cometer se errar? Como você validou sua análise? [rubrica de rubrica relevante: "estratégia de validação"]

A validação testa o desempenho do seu modelo. Um erro clássico é abrir mão da divisão dos dados em um conjunto de treinamento e teste e, assim, usar todo o conjunto de dados para treinar seu modelo. Consequentemente, o modelo será ajustado e terá um desempenho ruim em novos dados. Portanto, divido os dados em um trem (70% dos dados) e um conjunto de testes (30% dos dados).

Além disso, StratifiedShuffleSplit de tester.py foi usado. Como estamos lidando com um conjunto de dados pequeno e desequilibrado neste projeto, trabalhar com conjuntos de dados menores é difícil e, a fim de tornar os modelos de validação robustos, muitas vezes usamos a validação cruzada. Esse método de validação cruzada divide os dados em conjuntos de treinamento / teste pelo embaralhamento de dobras aleatórias. Por padrão, ele reorganiza e divide os dados 10 vezes. Além disso, ao lidar com pequenos conjuntos de dados desbalanceados, é possível que algumas dobras contenham quase nenhuma (ou mesmo nenhuma!) Instâncias da classe minoritária. A ideia por trás da estratificação é manter a porcentagem da classe alvo tão próxima quanto possível da que temos no conjunto de dados completo.

Dê pelo menos duas métricas de avaliação e seu desempenho médio para cada uma delas. Explique uma interpretação de suas métricas que diz algo que seja compreensível ao homem sobre o desempenho do seu algoritmo. [item de rubrica relevante: "uso de métricas de avaliação"]

A métrica de avaliação mais simples é a precisão, que divide as observações corretamente rotuladas por todas as observações. No entanto, uma pontuação alta pode ser devido ao paradoxo de precisão . Isso acontece quando uma classe é muito rara na população. Para este conjunto de dados, onde há poucos POIs, isso pode acontecer, portanto, as taxas de recall e precisão podem ser mais apropriadas.

Precisão: verdadeiro positivo / (verdadeiro positivo + falso positivo )
Lembre-se: verdadeiro positivo / (verdadeiro positivo + falso negativo )
Uma boa precisão significa que sempre que um POI é sinalizado no conjunto de testes, sabemos com muita segurança que é muito provável que seja um POI real e não um alarme falso. Por outro lado, um bom recall significa que, quase sempre que um POI aparece no conjunto de testes, somos capazes de identificar a pessoa. Podemos ter alguns falsos positivos aqui, mas puxar o gatilho para o início neste caso significa apenas mais investigações, o que não é igual a ser diretamente indiciado. Então, recordar pode ser mais importante a precisão.


# Identify-Fraud-from-Enron-Email
In this project I played detective and put my machine learning skills to use by building an algorithm to identify Enron Employees who may
have committed fraud based on the public Enron financial and email dataset. Starter code was provided by Udacity.

* Final Project Write-up: Q_A.ipynb
* Pickle files: my_dataset.pkl, my_classifier.pkl, my_feature_list.pkl
* Machine Learning file: poi_id.py (run this file if needed)
* Tester file: tester.py (unmodified from Udacity-distributed code)
* feautere formatting: feature_format.py
* References: Reference.txt 

I have also attached my workflow as documentation.html .It can be downloaded to view .

Final result :

Pipeline(steps=[('scaler', MinMaxScaler(copy=True, feature_range=(0, 1))),
                          ('selection', SelectKBest(k=10, score_func=<function f_classif at 0x00000000071B2278>)),
                                          ('pca', PCA(copy=True, n_components=7, whiten=False)), ('naive_bayes', GaussianNB())])

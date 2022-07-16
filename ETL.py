import logging
import pandas as pd

logging.basicConfig(format='%(message)s', level=logging.INFO)

# * Extract
logging.info('Extraindo dados\n')
file1 = 'Arquivos\importacao-gas-natural-2000-2022.csv'
file2 = 'Arquivos\importacoes-exportacoes-derivados-2000-2022.csv'
file3 = 'Arquivos\importacoes-exportacoes-etanol-2012-2022.csv'
file4 = 'Arquivos\preços-combustiveis-2004-2021.tsv'
df1 = pd.read_csv(file1, sep=';')
df2 = pd.read_csv(file2, sep=';')
df3 = pd.read_csv(file3, sep=';')
df4 = pd.read_csv(file4, sep='\t')
logging.debug(f'{file1}\n{df1.head(3)}\n')
logging.debug(f'{file2}\n{df2.head(3)}\n')
logging.debug(f'{file3}\n{df3.head(3)}\n')
logging.debug(f'{file4}\n{df4.head(3)}\n')

# * Transform

# * Load
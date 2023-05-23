# SysTux  v1.0.a3

#### software linha de comando.

#### Às vezes, é necessário reformatar o seu sistema operacional Linux e reinstalar diversos pacotes. Este script foi desenvolvido para simplificar esse processo, permitindo que você salve uma lista desses pacotes em um banco de dados SQLite portátil. Dessa forma, você pode até mesmo armazenar essa lista em um pendrive, executar os comandos para reinstalar esses pacotes em sua máquina e guardar o script juntamente com o banco de dados em um local conveniente para uso futuro.

### Instalação:

    git clone https://github.com/AutoTux/SysTux-v1.0.a2/
    
----------

    cd SysTux-v1.0.a2/
    
### Como usar:

#### inserir um nome de pacote no banco de dados:

    python3 systux.py -i
    
#### Ver o banco de dados:

    python3 systux.py -v
    
#### Fazer download dos pacotes salvos no banco de dados:

    python3 systux.py -d
    
#### Ver o menu de opções:

    python3 systux -h

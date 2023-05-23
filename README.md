# SysTux  v1.0.a1

#### software linha de comando.

#### As vezes você precisa formatar seu linux e tem que instalar um monte de pacotes novamente, este script salva estes pacotes em uma lista em um banco de dados sqlite de bolso ou seja você pode livar até em um pendrive, executar os comandos para instalar instalar novamente estes comandos em sua maquina, salve este script com o banco de dados onde achar melhor para usa-lo novamente no futuro.

### Instalação:

    git clone https://github.com/AutoTux/SysTux-v1.0.a1/
    
----------

    cd SysTux-v1.0.a1/
    
### Como usar:

#### inserir um nome de pacote no banco de dados:

    python3 systux.py -i
    
#### Ver o banco de dados:

    python3 systux.py -v
    
#### Fazer download dos pacotes salvos no banco de dados:

    python3 systux.py -d
    
#### Ver o menu de opções:

    python3 systux -h

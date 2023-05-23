# this is part of the SysTux project.
#
# Release: v1.0.a1
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sqlite3
import subprocess
import argparse


def create_connection():
    connection = sqlite3.connect('inittux.db')
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacotes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)''')
    connection.commit()


def inserir_pacote(connection, nome_pacote):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pacotes (nome) VALUES (?)", (nome_pacote,))
    connection.commit()
    print("Pacote inserido com sucesso!")


def baixar_pacotes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM pacotes")
    nomes_pacotes = cursor.fetchall()

    if nomes_pacotes:
        nomes_pacotes = [pacote[0] for pacote in nomes_pacotes]

        comando = ["sudo", "apt-get", "install", "-y"] + nomes_pacotes
        subprocess.run(comando)
        print("Pacotes baixados e instalados com sucesso!")
    else:
        print("Nenhum pacote encontrado na tabela.")


def visualizar_pacotes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pacotes")
    pacotes = cursor.fetchall()

    if pacotes:
        print("Pacotes salvos no banco de dados:")
        for pacote in pacotes:
            print(pacote[1])
    else:
        print("Nenhum pacote encontrado na tabela.")


def main():
    conexao = create_connection()

    create_table(conexao)

    while True:
        parser = argparse.ArgumentParser(description="""[SysTux] Armazena nome de programas a serem baixados no futuro,
                                                         Este software é livre sobre a licença GNU GPLv2.0""")

        parser.add_argument('-d', action='store_true', help='Inicia o download dos pacotes')
        parser.add_argument('-v', action='store_true', help='Vizualizar o banco de dados')
        parser.add_argument('-i', action='store_true', help='Inserir nome dos pacotes para o banco de dados')

        args = parser.parse_args()
        
        if args.d:
            baixar_pacotes(conexao)
            break
        elif args.v:
            visualizar_pacotes(conexao)
            break
        elif args.i:
            print("Ctrl + C para sair")
            entry = input('pacote>>>')
            inserir_pacote(conexao, entry)
            break
        else:
            visualizar_pacotes(conexao)
            break
            
    conexao.close()

if __name__ == '__main__':
    main()

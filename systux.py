# this is part of the SysTux project.
#
# Release: v1.0.rc1
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
import os


def create_connection():
    connection = sqlite3.connect('systux.db')
    return connection


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacotes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)''')
    connection.commit()


def input_package(connection, nome_pacote):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO pacotes (nome) VALUES (?)", (nome_pacote,))
    connection.commit()
    print("Pacote inserido com sucesso!")


def purge_package(nome):
    conn = sqlite3.connect('systux.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pacotes WHERE nome = ?", (nome,))

    conn.commit()
    conn.close()


def download_package(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM pacotes")
    nomes_pacotes = cursor.fetchall()

    if nomes_pacotes:
        nomes_pacotes = [pacote[0] for pacote in nomes_pacotes]

        comando = ["sudo", "apt-get", "install", "-y"] + nomes_pacotes
        subprocess.run(comando)
        print("Packages successfully downloaded and installed!")
    else:
        os.system("clear")
        print("No packages found in database!")


def visualize_package(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pacotes")
    pacotes = cursor.fetchall()

    if pacotes:
        os.system("clear")
        print("Package names saved in the database:")
        for pacote in pacotes:
            print(pacote[1])
    else:
        os.system("clear")
        print("No packages found in database!")


def main():
    connection = create_connection()

    create_table(connection)

    while True:
        parser = argparse.ArgumentParser(prog='python3 systux.py', description="""Stores names of programs to be downloaded in the future,""")

        parser.add_argument('-d', action='store_true', help='Start downloading packages')
        parser.add_argument('-v', action='store_true', help='Visualize the database')
        parser.add_argument('-i', action='store_true', help='Insert package names to database')
        parser.add_argument('-V', '--version', action='version', version='SysTux 1.0.rc1')
        parser.add_argument('-L', action='store_true', help='Show software license')
        parser.add_argument('-p', '--purge', help='Pass by argument, name of the package to be deleted')

        args = parser.parse_args()
        
        if args.d:
            download_package(connection)
            break
        elif args.v:
            visualize_package(connection)
            break
        elif args.i:
            try:
                os.system("clear")
                print("Ctrl + C to exit")
                entry = input('package name >>>')
                input_package(connection, entry)
            except KeyboardInterrupt:
                break
        elif args.L:
            os.system("clear")
            print("GNU GPLv2.0 license for more details visit <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>")
            break
        elif args.purge:
            purge_package(args.purge)
            break
        else:
            os.system("clear")
            print("No arguments entered! >> usage: python3 systux.py [-h] [-d] [-v] [-i] [-V] [-L] [-p , --purge]")
            break
            
    connection.close()

if __name__ == '__main__':
    main()

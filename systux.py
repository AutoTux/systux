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

DB_NAME = 'systux.db'

def create_connection():
    connection = sqlite3.connect(DB_NAME)
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
    conn = sqlite3.connect(DB_NAME)
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

    parser = argparse.ArgumentParser(prog='systux', description="Stores names of programs to be downloaded in the future.")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Subcommand to insert a package
    insert_parser = subparsers.add_parser('insert', help='Insert package names to the database')
    insert_parser.add_argument('package_name', help='Name of the package to insert')

    # Subcommand to delete a package
    purge_parser = subparsers.add_parser('purge', help='Delete a package from the database')
    purge_parser.add_argument('package_name', help='Name of the package to delete')

    # Subcommand to download packages
    download_parser = subparsers.add_parser('download', help='Start downloading packages')

    # Subcommand to visualize the database
    visualize_parser = subparsers.add_parser('visualize', help='Visualize the database')

    args = parser.parse_args()

    if args.subcommand == 'insert':
        input_package(connection, args.package_name)
    elif args.subcommand == 'purge':
        purge_package(connection, args.package_name)
    elif args.subcommand == 'download':
        download_package(connection)
    elif args.subcommand == 'visualize':
        visualize_package(connection)
    else:
        print("No subcommand provided. Use 'systux -h' for help.")

    connection.close()

if __name__ == '__main__':
    main()

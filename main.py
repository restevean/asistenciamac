# Reformat TEAMS assistance meeting logs

import click
import csv
from csv import reader as readcsv
from parser import parse_row, parse_file_name


@click.command()
def asistencia():
    click.echo("Copyrigt© 2021 Rafael Esteve Antonino")
    click.echo("Todos los derechos reservados")

    while True:
        file = input("Introduce el nombre del archivo ('q' para salir): ")
        if file == "Q" or file == "q":
            break
        # controlamos la extensión del nombre de archivo, puede no llevarla o llevarla mal escrita
        file = parse_file_name(file)

        try:
            parsed_list = []
            with open(file, encoding="utf-16") as csvfile:
                # Lo leemos con csv.Reader()
                contenidocsv: readcsv = csv.reader(csvfile, dialect="excel-tab")
                click.echo("Leyendo lista...")
                parsed_list.append(['Nombre completo', 'Acción del usuario', 'Marca de tiempo'])
                next(contenidocsv)

                for linea in contenidocsv:
                    parsed_list.append(parse_row(linea))

            with open(f"N {file}", "w", encoding="utf-16") as csvFileOutput:
                # Lo escribimos con csv.Writer()
                writer = csv.writer(csvFileOutput)

                for line in parsed_list:
                    writer.writerow(line)

                click.echo("Hecho ;)")

        except FileNotFoundError:
            click.echo("**********************************")
            click.echo("*** No se encuentra el archivo ***")
            click.echo("**********************************")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asistencia()

import pytest
from parser import parse_row, parse_file_name


@pytest.mark.parametrize(
    'file_name, processed_file_name',
    [
        ('file', 'file.csv'),
        ('file.csv', 'file.csv'),
        ('2021-10-01', '2021-10-01.csv'),
        ('2021-10-01.csv', '2021-10-01.csv'),
        ('2021 Pepe', '2021 Pepe.csv'),
        ('2021 Pepe.csv', '2021 Pepe.csv')
    ]
)
def test_parse_file_name(file_name, processed_file_name):
    assert processed_file_name == parse_file_name(file_name)


@pytest.mark.parametrize(
    'row, processed_row',
    [
        (["MARIA JACQUELINE PALOMARES GAÑAN", "Abandonó", "10/1/2021, 2:27:05 PM"],
         ('MARIA JACQUELINE PALOMARES GAÑAN', 'Abandonó', '01/10/2021, 14:27:05')),
        (["MARIA JACQUELINE PALOMARES GAÑAN", "Abandonó", "10/1/2021, 11:47:48 AM"],
         ('MARIA JACQUELINE PALOMARES GAÑAN', 'Abandonó', '01/10/2021, 11:47:48'))
    ]
)
def test_parse_row(row, processed_row):
    assert processed_row == parse_row(row)


def test_parse_single_row():
    assert ('MARIA JACQUELINE PALOMARES GAÑAN', 'Abandonó', '01/10/2021, 11:47:48') == \
           parse_row(["MARIA JACQUELINE PALOMARES GAÑAN", "Abandonó", "10/1/2021, 11:47:48 AM"])

    assert ('MARIA JACQUELINE PALOMARES GAÑAN', 'Abandonó', '01/10/2021, 14:27:05') == \
           parse_row(["MARIA JACQUELINE PALOMARES GAÑAN", "Abandonó", "10/1/2021, 2:27:05 PM"])

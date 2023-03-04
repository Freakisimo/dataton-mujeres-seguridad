from dagster import asset

from data_integration.utils import download_files, unzip_files, \
    upload_s3_files, xlsx_to_csv


@asset
def get_c5_files() -> list:
    return download_files(
        url='https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5',
        path='/tmp/c5/',
        label='a',
        innertext='Descargar'
        )
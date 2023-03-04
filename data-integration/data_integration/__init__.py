from dagster import Definitions, load_assets_from_modules

from . import assets, scrapper

defs = Definitions(assets=load_assets_from_modules([assets,scrapper]))

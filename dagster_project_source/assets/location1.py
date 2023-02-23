from dagster import Definitions, asset
from dagster import define_asset_job

@asset
def code_location1_asset(context):
    data = list(range(10))
    context.log.info(data)
    return data

from dagster import AssetSelection, AssetKey
my_job = define_asset_job("my_job", selection=AssetSelection.keys(
    AssetKey('code_location1_asset')
))
defs = Definitions(
    assets=[code_location1_asset],
    jobs=[my_job]    
)
from dagster import AssetKey, Definitions, SourceAsset, asset

code_location1_source_asset = SourceAsset(key=AssetKey("code_location1_asset"))

@asset
def code_location2_asset(context, code_location1_asset):
    result = [val ** 2 for val in code_location1_asset]
    context.log.info(result)

    return result

defs = Definitions(
    assets=[code_location1_source_asset, code_location2_asset]
)
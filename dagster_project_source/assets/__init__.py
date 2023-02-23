# from dagster_dbt import load_assets_from_dbt_project
# from dagster import file_relative_path
# from dagster import job
# import time
# @job
# def start_job():
#     print(time.time())
    
# dbt_assets = load_assets_from_dbt_project(
#     project_dir= file_relative_path(__file__, "../../dbt_project_source"),
#     profiles_dir=file_relative_path(__file__, "../../")
# )

from .location2 import defs
from dagster_graphql import DagsterGraphQLClient

client = DagsterGraphQLClient(
    'admin:vinbdi@123@dev-dagster.vinbase.ai',
    use_https=True
)

from dagster_graphql import DagsterGraphQLClientError

try:
    new_run_id: str = client.submit_job_execution(
        'cb_stats_job',
        run_config={},
    )
    print(new_run_id)
except DagsterGraphQLClientError as exc:
    print(exc)
    raise exc
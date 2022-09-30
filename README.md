init db first - `docker-compose up airflow-init` \
then start other services - `docker-compose up -d`\

=======

So that we have no scheduled interval and catchup set to False
we need to unpause(start) both dags, then trigger `dag_one`
and it will trigger both `dag_two`
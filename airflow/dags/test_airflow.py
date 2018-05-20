import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'opsbuild',
    #'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    #'retries': 1,
    'retry_delay': timedelta(seconds=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('django-airflow', default_args=default_args, schedule_interval=None)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='succ_task',
    bash_command='echo "Trying task" && exit 0',
    retries=2,
    dag=dag)

t2 = BashOperator(
    task_id='vote',
    bash_command='/root/django-airflow/bin/python /root/django_airflow_tutorial/manage.py vote',
    retries=3,
    dag=dag)

t2.set_upstream(t1)

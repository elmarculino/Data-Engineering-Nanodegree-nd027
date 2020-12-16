from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tests=[{ 'query': None, 'result': 0 }],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.tests = tests
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        for dic in self.tests:
            query, result = (dic[k] for k in ('query','result'))
            if query is not None:
                records = redshift.get_records(query)
                if len(records) < 1 or len(records[0]) < 1:
                    raise ValueError(f"Data quality check failed. Query returned no results")
                    
                actual_result = records[0][0]
                if actual_result != result:
                    raise ValueError(f"Data quality check failed. Result {actual_result} different than expected {result}")
        
                self.log.info(f"Data quality test passed with the expected result: {actual_result}")

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    
    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_statement="",
                 delete_load=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.sql_statement = sql_statement
        self.delete_load = delete_load

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.delete_load:
            self.log.info("Clearing data from destination Dimension table")
            redshift.run(f"TRUNCATE TABLE {self.table}")
        
        self.log.info("Copying data from Stage table to a Dimension table")
        redshift.run(f"INSERT INTO {self.table} {self.sql_statement}")
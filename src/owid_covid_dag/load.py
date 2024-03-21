from google.cloud import bigquery
from pandas import DataFrame

class Load:
    def __init__(self, dataframe: DataFrame) -> None:
        self.dataframe = dataframe

    def load(self) -> None:
        #connect to BigQuery
        client = bigquery.Client()

        table_id = "airflow-417805.testdata.test00001"
        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")
        job = client.load_table_from_dataframe(
            self.dataframe,
            table_id,
            job_config=job_config
        ) 
        job.result()  
        table = client.get_table(table_id)
        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_id
            )
        )
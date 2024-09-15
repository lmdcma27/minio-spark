from minio import Minio
import io
import pandas as pd

client = Minio(
    "localhost:9000",
    access_key="Nyy86oIKdTOA4HqTAast",
    secret_key="iALsidLdjQbTNh5T3jZI870exdJa6WOiwuPAIm67",
    secure=False
)



objects=client.list_objects("orders")
for object in objects:
    file_name=object.object_name    
    break
response=client.get_object('orders',file_name)

df = pd.read_json(io.BytesIO(response.read()))
print(df)

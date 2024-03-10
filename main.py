import url_query
import dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


dotenv.load_dotenv()

docs  = SimpleDirectoryReader("data").load_data()
index= VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine()
response = query_engine.query(""" Please provide the following details in json: 
                             
1.	Title 	(title of project/tender)
2.	Description (description of the project. easy to read and concise)
3.	Status	(project or tender's current status)
4.	Stages
5.	Date(The date on which the information contained in the release was first recorded in, or published by, any system)
6.	ProcurementMethod 	(The procurement method is the procedure used to purchase the relevant works,goods or services.)
7.	Budget	(total cost or upper value in procurement)
8.  Map coordiantes [Geo Point of the region. Should be formatted like this. {"coordinates":[longitude,latitude]}(vlaues are expected in geojson format)]                           
8.	Currency (The currency code from ISO4217)                          
9.  Country Name  (Region Name for a Country according to World Bank Standards)
10. Country Code   
                           
10.	Sector	(Use of UN COFOG codes)
11.	Subsector (further division of sector)

if any of the above information is not available then return no specific data available	
                              
"""  )


print(response)




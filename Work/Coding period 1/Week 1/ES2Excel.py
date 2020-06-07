from elasticsearch import Elasticsearch
import csv
import pandas as pd
import requests
import json
"""
Input: enriched aliased index
Output: CSV (merged_output.csv),Excel(merged_output.xlsx), Airtable Speadsheet
containing 5 headers namely:"id","channel",context","body","grimoire_creation_date"
"""


def search():
	
	es = Elasticsearch()

	res = es.search(index="all_scms", body={"query": {"match_all": {}}},size=1200)
	dict_data=[]
	
	for hit in res['hits']['hits']:
		dict_data.append(hit['_source'])

	arr_id=[]
	arr_grimoire_creation_date=[]
	arr_context=[]
	arr_body=[]
	arr_channel=[]

	for data in dict_data:	
		arr_id.append(data["id"])
		arr_grimoire_creation_date.append(data["grimoire_creation_date"])
		arr_context.append(data["context"])
		arr_body.append(data["body"])
		arr_channel.append(data["data_source"])

	df=pd.DataFrame({
		'id':arr_id,
		'grimoire_creation_date':arr_grimoire_creation_date,
		'context':arr_context,
		'body':arr_body,
		'channel':arr_channel
		})

	convert_csv(df)
	convert_xlsx(df)
	convert_airtable(df)

def convert_csv(df):
	df.to_csv(csv_file_name,index=None)
	print("Output CSV file is "+csv_file_name)
def convert_xlsx(df):
	df.to_excel(xls_file_name, index=None)
	print("Output XLS file is "+xls_file_name)

def convert_airtable(df):

	post_url = 'https://api.airtable.com/v0/appPmJ0Mbq7tz5yHP/Table2'
	post_headers = {
	    'Authorization' : 'Bearer keylwWqsUb27EACcv',
	    'Content-Type': 'application/json'
	}
	for ind in df.index: 
		id_index=df['id'][ind]
		grimoire_creation_date=df['grimoire_creation_date'][ind]
		context=df['context'][ind]
		body=df['body'][ind]
		channel=df['channel'][ind]	

		data = {
			"fields": {
				"id":id_index,
				"grimoire_creation_date":grimoire_creation_date,
				"context":context,
				"body":body,
				"channel":channel
		        }
		    }

		post_airtable_request = requests.post(post_url, headers = post_headers, json = data)
		print(post_airtable_request.status_code)
	if (post_airtable_request.status_code ==200):
		print("Data successfully exported to Airtable " )



def main():
	global csv_file_name,xls_file_name 
	filename="merged_output"
	csv_file_name= filename+".csv"
	xls_file_name= filename+".xlsx"
	search()
	print("Finished")

if __name__ == "__main__":
    main()

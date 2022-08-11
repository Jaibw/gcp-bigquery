from google.cloud import bigquery 

client = bigquery.Client() 
query = '''
SELECT name, SUM(number) as total_people
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE state = 'TX'
GROUP BY name, state
ORDER BY total_people DESC
LIMIT 20
'''

results = client.query(query)
for x1 in results:
  print(x1)

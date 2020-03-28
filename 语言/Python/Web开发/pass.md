## MVC模型—视图—控制器模式

用来设计Web应用

```python
def put_to_store(file_list):
	ath = get_coach_data(each_file)
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes = {}
	all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle','Web') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print('File error(put_and_store):' + str(ioerr))
	return(all_athletes)

def get_fron_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error(put_and_store):' + str(ioerr))
	return(all_athletes)
```

​	
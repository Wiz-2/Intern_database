# Intern_database

At first, you must do 
```pip install sqlalchemy psycopg2```

After that 
```sudo service postgresql start```
Now, in the prompt create:-

```CREATE DATABASE students_marks;```
```CREATE USER me WITH PASSWORD 'stydent_marks';```

And then,
```GRANT ALL PRIVILEGES ON DATABASE myproductdb TO myuser;```


After that run 
```python data.py```.

And you must see the prompt like this :-
![image](https://github.com/user-attachments/assets/bed8750b-1eac-4dff-a73f-ba23254579f8)


After that you enter 1 to add a new student to the database, or select 2 to display the info.

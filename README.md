# Intern_database

At first, you must do 
```pip install sqlalchemy psycopg2```

After that 
```sudo service postgresql start```
Now, in the prompt create:-

```CREATE DATABASE students_marks;```
```CREATE USER me WITH PASSWORD 'student_marks';```

And then,
```GRANT ALL PRIVILEGES ON DATABASE student_marks TO me;```


After that run 
```python data.py```.

And you must see the prompt like this :-
![image](https://github.com/user-attachments/assets/bed8750b-1eac-4dff-a73f-ba23254579f8)


After that you enter 1 to add a new student to the database, or select 2 to display the info.

The sample input and output in my case is shown below:-

![Screenshot_output](https://github.com/user-attachments/assets/88765d44-33ad-47b1-8d54-96efa9df0b46)

The output with the correct code for rank is given below:-

![image](https://github.com/user-attachments/assets/5bbf248a-8f8f-4a85-abd9-10307a707937)


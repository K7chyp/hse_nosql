# Структура базы данных
## Таблицы 
### students
Хранит данные о студентах.
```
{
  _id: ObjectId,
  name: String,
  email: String,
  group_id: ObjectId, // Ссылка на группу
  department_id: ObjectId // Ссылка на факультет
}
```
### teachers
Содержит информацию о преподавателях.
```
{
  _id: ObjectId,
  name: String,
  department_id: ObjectId // Ссылка на факультет
}
```

### courses
Описывает учебные курсы.
```
{
  _id: ObjectId,
  name: String,
  teacher_id: ObjectId, // Ссылка на преподавателя
  department_id: ObjectId,
  semester: Number,
  year: Number
}
```

### grades
Фиксирует оценки студентов.
```
{
  _id: ObjectId,
  student_id: ObjectId,
  course_id: ObjectId,
  grade: Number,
  date: Date
}
```

### departments
Список факультетов.
```
{
  _id: ObjectId,
  name: String
}
```
### groups
Учебные группы.
```
{
  _id: ObjectId,
  name: String,
  department_id: ObjectId
}
```

# Индексы 
Они создаются одинаково, поэтому просто сделал для всех вот так
![alt text](image-15.png)

- grades.student_id (поиск оценок студента).
- grades.course_id (поиск оценок по курсу).
- students.group_id (фильтрация студентов по группе).
- courses.teacher_id (поиск курсов преподавателя).
- Составной индекс grades.student_id + grades.course_id 

# Типовые запросы
PS Данные синтетические (поэтому выглядят странно). Генерацию можно посмотреть в ./data_generator.py
## Топ-5 студентов факультета по среднему баллу
Можем взять любой факультет (Я взял айдишку полиметала)
![alt text](image-1.png)
Потом считатем 
![alt text](image-2.png)
## Посмотреть сколько студентов ходят на курсы
![alt text](image-3.png)
## Посмотреть какие оценки на курсе
Берем айдишку курса. Я взял (Поэтапная и направленная политика)
![alt text](image-4.png)
![alt text](image-5.png)
## Посмотреть сколько стуентов у преподаваталей
![alt text](image-6.png)
## Посмотреть у каких студентов нет оценок 
У всех есть!
![alt text](image-7.png)
## Посмотреть статистику по факультетам 
![alt text](image-8.png)
## Посмотреть успеваемость по семестрам 
![alt text](image-9.png)
## Поискать аномалии в оценках с помощью трех сигм
![alt text](image-10.png)
## Можно обновить расписание 
### как было 
![alt text](image-11.png)
### исполняем 
![alt text](image-12.png)
### получаем 
![alt text](image-13.png)
### Самые популярные курсы 
![alt text](image-14.png)
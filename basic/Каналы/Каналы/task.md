# Standard channels

`В UNIX всё - файл`.  

Экран, клавиатура, сетевое соединение, устройство - файл.
Что это означает? Как минимум:
1. Его можно прочитать, и в него можно записать. Файл имеет потоки ввода и вывода. 
2. Файл имеет местоположение, путь к нему в файловой системе.
3. Файл можно создать, удалить. 
4. Файл имеет права доступа. Кто-то может читать, кто-то может редактировать, кто-то может создать и удалить. 

Тогда вопрос. Как можно обменяться информацией с файлом?

Откроем терминал и введём:   

```shell
echo "Это сообщение"
```
  
Нажмём `Enter`. Команда выполниться, мы увидим на экране наше сообщение.

Что произошло? Мы запустили команду в командном процессоре. 
Его ещё называют командной строкой, терминалом.

Это программа, она вызывает функции ядра операционной системы, 
предоставляя пользователю набор команд. Сейчас мы используем программу, которая называется **bash**. 

Командный процессор, получает строку, которую вы ввели, интерпретирует её, выделяет команду и параметры, после чего выполняет команду.

`echo` - одна из команд командного процессора. Она вызвана с параметром `"Это сообщение"`. Назначение этой команды - вывод строки. 

Куда выводится строка? В канал стандартного вывода. Для этой команды, по умолчанию, канал стандартного вывода - экран терминала.

Запуская команды мы создаём процесс исполнения. Каждому процессу ядро назначает три коммуникационных канала:
- STDIN (стандартный ввод)
- STDOUT (стандартный вывод)
- STDERR (стандартная ошибка)

Чтобы отправить или получить данные, процесс использует соответствующий канал.

Важно, что процесс не знает, куда направлены данные, а значит не может сделать ничего, чтобы подстроиться под это подключение.

Задача управления потоком лежит на программисте, при вызове команды он конфигурирует команду с помощью параметров - опций (еще их называют флаги)

Каналу назначается файл в качестве источника или приёмника данных. 
Консольный ввод, консольный вывод, порт принтера, файл файловой системы - всё это может быть назначено каналом ввода или вывода.

Для адресации файлов используется модель UNIX, где каждый файл описывается числом, называемым `file descriptor`.
Для STDIN, STDOUT, STDERR назначены файловые дескрипторы 0, 1, 2.

Большинство команд способны получить данные через канал STDIN, вывести данные в канал STDOUT, вывести сообщения об ошибках в канал STDERR.

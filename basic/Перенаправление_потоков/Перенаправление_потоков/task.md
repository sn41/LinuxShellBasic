# Перенаправление потоков данных

Потоки можно перенаправить.  
Для этого используются команды перенаправления, обозначаемые символами `>`, `<`, `>>`, `|`.

- Символ `<` перенаправляет стандартный поток ввода STDIN,  
- Символы `>`, `>>` перенаправляют потоки вывода STDOUT и STDERR, при этом, 
  - `>` переписывает начальное содержимое файла, 
  - `>>` добавляет данные,  
  - `2>` перенаправляет поток с заданным номером (2 - это поток ошибок STDERR) 
  - `>&` перенаправляет все потоки вывода, и STDOUT и STDERR.

-  Символ `|` (pipe - поток, труба), используется, для перенаправления потока вывода STDOUT одной программы в поток ввода


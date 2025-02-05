if  [ условие ]
then
  команды, которые должны быть выполнены, если указанное условие окажется верным
fi


При использовании условных конструкций важно ставить пробелы вокруг операторов сравнения. Если этого не сделать, то скрипт будет воспринимать ее как одиночную строку, а не как операцию сравнения.

Пример:

#!/bin/bash
echo "Enter the number: "
read num
if (( $num % 2 == 0 ))
then
  echo "Number $num is even"
else
  echo "Number $num is odd"
fi



Также в условных конструкциях можно использовать следующие операторы сравнения:

-gt — больше,
-lt — меньше,
-eq — равно,
-ne — не равно,
-ge — больше или равно,
-le — меньше или равно.


Пример:


#!/bin/bash
echo "Enter the first number: "
read num1
echo "Enter the second number: "
read num2
if [ $num1 -lt $num2 ]
then
  echo "$num1 is less than $num2"
fi
if [ $num1 -gt $num2 ]
then
  echo "$num1 is greater than $num2"
fi
if [ $num1 -eq $num2 ]
then
  echo "$num1 is equal to $num2"
fi


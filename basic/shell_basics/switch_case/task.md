Синтаксис конструкции switch-case выглядит следующим образом:
~~~
case variable in
    condition1)
        command
        ;;
    condition2)
        command
        ;;
       *)
        default command
        ;;
esac
~~~


где:

variable — переменная, которую необходимо проверить,
condition — возможное значение, которое необходимо проверить,
command — команды, которые необходимо выполнить в зависимости от значения переменной,
* — обработчик, который будет использоваться, если ни одно из значений не соответствует переменной.


Пример скрипта, который определяет официальный язык страны по ее названию:

#!/bin/bash
echo -n "Enter the name of a country: "
read COUNTRY
echo -n "The official language of $COUNTRY is "
case $COUNTRY in
  Russia)
    echo -n "Russian"
    ;;
 Kazakhstan)
    echo -n "Kazakh"
    ;;
  Italia)
    echo -n "Italian"
    ;;
  *)
    echo -n "unknown"
    ;;
esac

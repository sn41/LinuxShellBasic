## Конструкция switch-case

Синтаксис конструкции switch-case выглядит следующим образом:
```shell
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
```
Где:

`variable` — переменная, которую необходимо проверить,
`condition` — дискретные условия, например: `condition1|condition2`, в каждом условии операторы заканчиваются знаком `;;`  
`command` — команды, которые необходимо выполнить в зависимости от значения переменной,
`*` — обработчик, который будет использоваться, если ни одно из значений не соответствует переменной.


Пример скрипта, который определяет официальный язык страны по ее названию:
```shell
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
```
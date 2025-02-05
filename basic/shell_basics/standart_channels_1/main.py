# echo "Это сообщение"
# echo Это сообщение
# echo Это сообщение > /tmp/mymessage
# echo Это сообщение > ~/mymessage
# echo Это сообщение > ~/tmp/mymessage
# cat /tmp/mymessage > ~/mymessage1
# find / -name core
# find / -name core 2> ~/finderr
# find / -name core > ~/findmessage 2> ~/finderr
# find / -name core >& /dev/null
# ps -ef
# ps -ef|grep httpd
# echo -e "Winter: white: snow: frost\nSpring: green: grass: warm\nSummer: colorful: blossom: hot\nAutumn: yellow: leaves: cool" > ~/example.txt
# echo "The sky was yellow as brass." | cut -b 1
# echo "I looked at my watch; not eight o'clock." | cut -b 5,8,17
# echo "Still I opened the gate, and put the petrol pump in readiness." | cut -b 1-7
# echo "Still" | cut -b 1-1000
# echo "Still I opened the gate, and put the petrol pump in readiness." | cut -b 6-
# echo "Стренжерс ин ве найт..." | cut -b 1-9
# echo "Стренжерс ин ве найт..." | cut -c 1-9
# cut -b 1-9 example.txt
# cut -b 1-9 example.txt | sort
# cut -b 1-9 example.txt | sort -r
# echo "From the inn issued a smell of frying liver." | cut -d ' ' -f 1
# cut -d ':' -f 1 example.txt
# cut -d ':' -f 1,2 example.txt
# cut -d ':' -f 1-40 example.txt
# cut -d ':' -f 1 example.txt| sort
# cut -d ':' -f 1 example.txt|  sort | awk '{print NR,$0}'
# cat ~/example.txt && rm ~/example.txt
# cat ~/example.txt 2>/dev/null || echo "Такой файл отсутствует"
# my_variable_home_dir='~/'
# echo $my_variable_home_dir

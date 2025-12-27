TASKS_MEDIUM = [
    # --- Работа с архивами (флаги и специфика) ---
    {"prompt": "Создать сжатый архив tar.gz из папки 'data' с подробным выводом (verbose).", "answers": ["tar -cvzf data.tar.gz data"]},
    {"prompt": "Распаковать архив 'backup.tar.gz' в конкретную папку /tmp/restore.", "answers": ["tar -xzf backup.tar.gz -C /tmp/restore"]},
    {"prompt": "Посмотреть содержимое архива 'files.tar.gz' без его распаковки.", "answers": ["tar -tf files.tar.gz"]},
    {"prompt": "Создать архив папки 'project', исключив из него подпапку 'node_modules'.", "answers": ["tar --exclude='node_modules' -czf project.tar.gz project"]},
    {"prompt": "Добавить новый файл 'extra.txt' в уже существующий (не сжатый) tar-архив.", "answers": ["tar -rf archive.tar extra.txt"]},
    {"prompt": "Распаковать только один конкретный файл 'config.json' из большого архива 'all.tar'.", "answers": ["tar -xf all.tar config.json"]},
    {"prompt": "Создать простой архив 'site.tar' (без сжатия) из нескольких папок: 'html' и 'css'.", "answers": ["tar -cf site.tar html css"]},

    # --- Поиск файлов и текста (фильтры и параметры) ---
    {"prompt": "Найти все файлы в /etc, которые заканчиваются на '.conf'.", "answers": ["find /etc -name '*.conf'"]},
    {"prompt": "Найти в текущей папке файлы размером ровно 10 Мегабайт.", "answers": ["find . -size 10M"]},
    {"prompt": "Найти в текущей папке файлы размером более 100 Мегабайт.", "answers": ["find . -size +100M"]},
    {"prompt": "Найти все файлы, которые были изменены за последние 24 часа.", "answers": ["find . -mtime -1"]},
    {"prompt": "Найти строку 'error' в логе, игнорируя регистр (Error, ERROR).", "answers": ["grep -i 'error' app.log"]},
    {"prompt": "Вывести количество строк, в которых встречается слово 'FAIL' в файле 'results.txt'.", "answers": ["grep -c 'FAIL' results.txt"]},
    {"prompt": "Найти рекурсивно во всех файлах папки /var/log текст '192.168.1.1'.", "answers": ["grep -r '192.168.1.1' /var/log"]},
    {"prompt": "Вывести строки из файла, которые НЕ содержат слово 'DEBUG'.", "answers": ["grep -v 'DEBUG' system.log"]},
    {"prompt": "Найти все пустые файлы в текущей директории.", "answers": ["find . -type f -empty"]},
    {"prompt": "Найти файл 'main.py' только в текущей директории, не заходя в подпапки.", "answers": ["find . -maxdepth 1 -name 'main.py'"]},

    # --- Обработка текста (Pipes и базовый инструментарий) ---
    {"prompt": "Вывести 15-ю строку файла 'data.txt' (используя sed).", "answers": ["sed -n '15p' data.txt"]},
    {"prompt": "Заменить все вхождения 'http' на 'https' в файле (вывод в консоль).", "answers": ["sed 's/http/https/g' links.txt"]},
    {"prompt": "Удалить все пустые строки в файле 'text.txt' через sed (вывод в консоль).", "answers": ["sed '/^$/d' text.txt"]},
    {"prompt": "Вывести только второй столбец из вывода команды 'df -h' (через awk).", "answers": ["df -h | awk '{print $2}'"]},
    {"prompt": "Посчитать общее количество файлов в текущей директории (через ls и wc).", "answers": ["ls | wc -l"]},
    {"prompt": "Вывести 5 самых больших файлов в папке (через du, sort и head).", "answers": ["du -sh * | sort -rh | head -n 5"]},
    {"prompt": "Показать только уникальные строки из файла, предварительно отсортировав его.", "answers": ["sort file.txt | uniq"]},
    {"prompt": "Вырезать первые 5 символов из каждой строки файла 'keys.txt'.", "answers": ["cut -c 1-5 keys.txt"]},
    {"prompt": "Объединить два файла 'part1.txt' и 'part2.txt' в один новый 'full.txt'.", "answers": ["cat part1.txt part2.txt > full.txt"]},

    # --- Права доступа (Числовые и символьные) ---
    {"prompt": "Установить права '644' (rw-r--r--) на файл 'config.yml'.", "answers": ["chmod 644 config.yml"]},
    {"prompt": "Сделать скрипт 'build.sh' исполняемым для всех пользователей.", "answers": ["chmod +x build.sh", "chmod 755 build.sh"]},
    {"prompt": "Рекурсивно сменить владельца папки /var/www на пользователя 'www-data'.", "answers": ["chown -R www-data /var/www"]},
    {"prompt": "Убрать у группы и остальных права на чтение файла 'private.key'.", "answers": ["chmod go-r private.key"]},
    {"prompt": "Установить права '700' на папку '.ssh' (чтение/запись/доступ только владельцу).", "answers": ["chmod 700 .ssh"]},
    {"prompt": "Сменить группу файла 'test.log' на 'developers'.", "answers": ["chgrp developers test.log"]},

    # --- Процессы и мониторинг ---
    {"prompt": "Найти PID процесса, который называется 'nginx'.", "answers": ["pgrep nginx", "pidof nginx"]},
    {"prompt": "Показать дерево процессов.", "answers": ["pstree"]},
    {"prompt": "Завершить процесс по его имени 'firefox' (сигналом по умолчанию).", "answers": ["pkill firefox", "killall firefox"]},
    {"prompt": "Посмотреть подробную информацию о процессе с конкретным PID 1234.", "answers": ["ps -p 1234 -u"]},
    {"prompt": "Отправить сигнал принудительного завершения (SIGKILL) процессу с PID 987.", "answers": ["kill -9 987"]},
    {"prompt": "Посмотреть, сколько памяти потребляют процессы (статический список, сортировка по памяти).", "answers": ["ps aux --sort=-%mem"]},

    # --- Сеть и передача данных ---
    {"prompt": "Проверить, открыт ли порт 80 на хосте 'localhost' (через nc).", "answers": ["nc -zv localhost 80"]},
    {"prompt": "Показать все слушающие порты (TCP/UDP) с именами программ.", "answers": ["ss -lptn", "netstat -lptn"]},
    {"prompt": "Скачать файл из интернета и сохранить под конкретным именем 'setup.sh'.", "answers": ["curl -o setup.sh URL", "wget -O setup.sh URL"]},
    {"prompt": "Скопировать файл 'app.js' на удаленный сервер по пути /tmp/.", "answers": ["scp app.js user@host:/tmp/"]},
    {"prompt": "Подключиться к удаленному серверу по SSH на порт 2222.", "answers": ["ssh -p 2222 user@host"]},
    {"prompt": "Показать таблицу маршрутизации.", "answers": ["ip route", "route -n"]},

    # --- Планировщик (Cron) ---
    {"prompt": "Cron: настроить запуск задачи каждые 15 минут.", "answers": ["*/15 * * * *"]},
    {"prompt": "Cron: настроить запуск скрипта в 4:30 утра каждый день.", "answers": ["30 4 * * *"]},
    {"prompt": "Cron: запускать задачу только по субботам.", "answers": ["0 0 * * 6"]},
    {"prompt": "Cron: направить стандартный вывод (stdout) задачи в файл log.txt (перезапись).", "answers": ["> log.txt"]},

    # --- Система и Диски ---
    {"prompt": "Показать список всех дисков и их разделов.", "answers": ["lsblk"]},
    {"prompt": "Показать размер каждой папки в текущей директории (сумма по папке).", "answers": ["du -sh *"]},
    {"prompt": "Показать информацию о версии операционной системы (из /etc/issue или os-release).", "answers": ["cat /etc/os-release"]},
    {"prompt": "Показать последние 20 строк системного журнала ядра.", "answers": ["dmesg | tail -n 20"]},
    {"prompt": "Посмотреть текущие лимиты пользователя (открытые файлы и т.д.).", "answers": ["ulimit -a"]},

    # --- Переменные и Bash ---
    {"prompt": "Создать временный алиас 'll' для команды 'ls -la'.", "answers": ["alias ll='ls -la'"]},
    {"prompt": "Вывести значение системной переменной PATH.", "answers": ["echo $PATH"]},
    {"prompt": "Дописать результат команды 'date' в конец существующего файла 'log.txt'.", "answers": ["date >> log.txt"]},
    {"prompt": "Перенаправить только ошибки (stderr) в файл 'error.log'.", "answers": ["command 2> error.log"]},
    {"prompt": "Выполнить команду и подавить вывод ошибок (отправить в никуда).", "answers": ["command 2> /dev/null"]},
    {"prompt": "Создать структуру папок project/src и project/bin одной командой.", "answers": ["mkdir -p project/src project/bin"]},
    {"prompt": "Посмотреть, где находится бинарный файл команды 'grep'.", "answers": ["which grep"]}
]
TASKS_MEDIUM = [
    # --- Архивация и сжатие (tar, gzip) ---
    {"prompt": "Создать tar.gz архив с подробным выводом из папки data.", "answers": ["tar -cvzf data.tar.gz data"]},
    {"prompt": "Посмотреть содержимое tar.gz архива без распаковки.", "answers": ["tar -tf data.tar.gz"]},
    {"prompt": "Распаковать tar.gz в текущую директорию с подробным выводом.", "answers": ["tar -xvzf data.tar.gz"]},
    {"prompt": "Распаковать archive.tar в конкретную директорию /tmp/backup.", "answers": ["tar -xf archive.tar -C /tmp/backup"]},
    {"prompt": "Добавить файл a.txt в существующий (не сжатый) archive.tar.", "answers": ["tar -rf archive.tar a.txt"]},
    {"prompt": "Создать архив, исключив из него папку .git.", "answers": ["tar -cf archive.tar project --exclude=.git"]},
    {"prompt": "Создать архив из файлов, перечисленных в текстовом списке list.txt.", "answers": ["tar -cf archive.tar -T list.txt"]},
    {"prompt": "Создать простой tar-архив всех .log файлов в текущей папке.", "answers": ["tar -cf logs.tar *.log"]},

    # --- Поиск и фильтрация (grep, find, wc) ---
    {"prompt": "Найти строки с ERROR в log.txt (регистр не важен).", "answers": ["grep -i error log.txt"]},
    {"prompt": "Найти строки, НЕ содержащие слово error в log.txt.", "answers": ["grep -v error log.txt"]},
    {"prompt": "Посчитать количество строк со словом error в log.txt.", "answers": ["grep -c error log.txt", "grep error log.txt | wc -l"]},
    {"prompt": "Найти все файлы с расширением .conf в текущей директории и подпапках.", "answers": ["find . -name '*.conf'"]},
    {"prompt": "Найти все директории с именем logs.", "answers": ["find . -type d -name logs"]},
    {"prompt": "Найти файлы крупнее 100МБ в текущей директории.", "answers": ["find . -size +100M"]},
    {"prompt": "Посчитать общее количество файлов в текущей директории.", "answers": ["ls | wc -l"]},
    {"prompt": "Найти файл config.yml только в текущей директории (без поддиректорий).", "answers": ["find . -maxdepth 1 -name config.yml"]},

    # --- Обработка текста (sed, awk, sort, uniq) ---
    {"prompt": "Показать только уникальные строки из file.txt (после сортировки).", "answers": ["sort file.txt | uniq"]},
    {"prompt": "Заменить все foo на bar в file.txt и вывести результат.", "answers": ["sed 's/foo/bar/g' file.txt"]},
    {"prompt": "Удалить все пустые строки в файле file.txt и вывести результат.", "answers": ["sed '/^$/d' file.txt"]},
    {"prompt": "Показать строки с 5-й по 10-ю в файле file.txt.", "answers": ["sed -n '5,10p' file.txt"]},
    {"prompt": "Вывести только третий столбец из файла data.txt.", "answers": ["awk '{print $3}' data.txt"]},
    {"prompt": "Вывести строки из data.txt, где во втором столбце значение больше 100.", "answers": ["awk '$2 > 100' data.txt"]},
    {"prompt": "Показать последние 50 строк файла log.txt.", "answers": ["tail -n 50 log.txt"]},
    {"prompt": "Показать первые 20 строк файла log.txt.", "answers": ["head -n 20 log.txt"]},
    {"prompt": "Инвертировать порядок строк в файле (последняя станет первой).", "answers": ["tac file.txt"]},

    # --- Права доступа и файловая система ---
    {"prompt": "Сделать файл script.sh исполняемым.", "answers": ["chmod +x script.sh"]},
    {"prompt": "Установить права 644 для файла file.txt.", "answers": ["chmod 644 file.txt"]},
    {"prompt": "Сменить владельца файла на user и группу на group.", "answers": ["chown user:group file"]},
    {"prompt": "Убрать право на запись у группы для файла file.txt.", "answers": ["chmod g-w file.txt"]},
    {"prompt": "Показать размер директории data в человекочитаемом виде.", "answers": ["du -sh data"]},
    {"prompt": "Показать свободное место на дисках в человекочитаемом виде.", "answers": ["df -h"]},
    {"prompt": "Показать скрытые файлы в текущей директории.", "answers": ["ls -a"]},
    {"prompt": "Показать права и владельца файла script.sh.", "answers": ["ls -l script.sh"]},
    {"prompt": "Создать символическую ссылку link на файл target.", "answers": ["ln -s target link"]},

    # --- Процессы и мониторинг системы ---
    {"prompt": "Показать PID всех процессов bash.", "answers": ["pgrep bash"]},
    {"prompt": "Показать дерево процессов.", "answers": ["pstree"]},
    {"prompt": "Завершить процесс с PID 1234 (сигнал SIGTERM).", "answers": ["kill 1234"]},
    {"prompt": "Принудительно завершить процесс с PID 1234 (сигнал SIGKILL).", "answers": ["kill -9 1234"]},
    {"prompt": "Показать подробную информацию о процессе с PID 1234.", "answers": ["ps -fp 1234"]},
    {"prompt": "Найти и завершить все процессы с именем nginx.", "answers": ["pkill nginx"]},
    {"prompt": "Показать текущую дату в формате ГГГГ-ММ-ДД.", "answers": ["date +%F"]},
    {"prompt": "Узнать полный путь до исполняемого файла команды python3.", "answers": ["which python3"]},
    {"prompt": "Показать список открытых файлов процессом (через PID).", "answers": ["lsof -p 1234"]},

    # --- Планировщик задач (Cron) ---
    {"prompt": "Cron: запуск задачи каждые 15 минут.", "answers": ["*/15 * * * *"]},
    {"prompt": "Cron: запуск каждый будний день в 09:30.", "answers": ["30 9 * * 1-5"]},
    {"prompt": "Cron: запуск 1-го числа каждого месяца в полночь.", "answers": ["0 0 1 * *"]},
    {"prompt": "Cron: запуск каждую субботу в 18:00.", "answers": ["0 18 * * 6"]},
    {"prompt": "Cron: запуск каждые 3 часа.", "answers": ["0 */3 * * *"]},
    {"prompt": "Cron: перенаправить стандартный вывод и ошибки в /tmp/cron.log.", "answers": ["> /tmp/cron.log 2>&1"]},
    {"prompt": "Cron: запуск скрипта backup.sh каждый день в 01:00.", "answers": ["0 1 * * * /home/user/backup.sh"]},

    # --- Сеть и SSH ---
    {"prompt": "Проверить доступность хоста google.com.", "answers": ["ping google.com"]},
    {"prompt": "Подключиться к серверу по SSH под пользователем admin.", "answers": ["ssh admin@server"]},
    {"prompt": "Скопировать локальный файл file.txt на сервер в папку /tmp.", "answers": ["scp file.txt user@server:/tmp"]},
    {"prompt": "Скопировать папку dir на удаленный сервер (рекурсивно).", "answers": ["scp -r dir user@server:/tmp"]},
    {"prompt": "Показать все активные сетевые соединения (порты).", "answers": ["ss -tulpn", "netstat -tulpn"]},
    {"prompt": "Загрузить файл по ссылке через терминал.", "answers": ["curl -O URL", "wget URL"]},

    # --- Окружение и Bash ---
    {"prompt": "Показать все текущие переменные окружения.", "answers": ["env", "printenv"]},
    {"prompt": "Показать значение переменной PATH.", "answers": ["echo $PATH"]},
    {"prompt": "Создать временный алиас 'll' для команды 'ls -la'.", "answers": ["alias ll='ls -la'"]},
    {"prompt": "Перенаправить только стандартную ошибку (stderr) в файл error.log.", "answers": ["2> error.log"]},
]
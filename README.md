# api_final
api final
Postman-коллекция для проверки API
Файл API_for_yatube.postman_collection.json содержит postman-коллекцию - набор заранее подготовленных запросов для проверки работы API.

Подготовка Django-проекта к запуску коллекции:
Проверьте, что виртуальное окружение развёрнуто и активировано, зависимости проекта установлены.
Перейдите в директорию postman_collection и командой `bash set_up_data.sh`` запустите bash-скрипт для создания необходимых для работы коллекции объектов в базе данных.
Внимание, скрипт предварительно очищает существующую базу данных.
Перейдите в директорию с файлом manage.py и запустите тестовый сервер.
Загрузка коллекции в Postman:
Запустите Postman;
В левом верхнем углу нажмите File -> Import;
Во всплывающем окне будет предложено перетащить в него файл с коллекцией либо выбрать файл через окно файлового менеджера. Загрузите файл API_for_yatube.postman_collection.json в Postman.
Запуск коллекции:
После выполнения предыдущих шагов, в левой части окна Postman во вкладке Collections появилась импортированная коллекция. Наведите на нее, нажмите на три точки напротив названия коллекции и в выпадающем списке выберите Run collection. В центре экрана появится список запросов коллекции, а в правой части экрана - меню для настройки параметров запуска;
В правом меню включите фунцию Persist responses for a session - это даст возможность посмотреть ответы API после запуска коллекции;
Нажмите кнопку Run <название коллекции>;
В центре экрана отобразится результат запуска коллекции и тестов. Провалившиеся тесты можно отфильтровать, перейдя во вкладку Failed. Посмотрите детали выполненного запроса и полученного ответа: для этого нажмите на тест.
Перед повторным запуском коллекции следует повторно запустить bash-скрипт - он очистит базу и создаст заново необходимые фикстуры.

P.S.: очистка базы данных от тестовых постов и комментариев в случае падения тестов не гарантирована.

Ограничения от разработчиков Postman
В бесплатной версии программы Postman есть техническое ограничение: коллекцию можно беспрепятственно запускать 25 раз в месяц.
После исчерпания этого лимита Postman не превратится в тыкву: он по-прежнему будет запускать коллекции, но запуск иногда будет блокироваться на 30 секунд (иногда дважды подряд), и в это время в интерфейсе программы будет появляться предложение приобрести платную версию.
Вы можете купить платную версию, а можете просто продолжить пользоваться бесплатной версией, время от времени прерываясь на просмотр рекламы.

Для отправки отдельных запросов никаких ограничений нет.
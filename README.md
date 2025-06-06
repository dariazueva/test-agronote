# test-agronote
Django Weather App

## Описание

Приложение для просмотра прогноза погоды по городам. Основано на Django и разворачивается с помощью Docker.

## Требования

- Python 3.12
- PostgreSQL
- Django
- OpenWeatherMap API
- Docker

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/test-agronote.git
cd weather_project
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

#### Создайте .env по образцу:
cp .env.example .env

#### Запустите систему контейнеров.
```bash
docker-compose -f docker/docker-compose.yml up --build
```
#### Выполните миграции в контейнере backend.
```bash
docker-compose -f docker/docker-compose.yml exec web python manage.py migrate
```
#### Создайте суперпользователя.
```bash
docker-compose -f docker/docker-compose.yml exec web python manage.py createsuperuser
```
#### Запустите тесты.
```bash
docker-compose -f docker/docker-compose.yml exec web python manage.py test weather 
```
#### Остановить контейнер.
```bash
docker-compose -f docker/docker-compose.yml down
```

## Структура проекта
```bash
weather_project/
├── .env
├── .env.example                       # Пример .env для разработки
├── docker/                            # Каталог с файлами для Docker'а
│   ├── Dockerfile                     # Инструкция сборки образа веб-приложения
│   └── docker-compose.yml             # Конфигурация для запуска контейнеров (web + db)
├── manage.py
├── requirements.txt                   # Файл с зависимостями Python
├── src/                               # Основной код проекта
│   ├── weather/                       # Django-приложение "weather"
│   │   ├── __init__.py
│   │   ├── admin.py                   # Админка для модели City
│   │   ├── apps.py
│   │   ├── forms.py                   # Django-форма для добавления города
│   │   ├── models.py                  # Модель City, хранит список городов
│   │   ├── urls.py                    # URL-маршруты для weather
│   │   ├── views.py                   # View-функции: отображение погоды, обработка формы
│   │   ├── templates/                 # Шаблоны HTML
│   │   │   └── weather/
│   │   │       └── index.html         # Главная страница с формой и результатами погоды
│   │   ├── tests/                     # Тесты для модели и view'ов
│   │   │   ├── test_models.py
│   │   │   └── test_views.py
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│
│   └── weather_project/              # Настройки проекта Django
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── .github/
    └── workflows/
        └── main.yml                    # CI-конфигурация GitHub Actions
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/
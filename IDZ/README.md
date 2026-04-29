# Word Counter

Консольний додаток на Python для підрахунку кількості слів у введеному тексті. Якщо текст порожній - кидається помилка `EmptyTextError`.

## Можливості

- Підрахунок слів з підтримкою Unicode (українська, англійська тощо).
- Коректна обробка пунктуації, апострофів, чисел, табуляцій та переносів рядків.
- Виняток `EmptyTextError` для порожнього вводу.
- Покриття unit-тестами та doctests.
- Перевірка форматування (black) та стилю (flake8).
- Перевірка вразливостей залежностей (pip-audit).
- Автоматичний CI на GitHub Actions.
- Інтеграція з Sentry для відстеження помилок у продакшені.

## Структура проєкту

```
word-counter/
├── src/
│   ├── word_counter.py
│   └── sentry_config.py
├── tests/
│   ├── test_word_counter.py
│   └── test_doctests.py
├── .github/workflows/ci.yml
├── Makefile
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .flake8
├── .pre-commit-config.yaml
├── .env.example
└── .gitignore
```

## Встановлення

```bash
git clone https://github.com/<your-username>/word-counter.git
cd word-counter

python3 -m venv .venv
source .venv/bin/activate

make install-dev
```

## Налаштування Sentry

1. Створіть проєкт на [sentry.io](https://sentry.io/).
2. Скопіюйте файл-приклад змінних оточення:
   ```bash
   cp .env.example .env
   ```
3. Відкрийте `.env` та вставте ваш DSN:
   ```
   SENTRY_DSN=https://<key>@<org>.ingest.sentry.io/<project>
   SENTRY_ENVIRONMENT=development
   ```

## Запуск додатку

```bash
make run
```

## Тестування

```bash
make test
```

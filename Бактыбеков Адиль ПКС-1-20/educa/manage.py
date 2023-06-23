import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "educa.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, что он установлен и "
            "доступно в вашей переменной окружения PYTHONPATH? Неужели ты "
            "забыли активировать виртуальную среду?"
        ) from exc
    execute_from_command_line(sys.argv)

# Поддерживаемая версия Python на Debian 13 (trixie), вариант slim
FROM python:3.13-slim-trixie
# Не создавать .pyc, сразу выводить логи, не хранить кэш pip
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
PIP_NO_CACHE_DIR=1 \
PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
# Системный пользователь без shell и без домашнего каталога
RUN groupadd --system --gid 10001 app \
&& useradd --system --uid 10001 --gid app \
--no-create-home --shell /usr/sbin/nologin app
# Сначала зависимости (слой лучше кэшируется), затем код
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /usr/local/lib/python3.13/site-packages/pip \
              /usr/local/lib/python3.13/site-packages/pip-*.dist-info \
              /usr/local/bin/pip \
              /usr/local/bin/pip3 \
              /usr/local/bin/pip3.13
# Код остается во владении root: процесс приложения
# сможет его читать, но не сможет изменить
COPY app.py .
USER app
EXPOSE 5000
# Проверка живости: Docker сам будет опрашивать /health
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
CMD ["python", "-c", \
"import urllib.request as u; u.urlopen('http://localhost:5000/health')"]
# Production WSGI-сервер вместо встроенного dev-сервера Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", \
"--access-logfile", "-", "app:app"]
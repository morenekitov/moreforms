# Серверный деплой moreforms

Этот каталог хранит безопасные deploy-артефакты для серверного контура:

- `docker-compose.yml` — контейнеры `streamlit`, `oauth2-proxy`, `caddy`, `openclaw`
- `streamlit.Dockerfile` — образ для текущего дашборда
- `Caddyfile` — reverse proxy и автоматический HTTPS
- `.env.example` — шаблон переменных окружения без секретов
- `scripts/server-sync.sh` — pull-and-restart сценарий для сервера

## Целевой контур

`Интернет -> Caddy -> oauth2-proxy (Google) -> Streamlit -> OpenClaw`

Ключевые принципы:

- публично открыт только `Caddy`
- `Streamlit` и `OpenClaw` живут во внутренней docker-сети
- доступ в приложение идет только после Google login через `oauth2-proxy`
- реальные секреты не хранятся в git

## Что нужно заполнить на сервере

1. Скопировать шаблон:

```bash
cp deploy/.env.example /srv/moreforms/runtime/.env
```

2. Заполнить в `/srv/moreforms/runtime/.env`:

- `APP_DOMAIN`
- `OAUTH2_PROXY_CLIENT_ID`
- `OAUTH2_PROXY_CLIENT_SECRET`
- `OAUTH2_PROXY_COOKIE_SECRET`
- `OAUTH2_PROXY_ALLOWED_EMAILS_FILE`
- `OPENCLAW_GATEWAY_TOKEN`
- при необходимости `OPENCLAW_IMAGE`

3. Создать файл allowlist для Google-логина, по одному email на строку:

```bash
mkdir -p /srv/moreforms/runtime/secrets
cat >/srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt <<'EOF'
you@example.com
teammate@example.com
EOF
chmod 600 /srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt
```

4. Запустить базовый контур:

```bash
cd /srv/moreforms/deploy/repo/deploy
docker compose --env-file /srv/moreforms/runtime/.env up -d --build
```

5. Когда будет готов образ/способ установки OpenClaw, поднять и его:

```bash
cd /srv/moreforms/deploy/repo/deploy
docker compose --env-file /srv/moreforms/runtime/.env --profile openclaw up -d --build
```

## Google OAuth

Для `oauth2-proxy` нужен redirect URI:

```text
https://app.moreforms.ru/oauth2/callback
```

## OpenClaw

Текущий шаблон рассчитывает на совместимый gateway endpoint:

```text
http://openclaw-gateway:18789/v1/responses
```

и на gateway token в `Authorization: Bearer ...`.

Контейнер `openclaw-gateway` в `docker-compose.yml` оставлен как production scaffold и вынесен в профиль `openclaw`. Перед боевым запуском нужно:

- либо использовать готовый образ/сборку OpenClaw,
- либо заменить сервис на тот способ установки, который ты выберешь по официальной документации.

## Git sync

`scripts/server-sync.sh` рассчитан на серверный clone в:

```text
/srv/moreforms/deploy/repo
```

Сценарий:

- делает `git fetch`
- fast-forward на `origin/main`
- перезапускает контейнеры через `docker compose up -d --build`
- если задан `COMPOSE_PROFILE=openclaw`, включает профиль OpenClaw

Его удобно вызывать из webhook handler или по cron.

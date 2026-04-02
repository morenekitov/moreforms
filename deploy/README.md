# Серверный деплой moreforms v1

Текущий production contour:

`Интернет -> Caddy -> oauth2-proxy (Google) -> Streamlit -> API -> PostgreSQL`

## Контейнеры

- `postgres` — основная БД
- `api` — FastAPI backend
- `streamlit` — read dashboard
- `oauth2-proxy` — Google OAuth + allowlist
- `caddy` — reverse proxy + HTTPS

## Что нужно заполнить на сервере

1. Скопировать шаблон:

```bash
cp deploy/.env.example /srv/moreforms/runtime/.env
```

2. Заполнить в `/srv/moreforms/runtime/.env`:

- `APP_DOMAIN`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `DATABASE_URL`
- `BOOTSTRAP_OWNER_EMAIL`
- `OAUTH2_PROXY_CLIENT_ID`
- `OAUTH2_PROXY_CLIENT_SECRET`
- `OAUTH2_PROXY_COOKIE_SECRET`
- `OAUTH2_PROXY_ALLOWED_EMAILS_FILE`

3. Создать allowlist-файл для Google login:

```bash
mkdir -p /srv/moreforms/runtime/secrets
cat >/srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt <<'EOF'
you@example.com
teammate@example.com
EOF
chmod 600 /srv/moreforms/runtime/secrets/oauth2-allowed-emails.txt
```

4. Запустить контур:

```bash
cd /srv/moreforms/deploy/repo/deploy
docker compose --env-file /srv/moreforms/runtime/.env up -d --build
```

## Google OAuth

Redirect URI для `oauth2-proxy`:

```text
https://app.moreforms.ru/oauth2/callback
```

## База данных

`api` контейнер на старте:

1. ждет PostgreSQL;
2. выполняет `alembic upgrade head`;
3. запускает `uvicorn`.

Allowed users bootstrap:

- emails из `ALLOWED_EMAILS`
- owner из `BOOTSTRAP_OWNER_EMAIL`

записываются в `allowed_users` при старте приложения.

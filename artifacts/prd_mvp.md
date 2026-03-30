# PRD На MVP

## Цель MVP

Собрать минимально полезный shared discovery workspace, в котором несколько участников команды могут:

- вести идеи и гипотезы;
- хранить контакты и research materials;
- смотреть competitor landscape;
- открывать discovery-артефакты;
- использовать OpenClaw для создания новых views и dashboards.

## Целевой пользователь

- small venture team;
- founder-led discovery team;
- product + research + builder trio;
- advisor circle с read-only потребностями.

## In Scope

- основной dashboard c workspace-разделами;
- chat dashboard на OpenClaw;
- trackers для идей, задач, контактов и материалов;
- просмотр артефактов;
- просмотр competitors и signals;
- generated dashboards по slug.

## Out Of Scope

- полноценная CRM;
- внешняя multi-tenant collaboration suite;
- сложные permissions и role matrix;
- автоматическая синхронизация с внешними knowledge bases.

## Ключевые user stories

- как venture lead, я хочу видеть идеи, сигналы и next steps в одном месте;
- как исследователь, я хочу быстро добавлять материалы и привязывать их к идее;
- как builder, я хочу просить чат создать dashboard или доработать существующий view;
- как advisor, я хочу быстро открыть текущую thesis и связанные доказательства.

## Acceptance Criteria

- идеи, задачи, контакты и материалы доступны в основном dashboard;
- чат может отвечать по knowledge base;
- чат может создавать generated dashboards и возвращать рабочую ссылку;
- продуктовые артефакты читаются прямо из dashboard;
- changes в repo можно использовать как источник правды для команды.

## Открытые вопросы

- нужен ли отдельный tracker решений;
- какие dashboards должны стать постоянными, а не generated;
- нужен ли экспорт для внешних участников.

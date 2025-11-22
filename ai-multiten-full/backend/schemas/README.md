# MongoDB Schemas & Indexes

This folder documents collection schemas and indexes used by the backend.

- `tenants`: documents representing tenants. Indexed by `tenant_id` (unique).
- `users`: users scoped by `tenant_id` and `user_id` (unique composite index).
- `chat_sessions`: chat sessions with `tenant_id`, `user_id`, `use_case_id`.
- `messages`: chat messages with `tenant_id`, `session_id`, `user_id`, `role`, `content`.
- `use_cases`: repository of use-cases per tenant.

Use `../create_indexes.py` to provision indexes in the database.

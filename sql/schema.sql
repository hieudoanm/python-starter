DROP SCHEMA IF EXISTS public;

CREATE SCHEMA IF NOT EXISTS public;

DROP TABLE IF EXISTS public.tasks;

CREATE TABLE IF NOT EXISTS public.tasks (
  id          VARCHAR PRIMARY KEY,
  title       VARCHAR,
  description VARCHAR DEFAULT "",
  completed   BOOLEAN DEFAULT false,
);

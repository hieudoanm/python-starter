DROP SCHEMA IF EXISTS public;

CREATE SCHEMA IF NOT EXISTS public;

-- Users

DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users (
  id          VARCHAR PRIMARY KEY,
  username    VARCHAR NOT NULL,
  password    VARCHAR NOT NULL,
  created_at  VARCHAR DEFAULT NOW(),
  updated_at  VARCHAR DEFAULT NOW()
);

-- Lists

DROP TABLE IF EXISTS public.lists;

CREATE TABLE IF EXISTS public.lists (
  id          VARCHAR PRIMARY KEY,
  title       VARCHAR,
  description VARCHAR DEFAULT "",
  user_id     VARCHAR DEFAULT "",
  created_at  VARCHAR DEFAULT NOW(),
  updated_at  VARCHAR DEFAULT NOW()
);

-- Tasks

DROP TABLE IF EXISTS public.tasks;

CREATE TABLE IF NOT EXISTS public.tasks (
  id          VARCHAR PRIMARY KEY,
  title       VARCHAR,
  description VARCHAR DEFAULT "",
  list_id     VARCHAR DEFAULT "",
  completed   BOOLEAN DEFAULT false,
  created_at  VARCHAR DEFAULT NOW(),
  updated_at  VARCHAR DEFAULT NOW()
);

create table if not exists ploxy_users
(
    user_id       varchar not null
        constraint ploxy_users_pk
            primary key,
    username      text    not null,
    discriminator varchar not null,
    user_avatar   TEXT,
    email         text,
    premium       smallint default 0,
    banned        int      default 0,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    updated_at timestamptz NOT NULL DEFAULT NOW()
);

comment on table ploxy_users is 'Where normal user data is stored from discord';

comment on column ploxy_users.username is 'Used for website purposes';

comment on column ploxy_users.user_avatar is 'Link to cdn of user''s avatar image';

comment on column ploxy_users.email is 'Used for oauth';

create index ploxy_users_email_index
    on ploxy_users (email);

create unique index ploxy_users_user_id_uindex
    on ploxy_users (user_id);

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON ploxy_users
FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();
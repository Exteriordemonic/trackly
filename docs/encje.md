USER — identity: email, name, optional password (a client without a password logs in via magic link). Created in the background when access is granted. No role field — because the role is per project, not global.
PROJECT — a project managed on the platform.
PROJECT_ACCESS — linking table between USER↔PROJECT with the 'role' field (owner / client). This is the heart of the schema: it stores "who, in which project, in what role".
TICKET — a submission within a project. Attributes: status (choices), deadline, testing instruction.
COMMENT — a comment under a ticket.
LOGIN_TOKEN — a temporary access key (magic link), associated with USER.

USER ↔ PROJECT = M:N, split through PROJECT_ACCESS (with the 'role' attribute) — one user can participate in multiple projects in different roles, one project has many users (owners + clients)
PROJECT ↔ TICKET = 1:N — a project has many tickets, a ticket belongs to one project
TICKET ↔ COMMENT = 1:N — a ticket has many comments
USER ↔ COMMENT = 1:N — the author of the comment is one FK to USER (because everyone, owner and client, is a USER — this is the benefit of "background user" concept)
USER ↔ TICKET = 1:N — the creator of the ticket is one FK to USER (same benefit)
USER ↔ LOGIN_TOKEN = 1:N — one user can generate many tokens over time
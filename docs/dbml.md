Table user {
  id int [primary key]
  name varchar
  email varchar
  password varchar [null]
}

Table project {
  id int [primary key]
  title varchar
  description text
}

Table project_access {
  id integer [primary key]
  user_id integer [ref: > user.id, note: 'on delete cascade']
  project_id integer [ref: > project.id, note: 'on delete cascade']
  role varchar

  indexes {
    (user_id, project_id) [unique]   // composite unique - ta fiszka!
  }
}

Table ticket {
  id int [primary key]
  project_id integer [ref: > project.id ,note: 'on delete cascade']
  user_id integer [ref: > user.id]
  status varchar
  deadline date
  title varchar
  description text
  testing_instruction text
}

Table comment {
  id int [primary key]
  user_id integer [ref: > user.id]
  ticket_id integer [ref: > ticket.id ,note: 'on delete cascade']
  text text
}

Table login_token {
  id int [primary key]
  user_id integer [ref: > user.id ,note: 'on delete cascade']
  token text
  expires_at datetime
}
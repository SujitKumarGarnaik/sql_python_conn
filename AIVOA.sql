
use blog_db;

-- CREATING THE POST TABLE -- 
CREATE TABLE posts(
  id int auto_increment primary key,
  title varchar(30) not null unique,
  content text not null
);

-- CREATING TAGS TABLE --
create table tags(
   id int auto_increment primary key,
   name varchar(100) not  null unique
);

-- CREATING TABLE POST TAGS --
create table post_tags(
  post_id int,
  tag_id int,
  primary key(post_id, tag_id),
  foreign key (post_id) references posts(id) on delete cascade,
  foreign key (tag_id) references tags(id) on delete cascade
);
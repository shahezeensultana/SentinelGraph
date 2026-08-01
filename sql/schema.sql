create database if not exists sentinelgraph;
use sentinelgraph;

create table users(
    user_id varchar(20) primary key,
    employee_name varchar(100)
);


-- ==========================================
-- Psychometric
-- ==========================================
create table psychometric(
    user_id varchar(20) primary key,
    O decimal(4,2),
    C decimal(4,2), 
    E decimal(4,2), 
    A decimal(4,2),
    N decimal(4,2),

    constraint fk_psychometric_user FOREIGN key (user_id) references users(user_id) ON DELETE CASCADE
);

-- ==========================================
-- logon events
-- ==========================================
create table logon_events(
    id varchar(30) primary key,
    event_time datetime not null,
    user_id varchar(20) not null,
    pc varchar(30) not null,
    activity varchar(20) not null,

    constraint fk_logon_user FOREIGN key (user_id) references users(user_id) ON DELETE CASCADE
);

-- ==========================================
-- Device Events
-- ==========================================
create table device_events(
    id varchar(30) primary key,
    event_time datetime not null,
    user_id varchar(20) not null,
    pc varchar(30) not null,
    activity varchar(20) not null,

    constraint fk_device_user FOREIGN key (user_id) references users(user_id) ON DELETE CASCADE
);

-- ==========================================
-- Email Events
-- ==========================================
create table email_events(
    id varchar(30) primary key,
    event_time DATETIME NOT NULL,
    user_id VARCHAR(20) NOT NULL,
    pc VARCHAR(30) NOT NULL,
    recipient_to TEXT,
    cc text,
    bcc text,
    sender varchar(255),
    size INT,
    attachments INT,
    content text,

    constraint fk_email_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id) ON DELETE CASCADE
);

-- ==========================================
-- File Events
-- ==========================================
CREATE TABLE file_events (
    id VARCHAR(30) PRIMARY KEY,
    event_time DATETIME NOT NULL,
    user_id VARCHAR(20) NOT NULL,
    pc VARCHAR(30) NOT NULL,
    filename VARCHAR(255),
    content TEXT,

    CONSTRAINT fk_file_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id) ON DELETE CASCADE
);

-- ==========================================
-- HTTP Events
-- ==========================================
CREATE TABLE http_events (
    id VARCHAR(30) PRIMARY KEY,
    event_time DATETIME NOT NULL,
    user_id VARCHAR(20) NOT NULL,
    pc VARCHAR(30) NOT NULL,
    url TEXT,
    content TEXT,

    CONSTRAINT fk_http_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id) ON DELETE CASCADE
);
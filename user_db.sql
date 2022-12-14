CREATE TABLE users (
    user_id SERIAL,
    username    VARCHAR(255) NOT NULL,
    passwords VARCHAR(255) NOT NULL,
    email   VARCHAR(255)  NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE post (
    post_id SERIAL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (post_id), 
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    FOREIGN KEY (group_id) REFERENCES group(group_id)
);

CREATE TABLE group (
    group_id SERIAL,
    group_name VARCHAR(255) NOT NULL,
    descript VARCHAR(255) NOT NULL,
    PRIMARY KEY (group_id),
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
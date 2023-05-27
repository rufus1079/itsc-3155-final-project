CREATE TABLE Users (
    user_id SERIAL,
    username    VARCHAR(255) NOT NULL,
    passwords VARCHAR(255) NOT NULL,
    email   VARCHAR(255)  NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE Post (
    post_id SERIAL,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (post_id), 
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE User_Group (
    group_id SERIAL,
    user_id INT NOT NULL,
    group_name VARCHAR(255) NOT NULL,
    descript VARCHAR(255) NOT NULL,
    members VARCHAR(255) NOT NULL,
    PRIMARY KEY (group_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)



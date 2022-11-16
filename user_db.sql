CREATE TABLE users (
    user_id INT     NOT NULL,
    username    VARCHAR(255) NOT NULL,
    passwords VARCHAR(255) NOT NULL,
    email   VARCHAR(255)  NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE post (
    post_id SERIAL  NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (post_id), 
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

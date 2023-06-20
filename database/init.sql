DROP TABLE IF EXISTS `sample_data`;
CREATE TABLE `sample_data`(
    `firstname` VARCHAR(255),
    `lastname` VARCHAR(255),
    `email` VARCHAR(255),
    PRIMARY KEY (`email`)
);
INSERT INTO `sample_data`(`firstname`, `lastname`, `email`) VALUES ('John', 'Doe', 'john.doe@email.com');
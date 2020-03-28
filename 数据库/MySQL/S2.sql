CREATE TABLE news(
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(20) NOT NULL,
	`content` VARCHAR(2000) NOT NULL,
	`types` VARCHAR(10) NOT NULL,
	`image` VARCHAR(300) NULL,
	`author` VARCHAR(20) NULL,
	`view_count` INT DEFAULT 0,
	`created_at` DATETIME NULL,
	`is_valid` SMALLINT DEFAULT 1,
	PRIMARY KEY(`id`)
) DEFAULT CHARSET = 'UTF8'

INSERT INTO `news`(`title`, `image`, `content`, `types`) VALUE
	('标题1', 'D:\Typora_notes\notes\计算机网络\photo\2.png', '新闻内容1', '推荐');
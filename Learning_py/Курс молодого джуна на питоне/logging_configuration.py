LOGGING = {
	"version": 1,
	"handlers": {
		"fileHandler_1": {
			"class": "logging.FileHandler",
			"formatter": "myFormatter_1",
			"filename": "C:\\Users\\Семья\\PycharmProjects\\pythonProject\\Log_files\\log_1.log",
			"level": "DEBUG",
			"encoding": "UTF-8"
		},
		"fileHandler_2": {
			"class": "logging.FileHandler",
			"formatter": "myFormatter_2",
			"filename": "C:\\Users\\Семья\\PycharmProjects\\pythonProject\\Log_files\\log_2.log",
			"level": "DEBUG",
			"encoding": "UTF-8"
		},
		"fileHandler_3": {
			"class": "logging.FileHandler",
			"formatter": "myFormatter_3",
			"filename": "C:\\Users\\Семья\\PycharmProjects\\pythonProject\\Log_files\\log_3.log",
			"level": "DEBUG",
			"encoding": "UTF-8"
		}
	},
	"loggers": {
		"logger_conf_1": {
			"handlers": ["fileHandler_1"],
			"level": "DEBUG"
		},
		"logger_conf_2": {
			"handlers": ["fileHandler_2"],
			"level": "DEBUG"
		},
		"logger_conf_3": {
			"handlers": ["fileHandler_3"],
			"level": "DEBUG"
		}
	},
	"formatters": {
		"myFormatter_1": {
			"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
		},
		"myFormatter_2": {
			"format": "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
		},
		"myFormatter_3": {
			"format": "%(name)s - %(filename)s - %(levelname)s - %(funcName)s - %(message)s"
		}
	}
}

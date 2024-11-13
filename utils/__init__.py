import yaml
import logging
import logging.config  # Garante a disponibilidade de logging.config

def set_config_yaml(texto, app_name, config_file): 
    """
    Reads the configuration file and payment preference (required).
    :param text: Primary visible text.
    :param app_name: Main logger name.
    :param config_file: YAML format file that loads the configuration.
    """
    try:
        with open(config_file, 'r') as stream:
            global_config = yaml.load(stream, Loader=yaml.FullLoader)
            logging.config.dictConfig(global_config['logging'])  # Usando a chave 'logging' conforme definida
            log = logging.getLogger(app_name)
            log.info('Starting %s, loading setup file: %s', texto, config_file)
            return global_config, log

    except yaml.YAMLError as exc:
        print('Arquivo: {0}, Erro: {1}'.format(config_file, repr(exc)))

    except Exception as exp:
        print('Arquivo: {0}, Erro Geral: {1}'.format(config_file, repr(exp)))

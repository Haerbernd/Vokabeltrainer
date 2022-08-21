import re
import logger as log


def clean_list(text):
    log.main.info('Received list to clean...')
    log.debug.debug('Received list\'s content=' + str(text) + '...')
    text = str(text)
    log.main.info('Converted received list to string...')
    text = re.sub('\[', '', text)
    log.debug.debug('Replaced all mentions of [ with empty string...')
    text = re.sub(']', '', text)
    log.debug.debug('Replaced all mentions of ] with empty string...')
    text = re.sub('\'', '', text)
    log.debug.debug('Replaced all mentions of \' with empty string...')
    log.main.info('Cleaned list successfully...')
    return text


def clean_dict(text):
    log.main.info('Received dictionary to clean...')
    log.debug.debug('Received dictionary\'s content=' + str(text) + '...')
    text = str(text)
    log.main.info('Converted received dictionary to string...')
    text = re.sub('{', '', text)
    log.debug.debug('Replaced all mentions of { with empty string...')
    text = re.sub('}', '', text)
    log.debug.debug('Replaced all mentions of } with empty string...')
    text = re.sub('\'', '', text)
    log.debug.debug('Replaced all mentions of \' with empty string...')
    log.main.info('Cleaned dictionary successfully...')
    return text

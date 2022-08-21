import json
import random
import sys
import os
from src import logger as log, textcleaner as tlc

# opens the vocabulary dictionary
log.main.info('Start reading vocabulary dictionary...')
try:
    file = open('./vocab/vocabulary.json', 'r+', encoding='UTF-8')
except FileNotFoundError:
    log.main.error('"vocabulary.json" was not found...')
    print('\u001b[31mError\u001b[0m: "vocabulary.json" was not found...')
    log.main.info('The program will be shutted down...\n\n')
    sys.exit(0)
vocab = json.load(file)
file.close()
log.main.info('Finished reading vocabulary dictionary...')

# opens the config file
log.main.info('Start reading config...')
try:
    file = open('./config/config.json', 'r+', encoding='UTF-8')
except FileNotFoundError:
    log.main.error('"config.json" was not found...')
    print('\u001b[31mError\u001b[0m: "config.json" was not found...')
    log.main.info('The program will be shutted down...\n\n')
    sys.exit(0)
config = json.load(file)
file.close()
log.main.info('Finished reading config...')

# decides the language of the program
log.main.info('Start setting program language...')
file = open('./config/language.json', 'r+', encoding='UTF-8')
prog_lang = json.load(file)
file.close()
if config['program-language'] in prog_lang['possible-options']:
    prog_text = prog_lang[config['program-language']]
else:
    print('\u001b[31mError\u001b[0m: Invalid option at "program-language" in "config.json"\n'
          'Use one of the following', prog_lang['possible-options'])
    input('Press any key...\n')
    log.main.error('\u001b[31mError\u001b[0m: Invalid option at "program-language" in "config.json"\n'
                   'Use one of the following', prog_lang['possible-options'], '...')
    log.main.info('The program will be shutted down...\n\n')
    sys.exit(0)
log.main.info('Finished setting program language...')

# decides which vocabularies are used
log.main.info('Start setting vocabulary-language...')
if config['vocab-to'] in config['possible-vocab-to-options']:
    vocab_origin_lang = vocab['lang-codes'][config['vocab-to']]['origin-lang']
    vocab_lang = vocab['lang-codes'][config['vocab-to']]['vocab-lang']
else:
    print('\u001b[31mError\u001b[0m: Invalid option at "possible-vocab-to-options" in "config.json"\n'
          'Use one of the following', config['possible-vocab-to-options'])
    input('Press any key...\n')
    log.main.error('\u001b[31mError\u001b[0m: Invalid option at "possible-vocab-to-options" in "config.json"\n'
                   'Use one of the following', config['possible-vocab-to-options'], '...')
    log.main.info('The program will be shutted down...\n\n')
    sys.exit(0)
log.main.info('Finished setting vocabulary-language...')


def random_vocab():
    chosen = random.choice(list(vocab[config['vocab-to']]))
    return chosen


# a first usage of colored text to ensure that it is initialized correctly (I had graphic bugs at first tests of the
# program and that is to solve the problem, I don't know if it's neccessary anymore)
# ensures that the right os is used
log.main.info('Start setting operating system...')
if config['os'] == 'windows':
    os.system('cls')
elif config['os'] == 'linux':
    os.system('clear')
else:
    input('\u001b[31mError\u001b[0m: Invalid option at "os" in "config.json"\nUse either "windows" or "linux"')
    log.main.error('\u001b[31mError\u001b[0m: Invalid option at "os" in "config.json"\nUse either "windows" or "linux"')
    log.main.info('The program will be shutted down...\n\n')
    sys.exit(0)
log.main.info('Finished setting operating system...')

# main program
while True:
    log.main.info('Start selecting vocabulary...')
    vocabulary = random_vocab()
    log.main.info('Finished selecting vocabulary...')
    log.debug.debug(vocabulary + ' was selected as vocabulary...')
    print(prog_text['1'])
    print(prog_text['2'], vocabulary.upper(), prog_text['3'], prog_text[vocab_lang], prog_text['7'])
    player_input = input('>')
    if player_input.lower() == vocab[config['vocab-to']][vocabulary]:
        print(prog_text['5'])
        input(prog_text['4'])
        log.main.info('The player successfully guessed the vocabulary...')
    elif player_input.lower() == '!quit':
        log.main.info('The program will be shutted down...\n\n')
        sys.exit(0)
    else:
        print(prog_text['6'], vocab[config['vocab-to']][vocabulary])
        input(prog_text['4'])
        log.main.info('The player failed guessing the vocabulary...')
    if config['os'] == 'windows':
        os.system('cls')
    elif config['os'] == 'linux':
        os.system('clear')

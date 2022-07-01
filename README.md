Use the config.json file to config the program.
It is important that you change the value of "os" to "linux" if you're using a Linux-Distribution.


##Explanation of config and possible options
####program-language
Decides the language in which the program's texts are. Possible options: `de` for German and `en` for English.

####vocab-to
Decides the language in which the vocabulary should be translated. Possible options: `de` for German and `en` for English.

####os
Decides which operating system is used. Possible options: `windows` for Windows and `linux` for Linux-Distributions

##Adding more vocabularies
To add more vocabularies edit the vocabulary.json file. **Be careful**: Every word has to be in double quotation marks and 
the word for the vocabulary language has to be lower case. Edit the file following the following template

    {program language (right now `Deutsch` and `English`)  :
        {vocabulary in program language : vocabulary in vocabulary language},
        {"cat" : "katze"},
        {dog : "hund"}
    }

##Known Problems
When a word is translated wrong a newline is there altough there should be none and a None is given before the right 
translation is shown.

##Legal Things
This program is licensed under the GNU General Public License v3.0

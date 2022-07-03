# Vokabeltrainer

This program, the Vokabeltrainer (german for Vocabulary trainer), was made to help you practice vocabularies of 
different languages. It relies but not on an API but of a self-written customizable dictionary in form of a .json file.

## Configuration

You can configure the program by editing the config.json file in the config folder. Through changing the value of each 
key (the words in the second double quation marks (example: `"program-language" : "en"`, "program language" = key, 
"en"= value)) you can configure the program.

`"program-language"` decides the language in which the programs texts will be displayed. Currently German, Englisch and 
machine translated Spanish (`es-mt`) are supported. You can see all possible values at `"possible-options"` in 
language.json in the config folder. In this file you can also add more translations by opening a new dictionary in it, 
choosing a language code, adding it to `"possible-options"` and translating all the values for the same keys in your 
new dictionary.

`"vocab-to"` decides the origin language and the translated language of the vocabularies. The first value (for 
example: `en`) sets the origin language (the language you know and will start translating from), then a hyphen (-) is 
set to separate the first value from the second which decides the vocabulary language (the language to which you will 
translate, for example: `de`). All possible options are displayed directly below in `"possible-vocab-to-options"`.

Last but not least `"os"` decides which os you use. This is extremly important because this program uses a terminal 
command which is different on different operating systems. Currently, supported are Windows and Linux. Their respective 
values are `"windows"` and `"linux"`.

## Adding Vocabularies

To add vocabularies or change existing ones, edit the vocabulary.json in the vocab folder.

First decide for which origin language and for which vocabulary language you want to add/change vocabularies. If your 
combination of origin language-vocabulary language does not yet exist, add it under `lang-codes` if it exists change 
the keys/values of the respective dictionary.

An entry has to look like this:

    {"en-de" : {
            "word in origin language" : "word in vocabulary language",
            "cow" : "kuh",
            "crow" : "rabe"
        }
    }

Don't forget: Every word as to be in double quation marks ("word") and after each entry has to be set a comma (except 
the last one, there you must not set a comma). All values (words in vocabulary languages) **MUST** be written lower case 
only.

## Ideas, Problems, Translations, Questions, etc

If you have ideas for new programs or for new or better functions of existing ones I'd be happy if you would inform me. 
The same applies for if you find problems in one of my programs, want to translate it (or already have) and don't 
know how to add it properly, have questions or anything similar please inform me/write me a message (preferably in 
German or English) on Discord (Der sportliche Metzger#9465) or write an email to dersportlichemetzger@gmail.com.

## Legal

As you can see in the LICENSE this program uses the GNU General Public License v3.0. You can find out more about it 
here: https://choosealicense.com/licenses/gpl-3.0/

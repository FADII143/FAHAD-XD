from os import (

    system

)
try:
    from requests import (
        get
)
except:
    system('pip install requests')
from re import (
    findall
)
from random import (
    choice
)

from platform import(
    machine
)
def mach(
        #os checker
) -> str:
    cls = 'clear'
    if "AMD" in machine():
        cls = 'cls'
    return cls

colors_list = ["\033[0;36m",
                 "\033[1;33m",
                 "\033[0;93m",
                 "\033[1;32m",
                 "\033[0;92m",
                 "\033[1;35m",
                 "\033[0;35m",
                 "\033[1;34m",
                 "\033[0;94m",
        "\033[1;96m"
        ]
colors = choice(
        colors_list
)
stop = "\033[0m"
class LOGO:
    def logo(self, version: float = 1.1) -> str:
        logo = f"""
                {colors}███████ {colors}██████
                {colors}██      {colors}██   ██
                {colors}█████   {colors}██████
                {colors}██      {colors}██   ██
                {colors}██      {colors}██████{stop}
{50*'.'}
                 version : {version}
        developed by qaiser abbass
{50*'-'}"""
        return logo


def main():
    system(mach())
    print(LOGO.logo(1.1))
    print(
        " {}file name you have in your sdcard{}"
    .format(
            colors,
            stop
        )
    )
    file = input(
        ' file from which ids will extract : '
    )
    save_as = input(
        " save file as : "
    )

    try:
        x = open(file,
                 'r',
                 encoding='utf-8'
        ).read(
            # reading file
        ).splitlines(
            # spliting lines
        )
        for ids in x:
            name = ids.split(
                '|'
            )[-1]
            po = get(
                'https://web.facebook.com/public/{}'
                     f''.format(
                    name
                )
            ).text
            done = set(
                findall(
                    r'\d+', str(
                        findall(
                            ',filter_ids:{(.*?)}', str(po)))))
            for ids in done:
                open(
                    save_as,
                    'a'
                ).write(
                    ids + '|' + name + '\n'
                )
                print(
                    "{} Done Extracted > {} Total {}{}"
                    .format(
                        choice(colors_list),
                        ids,
                        len(
                            open(
                                save_as,'r').readlines(

                            )
                        ),
                        stop
                    ))
    except FileNotFoundError:
        exit(' Invalid File Not Found')
    except Exception as __:
        print(__)

if __name__ == '__main__':
    main()

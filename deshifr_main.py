from collections import Counter

TEXT = "7ОУ8cr8ЛБ8ЧХОДХЛМtcbЛrАc<МАcРcМАЕc<ХЛД8cХcБАc5МА1c БКХ<Хr8cКД8cr8cБК87ЛМОРДb8МЛbcАБМХЕОД4r ЕcОД>АКХМЕАЕcЛУОМХb?cБАЛ2АД42tcАrcr8cХЛБАД4Фt8МcrХ2 О2А1cХrИАКЕОЧХХcАcЛУХЕО8ЕАЕcМ82ЛМ8?c<МАП cБАrbМ4c2О2cБКАХЛЙА7ХМcЛУОМХ8cХЛБАД4ФtaЬ88cФrОrХbc АcМ82ЛМ8cР8Кr8ЕЛbc2cБАrbМХbЕc5rМКАБХХcХcХrИАКЕОМХР rАЛМХcМ82ЛМОccЛРbФ4cЕ8У7tcР8КАbМrАЛМbЕХcХc2А7ОЕХcХ Фt<О8МЛbcРcОД>8ПКОХ<8Л2А1cМ8АКХХc2А7ХКАРОrХbcАЛrА РrА1cМ8АКХ81c2АМАКА1cbРДb8МЛbcrХ2МАcХrА1c2О2c2ДА7c5 ДРt7cЫ8rrАrc8>АcМ8АК8Е c2А7ХКАРОrХbcХЛМА<rХ2ОcХЛБАД4ФtaМЛbcА<8r4cО2МХРrАc ХcФ78Л4 "

ALF = ['х', 'щ', 'ю', 'б', '-', 'ц', 'ф', 'г', 'э', 'ж', 'з', 'й', 'ч', 'у', 'ь', 'д', 'ы', 'в', 'п', 'л', 'м', 'р',
       'я', 'к', 'а', 'с', 'н', 'т', 'е', 'и', 'о', ' ']


def count_symbols() -> list:
    simvols = Counter(TEXT)
    dict_simvols = {}
    alfa_text = []
    print(dict_simvols)
    for item in simvols:
        simvols[item] = simvols[item] / len(TEXT)
        dict_simvols[item] = simvols[item]
        print(item, simvols[item])
    dict_simvols = dict(sorted(dict_simvols.items(), key=lambda x: x[1]))
    print(dict_simvols)
    x = list(dict_simvols.keys())
    print(x)
    return x


count_symbols()


def chenging(new_text: str) -> str:
    list_alfa = count_symbols()
    ALF = ['х', 'щ', 'ц', '-', 'б', 'ю', 'э', 'г', 'ф', 'ж', 'й', 'з', 'у', 'ч', 'ь', 'д', 'ы', 'п', 'в', 'л', 'м', 'р',
           'я', 'к', 'а', 'с', 'н', 'т', 'е', 'и', 'о', ' ']
    len(ALF)
    i = 0
    new_text = new_text.replace(" ", "")
    for simvol in count_symbols():
        if simvol == 'Ы':
            new_text = new_text.replace(simvol, "ш")
        else:
            s = ALF[i]
            new_text = new_text.replace(simvol, ALF[i])
            i = i + 1
    return new_text


TEXT = chenging(TEXT)


def write_text(TEXT):
    with open('deshifr.txt', "w+") as f:
        f.write(TEXT)

write_text(TEXT)

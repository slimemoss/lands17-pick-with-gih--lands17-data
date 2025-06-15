import public_data
from lands17 import card_detail, lands_filter
from public_data import CardData, SetData


def main():
    f = lands_filter.get()
    expansion = f.expansions[0]
    start_date = f.start_dates[expansion]

    cards_by_color = card_detail.get(expansion, start_date)

    # res[name] -> {gih, alsa}
    res: SetData = {}
    for color, cards in cards_by_color:
        for card in cards.root:
            name = card.name
            data = res.get(name, CardData(gih={}, alsa=None))
            if color is None:
                data.alsa = card.avg_seen
            else:
                data.gih[color] = card.ever_drawn_win_rate
            res[name] = data

    public_data.write(expansion, res)


if __name__ == '__main__':
    main()

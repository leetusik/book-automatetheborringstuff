def isValidChessBoard(dic):
    result = True
    valid_int = [1, 2, 3, 4, 5, 6, 7, 8]
    valid_alp = ["a", "b", "c", "d", "e", "f", "g", "h"]
    count = {}
    count_place = {}

    for i in dic.values():
        count.setdefault(i, 0)
        count[i] += 1

    for i in dic.keys():
        if int(i[0]) not in valid_int:
            result = False
        if i[1] not in valid_alp:
            result = False

        count_place.setdefault(i, 0)
        count_place[i] += 1

    if (
        not count["bking"]
        or not count["wking"]
        or count["bking"] != 1
        or count["wking"] != 1
    ):
        result = False

    b_pieces = 0
    b_pawns = 0
    w_pieces = 0
    w_pawns = 0
    for i in count.items():
        if i[0][0] == "b":
            b_pieces += i[1]
            if i[0][1] == "p":
                b_pawns += i[1]
        if i[0][0] == "w":
            w_pieces += i[1]
            if i[0][1] == "p":
                w_pawns += i[1]

    if b_pieces > 16 or w_pieces > 16:
        result = False
    if b_pawns > 8 or w_pawns > 8:
        result = False

    # print(b_pawns, w_pawns)
    return result


temp = {
    "7h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
    "4h": "bpawn",
    "2e": "wpawn",
    "5e": "wpawn",
}
print(isValidChessBoard(temp))

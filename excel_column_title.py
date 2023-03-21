def convertToTitle(columnNumber: int) -> str:
    title = ""
    while columnNumber > 0:
        columnNumber -= 1
        print("col_num",columnNumber)
        title = chr(columnNumber % 26 + 65) + title
        print(title)
        columnNumber //= 26
        print("column",columnNumber)
    return title


print(convertToTitle(27))
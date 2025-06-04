def timeStrToDecimal(timeStr):
    hours, minutes = map(int, timeStr.split(":"))
    return round(hours + minutes / 60, 2)

def processCourses(rawData):
    for code, data in rawData.items():
        data["Start"] = timeStrToDecimal(data["Start"])
        data["End"] = timeStrToDecimal(data["End"])

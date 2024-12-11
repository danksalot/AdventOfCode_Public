import json
import numbers

def sumNumbers(data):
    if isinstance(data, numbers.Number):
        return data
    elif isinstance(data, list):
        return sum(sumNumbers(x) for x in data)
    elif isinstance(data, dict):
        return sum(sumNumbers(data[key]) for key in data.keys())
    else:
        return 0

def sumNumbersWithoutRed(data):
    if isinstance(data, numbers.Number):
        return data
    elif isinstance(data, list):
        return sum(sumNumbersWithoutRed(x) for x in data)
    elif isinstance(data, dict):
        return sum(sumNumbersWithoutRed(data[key]) for key in data.keys() if "red" not in data.values())
    else:
        return 0

with open('Input') as inputFile:
    jsonData = json.loads(inputFile.read())
    print("Part 1:", sumNumbers(jsonData))
    print("Part 2:", sumNumbersWithoutRed(jsonData))
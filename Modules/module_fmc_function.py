def function_convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


def function_extract(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

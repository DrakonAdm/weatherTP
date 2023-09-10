import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


def outputSTR(value):
    if 0 > value < 100:
        return None

    if 0 <= value < 3:
        return "Тёплая шапка, утеплённые брюки, свитер, пуховик"

    if 3 <= value < 7:
        return "Тёплая шапка, утеплённые брюки, свитер, тёплая куртка"

    if 7 <= value < 10:
        return "Шапка, утеплённые брюки, водолазка, тёплая куртка"

    if 10 <= value < 13:
        return "Шапка, джинсы, водолазка, пальто"

    if 13 <= value < 16:
        return "Шапка, джинсы, водолазка, лёгкая куртка"

    if 16 <= value < 19:
        return "Брюки, водолазка, лёгкая куртка"

    if 19 <= value < 22:
        return "Брюки, водолазка, лёгкая куртка, зонт"

    if 22 <= value < 25:
        return "Брюки, водолазка, лёгкая куртка, дождевик"

    if 25 <= value < 28:
        return "Брюки, рубашка, лёгкая куртка"

    if 28 <= value < 31:
        return "Брюки, рубашка, лёгкая куртка, зонт"

    if 31 <= value < 34:
        return "Брюки, рубашка, лёгкая куртка, дождевик"

    if 34 <= value < 37:
        return "Брюки, рубашка"

    if 37 <= value < 40:
        return "Брюки, рубашка, зонт"

    if 40 <= value < 43:
        return "Брюки, рубашка, дождевик"

    if 43 <= value < 46:
        return "Брюки, рубашка, ветровка"

    if 46 <= value < 50:
        return "Брюки, рубашка, ветровка, зонт"

    if 50 <= value < 54:
        return "Брюки, рубашка, ветровка, дождевик"

    if 54 <= value < 58:
        return "Брюки, футболка"

    if 58 <= value < 62:
        return "Брюки, футболка, зонт"

    if 62 <= value < 66:
        return "Брюки, футболка, дождевик"

    if 66 <= value < 70:
        return "Брюки, футболка, ветровка"

    if 70 <= value < 74:
        return "Брюки, футболка, ветровка, зонт"

    if 74 <= value < 78:
        return "Брюки, футболка, ветровка, дождевик"

    if 78 <= value < 82:
        return "Кепка, шорты/юбка, футболка"

    if 82 <= value < 86:
        return "Кепка, шорты/юбка, футболка, зонт"

    if 86 <= value < 90:
        return "Кепка, шорты/юбка, футболка, дождевик"

    if 90 <= value < 93:
        return "Кепка, шорты/юбка, майка"

    if 93 <= value < 97:
        return "Кепка, шорты/юбка, майка, зонт"

    if 97 <= value < 100:
        return "Кепка, шорты/юбка, майка, дождевик"



def forecastClothes(queryset):
    """проверить условие, если всё больше или меньше ограничений, то return"""
    # queryset[0].maxTem
    # queryset[0].minTem
    # queryset[0].averageTem

    if not queryset[0].maxTem:
        return None, None, None

    if queryset[0].maxTem > 30 or queryset[0].minTem > 30 or queryset[0].averageTem > 30:
        return "Слишком жарко", "Сидите дома", "Вам нужен вентилятор"

    if queryset[0].maxTem < -30 or queryset[0].minTem < -30 or queryset[0].averageTem < -30:
        return "Слишком холодно", "Сидите дома", "Одевайтесь как можно теплее"

    if queryset[0].windSpeed > 20:
        return "Слишком сильный ветер", "Очень сильный ветер", "Сидите дома"

    if queryset[0].precipitation > 30:
        return "Слишком много осадков", "Сидите дома", "Или не забудь зонт, но он не поможет)"

    # Define the fuzzy input variables
    temperature = ctrl.Antecedent(np.arange(-30, 31, 1), 'temperature')
    wind_speed = ctrl.Antecedent(np.arange(0, 21, 1), 'wind_speed')
    precipitation = ctrl.Antecedent(np.arange(0, 31, 1), 'precipitation')

    # Define the fuzzy output variable
    clothing = ctrl.Consequent(np.arange(0, 101, 1), 'clothing')

    # Define the fuzzy membership functions
    temperature['coldOne'] = fuzz.trimf(temperature.universe, [-30, -22, -14])
    temperature['coldTwo'] = fuzz.trimf(temperature.universe, [-14, -12, -10])
    temperature['coldThree'] = fuzz.trimf(temperature.universe, [-10, -8, -6])
    temperature['coldFour'] = fuzz.trimf(temperature.universe, [-6, -4, -2])
    temperature['coldHot'] = fuzz.trimf(temperature.universe, [-2, 0, 2])
    temperature['hotSix'] = fuzz.trimf(temperature.universe, [2, 6, 10])
    temperature['hotFive'] = fuzz.trimf(temperature.universe, [10, 12, 14])
    temperature['hotFour'] = fuzz.trimf(temperature.universe, [14, 16, 18])
    temperature['hotThree'] = fuzz.trimf(temperature.universe, [18, 20, 22])
    temperature['hotTwo'] = fuzz.trimf(temperature.universe, [22, 24, 26])
    temperature['hotOne'] = fuzz.trimf(temperature.universe, [26, 28, 30])

    wind_speed['low'] = fuzz.trimf(wind_speed.universe, [0, 5, 10])
    wind_speed['high'] = fuzz.trimf(wind_speed.universe, [10, 15, 20])

    precipitation['zero'] = fuzz.trimf(precipitation.universe, [0, 0, 0])
    precipitation['low'] = fuzz.trimf(precipitation.universe, [0, 8, 15])
    precipitation['high'] = fuzz.trimf(precipitation.universe, [15, 23, 30])

    clothing['WarmHat_WarmTrousers_Sweater_DownJacket'] = fuzz.trimf(clothing.universe, [0, 1, 3])
    clothing['WarmHat_WarmTrousers_Sweater_Overcoat'] = fuzz.trimf(clothing.universe, [3, 5, 7])
    clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'] = fuzz.trimf(clothing.universe, [7, 8, 10])

    clothing['Beanie_Jeans_Turtleneck_Coat'] = fuzz.trimf(clothing.universe, [10, 11, 13])
    clothing['Beanie_Jeans_Turtleneck_Jacket'] = fuzz.trimf(clothing.universe, [13, 14, 16])

    clothing['Trousers_Turtleneck_Jacket'] = fuzz.trimf(clothing.universe, [16, 17, 19])
    clothing['Trousers_Turtleneck_Jacket_Umbrella'] = fuzz.trimf(clothing.universe, [19, 20, 22])
    clothing['Trousers_Turtleneck_Jacket_Raincoat'] = fuzz.trimf(clothing.universe, [22, 23, 25])

    clothing['Trousers_Shirt_Jacket'] = fuzz.trimf(clothing.universe, [25, 26, 28])
    clothing['Trousers_Shirt_Jacket_Umbrella'] = fuzz.trimf(clothing.universe, [28, 29, 31])
    clothing['Trousers_Shirt_Jacket_Raincoat'] = fuzz.trimf(clothing.universe, [31, 32, 34])

    clothing['Trousers_Shirt'] = fuzz.trimf(clothing.universe, [34, 35, 37])
    clothing['Trousers_Shirt_Umbrella'] = fuzz.trimf(clothing.universe, [37, 38, 40])
    clothing['Trousers_Shirt_Raincoat'] = fuzz.trimf(clothing.universe, [40, 41, 43])

    clothing['Trousers_Shirt_Windbreaker'] = fuzz.trimf(clothing.universe, [43, 44, 46])
    clothing['Trousers_Shirt_Windbreaker_Umbrella'] = fuzz.trimf(clothing.universe, [46, 48, 50])
    clothing['Trousers_Shirt_Windbreaker_Raincoat'] = fuzz.trimf(clothing.universe, [50, 52, 54])

    clothing['Trousers_TShirt'] = fuzz.trimf(clothing.universe, [54, 56, 58])
    clothing['Trousers_TShirt_Umbrella'] = fuzz.trimf(clothing.universe, [58, 60, 62])
    clothing['Trousers_TShirt_Raincoat'] = fuzz.trimf(clothing.universe, [62, 64, 66])

    clothing['Trousers_TShirt_Windbreaker'] = fuzz.trimf(clothing.universe, [66, 68, 70])
    clothing['Trousers_TShirt_Windbreaker_Umbrella'] = fuzz.trimf(clothing.universe, [70, 72, 74])
    clothing['Trousers_TShirt_Windbreaker_Raincoat'] = fuzz.trimf(clothing.universe, [74, 76, 78])

    clothing['Cap_Shorts_TShirt'] = fuzz.trimf(clothing.universe, [78, 80, 82])
    clothing['Cap_Shorts_TShirt_Umbrella'] = fuzz.trimf(clothing.universe, [82, 84, 86])
    clothing['Cap_Shorts_TShirt_Raincoat'] = fuzz.trimf(clothing.universe, [86, 88, 90])

    clothing['Cap_Shorts_Vest'] = fuzz.trimf(clothing.universe, [90, 92, 93])
    clothing['Cap_Shorts_Vest_Umbrella'] = fuzz.trimf(clothing.universe, [93, 95, 97])
    clothing['Cap_Shorts_Vest_Raincoat'] = fuzz.trimf(clothing.universe, [97, 99, 100])


    # Define the fuzzy rules
    rule1 = ctrl.Rule(temperature['coldOne'] & wind_speed['low'] & precipitation['zero'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])
    rule2 = ctrl.Rule(temperature['coldOne'] & wind_speed['low'] & precipitation['low'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])
    rule3 = ctrl.Rule(temperature['coldOne'] & wind_speed['low'] & precipitation['high'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])
    rule4 = ctrl.Rule(temperature['coldOne'] & wind_speed['high'] & precipitation['zero'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])
    rule5 = ctrl.Rule(temperature['coldOne'] & wind_speed['high'] & precipitation['low'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])
    rule6 = ctrl.Rule(temperature['coldOne'] & wind_speed['high'] & precipitation['high'],
                      clothing['WarmHat_WarmTrousers_Sweater_DownJacket'])

    rule7 = ctrl.Rule(temperature['coldTwo'] & wind_speed['low'] & precipitation['zero'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])
    rule8 = ctrl.Rule(temperature['coldTwo'] & wind_speed['low'] & precipitation['low'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])
    rule9 = ctrl.Rule(temperature['coldTwo'] & wind_speed['low'] & precipitation['high'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])
    rule10 = ctrl.Rule(temperature['coldTwo'] & wind_speed['high'] & precipitation['zero'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])
    rule11 = ctrl.Rule(temperature['coldTwo'] & wind_speed['high'] & precipitation['low'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])
    rule12 = ctrl.Rule(temperature['coldTwo'] & wind_speed['high'] & precipitation['high'],
                      clothing['WarmHat_WarmTrousers_Sweater_Overcoat'])

    rule13 = ctrl.Rule(temperature['coldThree'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])
    rule14 = ctrl.Rule(temperature['coldThree'] & wind_speed['low'] & precipitation['low'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])
    rule15 = ctrl.Rule(temperature['coldThree'] & wind_speed['low'] & precipitation['high'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])
    rule16 = ctrl.Rule(temperature['coldThree'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])
    rule17 = ctrl.Rule(temperature['coldThree'] & wind_speed['high'] & precipitation['low'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])
    rule18 = ctrl.Rule(temperature['coldThree'] & wind_speed['high'] & precipitation['high'],
                       clothing['Beanie_WarmTrousers_Turtleneck_Overcoat'])

    rule19 = ctrl.Rule(temperature['coldFour'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])
    rule20 = ctrl.Rule(temperature['coldFour'] & wind_speed['low'] & precipitation['low'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])
    rule21 = ctrl.Rule(temperature['coldFour'] & wind_speed['low'] & precipitation['high'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])
    rule22 = ctrl.Rule(temperature['coldFour'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])
    rule23 = ctrl.Rule(temperature['coldFour'] & wind_speed['high'] & precipitation['low'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])
    rule24 = ctrl.Rule(temperature['coldFour'] & wind_speed['high'] & precipitation['high'],
                       clothing['Beanie_Jeans_Turtleneck_Coat'])

    rule25 = ctrl.Rule(temperature['coldHot'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])
    rule26 = ctrl.Rule(temperature['coldHot'] & wind_speed['low'] & precipitation['low'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])
    rule27 = ctrl.Rule(temperature['coldHot'] & wind_speed['low'] & precipitation['high'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])
    rule28 = ctrl.Rule(temperature['coldHot'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])
    rule29 = ctrl.Rule(temperature['coldHot'] & wind_speed['high'] & precipitation['low'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])
    rule30 = ctrl.Rule(temperature['coldHot'] & wind_speed['high'] & precipitation['high'],
                       clothing['Beanie_Jeans_Turtleneck_Jacket'])

    rule31 = ctrl.Rule(temperature['hotSix'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Trousers_Turtleneck_Jacket'])
    rule32 = ctrl.Rule(temperature['hotSix'] & wind_speed['low'] & precipitation['low'],
                       clothing['Trousers_Turtleneck_Jacket_Umbrella'])
    rule33 = ctrl.Rule(temperature['hotSix'] & wind_speed['low'] & precipitation['high'],
                       clothing['Trousers_Turtleneck_Jacket_Raincoat'])
    rule34 = ctrl.Rule(temperature['hotSix'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Trousers_Turtleneck_Jacket'])
    rule35 = ctrl.Rule(temperature['hotSix'] & wind_speed['high'] & precipitation['low'],
                       clothing['Trousers_Turtleneck_Jacket_Umbrella'])
    rule36 = ctrl.Rule(temperature['hotSix'] & wind_speed['high'] & precipitation['high'],
                       clothing['Trousers_Turtleneck_Jacket_Raincoat'])

    rule37 = ctrl.Rule(temperature['hotFive'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Trousers_Shirt_Jacket'])
    rule38 = ctrl.Rule(temperature['hotFive'] & wind_speed['low'] & precipitation['low'],
                       clothing['Trousers_Shirt_Jacket_Umbrella'])
    rule39 = ctrl.Rule(temperature['hotFive'] & wind_speed['low'] & precipitation['high'],
                       clothing['Trousers_Shirt_Jacket_Raincoat'])
    rule40 = ctrl.Rule(temperature['hotFive'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Trousers_Shirt_Jacket'])
    rule41 = ctrl.Rule(temperature['hotFive'] & wind_speed['high'] & precipitation['low'],
                       clothing['Trousers_Shirt_Jacket_Umbrella'])
    rule42 = ctrl.Rule(temperature['hotFive'] & wind_speed['high'] & precipitation['high'],
                       clothing['Trousers_Shirt_Jacket_Raincoat'])

    rule43 = ctrl.Rule(temperature['hotFour'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Trousers_Shirt'])
    rule44 = ctrl.Rule(temperature['hotFour'] & wind_speed['low'] & precipitation['low'],
                       clothing['Trousers_Shirt_Umbrella'])
    rule45 = ctrl.Rule(temperature['hotFour'] & wind_speed['low'] & precipitation['high'],
                       clothing['Trousers_Shirt_Raincoat'])
    rule46 = ctrl.Rule(temperature['hotFour'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Trousers_Shirt_Windbreaker'])
    rule47 = ctrl.Rule(temperature['hotFour'] & wind_speed['high'] & precipitation['low'],
                       clothing['Trousers_Shirt_Windbreaker_Umbrella'])
    rule48 = ctrl.Rule(temperature['hotFour'] & wind_speed['high'] & precipitation['high'],
                       clothing['Trousers_Shirt_Windbreaker_Raincoat'])

    rule49 = ctrl.Rule(temperature['hotThree'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Trousers_TShirt'])
    rule50 = ctrl.Rule(temperature['hotThree'] & wind_speed['low'] & precipitation['low'],
                       clothing['Trousers_TShirt_Umbrella'])
    rule51 = ctrl.Rule(temperature['hotThree'] & wind_speed['low'] & precipitation['high'],
                       clothing['Trousers_TShirt_Raincoat'])
    rule52 = ctrl.Rule(temperature['hotThree'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Trousers_TShirt_Windbreaker'])
    rule53 = ctrl.Rule(temperature['hotThree'] & wind_speed['high'] & precipitation['low'],
                       clothing['Trousers_TShirt_Windbreaker_Umbrella'])
    rule54 = ctrl.Rule(temperature['hotThree'] & wind_speed['high'] & precipitation['high'],
                       clothing['Trousers_TShirt_Windbreaker_Raincoat'])

    rule55 = ctrl.Rule(temperature['hotTwo'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Cap_Shorts_TShirt'])
    rule56 = ctrl.Rule(temperature['hotTwo'] & wind_speed['low'] & precipitation['low'],
                       clothing['Cap_Shorts_TShirt_Umbrella'])
    rule57 = ctrl.Rule(temperature['hotTwo'] & wind_speed['low'] & precipitation['high'],
                       clothing['Cap_Shorts_TShirt_Raincoat'])
    rule58 = ctrl.Rule(temperature['hotTwo'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Cap_Shorts_TShirt'])
    rule59 = ctrl.Rule(temperature['hotTwo'] & wind_speed['high'] & precipitation['low'],
                       clothing['Cap_Shorts_TShirt_Umbrella'])
    rule60 = ctrl.Rule(temperature['hotTwo'] & wind_speed['high'] & precipitation['high'],
                       clothing['Cap_Shorts_TShirt_Raincoat'])

    rule61 = ctrl.Rule(temperature['hotOne'] & wind_speed['low'] & precipitation['zero'],
                       clothing['Cap_Shorts_Vest'])
    rule62 = ctrl.Rule(temperature['hotOne'] & wind_speed['low'] & precipitation['low'],
                       clothing['Cap_Shorts_Vest_Umbrella'])
    rule63 = ctrl.Rule(temperature['hotOne'] & wind_speed['low'] & precipitation['high'],
                       clothing['Cap_Shorts_Vest_Raincoat'])
    rule64 = ctrl.Rule(temperature['hotOne'] & wind_speed['high'] & precipitation['zero'],
                       clothing['Cap_Shorts_Vest'])
    rule65 = ctrl.Rule(temperature['hotOne'] & wind_speed['high'] & precipitation['low'],
                       clothing['Cap_Shorts_Vest_Umbrella'])
    rule66 = ctrl.Rule(temperature['hotOne'] & wind_speed['high'] & precipitation['high'],
                       clothing['Cap_Shorts_Vest_Raincoat'])


    # Create the fuzzy control system
    clothing_ctrl = ctrl.ControlSystem(
        [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
         rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
         rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
         rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
         rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49,
         rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59,
         rule60, rule61, rule62, rule63, rule64, rule65, rule66])
    forecast = ctrl.ControlSystemSimulation(clothing_ctrl)

    # Set the input values from the queryset
    forecast.input['temperature'] = float(queryset[0].maxTem)
    forecast.input['wind_speed'] = float(queryset[0].windSpeed)
    forecast.input['precipitation'] = float(queryset[0].precipitation)
    # Compute the fuzzy output
    forecast.compute()
    maxStr = forecast.output['clothing']

    forecast.input['temperature'] = float(queryset[0].minTem)
    forecast.compute()
    minStr = forecast.output['clothing']

    forecast.input['temperature'] = float(queryset[0].averageTem)
    forecast.compute()
    averageStr = forecast.output['clothing']

    """возвращает значение, а мне нужна строка"""

    # Return the clothing forecast value
    return outputSTR(maxStr), outputSTR(averageStr), outputSTR(minStr)
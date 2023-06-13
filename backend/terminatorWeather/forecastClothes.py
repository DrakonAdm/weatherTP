import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


def outputSTR(value):
    if 0 > value < 100:
        return None

    if 0 <= value < 3:
        return "Пуховик, свитер, футболка, тёплые брюки, тёплая шапка, тёплая обувь"

    if 3 <= value < 7:
        return "Пуховик, рубашка, тёплые брюки, тёплая шапка, тёплая обувь"

    if 7 <= value < 10:
        return "Пальто, рубашка, тёплые брюки, тёплая шапка, тёплая обувь"

    if 10 <= value < 13:
        return "Утеплённая куртка, свитер, майка, тёплые брюки, тёплая шапка, тёплая обувь"

    if 13 <= value < 16:
        return "Утеплённая куртка, водолазка, тёплые брюки, тёплая шапка, тёплая обувь"

    if 16 <= value < 19:
        return "Утеплённая куртка, рубашка, брюки, шапка, тёплая обувь"

    if 19 <= value < 22:
        return "Пальто, рубашка, брюки, тёплая шапка, тёплая обувь"

    if 22 <= value < 25:
        return "Пальто, майка, брюки, шапка, тёплая обувь"

    if 25 <= value < 28:
        return "Утеплённая куртка, свитер, брюки, тёплая шапка, тёплая обувь"

    if 28 <= value < 31:
        return "Куртка, рубашка, брюки, тёплая шапка, тёплая обувь"

    if 31 <= value < 34:
        return "Куртка, майка, брюки, тёплая шапка, тёплая обувь"

    if 34 <= value < 37:
        return "Ветровка, свитер, брюки, шапка, кроссовки"

    if 37 <= value < 40:
        return "Ветровка, рубашка, брюки, шапка, кроссовки"

    if 40 <= value < 43:
        return "Ветровка,майка, брюки, шапка, кроссовки"

    if 43 <= value < 46:
        return "Плащ, футболка, брюки, кепка, кроссовки"

    if 46 <= value < 49:
        return "Плащ, рубашка, брюки, панама, кроссовки"

    if 49 <= value < 52:
        return "Плащ, майка, брюки, кепка, кроссовки"

    if 52 <= value < 55:
        return "Плащ, водолазка, шорты/юбка, кепка, кроссовки"

    if 55 <= value < 58:
        return "Плащ, рубашка, шорты/юбка, кепка, кроссовки"

    if 58 <= value < 61:
        return "Плащ, майка, шорты/юбка, кепка, кроссовки"

    if 61 <= value < 65:
        return "Зонт, водолазка, шорты/юбка, кепка, кроссовки"

    if 65 <= value < 68:
        return "Зонт, рубашка, шорты/юбка, кепка, кроссовки"

    if 68 <= value < 71:
        return "Зонт, майка, шорты/юбка, кепка, кроссовки"

    if 71 <= value < 74:
        return "Футболка, брюки, кепка, кроссовки"

    if 74 <= value < 77:
        return "Рубашка, брюки, панама, кроссовки"

    if 77 <= value < 80:
        return "Свитер, брюки, шапка, кроссовки"

    if 80 <= value < 83:
        return "Водолазка, брюки, кепка, кроссовки"

    if 83 <= value < 86:
        return "Майка, шорты/юбка, кепка, кроссовки"

    if 86 <= value < 89:
        return "Рубашка, шорты/юбка, кепка, кроссовки"

    if 89 <= value < 93:
        return "Водолазка, шорты/юбка, кепка, кроссовки"

    if 93 <= value < 97:
        return "Майка, шорты/юбка, кепка, шлёпанцы"

    if 97 <= value <= 100:
        return "Рубашка, шорты/юбка, кепка, шлёпанцы"


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
        return "Слишком сильный ветер", "Слишком сильный ветер", "Сидите дома"

    if queryset[0].precipitation > 30:
        return "Слишком много осадков", "Сидите дома", "Или не забудь зонт, но он не поможет)"

    # Define the fuzzy input variables
    temperature = ctrl.Antecedent(np.arange(-30, 31, 1), 'temperature')
    wind_speed = ctrl.Antecedent(np.arange(0, 21, 1), 'wind_speed')
    precipitation = ctrl.Antecedent(np.arange(0, 31, 1), 'precipitation')

    # Define the fuzzy output variable
    clothing = ctrl.Consequent(np.arange(0, 101, 1), 'clothing')

    # Define the fuzzy membership functions
    temperature['coldOne'] = fuzz.trimf(temperature.universe, [-30, -28, -26])
    temperature['coldTwo'] = fuzz.trimf(temperature.universe, [-26, -24, -22])
    temperature['coldThree'] = fuzz.trimf(temperature.universe, [-22, -20, -18])
    temperature['coldFour'] = fuzz.trimf(temperature.universe, [-18, -16, -14])
    temperature['coldFive'] = fuzz.trimf(temperature.universe, [-14, -12, -10])
    temperature['coldSix'] = fuzz.trimf(temperature.universe, [-10, -8, -6])
    temperature['coldSeven'] = fuzz.trimf(temperature.universe, [-6, -4, -2])
    temperature['coldHot'] = fuzz.trimf(temperature.universe, [-2, 0, 2])
    temperature['hotSeven'] = fuzz.trimf(temperature.universe, [2, 4, 6])
    temperature['hotSix'] = fuzz.trimf(temperature.universe, [6, 8, 10])
    temperature['hotFive'] = fuzz.trimf(temperature.universe, [10, 12, 14])
    temperature['hotFour'] = fuzz.trimf(temperature.universe, [14, 16, 18])
    temperature['hotThree'] = fuzz.trimf(temperature.universe, [18, 20, 22])
    temperature['hotTwo'] = fuzz.trimf(temperature.universe, [22, 25, 26])
    temperature['hotOne'] = fuzz.trimf(temperature.universe, [26, 28, 30])

    wind_speed['lowOne'] = fuzz.trimf(wind_speed.universe, [0, 2, 4])
    wind_speed['lowTwo'] = fuzz.trimf(wind_speed.universe, [4, 6, 8])
    wind_speed['lowHigh'] = fuzz.trimf(wind_speed.universe, [8, 10, 12])
    wind_speed['highTwo'] = fuzz.trimf(wind_speed.universe, [12, 14, 16])
    wind_speed['highOne'] = fuzz.trimf(wind_speed.universe, [16, 18, 20])

    precipitation['zero'] = fuzz.trimf(precipitation.universe, [0, 0, 0])
    precipitation['low'] = fuzz.trimf(precipitation.universe, [0, 8, 15])
    precipitation['high'] = fuzz.trimf(precipitation.universe, [15, 23, 30])

    clothing['Down_Jacket_Sweater_T-shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [0, 1, 3])
    clothing['Down_Jacket_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [3, 5, 7])
    clothing['Coat_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [7, 8, 10])
    clothing['Overcoat_Sweater_Vest_Warm_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [10, 11, 13])
    clothing['Overcoat_Turtleneck_Warm_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [13, 14, 16])
    clothing['Overcoat_Shirt_Trousers_Beanie_Warm_Shoes'] = fuzz.trimf(clothing.universe, [16, 17, 19])
    clothing['Coat_Shirt_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [19, 20, 22])
    clothing['Coat_Vest_Trousers_Beanie_Warm_Shoes'] = fuzz.trimf(clothing.universe, [22, 23, 25])
    clothing['Overcoat_Sweater_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [25, 26, 28])
    clothing['Jacket_Shirt_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [28, 29, 31])
    clothing['Jacket_Vest_Trousers_Warm_Hat_Warm_Shoes'] = fuzz.trimf(clothing.universe, [31, 32, 34])
    clothing['Windbreaker_Sweater_Trousers_Beanie_Sneakers'] = fuzz.trimf(clothing.universe, [34, 35, 37])
    clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'] = fuzz.trimf(clothing.universe, [37, 38, 40])
    clothing['Windbreaker_Vest_Trousers_Beanie_Sneakers'] = fuzz.trimf(clothing.universe, [40, 41, 43])

    clothing['Raincoat_T-shirt_Trousers_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [43, 44, 46])
    clothing['Raincoat_Shirt_Trousers_Panama_Sneakers'] = fuzz.trimf(clothing.universe, [46, 47, 49])
    clothing['Raincoat_Sweater_Trousers_Hat_Sneakers'] = fuzz.trimf(clothing.universe, [49, 50, 52])
    clothing['Raincoat_Turtleneck_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [52, 53, 55])
    clothing['Raincoat_Shirt_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [55, 56, 58])
    clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [58, 59, 61])

    clothing['Umbrella_Turtleneck_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [61, 62, 65])
    clothing['Umbrella_Shirt_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [65, 66, 68])
    clothing['Umbrella_Vest_Shorts/skirt_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [68, 69, 71])

    clothing['T-shirt_Trousers_Cap_Sneakers'] = fuzz.trimf(clothing.universe, [71, 72, 74])
    clothing['Shirt_Trousers_Panama_Sneakers'] = fuzz.trimf(clothing.universe, [74, 75, 77])
    clothing['Sweater_Trousers_Hat_Sneakers'] = fuzz.trimf(clothing.universe, [77, 78, 80])
    clothing['Turtleneck_Shorts/skirt_Cap_Sneaker'] = fuzz.trimf(clothing.universe, [80, 81, 83])
    clothing['Vest_Shorts/skirt_Cap_Sneaker'] = fuzz.trimf(clothing.universe, [83, 84, 86])
    clothing['Shirt_Shorts/skirt_Cap_Sneaker'] = fuzz.trimf(clothing.universe, [86, 87, 89])
    clothing['Turtleneck_Shorts/skirt_Cap_Sneaker'] = fuzz.trimf(clothing.universe, [89, 90, 93])
    clothing['Vest_Shorts/skirt_Cap_spanking'] = fuzz.trimf(clothing.universe, [93, 95, 97])
    clothing['Shirt_Shorts/skirt_Cap_spanking'] = fuzz.trimf(clothing.universe, [97, 99, 100])

    # Define the fuzzy rules
    rule1 = ctrl.Rule(temperature['coldOne'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                      | wind_speed['highTwo'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
                      | precipitation['high'],
                      clothing['Down_Jacket_Sweater_T-shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule2 = ctrl.Rule(temperature['coldTwo'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                      | wind_speed['highTwo'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
                      | precipitation['high'],
                      clothing['Down_Jacket_Sweater_T-shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule3 = ctrl.Rule(temperature['coldThree'] | wind_speed['lowOne'] | wind_speed['lowTwo'] |
                      precipitation['zero'], clothing['Down_Jacket_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule16 = ctrl.Rule(temperature['coldThree'] | wind_speed['lowHigh'] | wind_speed['highTwo'] |
                       wind_speed['highOne'] | precipitation['low'] | precipitation['high'],
                       clothing['Down_Jacket_Sweater_T-shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule4 = ctrl.Rule(temperature['coldFour'] | wind_speed['lowOne'] | wind_speed['lowTwo'] |
                      precipitation['zero'], clothing['Coat_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule17 = ctrl.Rule(temperature['coldFour'] | wind_speed['lowHigh'] | wind_speed['highTwo'] |
                       precipitation['low'], clothing['Coat_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule18 = ctrl.Rule(temperature['coldFour'] | wind_speed['highOne'] |
                       precipitation['high'], clothing['Coat_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule5 = ctrl.Rule(temperature['coldFive'] | wind_speed['lowOne'] | precipitation['zero'],
                      clothing['Overcoat_Turtleneck_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule19 = ctrl.Rule(
        temperature['coldFive'] | wind_speed['lowTwo'] | wind_speed['lowHigh'] | precipitation['low'],
        clothing['Overcoat_Sweater_Vest_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule20 = ctrl.Rule(temperature['coldFive'] | wind_speed['highTwo'] | precipitation['high'],
                       clothing['Coat_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule21 = ctrl.Rule(temperature['coldFive'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Down_Jacket_Shirt_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule6 = ctrl.Rule(temperature['coldSix'] | wind_speed['lowOne'] | precipitation['zero'],
                      clothing['Coat_Vest_Trousers_Beanie_Warm_Shoes'])
    rule22 = ctrl.Rule(temperature['coldSix'] | wind_speed['lowTwo'] | precipitation['low'],
                       clothing['Coat_Shirt_Trousers_Warm_Hat_Warm_Shoes'])
    rule23 = ctrl.Rule(temperature['coldSix'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Overcoat_Shirt_Trousers_Beanie_Warm_Shoes'])
    rule24 = ctrl.Rule(temperature['coldSix'] | wind_speed['highTwo'] | precipitation['high'],
                       clothing['Overcoat_Turtleneck_Warm_Trousers_Warm_Hat_Warm_Shoes'])
    rule25 = ctrl.Rule(temperature['coldSix'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Overcoat_Sweater_Vest_Warm_Trousers_Warm_Hat_Warm_Shoes'])

    rule7 = ctrl.Rule(temperature['coldSeven'] | wind_speed['lowOne'] | precipitation['zero'],
                      clothing['Jacket_Shirt_Trousers_Warm_Hat_Warm_Shoes'])
    rule26 = ctrl.Rule(temperature['coldSeven'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Overcoat_Sweater_Trousers_Warm_Hat_Warm_Shoes'])
    rule27 = ctrl.Rule(temperature['coldSeven'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Coat_Vest_Trousers_Beanie_Warm_Shoes'])
    rule28 = ctrl.Rule(temperature['coldSeven'] | wind_speed['highTwo'] | precipitation['low'],
                       clothing['Coat_Shirt_Trousers_Warm_Hat_Warm_Shoes'])
    rule29 = ctrl.Rule(temperature['coldSeven'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Overcoat_Shirt_Trousers_Beanie_Warm_Shoes'])

    rule8 = ctrl.Rule(temperature['coldHot'] | wind_speed['lowOne'] | precipitation['zero'],
                      clothing['Jacket_Vest_Trousers_Warm_Hat_Warm_Shoes'])
    rule30 = ctrl.Rule(temperature['coldHot'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Jacket_Shirt_Trousers_Warm_Hat_Warm_Shoes'])
    rule31 = ctrl.Rule(temperature['coldHot'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Overcoat_Sweater_Trousers_Warm_Hat_Warm_Shoes'])
    rule32 = ctrl.Rule(temperature['coldHot'] | wind_speed['highTwo'] | precipitation['low'],
                       clothing['Coat_Vest_Trousers_Beanie_Warm_Shoes'])
    rule33 = ctrl.Rule(temperature['coldHot'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Coat_Vest_Trousers_Beanie_Warm_Shoes'])

    rule9 = ctrl.Rule(temperature['hotSeven'] | wind_speed['lowOne'] | precipitation['zero'],
                      clothing['Windbreaker_Sweater_Trousers_Beanie_Sneakers'])
    rule34 = ctrl.Rule(temperature['hotSeven'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Jacket_Vest_Trousers_Warm_Hat_Warm_Shoes'])
    rule35 = ctrl.Rule(temperature['hotSeven'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Jacket_Vest_Trousers_Warm_Hat_Warm_Shoes'])
    rule36 = ctrl.Rule(temperature['hotSeven'] | wind_speed['highTwo'] | precipitation['low'],
                       clothing['Jacket_Shirt_Trousers_Warm_Hat_Warm_Shoes'])
    rule37 = ctrl.Rule(temperature['hotSeven'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Overcoat_Sweater_Trousers_Warm_Hat_Warm_Shoes'])

    rule10 = ctrl.Rule(temperature['hotSix'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'])
    rule38 = ctrl.Rule(temperature['hotSix'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'])
    rule39 = ctrl.Rule(temperature['hotSix'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Windbreaker_Sweater_Trousers_Beanie_Sneakers'])
    rule40 = ctrl.Rule(temperature['hotSix'] | wind_speed['highTwo'] | precipitation['low'],
                       clothing['Jacket_Vest_Trousers_Warm_Hat_Warm_Shoes'])
    rule41 = ctrl.Rule(temperature['hotSix'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Jacket_Shirt_Trousers_Warm_Hat_Warm_Shoes'])

    rule11 = ctrl.Rule(temperature['hotFive'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Windbreaker_Vest_Trousers_Beanie_Sneakers'])
    rule42 = ctrl.Rule(temperature['hotFive'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Windbreaker_Vest_Trousers_Beanie_Sneakers'])
    rule43 = ctrl.Rule(temperature['hotFive'] | wind_speed['lowHigh'] | precipitation['low'],
                       clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'])
    rule44 = ctrl.Rule(temperature['hotFive'] | wind_speed['highTwo'] | precipitation['low'],
                       clothing['Windbreaker_Sweater_Trousers_Beanie_Sneakers'])
    rule45 = ctrl.Rule(temperature['hotFive'] | wind_speed['highOne'] | precipitation['high'],
                       clothing['Windbreaker_Sweater_Trousers_Beanie_Sneakers'])

    rule12 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Raincoat_Shirt_Trousers_Panama_Sneakers'])
    rule46 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Raincoat_Shirt_Trousers_Panama_Sneakers'])
    rule47 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowHigh'] | precipitation['zero'],
                       clothing['Raincoat_T-shirt_Trousers_Cap_Sneakers'])
    rule48 = ctrl.Rule(
        temperature['hotFour'] | wind_speed['highTwo'] | precipitation['zero'] | precipitation['low'],
        clothing['Raincoat_T-shirt_Trousers_Cap_Sneakers'])
    rule49 = ctrl.Rule(temperature['hotFour'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
                       | precipitation['high'],
                       clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'])
    rule50 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['low'] | precipitation['high'],
                       clothing['Windbreaker_Shirt_Trousers_Beanie_Sneakers'])
    rule51 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['high'],
                       clothing['Windbreaker_Vest_Trousers_Beanie_Sneakers'])

    rule13 = ctrl.Rule(temperature['hotThree'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Turtleneck_Shorts/skirt_Cap_Sneaker'])
    rule52 = ctrl.Rule(temperature['hotThree'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Sweater_Trousers_Hat_Sneakers'])
    rule53 = ctrl.Rule(temperature['hotThree'] | wind_speed['lowHigh'] | precipitation['zero'],
                       clothing['Shirt_Trousers_Panama_Sneakers'])
    rule54 = ctrl.Rule(
        temperature['hotThree'] | wind_speed['highTwo'] | precipitation['zero'] | precipitation['low'],
        clothing['Umbrella_Vest_Shorts/skirt_Cap_Sneakers'])
    rule55 = ctrl.Rule(
        temperature['hotThree'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
        | precipitation['high'],
        clothing['Umbrella_Shirt_Shorts/skirt_Cap_Sneakers'])
    rule56 = ctrl.Rule(temperature['hotThree'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['low'] | precipitation['high'],
                       clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'])
    rule57 = ctrl.Rule(temperature['hotThree'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['high'],
                       clothing['Raincoat_Shirt_Shorts/skirt_Cap_Sneakers'])

    rule14 = ctrl.Rule(temperature['hotTwo'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Vest_Shorts/skirt_Cap_spanking'])
    rule58 = ctrl.Rule(temperature['hotTwo'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Turtleneck_Shorts/skirt_Cap_Sneaker'])
    rule59 = ctrl.Rule(temperature['hotTwo'] | wind_speed['lowHigh'] | precipitation['zero'],
                       clothing['Shirt_Shorts/skirt_Cap_Sneaker'])
    rule60 = ctrl.Rule(
        temperature['hotTwo'] | wind_speed['highTwo'] | precipitation['zero'] | precipitation['low'],
        clothing['Vest_Shorts/skirt_Cap_Sneaker'])
    rule61 = ctrl.Rule(temperature['hotTwo'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
                       | precipitation['high'],
                       clothing['Umbrella_Vest_Shorts/skirt_Cap_Sneakers'])
    rule62 = ctrl.Rule(temperature['hotTwo'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['low'] | precipitation['high'],
                       clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'])
    rule63 = ctrl.Rule(temperature['hotTwo'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['high'],
                       clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'])

    rule15 = ctrl.Rule(temperature['hotOne'] | wind_speed['lowOne'] | precipitation['zero'],
                       clothing['Shirt_Shorts/skirt_Cap_spanking'])
    rule64 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowTwo'] | precipitation['zero'],
                       clothing['Shirt_Shorts/skirt_Cap_spanking'])
    rule65 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowHigh'] | precipitation['zero'],
                       clothing['Vest_Shorts/skirt_Cap_spanking'])
    rule66 = ctrl.Rule(
        temperature['hotFour'] | wind_speed['highTwo'] | precipitation['zero'] | precipitation['low'],
        clothing['Umbrella_Shirt_Shorts/skirt_Cap_Sneakers'])
    rule67 = ctrl.Rule(temperature['hotFour'] | wind_speed['highOne'] | precipitation['zero'] | precipitation['low']
                       | precipitation['high'],
                       clothing['Umbrella_Turtleneck_Shorts/skirt_Cap_Sneakers'])
    rule68 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['low'] | precipitation['high'],
                       clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'])
    rule69 = ctrl.Rule(temperature['hotFour'] | wind_speed['lowOne'] | wind_speed['lowTwo'] | wind_speed['lowHigh']
                       | precipitation['high'],
                       clothing['Raincoat_Vest_Shorts/skirt_Cap_Sneakers'])

    # Create the fuzzy control system
    clothing_ctrl = ctrl.ControlSystem(
        [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
         rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19,
         rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29,
         rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39,
         rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49,
         rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59,
         rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69])
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

from foods import mic_dejun, gustare, pranz, cina, bauturi, fructe


def main():
	welcome()
	gender = sex()
	weight = get_weight()
	height = get_height()
	age = get_age()
	rest_bmr = calculate_bmr(gender, weight, height, age)
	total_calculation(rest_bmr)
	recomandations()
	breakfast = get_breakfast()
	fruits = get_fruits()
	lunch = get_lunch()
	drink = get_drink()
	snack = get_snack()
	diner = get_diner()


def welcome():
	print("Bun venit pe calculatorul de calorii bazat pe BMR !\nHaideti sa aflam cate calorii trebuie sa consumati "
	      "zilnic.\n")


def sex():
	sexes = ["masculin", "feminim", "M", "F", "f", "m", "Masculin", "Feminin"]
	while True:
		sex = str(input("Sunteti de sex masculin sau feminim ? "))
		while sex not in sexes:
			sex = str(input("Va rog sa introduceti masculin sau feminim ' "))
		else:
			return sex


def get_weight():
	weight_kg = float(input("Va rog sa introduceti greutatea dumnevoastra in kg: "))
	while weight_kg <= 0:
		weight_kg = float(input("Valoare incorecta! Va rog sa introduceti greutatea in kg : "))
	else:
		return weight_kg


def get_height():
	height_cm = float(input("Introduceti inaltimea in centimetri:  "))
	while height_cm <= 0:
		height_cm = float(input("Valoare incorecta ! Va rog introduceti inaltimea in centimetri : "))
	else:
		return height_cm


def get_age():
	age_yrs = int(input("Introduceti varsta : "))
	while age_yrs <= 0:
		age_yrs = int(input("Valoare incorecta !Va rog introduceti varsta dumnevoastra in ani : "))
	else:
		return age_yrs


def calculate_bmr(gender, weight, height, age):
	male = ["masculin", "M", "m", "Masculin"]
	female = ["feminin", "F", "f", "Feminin"]
	if gender == female:
		women = (weight * 10) + (height * 6.25) - (age * 5) - 161
		return int(women)
	else:
		men = (weight * 10) + (height * 6.25) - (age * 5) + 5
		return int(men)


def total_calculation(rest_bmr):
	user_activity_lvl = get_user_activity()

	maintain = {
		"sedentar": get_sedentary(rest_bmr),
		"usor": get_light_activity(rest_bmr),
		"moderat": get_moderate_activity(rest_bmr),
		"activ": get_very_active(rest_bmr)
	}

	if user_activity_lvl == "sedentar":
		print(
			"Trebuie sa consumati  " + str(maintain["sedentar"]) + " calorii pe zi pentru a mentine greutatea actuala.")

	if user_activity_lvl == "usor":
		print("Trebuie sa consumati  " + str(maintain["usor"]) + " calorii pe zi pentru a mentine greutatea actuala.")

	if user_activity_lvl == "moderat":
		print(
			"Trebuie sa consumati  " + str(maintain["moderat"]) + " calorii pe zi pentru a mentine greutatea actuala.")

	if user_activity_lvl == "activ":
		print("Trebuie sa consumati  " + str(maintain["activ"]) + " calorii pe zi pentru a mentine greutatea actuala.")


def get_user_activity():
	activity_lvl = ["sedentar", "usor", "moderat", "activ"]
	while True:
		user_lvl = str(input(
			"\nCare este nivelul activitatii dumneavostra ?\n\nSedentar inseamna ca faceti putin sport spre deloc "
			".\nUsor inseamna ca faceti sport 1 - 3 zile / saptamana.\nModerat inseamna ca faceti activitati sportive "
			"de 3 - 5 ori pe saptamana .\nActiv inseamna ca faceti 2 exercitii / zi 5 - 7 zile pe saptamana .\n\nVa "
			"rog sa selectati sedentar , usor , moderat , activ ' "))

		while user_lvl not in activity_lvl:
			user_lvl = str(input("Valoare incorecta ! Va rog selectati: 'sedentar', 'usor', 'moderat',  or 'activ' "))
		else:
			return user_lvl



def get_sedentary(rest_bmr):
	sedentary = rest_bmr * 1.25
	return sedentary


def get_light_activity(rest_bmr):
	light = rest_bmr * 1.375
	return light


def get_moderate_activity(rest_bmr):
	moderate = rest_bmr * 1.550
	return moderate


def get_very_active(rest_bmr):
	active = rest_bmr * 1.725
	return active


def recomandations():
	print(f'Bazandu-ne pe rezultatul primit , adica numarul de calorii , puteti acum sa va faceti un meniu\n Cu '
			f'alimentele pe care noi le recomandam mai jos .\n Pofta buna !')


def get_breakfast():
	print('La micul dejun puteti alege: ')
	for k, v in mic_dejun.items():
		print(f'{k} care contine {v} .')


def get_fruits():
	print('Ca si fruct puteti alege: ')
	for k, v in fructe.items():
		print(f'{k} care contine {v} .')


def get_lunch():
	print('Pentru pranz puteti alege : ')
	for k, v in pranz.items():
		print(f'{k} care contine {v} .')


def get_drink():
	print('Langa pranz puteti consuma si una din bauturile : ')
	for k, v in bauturi.items():
		print(f'{k} care contine {v} .')


def get_snack():
	print('Dupa pranz , aveti dreptul si o gustare : ')
	for k, v in gustare.items():
		print(f'{k} care contine {v} .')


def get_diner():
	print('Cina ar trebui sa fie una cat mai light . puteti alege : ')
	for k, v in cina.items():
		print(f'{k} care contine {v} .')


if __name__ == '__main__':
	main()

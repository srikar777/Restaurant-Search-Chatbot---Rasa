from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json
import requests
# For email
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
d_email_rest = []
budgetmin = 0
budgetmax = 0

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"09d230b4c94b86c501bc2d519c48108a"}
		zomato = zomatopy.initialize_app(config)
		response_email = ""

		#Getting values from slots- location,cuisine,bugetmin & budgetmax
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budgetmin = int(tracker.get_slot('budgetmin'))
		budgetmax = int(tracker.get_slot('budgetmax'))
		#print('Printing Location:', loc)

		#Getting location details from zomato api
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]


		if len(d1) == 0:
			print('action_search_restaurants - Inside IF of If not results in d1 or...')
			restaurant_found = False
			#response= "Sorry, we did not find any results for this location."
			#dispatcher.utter_message(response)
		else:
			# If restuarants exists
			restaurant_found = True

			d_rest = self.get_restaurants(lat, lon, budgetmin, budgetmax, cuisine)
			#print('Printing budgetmin',budgetmin)
			#print('Printing budgetmax', budgetmax)


			# Filter the results based on budget
			d_res_budget = [d_rest_single for d_rest_single in d_rest if
						((d_rest_single['restaurant']['average_cost_for_two'] >= budgetmin) & (d_rest_single['restaurant']['average_cost_for_two'] <= budgetmax))]
			#print('Printing d_res_budget...')
			#print(d_res_budget)
			# Sort the results according to the restaurant's rating
			d_budget_rating_sorted = []
			if len(d_res_budget) != 0:
				try:
					d_budget_rating_sorted = sorted(d_res_budget, key=lambda k: float(k['restaurant']['user_rating']['aggregate_rating']), reverse=True)
				except Exception as e:
					restaurant_found = False

			# Build the response
			response = ""

			if len(d_budget_rating_sorted) == 0:
				#print('Inside if len(d_budget_rating_sorted) == 0...')
				restaurant_found = False
			else:
				# Pick Top 5
				restaurant_found = True
				d_budget_rating_top5 = d_budget_rating_sorted[:5]

				#Pick Top 10 Restaurants for sending Email
				d_email_rest = d_budget_rating_sorted[:10]

				if (d_email_rest and len(d_email_rest) > 0):
					#restaurant_found = True

					slno = 1
					for restaurant in d_budget_rating_top5:
						response = response + str(slno) + ". " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " - Rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating'])
						response = response + ". And the average price for two people here is: " + str(restaurant['restaurant']['average_cost_for_two']) + "\n"
						slno += 1
					dispatcher.utter_message("Showing you top rated restaurants:" + "\n" + response +"\n"+ "----------------------------------")

					response_email = "The top rated restaurants you have enquired are:" + "\n"
					slno = 1
					for restaurant in d_email_rest:
						response_email = response_email + str(slno) + ". " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " - Rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating'])
						response_email = response_email + ". And the average price for two people here is: " + str(restaurant['restaurant']['average_cost_for_two']) + "\n"
						slno += 1
		if len(response_email) == 0:
			#print('Inside IF of if len(response_email) == 0...')
			return [SlotSet('location', loc), SlotSet('restaurant_found', restaurant_found),SlotSet('emailbody', None)]
		else:
			#print('Inside ELSE of if len(response_email) == 0...')
			return [SlotSet('location', loc), SlotSet('restaurant_found', restaurant_found),SlotSet('emailbody', response_email)]

	def get_restaurants(self, lat, lon, budgetmin, budgetmax, cuisine):

		cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,'mexican': 73, 'north indian': 50, 'south indian': 85}

		d_rest = []
		executor = ThreadPoolExecutor(max_workers=5)
		for res_key in range(0, 101, 20):

			executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
		executor.shutdown()
		return d_rest

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
	base_url = "https://developers.zomato.com/api/v2.1/"
	headers = {'Accept': 'application/json',
				'user-key': '09d230b4c94b86c501bc2d519c48108a'}
	result = ""
	try:
		#print(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(cuisines_dict.get(cuisine)) + "&start=" + str(res_key) + "&count=20")
		results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(cuisines_dict.get(cuisine)) + "&start=" + str(res_key) + "&count=20", headers=headers).content).decode("utf-8")
		#results = (requests.get(base_url + "search?q=" + str(query) + "&count=" + str(limit) + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + str(cuisines_dict.get(cuisine)), headers=headers).content).decode("utf-8")
	except Exception as e:
		print('Exception:',e)
		return()
	d = json.loads(results)
	d_rest.extend(d['restaurants'])


# ---------------- Modified----------------------------------------------------------------------------

#List of T1-T2 cities
t1_t2_cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
"Agra","Ajmer","Aligarh","Amravati","Amritsar","Asansol","Aurangabad","Bareilly","Belgaum","Bhavnagar",
"Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bilaspur","Bokaro Steel City","Chandigarh","Coimbatore",
"Cuttack","Dehradun","Dhanbad","Bhilai","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad","Gorakhpur",
"Gulbarga","Guntur","Gwalior","Gurgaon","Guwahati","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar",
"jammu","jamnagar","jamshedpur","jhansi","jodhpur","kakinada","kannur","kanpur","kochi","kolhapur","kollam",
"Kozhikode","Kurnool","Ludhiana","Lucknow","Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry",
"Purulia Prayagraj","Raipur","Rajkot","Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Shimla","Siliguri",
"Solapur","Srinagar","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tiruppur","Ujjain","Vijayapura",
"Vadodara","Varanasi","Vasai-Virar City","Vijayawada","Visakhapatnam","Vellore","Warangal"]


#Fetching the list of cities in lowercase
t1_t2_cities_list = [x.lower() for x in t1_t2_cities]

# New Class for Validating Cities(to check if they are tier1/tier2 cities)
class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		#print('City in location slot is: ',city)

		# If city not in tier1/tier2 cities then send a message to the user
		if city.lower() in t1_t2_cities_list:
			#print('City.Lower available in t1_t2_cities_list')
			return [SlotSet('location_match', "one")]
		else:
			#print('City.Lower NOT available in t1_t2_cities_list - ',city.lower())
			return [SlotSet('location_match', "zero"),SlotSet('location', None)]

#
class VerifyCuisine(Action):

	def name(self):
		return "action_verify_cuisine"

	def run(self, dispatcher, tracker, domain):
		cuisines = ['chinese','mexican','italian','american','south indian','north indian']
		cuisine = tracker.get_slot('cuisine')
		try:
			cuisine = cuisine.lower()
		except (RuntimeError, TypeError, NameError, AttributeError):
			return [SlotSet('cuisine', None), SlotSet('cuisine_valid', False)]
		if cuisine in cuisines:
			return [SlotSet('cuisine', cuisine), SlotSet('cuisine_valid', True)]
		else:
			return [SlotSet('cuisine', None), SlotSet('cuisine_valid', False)]


#	Class to check if the entered budget is within the given range

class ActionBudgetCheck(Action):
	def name(self):
		return "action_budget_check"

	def run(self, dispatcher, tracker, domain):
		#error_msg = "Sorry!! this is not a valid price range. Please enter again."
		price = tracker.get_slot('price')
		price_dict = {'low': 1, 'medium': 2, 'high': 3}
		budgetmin = 0
		budgetmax = 0
		try:
			pricenum = price_dict.get(price)
			if pricenum == 1:
				budgetmin = 0
				budgetmax = 299
			elif pricenum == 2:
				budgetmin = 300
				budgetmax = 700
			elif pricenum == 3:
				budgetmin = 701
				budgetmax = 100000

		except Exception as e :
			dispatcher.utter_message(e)
			return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 0), SlotSet('withinbudget', False)]

		if price in price_dict:
			return [SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('withinbudget', True)]
		else:
			return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 0), SlotSet('withinbudget', False)]


#Send email to the user if he / she wants the list of 10 restaurants

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		print('Inside action_send_email...')
		from_user = "kthek456@gmail.com"  # Enter sender address
		password = "kavt@123"  # Password
		to_user = tracker.get_slot('email')  # Enter receiver address
		smtp_server = "smtp.gmail.com"
		port = 465  # For SSL

		server = smtplib.SMTP_SSL(smtp_server, port)
		server.login(from_user, password)
		subject = 'Restaurant list from Foodie'
		msg = MIMEMultipart()
		msg['From'] = from_user
		#print('from_user', from_user)
		msg['To'] = to_user
		msg['Subject'] = subject
		#print('to_user', to_user)
		body = tracker.get_slot('emailbody')
		msg.attach(MIMEText(body, 'plain'))

		# message = "The details of all the restaurants you enquried \n \n"
		try:
			server.sendmail(from_user, to_user, msg.as_string())
			server.close()
		except:
			dispatcher.utter_message('Sorry,There is some issue with sending email')
		return [SlotSet('email', None), SlotSet('emailbody', None)]
## interactive_story_happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Taaza Thindi in 1004, 26th Main, 4th T Block, Beside HDFC Bank, Jayanagar, Bangalore - Rated 4.9. And the average price for two people here is: 100\n2. Brahmin's Coffee Bar in Ranga Rao Road, Near Shankar Mutt, Shankarapura, Near Basavanagudi, Bangalore - Rated 4.7. And the average price for two people here is: 100\n3. CTR in 7th Cross, Margosa Road, Malleshwaram, Bangalore - Rated 4.6. And the average price for two people here is: 150\n4. Taaza Thindi in 115, 100 Feet Ring Road, Kathriguppe, Banashankari, Bangalore - Rated 4.6. And the average price for two people here is: 100\n5. Arogya Ahaara in 13, AB Square,14th Main, Sector 5, HSR, Bangalore - Rated 4.6. And the average price for two people here is: 100\n6. Bengaluru Cafe in 6, 9th Cross, 9th Main, 2nd Block, Jayanagar, Bangalore - Rated 4.5. And the average price for two people here is: 150\n7. Malleshwaram Dosa Corner in 251, 17th Cross Road, Malleshwaram West, Malleshwaram, Bangalore - Rated 4.5. And the average price for two people here is: 150\n8. Chikkanna Tiffin Room in 32/1, 30th Cross, Cubbonpet Main Road, Chickpet, City Market, Bangalore - Rated 4.5. And the average price for two people here is: 200\n9. Namma SLN in Gandhi Bazaar, Basavanagudi, Bangalore - Rated 4.5. And the average price for two people here is: 100\n10. Namaste in 69, 7th Main Road, 2nd Stage, BTM, Bangalore - Rated 4.5. And the average price for two people here is: 100\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

    
## interactive_story_nothing_specified1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Kesar Da Dhabha in Near Telephone Exchange, Chowk Passian, Shastri Market, Near Town Hall, Amritsar - Rated 4.6. And the average price for two people here is: 500\n2. Charming Chicken in Shop 3, Opposite Nari Nikaten, Majithia Road, Near, Basant Nagar, Amritsar - Rated 4.6. And the average price for two people here is: 600\n3. Beera Chicken House in Opposite Bandari Hospital, Sehaj Avenue, Majitha Road, Near, Basant Nagar, Amritsar - Rated 4.4. And the average price for two people here is: 500\n4. Mintu Chicken Corner in Ghee Mandi, Bhushan Pura, Town Hall, Amritsar - Rated 4.3. And the average price for two people here is: 350\n5. Marwari Dhaba in 1327/2, Chowk Katra Ahluwalia, Near Jallianwala Bagh, Town Hall, Amritsar - Rated 4.1. And the average price for two people here is: 500\n6. Kale Da Dhaba in Shop 1, Kacheri Chowk, Ranjit Avenue, Amritsar - Rated 4.1. And the average price for two people here is: 500\n7. Krishna Madhur Mishthan Bhandar & Vaishno Dhaba in Near Navjot School, Batala Road, Basant Nagar, Amritsar - Rated 4.0. And the average price for two people here is: 300\n8. UBQ by Barbeque Nation in Plot 77, SGK Tower, Near Income Tax Office, Mall Road, Amritsar - Rated 4.0. And the average price for two people here is: 400\n9. Muskaan in SCO 107, Mezzanine Floor, Ranjit Avenue, Amritsar - Rated 4.0. And the average price for two people here is: 500\n10. Bukhaaraa in SCF 21, C Block Market, Ranjit Avenue, Amritsar - Rated 4.0. And the average price for two people here is: 500\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent
    

## interactive_story_conv1_nothing_specified2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Milano Ice Cream in 460, 2nd Cross, Krishna Temple Road, Indiranagar, Bangalore - Rated 4.7. And the average price for two people here is: 400\n2. Meghana Foods in 52, 1st Floor, 33rd Cross, 4th Block, Jayanagar, Bangalore - Rated 4.5. And the average price for two people here is: 600\n3. eat.fit in 69/A Ground Floor, West of Chord Road Layout, 2nd Stage, Rajajinagar, Bangalore - Rated 4.5. And the average price for two people here is: 400\n4. Mumbai Tiffin in 2345, 17th Cross, Opposite Water Tank, Sector 1, HSR, Bangalore - Rated 4.4. And the average price for two people here is: 400\n5. eat.fit in 1st Floor, BRS Towers, Kaikondrahalli, Sarjapur Road, Bangalore - Rated 4.4. And the average price for two people here is: 400\n6. Meghana Foods in 124, KHB Colony, 1st Cross, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore - Rated 4.4. And the average price for two people here is: 600\n7. Glen's Bakehouse in 24/1, Lavelle Road, Bangalore - Rated 4.3. And the average price for two people here is: 600\n8. Seven Ate Nine in 436, 17 Cross Road, Sector 4, HSR, Bangalore - Rated 4.3. And the average price for two people here is: 700\n9. Leon Grill in 2117/25, 4th Cross, 2nd Stage, HRBR Layout, Kalyan Nagar, Bangalore - Rated 4.3. And the average price for two people here is: 650\n10. Aligarh House in 34/154 & 155, 1st Floor, 11th Cross Somasundrapalya, Sector 2, HSR, Bangalore - Rated 4.3. And the average price for two people here is: 400\n"}
    - utter_ask_for_email_to_send
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

## interactive_story_Location_specified
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Eating Circles in 6, CP Ramaswamy Road, Alwarpet, Chennai - Rated 4.6. And the average price for two people here is: 250\n2. Millet Maagic Meal in 16/23, TTK Road, 1st Cross Street, Alwarpet, Chennai - Rated 4.5. And the average price for two people here is: 200\n3. Rayar's Mess in 31, Arundale Street, Mylapore, Chennai - Rated 4.5. And the average price for two people here is: 100\n4. Andhikkadai in 20, Dhandeeswaram Main Road, Velachery, Chennai - Rated 4.4. And the average price for two people here is: 200\n5. Udipi Shankar Bhavan in 682/568, Poonamalle High Road, Aminjikarai, Chennai - Rated 4.3. And the average price for two people here is: 200\n6. Hotel Krishna Prasad in 76, NSC Bose Road, Sowcarpet, Chennai - Rated 4.2. And the average price for two people here is: 200\n7. Idlies in 17, 18th Avenue, Ashok Nagar, Chennai - Rated 4.2. And the average price for two people here is: 250\n8. Hotel Sakthi Tiffin Center in 1, Vellalar Street, Mogappair, Chennai - Rated 4.2. And the average price for two people here is: 150\n9. Kasivinayaga Mess in 58/2, Akbar Saheb Street, Triplicane, Chennai - Rated 4.1. And the average price for two people here is: 200\n10. Millet Maagic in Super Market 31/2, 4th Main Road, Block U, Anna Nagar East, Chennai - Rated 4.0. And the average price for two people here is: 200\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

## interactive_story_no_restaurants_found
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Thiruvananthapuram"}
    - slot{"location": "Thiruvananthapuram"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - utter_no_restuarants_found

## interactive_story_Conv2_locationnotinoperation
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location_match": "zero"}
    - slot{"location": null}
    - utter_location_notinoperation
* restaurant_search{"location": "Purulia Prayagraj"}
    - slot{"location": "Purulia Prayagraj"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "Purulia Prayagraj"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Higgins IX C1 in 9C/1, Mahewa Uparhar, Allahabad - Rated 4.2. And the average price for two people here is: 600\n2. 9280 The Family Restaurant in 10/14, Elgin Road, Civil Lines, Allahabad, Uttar Pradesh, India - Rated 4.1. And the average price for two people here is: 600\n3. Hyderabadi Biryani in 138/30/1A, M.G. Marg, Civil Lines, Allahabad - Rated 4.1. And the average price for two people here is: 300\n4. Nazeer Foods in 17C/0-1, Elgin Road, Civil Lines, Allahabad - Rated 4.0. And the average price for two people here is: 600\n5. Maharani Zaika in 257A/12, M.G. Marg, Near Medical Chauraha, Georgetown, Allahabad - Rated 4.0. And the average price for two people here is: 500\n6. Aharam in 23/47/121 T, bajrang nagar, allahpur, allahabad, Allapur, Allahabad - Rated 4.0. And the average price for two people here is: 300\n7. UBQ by Barbeque Nation in 5th Floor, P Square Mall, Mahatma Gandhi Marg, Civil Lines, Allahabad - Rated 4.0. And the average price for two people here is: 400\n8. Wasabi Restaurant in Khan Chauraha, Near Awami Hospital, Mahewa, Naini, Allahabad - Rated 3.9. And the average price for two people here is: 300\n9. Samira Restaurant in Katju Road, Allahabad - Rated 3.9. And the average price for two people here is: 600\n10. Aroma The NonVeg Factory in Plot 37/5, LBS Marg, Civil Lines, Allahabad - Rated 3.9. And the average price for two people here is: 550\n"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent

## interactive_story_conv3_nothingspecified
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. The Chicken House in 29/1, Hare Krishna Kunal Road, Entally, Kolkata - Rated 4.0. And the average price for two people here is: 250\n2. Goofys Chicken Shack in 156, GT Road, Near Little Start High School, Bally, Howrah - Rated 3.5. And the average price for two people here is: 200\n3. Burger Bites in 35/1, AJC Bose Road, Near Mercy Hospital, Park Street Area, Kolkata - Rated 3.5. And the average price for two people here is: 200\n4. Burger Bites in NP-390, Nayapatti Main Road, Sector 5, Salt Lake, Kolkata - Rated 3.4. And the average price for two people here is: 200\n5. Crossroad in 2/31/A, Samajgarh Park, Tollygunge, Kolkata - Rated 3.3. And the average price for two people here is: 250\n6. Kolkata Fried Chicken in 50/17, K.B.Sarani, Mall Road, Arjunpur, Dum Dum, Kolkata - Rated 3.2. And the average price for two people here is: 200\n7. BFC in 1008, MB Road, Birati, Dum Dum, Kolkata - Rated 3.0. And the average price for two people here is: 250\n8. Kolkata Fried Chicken in 68, Jessore Road, Near Nagerbazar Flyover, Nagerbazar, Kolkata - Rated 2.5. And the average price for two people here is: 250\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

## interactive_story_conv5_noemailsent
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_budget_check
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 100000}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Falcon Cafe Lounge in Site 5, Sector 16, Panchkula - Rated 4.9. And the average price for two people here is: 1100\n2. The Great Bear in SCO 32, Madhya Marg, Sector 26, Chandigarh - Rated 4.7. And the average price for two people here is: 1600\n3. Qizo in SCO 43, Sector 26, Chandigarh - Rated 4.6. And the average price for two people here is: 1600\n4. Hops n Grains in SCO 358, Sector 9, Panchkula - Rated 4.6. And the average price for two people here is: 2100\n5. Barbeque Nation in SCO 39, Madhya Marg, Sector 26, Chandigarh - Rated 4.6. And the average price for two people here is: 1300\n6. Beach N Brew in SCO 61, Sector 26, Chandigarh - Rated 4.4. And the average price for two people here is: 1800\n7. The Brew Estate in SCO 25, Madhya Marg, Sector 26, Chandigarh - Rated 4.4. And the average price for two people here is: 2000\n8. OvenFresh in SCO 43, Sector 7C, Sector 7, Chandigarh - Rated 4.4. And the average price for two people here is: 850\n9. CAFÈ JC's in Shop 2 & 3, Coal Depot Complex, Sector 10 D, Near Sector 10, Chandigarh - Rated 4.3. And the average price for two people here is: 1200\n10. Pyramid in Elante Mall, 310, 3rd Floor, Phase 1, Chandigarh Industrial Area, Chandigarh - Rated 4.3. And the average price for two people here is: 1500\n"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent

## interactive_story_cuisinespecified
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Peco Peco in Shop 3, Opposite Mukteshwar Ashram Powai, Mumbai. - Rated 4.6. And the average price for two people here is: 700\n2. Peco Peco in Shop 26, Linkway Estate, New Link Road, Near Shakti Motors, Malad West, Mumbai - Rated 4.5. And the average price for two people here is: 700\n3. Dimsum Wū in Shop 4, Geeta Industrial Estate, IB Patel Road, Jay Prakash Nagar, Goregaon East, Mumbai - Rated 4.4. And the average price for two people here is: 650\n4. New Lom Chings in 19, Poonam Darshan, Poonam Nagar, Mahakali, Mumbai - Rated 4.1. And the average price for two people here is: 550\n5. Dimsum Momo Express in 17, Harivijay Co-operative Society, Shivaji Nagar, Kastur Park, Shimpoli, Opposite Telephone Exchange, Borivali West, Mumbai - Rated 4.1. And the average price for two people here is: 500\n6. Wally's Kitchen (China Garden Chinese) in Ground Floor, Opposite Lourdes School, Santoshi Mata Road, Kalyan West, Kalyan, Thane - Rated 4.1. And the average price for two people here is: 500\n7. Silli Chilli in 311, Snehanjali CHS, Near Samarth Aishwarya Building, Adarsh Nagar, Andheri Lokhandwala, Andheri West, Mumbai - Rated 4.1. And the average price for two people here is: 400\n8. Mystery Box in Shop 2 & 3, Pleasant Park, Opposite Movie Time Theatre, Kachpada Signal, Evershine Nagar, Malad West, Mumbai - Rated 4.1. And the average price for two people here is: 550\n9. Made In China in S.V Road, Goregaon West, Mumbai - Rated 4.1. And the average price for two people here is: 600\n10. Pincuk in Shop 6, Sul Building, Sector 20D, Airoli, Navi Mumbai - Rated 4.1. And the average price for two people here is: 700\n"}
    - utter_ask_for_email_to_send
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

## interactive_story_invalidcuisine
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_valid": false}
    - utter_invalid_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. The Wrapsters in Shop 1, Veera Desai Compound, Opposite Lotus Grandeur Building, Veera Desai Area, Mumbai - Rated 4.3. And the average price for two people here is: 400\n2. Bruciato Food Factory in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai - Rated 4.2. And the average price for two people here is: 500\n3. Frisbees in Shop 6, A39, Labaik House, Chimbai Road, Near St. Andrews Church, Hill Road, Bandra West - Rated 4.2. And the average price for two people here is: 600\n4. Diann's in A-8, Gala 1, Thakur House, Ramchandra Lane Extension, Kanchpada, Malad West, Mumbai - Rated 4.2. And the average price for two people here is: 300\n5. Frisbees in 4, Uttam Niwas, Maroshi Road, Near 7 Hills Hospital, Marol, Mumbai - Rated 4.2. And the average price for two people here is: 600\n6. Frisbees in 2, The Street Affaire, Inside City Park, E Block, Bandra Kurla Complex, Mumbai - Rated 4.1. And the average price for two people here is: 600\n7. Foodiator in Shop 3, Plot 14D, Shanti Kunj CHS, Sector 4, Near Seawoods Heritage, Kharghar, Navi Mumbai - Rated 4.1. And the average price for two people here is: 450\n8. Fire Wings in Shop 21, next to Okaz bakery, Okaz Shopping Centre, Millat Nagar, Oshiwara, Andheri West, Mumbai - Rated 4.1. And the average price for two people here is: 700\n9. The Serial Griller in Shop 9, Juhu Ekta CHS, Juhu Versova Link Road, Near Juhu Circle, Near Real Ceramics, Juhu, Mumbai - Rated 4.0. And the average price for two people here is: 500\n10. Hoddogs in Unit 107, 1st Floor, Near Bala Residency, Chandivli, Mumbai - Rated 4.0. And the average price for two people here is: 300\n"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent

## interactive_story_invalidbudget
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "400-800"}
    - slot{"price": "400-800"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 0}
    - slot{"withinbudget": false}
    - utter_invalid_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Greens N Leans in 2 A, Plot 139, Soho Court, Sindhi Society, Chembur, Mumbai - Rated 4.3. And the average price for two people here is: 600\n2. Bohemia the Lounge in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai - Rated 4.3. And the average price for two people here is: 600\n3. Pizzaronee in Shop 13, Emerald Plaza, Block 2, Hiranandani Meadows, Vasant Vihar, Thane West, Thane - Rated 4.3. And the average price for two people here is: 600\n4. Pishu's in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai - Rated 4.3. And the average price for two people here is: 400\n5. Pishu's in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west - Rated 4.3. And the average price for two people here is: 400\n6. 99 Pizzeria in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai - Rated 4.2. And the average price for two people here is: 550\n7. Bruciato Food Factory in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai - Rated 4.2. And the average price for two people here is: 500\n8. 99 Pizzeria in Shop 6, A Wing, Nestle Apartment, Link Road, Opposite Toyota Showroom, Malad West, Mumbai - Rated 4.2. And the average price for two people here is: 450\n9. Piazza Napoli in Shop 4, Sonas Tower, Near St. Paul Church, Parel, Mumbai - Rated 4.2. And the average price for two people here is: 700\n10. 63 By-Lane Pasta Deli in Shop 4, Gate 2, Visamo Building, TPS Road, Opposite Veer Savarkar Udyan, Borivali West, Mumbai - Rated 4.2. And the average price for two people here is: 400\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent

## interactive_story_location_price_specified
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_valid": true}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Eating Circles in 6, CP Ramaswamy Road, Alwarpet, Chennai - Rated 4.6. And the average price for two people here is: 250\n2. Rayar's Mess in 31, Arundale Street, Mylapore, Chennai - Rated 4.5. And the average price for two people here is: 100\n3. Millet Maagic Meal in 16/23, TTK Road, 1st Cross Street, Alwarpet, Chennai - Rated 4.5. And the average price for two people here is: 200\n4. Andhikkadai in 20, Dhandeeswaram Main Road, Velachery, Chennai - Rated 4.4. And the average price for two people here is: 200\n5. Udipi Shankar Bhavan in 682/568, Poonamalle High Road, Aminjikarai, Chennai - Rated 4.3. And the average price for two people here is: 200\n6. Idlies in 17, 18th Avenue, Ashok Nagar, Chennai - Rated 4.2. And the average price for two people here is: 250\n7. Hotel Sakthi Tiffin Center in 1, Vellalar Street, Mogappair, Chennai - Rated 4.2. And the average price for two people here is: 150\n8. Hotel Krishna Prasad in 76, NSC Bose Road, Sowcarpet, Chennai - Rated 4.2. And the average price for two people here is: 200\n9. Kasivinayaga Mess in 58/2, Akbar Saheb Street, Triplicane, Chennai - Rated 4.1. And the average price for two people here is: 200\n10. Jannal Kadai in 55/25, Near Kapaleeshwar Temple, South Mada Street, Mylapore, Chennai - Rated 4.0. And the average price for two people here is: 100\n"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent

## interactive_story_price_cuisine_location_specified
* restaurant_search{"price": "high", "cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid": true}
    - action_budget_check
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 100000}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Yazu - Pan Asian Supper Club in 9, Ground Floor, Raheja Classic Complex, Near Infinity Mall, Phase D, Shastri Nagar, Oshiwara, Andheri West, Mumbai - Rated 4.9. And the average price for two people here is: 2200\n2. Khow Chow in Shop 2, New Kamal CHS, Waterfield Road, Linking Road, Bandra West, Mumbai - Rated 4.6. And the average price for two people here is: 1500\n3. The Fatty Bao in G1, 108, Ground Floor, Morya Classic, Opposite Infinity Mall, Off Link Road, Andheri Lokhandwala, Andheri West, Mumbai - Rated 4.6. And the average price for two people here is: 1900\n4. The Red Turtle - Pan Asian Bistro in Shop 6 & 7, Ganga Niwas, Opposite Toyota Showroom, Link Road, Malad West, Mumbai - Rated 4.4. And the average price for two people here is: 1600\n5. East Asia - The Asian Fanfare in 15, Om Satyam Niwas CHS Limited, Off Shimpoli Road, Borivali West, Mumbai - Rated 4.3. And the average price for two people here is: 1200\n6. Jia The Oriental Kitchen in 2, Dhanraj Mahal, CS Marg, Colaba, Mumbai - Rated 4.3. And the average price for two people here is: 2500\n7. All Stir Fry - Gordon House Hotel in Gordon House Hotel, 5 Battery Street, Behind Regal Cinema, Apollo Bunder, Colaba, Mumbai - Rated 4.2. And the average price for two people here is: 2300\n8. Keiba in Gate 5, Amateurs Riders Club, Racecourse, Mahalaxmi, Mumbai - Rated 4.2. And the average price for two people here is: 2000\n9. Chi Na Chi Ni in Royal Tulip, 26 B, Sector 7, Kharghar, Navi Mumbai - Rated 4.2. And the average price for two people here is: 1200\n10. Mainland China in Ground Floor, Shalimar Morya Park, Opposite Infinity Mall, Off New Link Road, Veera Desai Area, Mumbai - Rated 4.2. And the average price for two people here is: 1800\n"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* emailid_confirm{"email": "kavita.thekkedath@gmail.com"}
    - slot{"email": "kavita.thekkedath@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent


## interactive_story_price_cuisine_no_restaurants
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "low"}
    - slot{"cuisine": "italian"}
    - slot{"price": "low"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid": true}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"restaurant_found": false}
    - slot{"emailbody": null}
    - utter_no_restuarants_found

## interactive_story_cuisine_loc_norestaurants_anotherrequest with cuisine
* restaurant_search{"cuisine": "italian", "location": "kurnool"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kurnool"}
    - action_check_location
    - slot{"location_match": "one"}
    - action_verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_valid": true}
    - utter_ask_budget
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_budget_check
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 299}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - utter_no_restuarants_found
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_valid": true}
    - utter_ask_location
* restaurant_search{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_budget_check
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"withinbudget": true}
    - action_search_restaurants
    - slot{"location": "kurnool"}
    - slot{"restaurant_found": true}
    - slot{"emailbody": "The top rated restaurants you have enquired are:\n1. Hotel International Foodworld(Raj Vihar circle) in Muhammadiya Waqf Complex, Bhagya Nagar, Kurnool - 518004, Opposite Moriya Inn, Kurnool Locality, Kurnool - Rated 4.2. And the average price for two people here is: 550\n2. DVR Restaurant in 40/839, SBI Circle, Kurnool, Kurnool Locality, Kurnool - Rated 4.2. And the average price for two people here is: 500\n3. Madhu Family Restaurant in Shop 51-12-12 F1, New Bus Stand Road, Ballary Road, Opposite Vidyut Bhavan, Kurnool Locality, Kurnool - Rated 4.1. And the average price for two people here is: 350\n4. Hotel Hindustan in Near Old control Room, opp. Exhibition Ground, kurnool., Kurnool Locality, Kurnool - Rated 4.1. And the average price for two people here is: 350\n5. Ruchi Restaurant in Bhagya Nagar, Kurnool Locality, Kurnool - Rated 4.0. And the average price for two people here is: 300\n6. Pushpak Multicuisine Restaurant in 1st Floor, Pv Complex, Gayathri Estate, Budavara Peta, Kurnool Locality, Kurnool - Rated 4.0. And the average price for two people here is: 700\n7. Biryani Hut in 45/142-A-7-2-A, Road no. 4, Venkataramana colony, 518003, Kurnool Locality, Kurnool - Rated 3.9. And the average price for two people here is: 400\n8. Samrat Restaurant in 40/527, 1st Floor, R S Road Main Road, R S Road, Kurnool Locality, Kurnool - Rated 3.9. And the average price for two people here is: 450\n9. Hotel Athidhi (Pitstop44 Drive in) in PitStop 44 drive inn, NH 44, Kurnool Locality, Kurnool - Rated 3.8. And the average price for two people here is: 700\n10. BrewBakes in 50/726-1, Deva Nagar, 518002, Kurnool Locality, Kurnool - Rated 3.8. And the average price for two people here is: 600\n"}
    - utter_ask_for_email_to_send
* emailid_confirm{"email": "srikar777@gmail.com"}
    - slot{"email": "srikar777@gmail.com"}
    - action_send_email
    - slot{"email": null}
    - slot{"emailbody": null}
    - utter_email_sent


from django.shortcuts import render

# •	Page 1: Home – This is the landing page (home page), 
def index(request):
    name_list = ['Jhon Carlo Lomboy', 'Kelly Shanahan', 'Limin Ni', 'Ted Ha']
    student_num_list = [ 'S344917', 'S120899', 's264102', 'S357498' ]
    contact_list = [ 'jhon.lomboy@students.cdu.edu.au', 'kelly.shanahan@students.cdu.edu.au', 'limin.ni@students.cdu.edu.au','giatienha@students.cdu.edu.au', 'contact@stopfoodwaste.com' ]
    Team = 'Team Members'
    name_data = {
        'Team': Team,
        'name_list': name_list,
        'student_num_list': student_num_list,
        'contact_list': contact_list,
    }   
    return render(request, 'food_app/index.html', name_data)
#•	Page 2: List – This page displays a list of all the items required by the Project Brief. 
def list(request):
    return render(request, 'food_app/list.html')

# •	Page 3: Detail – all pages displays all the specific information about each item. 


    # click first 'Learn More' go to Food Waste in Australia General Information page
def info(request):
	intro = 'Food waste is generally defined as “food prepared for human consumption, but for some reason is uneaten and hence wasted.” The Food and Agriculture Organization states, ‘One-third of the global food production is wasted along the food supply train.'
	house = 'Australia is the fourth largest food waster in the world. Much food waste occurs in the home in developed nations. Approximately one-third (34%) of Australia’s food waste is accountable to Australian households. The leading contributors to household waste are inedible food waste and meal leftovers. The subsequent reasons include people not being able to adequately judge whether the food is safe for consumption and food safety in general, as well as not being able to determine if they would eat the food that was stored for later. Several household-level food-handling practices, such as grocery planning, shopping, cooking, managing, and eating (including what happened to leftovers), can play a role in reducing household food waste. These methods include (1) Pre-planning purchases using shopping lists and sticking to them, (2) Preparing meal plans, (3) Checking home storage before shopping, and (4) Higher frequency of cooking to improve the ability to prepare more accurate food portions and store food components. Saving money, saving the planet, and doing the right thing have significantly motivated Australian households to reduce food waste.'
	bussin = 'Food and organic waste are often disposed of in landfills as it is the most cost-effective option in high-income nations. Australian food and organic waste comprise 40% of the municipal solid waste landfill. The food service sector within the hospitality industry can provide challenging circumstances that can make it susceptible to food wastage. The food services sector includes businesses such as cafes, restaurants, and takeaway services. The report suggests that these food services businesses generate higher concentrations of food and organic waste than households. However, there are strong deterrents to the adaption of food and organic waste management practices by food services businesses; economic costs, a lack of political leadership, and a lack or limited availability of resources, infrastructure, and services, as well as adapting such responsible practices and efforts are predominately voluntary.'
	commun = 'Reducing food waste is a significant community initiative that aims to minimize the amount of food that goes to waste and promote sustainable consumption practices. Food waste is a pressing issue that not only results in economic losses but also has environmental and social implications. Community initiatives to reduce food waste include promoting food donation programs, encouraging composting, and educating people on the importance of meal planning and proper food storage. These initiatives help to ensure that surplus food is not wasted but instead redirected to those in need. By reducing food waste, communities can conserve resources, reduce greenhouse gas emissions, and address issues of food insecurity. Overall, reducing food waste is a crucial community initiative that can have a significant impact on the well-being of both the community and the environment.'
	impact  = 'Reducing food waste is a critical community initiative that has numerous positive impacts on the environment, economy, and society. Environmentally, reducing food waste can help to conserve natural resources, lower greenhouse gas emissions, and promote sustainable waste management practices. Economically, reducing food waste can save money for households, businesses, and governments while also creating new opportunities for food recovery and redistribution. Societally, reducing food waste can help to address social challenges such as food insecurity and hunger, by redirecting surplus food to those in need. Additionally, promoting healthier eating habits and reducing food waste can improve the health and well-being of individuals and communities. Overall, reducing food waste is an essential step towards a more sustainable and equitable future for all.'
	tools  = 'As individuals, we can adopt several tools to reduce food waste, including planning our grocery shopping, storing food properly, using up food before it expires, and storing leftovers for future meals.  By planning our shopping and only buying what we need, we can avoid buying excess food that may go to waste.  Properly storing food in the refrigerator or freezer can help extend its shelf life and reduce spoilage.  Additionally, using up ingredients before they expire and making lists can help us make the most of the food we have.  Finally, storing leftovers can help us reduce waste by ensuring that we have meals for later.'
	detail_data = {
		'General Information' : intro,
		'Households' : house,
		'Food Services Industries' : bussin,
		'Community Initatives' : commun,
		'Impacts of food waste' : impact,
		'Tools for improving food waste management' : tools,
	} 

	return render(request, './food_app/info.html', {'detail_data' : detail_data})
 # click second 'Learn More' go to Strategies to Reduce Food Waste page
def strategies(request):
    return render(request, 'food_app/strategies.html')
    # click third 'Learn More' go to Donate to Reduce Food Waste page
def donation(request):
    return render(request, 'food_app/donation.html')
     # click 4th 'Learn More' go to My Food Inventory page

def problem(request):
    food_items = [
        {'name': 'Orange', 'quantity': 15, 'minimum_quantity': 10},
        {'name': 'Strawberry', 'quantity': 2, 'minimum_quantity': 5},
        {'name': 'Pineapple', 'quantity': 2, 'minimum_quantity': 2},
        {'name': 'Bread', 'quantity': 2, 'minimum_quantity': 1},
        {'name': 'Cheese', 'quantity': 4, 'minimum_quantity': 5},
        {'name': 'Yougurt', 'quantity': 5, 'minimum_quantity': 10},
        {'name': 'Eggs', 'quantity': 13, 'minimum_quantity': 12},
        {'name': 'Sausce', 'quantity': 1, 'minimum_quantity': 2},
    ]
    below_min_items = [
        item for item in food_items 
        if item['quantity'] < item['minimum_quantity']]
    return render(request, 'food_app/problem.html', {'food_items': food_items, 'below_min_items': below_min_items})
   

# Define a Python class to implement the data model for the items. 
class Item:
    def __init__(self, id, name, description, goals, img_url):
        self.id = id
        self.name = name
        self.description = description
        self.goals = goals
        self.img_url = img_url
    
    def get_details(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'goals': self.goals,
            'img_url': self.img_url
        }

def create_items():
    items = []

    items.append(Item(
        1,
        'Problem',
        'The food waste problem is a growing issue worldwide, with an estimated 1.3 billion tons of food wasted annually. This leads to environmental and economic costs, as well as social implications for those who go hungry. Reducing food waste is crucial to ensure food security, mitigate environmental impact, and support sustainable development. Innovative solutions are needed to address this problem at every stage of the food supply chain, from production to consumption.The goals of reducing food waste problems are to minimize food waste, prevent the negative environmental impact of food waste, and alleviate food insecurity by redirecting surplus food to people in need. These goals can be achieved through various initiatives, including reducing food waste at the source, optimizing food distribution and logistics, and encouraging individuals and businesses to take action.',
        'Australia wastes 7.3 million tonnes of food, costs $20 billion, government aims to reduce by 50% by 2030.',
        'food_app\list_img\problem1.jpg'
        ))
    items.append(Item(
        2,
        'Strategies',
        'Reducing food waste is a pressing issue that affects both the environment and society. In order to address this problem, it is important to implement strategies that promote smart shopping habits, such as planning meals in advance, creating a shopping list, and buying only what is needed. Proper refrigeration techniques can also help to reduce food spoilage and extend the shelf life of fresh produce. Additionally, utilizing leftovers effectively through meal planning, creative recipes, and food preservation methods can help to minimize food waste. By adopting these practices, individuals and communities can work towards the common goal of reducing food waste and promoting sustainability.',
        'Reduce food waste through smart shopping, proper refrigeration, and utilizing leftovers effectively.',
         'food_app\list_img\stra1.jpg'
        ))
    items.append(Item(
        3,
        'Donation',
        'Reducing food waste is an essential step towards creating a sustainable and equitable food system.  A significant part of this effort is to donate excess food to local food banks and organizations that serve the needy.  The impact of food waste is not just environmental, but also social, with millions of people suffering from food insecurity.  By redirecting food waste to those in need, we can help alleviate hunger while also minimizing the environmental impact of food waste.  Additionally, we can reduce waste by smart shopping, proper storage, and utilizing leftovers effectively, making a significant contribution to building a more sustainable future.',
        'Reduce waste and help fight food insecurity by donating excess food to food banks and local organizations.',
        'food_app\list_img\dana1.jpg'
        ))
    items.append(Item(
        4,
        'Food Tracker',
          '"My Food Inventory" is a valuable tool to help individuals and families reduce food waste and promote sustainable habits. With this app, users can easily track their food reserves, plan meals, and make more informed shopping decisions. By reducing food waste, users can save money and contribute to the overall sustainability of the environment. Additionally, the app encourages users to donate excess food to local organizations, helping to fight food insecurity and support their communities. With its user-friendly interface and customizable features, "My Food Inventory" is an essential tool for anyone looking to adopt a more sustainable lifestyle.',
        '"My Food Inventory" helps you track food reserves, plan meals and shopping, reduce waste, and promote sustainability.',
         'food_app\list_img\inven1.jpg'
        ))
    
    return items

def detail(request, item_id=1):
    items = create_items()

    for item in items:
        if item.id == item_id:
            context = {'item': item.get_details()}
            return render(request, 'food_app/detail.html', context)

    return render(request, 'food_app/404.html')

# •	Page 4: Data Model - This page describes your data model

    
    return render(request, 'food_app/data_model.html',)
def data_model(request):
    plateWaste_data = [
        {
            'Field_Name': 'ID',
            'Purpose': 'A unique identifier for each plate of food',
            'Data_Type': 'Numeric',
            'Validation': 'positive integer',
        },
        {
            'Field_Name': 'Table Number',
            'Purpose': 'The number of the table where the food was served',
            'Data_Type': 'Numeric',
            'Validation': 'positive integer',
        },
        {
            'Field_Name': 'Order Number',
            'Purpose': 'The number of the order where the food was served',
            'Data_Type': 'Numeric',
            'Validation': 'positive integer',
        },
        {
            'Field_Name': 'Plate Weight',
            'Purpose': 'The weight of the uneaten food on the plate',
            'Data_Type': 'Numeric',
            'Validation': 'positive number',
        },
        {
            'Field_Name': 'Plate Cost',
            'Purpose': 'The cost of the uneaten food on the plate',
            'Data_Type': 'Numeric',
            'Validation': 'positive number',
        },
        {
            'Field_Name': 'Plate Food Item',
            'Purpose': 'The food item(s) on the plate',
            'Data_Type': 'Text',
            'Validation': 'non-empty string',
        },
        {
            'Field_Name': 'Reason for Waste',
            'Purpose': 'The reason for the uneaten food on the plate',
            'Data_Type': 'Text',
            'Validation': 'non-empty string',
        },
        {
            'Field_Name': 'Date',
            'Purpose': 'The date when the plate of food was served',
            'Data_Type': 'Date',
            'Validation': 'valid date',
        },
    ]
    return render(request, './food_app/data_model.html', {'detail_data': plateWaste_data})






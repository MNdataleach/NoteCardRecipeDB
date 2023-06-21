#sk-V9iuGhZEyJVOqV38Rd4UT3B
#lbkFJeThJkyjtljcjzj3KRJtA
#wright an article explaining how the technology of avalanche transceivers works but please just print the article only no intro
import requests
from bs4 import BeautifulSoup
import re
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import openai
import markdown
from datetime import datetime
import ssl

openai.api_key = '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'


def chat(dish):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a writer for a simplistic recipe website ."},
        {"role": "user", "content": f"make a {dish} recipe with ingredients for each component in separate tables, and steps in numbered list. Format everything in markdown"}
    ]
    )

    mdr = (completion.choices[0].message)
    print(mdr["content"])
    return mdr["content"]


#chat("banana bread")

#{"role": "system", "content": "You are a writer for a fun, quirky, and informative website."},
#        {"role": "user", "content": "make a Crispy wonton chicken salad reacapie with ingredients for the sause and the salad put ingredeints in tables, and use a numbered list or bullets for the steps.  Format everything in Markdown"}
#   ]

#"role": "system", "content": "You are a writer for a fun, quirky, and informative outdoor blog."},
#       {"role": "user", "content": "make an article explaining how the technology of avalanche transceivers works but please just print the article only no intro. Write a headline, a teaser, a subtitle and a paragraph. Format everything in Markdown"}
#   ]

import requests
from lxml import html

def scrape_info(url):
    # Send a GET request
    response = requests.get(url)

    # Parse the HTML content of the page with lxml
    tree = html.fromstring(response.content)

    # Use XPath to find the second link tag in the head of the HTML
    link2 = tree.xpath('/html/head/link[2]')

    # Extract and print attributes of the link tag
    if link2:
        link2_attrib = link2[0].attrib
        # Open the file in append mode ('a')
        with open('recapies_nytURLscrape1.txt', 'a') as f:
            for key, value in link2_attrib.items():
                print(f"{key}: {value}")
                f.write(f"{key}: {value}\n")
    else:
        print("No second link tag found")
        with open('output.txt', 'a') as f:
            f.write("No second link tag found\n")

# Use the function on a sample webpage

#for i in range(945,9999999):
#    scrape_info(f'https://cooking.nytimes.com/recipes/{i}')

markdown_content = '# Crispy Wonton Chicken Salad Recipe\n\n## Ingredients:\n\n| For the chicken: | Quantity: |\n| --- | --- |\n| Boneless, skinless chicken breasts | 2 |\n| Salt and pepper | To taste |\n| Cornstarch | 1/2 cup |\n| Eggs, beaten | 2 |\n| Panko bread crumbs | 1 cup |\n| Vegetable oil | For frying |\n\n| For the salad: | Quantity: |\n| --- | --- |\n| Mixed greens | 6 cups |\n| Red cabbage, shredded | 1 cup |\n| Carrots, shredded | 1 cup |\n| Cucumber, sliced | 1 cup |\n| Red bell pepper, sliced | 1/2 cup |\n| Scallions, chopped | 1/4 cup |\n| Fresh cilantro, chopped | 1/4 cup |\n| Wonton strips | For topping |\n\n| For the sauce: | Quantity: |\n| --- | --- |\n| Mayonnaise | 1/2 cup |\n| Soy sauce | 1/4 cup |\n| Honey | 2 tbsp |\n| Rice vinegar | 2 tbsp |\n| Sesame oil | 1 tbsp |\n| Sriracha | 1 tsp |\n\n## Instructions:\n\n1. Preheat the oven to 375\u00b0F.\n2. Season the chicken breasts with salt and pepper.\n3. Place the cornstarch, beaten eggs, and panko bread crumbs in three separate bowls.\n4. Coat the chicken with cornstarch, then dip in the beaten eggs and coat with panko bread crumbs.\n5. Heat the vegetable oil in a frying pan over medium-high heat.\n6. Fry the chicken until golden brown, about 2-3 minutes per side. \n7. Place the chicken on a baking sheet and bake in the oven for 10-15 minutes or until cooked through.\n8. In a small bowl, whisk together the mayonnaise, soy sauce, honey, rice vinegar, sesame oil, and Sriracha until well combined to make the sauce.\n9. In a large bowl, toss together the mixed greens, red cabbage, carrots, cucumber, red bell pepper, scallions, and cilantro.\n10. Add the chicken to the salad and drizzle the sauce over the top.\n11. Serve with wonton strips on top for added crunch.\n\nEnjoy your delicious Crispy Wonton Chicken Salad!'

food_list = ['Chicken Parmesan', 'Apple Strudel', 'Apple Tarte Tatin', 'Apricot and Almond Galette', 'Argentinean Chimichurri Sauce', 'Artisan Baguette from Scratch', 'Austrian Linzer Cookies', 'Baba au Rhum', 'Bagna Cauda', 'Baked Alaska', 'Baked Camembert with Garlic and Rosemary', 'Baked Salmon', 'Baked Ziti', 'Baklava Cheesecake', 'Banana Bread', 'Battenberg Cake', 'BBQ Chicken Pizza', 'BBQ Ribs with Homemade BBQ Sauce', 'Beef and Broccoli', 'Beef and Mushroom Pie', 'Beef and Noodle Soup', 'Beef Banh Mi', 'Beef Bao Buns', 'Beef Barbacoa', 'Beef Biryani', 'Beef Bolognese', 'Beef Bourguignon', 'Beef Bulgogi', 'Beef Burritos', 'Beef Cacciatore', 'Beef Caesar Pasta', 'Beef Caprese', 'Beef Carnitas', 'Beef Carpaccio with Truffle Oil', 'Beef Chili', 'Beef Chimichanga', 'Beef Chow Mein', 'Beef Curry', 'Beef Empanadas', 'Beef Enchiladas', 'Beef Fajitas', 'Beef Fettuccine', 'Beef Flautas', 'Beef Goulash', 'Beef Gumbo', 'Beef Gyro', 'Beef Jambalaya', 'Beef Jerky', 'Beef Kabuli Pulao', 'Beef Katsu', 'Beef Kebabs', 'Beef Marsala Pasta', 'Beef Meatloaf', 'Beef Nachos', 'Beef Paillard', 'Beef Pho', 'Beef Pho Soup', 'Beef Pita', 'Beef Pot Pie', 'Beef Potstickers', 'Beef Ramen', 'Beef Rendang', 'Beef Ribs', 'Beef Roulade', 'Beef Satay', 'Beef Sausage Rolls', 'Beef Shawarma', 'Beef Short Ribs with Red Wine Sauce', 'Beef Sliders', 'Beef Souvlaki', 'Beef Stew', 'Beef Stroganoff', 'Beef Stuffed Peppers', 'Beef Tacos', 'Beef Tagine', 'Beef Tamales', 'Beef Tandoori', 'Beef Taquitos', 'Beef Teriyaki Bowl', 'Beef Tournedos with Béarnaise Sauce', 'Beef Tzatziki', 'Beef Wellington', 'Beet Salad', 'Black Bean Soup', 'Blood Orange Sorbet', 'Blueberry Blintzes', 'Boston Cream Pie', 'Bouef Flamande (Flemish Beef Stew)', 'Bouillabaisse', 'Bouillabaisse with Rouille Sauce', 'Braised Venison Shanks', 'Bruschetta', 'Bûche de Noël (Yule Log)', 'Butter Chicken Masala', 'Caesar Salad', 'Cajun Jambalaya', 'Candied Orange Peel', 'Cannoli', 'Caramel Flan', 'Carrot and Cardamom Soup', 'Cassata Siciliana', 'Cassoulet', 'Char Siu (Chinese BBQ Pork)', 'Chateaubriand Steak', 'Cheese Soufflé', 'Cherry Clafoutis', 'Chestnut and Chocolate Roulade', 'Chicken Alfredo', 'Chicken Alfredo Pizza', 'Chicken and Broccoli Stir Fry', 'Chicken and Dumplings', 'Chicken and Rice ...', 'Chicken and Waffles', 'Chicken Ballotine', 'Chicken Banh Mi', 'Chicken Bao Buns', 'Chicken Barbacoa', 'Chicken Beef Stir Fry', 'Chicken Biryani', 'Chicken Bolognese', 'Chicken Bulgogi', 'Chicken Burrito', 'Chicken Cacciatore', 'Chicken Caesar Pasta', 'Chicken Caesar Wrap', 'Chicken Caprese', 'Chicken Carnitas', 'Chicken Chimichanga', 'Chicken Chow Mein', 'Chicken Dumplings', 'Chicken Empanadas', 'Chicken Enchiladas', 'Chicken Fajitas', 'Chicken Fettuccine', 'Chicken Flautas', 'Chicken Fried Rice', 'Chicken Goulash', 'Chicken Gumbo', 'Chicken Gyro', 'Chicken Jambalaya', 'Chicken Kabuli Pulao', 'Chicken Katsu', 'Chicken Kebabs', 'Chicken Korma', 'Chicken Lo Mein', 'Chicken Marsala', 'Chicken Marsala Pasta', 'Chicken Miso Soup', 'Chicken Noodle Soup', 'Chicken Nuggets', 'Chicken Pad Thai', 'Chicken Paillard', 'Chicken Parmesan Sandwich', 'Chicken Pesto Pizza', 'Chicken Pho', 'Chicken Pho Soup', 'Chicken Piccata', 'Chicken Pita', 'Chicken Pot Pie', 'Chicken Potstickers', 'Chicken Quesadilla', 'Chicken Ramen', 'Chicken Rendang', 'Chicken Satay', 'Chicken Sausage Rolls', 'Chicken Scampi', 'Chicken Shawarma', 'Chicken Sliders', 'Chicken Souvlaki', 'Chicken Stuffed Peppers', 'Chicken Tagine', 'Chicken Tamales', 'Chicken Tandoori', 'Chicken Taquitos', 'Chicken Teriyaki', 'Chicken Teriyaki Bowl', 'Chicken Tikka Masala', 'Chicken Tortilla Soup', 'Chicken Tzatziki', 'Chiffon Cake', 'Chilean Pastel de Choclo', 'Chiles Rellenos', 'Chinese Dim Sum', 'Chocolate and Pistachio Biscotti', 'Chocolate Babka', 'Chocolate Chip Cookies', 'Chocolate Lava Cake', 'Chocolate Soufflé', 'Chocolate Truffle', 'Cioppino', 'Clam Chowder', 'Coffee and Cardamom Truffles', 'Confit de Canard', 'Coq Au Riesling', 'Coq au Vin', 'Coquilles Saint Jacques', 'Cornish Game Hen with Port Wine Sauce', 'Cornish Pasty', 'Crème Anglaise', 'Crème Brûlée', 'Creme de Menthe Brownies', 'Crepe Suzette', 'Croatian Peka', 'Croissant', 'Croissant Bread Pudding', 'Croquembouche', 'Cured Duck Prosciutto', 'Cured Salmon Gravlax', 'Danish Kringle', 'Dry Cured Ham', "Duck a l'Orange", 'Duck Confit', 'Duck Prosciutto', 'Egg Fried Rice', 'Eggplant Parmesan', 'Eggs Benedict', 'Escargots de Bourgogne', 'Espresso Martini Cheesecake', 'Eton Mess', 'Fettuccine Alfredo', 'Fettuccine with Truffle Sauce', 'Fish and Chips', 'Fish Tacos', 'Flambé Bananas Foster', 'Focaccia with Caramelized Onion and Balsamic Vinegar', 'Focaccia with Rosemary and Garlic', 'Foie Gras Torchon', 'French Cassoulet', 'French Cassoulet with Duck Confit', 'French Madeleines', 'French Onion Soup', 'French Onion Tart', 'French Toast', 'Fresh Fig and Honey Tart', 'Fresh Fig Tart', 'Fresh Pesto Sauce', 'Fried Chicken', 'Fried Rice', 'Fugu Sashimi (requires professional skills for safety)', 'German Pretzel', 'German Sauerbraten', 'German Stollen', 'Ginger and Lemongrass Chicken Satay', 'Gluten free Brownies', 'Gluten free Pizza', 'Gravlax (Cured Salmon)', 'Greek Salad', 'Grilled Cheese Sandwich', 'Grilled Steak', 'Homemade Bagels', 'Homemade Caramel Sauce', 'Homemade Chocolate Ganache', 'Homemade Dukkah Spice Mix', 'Homemade Fondant for Cake Decorating', 'Homemade Fresh Pasta', 'Homemade Gnocchi', 'Homemade Hoisin Sauce', 'Homemade Ketchup', 'Homemade Kimchi', 'Homemade Marshmallows', 'Homemade Mayonnaise', 'Homemade Pretzel Buns', 'Homemade Ricotta Cheese', 'Homemade Sausage Making', 'Homemade Seitan', 'Homemade Smoked Salmon', 'Homemade Tonkatsu Sauce', 'Honey Glazed Gammon', 'Honeycomb Candy', 'how about 100 more?', '10 georgia pecan turkey salad', '100 obstkuchen fruit tarts', '102 red wine sauce', '103 venison sashimi', '104 game stock', '105 venison tournedos', '106 wild turkey', '107 squabs in grape sauce', '108 grilled quails', '109 nasturtium blossom salad', '11 pecan pancakes', '110 leeks vinaigrette', '112 roslyn wasserstroms turkey marinade', '113 apple walnut stuffing', '114 sweet potato apricot casserole', '116 pumpkin and walnut pie', '117 pastry for a one crust pie', '118 spiced toasted seeds', '119 cheese straws', '12 curried beef skewers', '120 bagna cauda', '121 bang bang turkey', '122 chili cilantro potato cakes', '123 pear and cranberry chutney', '124 vietnamese turkey and cellophane noodle salad', '13 chickpea lamb cakes with red pepper sauce', '14 wild mushroom pie with polenta crust', '146 green beans with ginger and garlic', '147 bread stuffing', '149 braised red radishes', '15 poached fruit with clove granite and cookies', '150 corn bread and squash stuffing', '151 mashed potatoes with corn and chives', '153 stir fried cabbage with cumin seeds', '154 mirliton andouille and shrimp dressing', '155 simple heritage roast turkey', '16 pumpkin creme brulee', '17 pumpkin polenta', '175 grandmother ravers cake', '176 turkey breast with stuffing', '177 corn bread sausage stuffing', '178 corn bread', '179 spanish style cusk', '180 rice and cumin', '181 broiled bananas with lemon and sugar', '182 slow roasted fall vegetables', '183 carrots and turnips with fried sage leaves', '184 brussels sprouts with chestnuts', '185 roast stuffed turkey', '186 pork and sage stuffing', '187 giblet gravy', '188 oyster stew', '189 cauliflower and broccoli au gratin', '19 almond tarts', '190 scalloped tomatoes', '191 candied fruit cheesecake', '192 coconut custard pie', '193 cranberry orange muffins', '194 cranberry soup', '195 roast duck with cranberry glaze', '196 cranberry wild rice stuffing', '197 cranberry nut bars', '198 turkey lasagna', '199 green beans and endive salad', '20 meringue disks', '200 fresh bread stuffing', '201 chestnut cake with chocolate ganache and single malt scotch syrup', '202 milk chocolate ganache', '203 sweet potatoes anna', '204 deep fried turkey', '205 short pastry', '206 two crust pumpkin pie', '208 cider pecan tart', '209 creamed corn', '21 plum tart', '210 roast turkey with maple butter glaze', '211 laura bushs cornbread dressing', '213 pumpkin pie with ginger', '214 green beans with anchovy butter', '215 pie crust', '216 chicken in cider', '217 cider and maple tart', '218 olivier baussans chestnut soup', '219 duck breasts with honey and mustard', '22 pears poached in beaumes de venise and honey', '220 honey focaccia with apple figs and ricotta', '221 commanders palace duck wild mushroom and andouille file gumbo', '222 blanche franciss eggplant casserole', '223 gerri elies pumpkin pone', '224 gloria slaters stuffed veal pocket with oyster dressing', '225 pumpkin parfait', '226 pear gorgonzola and mesclun salad', '227 green beans with lemon', '228 no cook cranberry orange relish', '229 sweet potato home fries', '23 apple chaud froid', '230 sherry reduction gravy', '231 roast turkey with bread stuffing', '232 turkey braised with cranberries', '233 cranberry corn bread', '234 sausage stuffing with caramelized onions', '235 sweet potatoes with maple and chipotles', '236 brussels sprouts with pancetta', '237 creamed red and white pearl onions with bacon', '238 winter squash braised in cider', '239 corn pudding with herb braised chanterelles and spicy greens', '24 plum raspberry upside down cake', '240 roasted parsnips with orange zest', '241 wild rice with mushrooms cranberries and walnuts', '242 braised celery hearts with tomato and olives', '243 jerusalem artichoke pancakes', '244 roasted maple glazed baby carrots with dried grapes', '245 mixed mushroom and sweet potato stuffing', '246 savory bread pudding', '247 sweet bread pudding', '248 braised ligurian chicken', '249 chayote squash', '25 mushroom soup soupe aux champignons', '250 broiled oysters with salsa', '251 sweet potato pie', '252 southern greens', '253 shiitake and lotus seed stuffing', '254 brined roast turkey', '255 leek casserole', '256 marinated brussels sprouts', '257 provencal pumpkin from claudia roden', '258 pumpkin and onion soup', '259 pumpkin southwestern style', '26 meat broth', '260 maple tart with toasted pecans', '261 succotash gratin', '262 wild rice pilaf with cranberries', '263 rabbit in white wine and mustard sauce', '264 paillard of rabbit', '265 rabbit pojarski', '266 deep fried rabbit', '267 fried rabbit buffalo style', '268 blue cheese dressing', '269 karens sausage black olive and walnut stuffing', '27 stuffed mushrooms', '270 meatloaf', '271 blueberry polenta upside down cake', '272 cranberry clafoutis', '273 macerated fruit', '274 curried sweet potato soup with apricots', '275 corn bread chorizo stuffing', '276 thai turkey and makrut lime salad', '277 indian pilaf', '278 dark turkey stock', '279 mark bittmans pumpkin panna cotta', '28 mushroom and meat loaf', '280 cranberry onion jam', '281 cranberry crumble tart', '282 potato torte', '283 whipped potatoes with black beans', '284 potato crepes mere blanc', '285 craig claibornes ambrosia', '286 bourbon milk punch', '287 corn bread dressing', '288 oyster and rice dressing', '289 roast turkey', '29 mushroom and pepper salad', '290 corn bread', '291 pecan tart', '292 yellow lemon cake', '293 coffee shop turkey stuffing', '294 rack of lamb with sage crust', '295 brook trout roasted with sage walnuts and bacon', '296 bruschetta with white bean puree and fried sage leaves', '297 sage biscuits', '298 roasted potatoes', '299 turkey and cranberry meatloaf', '30 veal scaloppine with mushrooms bordelaise', '300 southwestern pork meatloaf', '301 basic meatloaf', '302 cranberry sausage and brioche stuffing', '303 phil ponzeks meat and potato stuffing', '304 oyster bread and spinach stuffing', '305 corn bread wild mushroom and pecan stuffing', '306 ginger pumpkin pie with pumpkin seed crust', '307 pumpkin pie with pepper', '308 applesauce pumpkin pie', '309 three layer pumpkin pie', '31 mushrooms in marsala wine funghi alla marsala', '310 pumpkin pie with rum and cream', '311 diana changs chinese salad', '312 dorothy stones bourbon glazed sweet potatoes', '313 helen hoies braised brussels sprouts', '314 kay roueches spinach gnocchi', '315 cranberry pecan cobbler', '316 pumpkin apple cobbler', '317 cornmeal biscuit dough', '318 roasted stuffed pumpkin', '319 monster cookies', '32 pumpkin cheesecake in nut crust', '320 butternut squash soup', '321 spiced chutney of cranberry and pineapple', '322 apple brown sugar tart', '323 bread and fruit stuffing', '324 cumin mustard carrots', '325 ginger braised brussels sprouts', '326 potato celery root puree', '327 pumpkin pie with fresh ginger and nutmeg', '328 graham cracker pie shell', '329 stewed red cabbage', '33 corn and oyster chowder', '330 roasted winter squash soup', '331 sweet potato casserole', '332 tortilla dressing', '333 pear and jicama salad', '334 cranberry jalapeno relish', '335 roasted garlic noodle cake', '336 praline pumpkin pie', '337 turkey giblet pate', '338 pureed butternut squash', '339 oyster sage dressing', '34 cornmeal biscuits', '340 cranberry mincemeat pie', '341 venison mincemeat', '342 cranberry sauce', '343 butter and shortening pastry dough', '344 cold shrimp with warm cocktail sauce', '345 fennel with olive oil dipping sauce', '347 figs stuffed with goat cheese', '348 real sour cream onion dip', '349 glazed turkey chops', '35 peanut soup', '350 alice waterss cranberry upside down cake', '351 wild mushroom stuffing', '352 stewed fennel', '353 brine cured roast turkey', '354 turkey cranberry pilaf', '355 arugula apple and roquefort salad', '356 roast breast of turkey with cranberry wine sauce', '357 onion bread pudding with corn', '358 maple walnut tart', '359 southwestern cornbread stuffing', '360 mushroom and kasha stuffing', '361 pumpernickel fruit stuffing', '362 pickled fennel', '363 stress free raspberry jam', '364 spiced pumpkin chutney', '365 nutmeg scented onion gratin', '366 carrots provencal', '367 celery root puree', '368 prune and almond tart', '369 golden cream and apple tart', '370 flaky sweet pastry', '371 southern turnip and mustard greens', '372 corn dumplings', '373 turnip casserole', '374 baked tomatoes', '375 roast pheasant stuffed with chestnut bread dressing', '376 sweet potatoes baked with lemon', '377 corn pudding', '378 bourbon pecan pie', '379 apricot mousse', '380 cranberry chutney', '381 squash and parsnip soup', '382 corn and mushroom stuffing', '383 roast turkey and giblet gravy', '384 brussels sprouts in brown butter', '385 gratin of sweet potatoes', '386 cider pecan tart', '387 from beans to apples cranberry beans with tomatoes and herbs', '388 braised leeks with lemons', '389 potato apple puree', '390 cranberry cassis mold', '391 tomato cranberry salsa', '392 cranberry ketchup', '393 turkey stew', '394 potatoes and sausages', '395 portuguese turkey with bread stuffing', '396 turkey stuffing', '397 gravy for turkey', '398 carrot pineapple cake', '399 orange sauce', '400 roast turkey breast with ribs', '401 old fashioned egg and bread dressing', '402 cooked turkey soup', '403 rice and squid', '404 iceberg lettuce with turkey cracklings', '405 braised endive with leeks', '406 braised radicchio with juniper berries', '407 turnip and potato puree', '408 creamed and curried lentil soup', '409 shiitake mushroom bisque with pumpkin', '41 fluffy buttermilk mashed potatoes', '410 smoked trout chowder', '411 kabocha squash pie', '412 ginger butterscotch sauce', '413 turkey with prune walnut and celery stuffing', '414 parsnip and potato puree', '415 brussels sprouts with chestnuts', '416 rice cooked in onions', '417 porcini bread stuffing', '418 rich cornbread dressing', '419 sausage stuffing with summer savory', '42 buttermilk marinated wild turkey with peppery milk gravy', '420 corn bread', '421 golden raisin and caper vinaigrette', '422 currant apple vinaigrette', '423 dessert vinaigrette for figs', '424 chili flavored pumpkin soup', '425 gratin of pumpkin and potatoes', '426 chocolate walnut pumpkin squares', '427 giblet gravy', '428 butternut squash risotto with sage', '429 grilled salmon with sage', '43 sweet potato custard pie in orange crust', '430 fettuccine with sausage and fried sage', '431 brussels sprouts and potato gratin with taleggio', '432 gratin of brussels sprouts with parmesan', '433 yam soup with yogurt', '434 baked yams with red onions', '435 risotto with yams and sage', '436 yam and celery custard', '438 gratin of butternut squash', '439 cranberry kisel', '44 roast turkey breast with ribs', '440 turkey in almond mole', '441 brown rice and pecan stuffing', '442 curried sweet potato puree', '443 kale with garlic and raisins', '444 wheat and cornmeal cheese rolls', '445 whole grain stuffing with kale and dried fruit', '446 rice and nut stuffing', '447 cornbread with corn and cheese', '448 pie crust', '449 honey apple pie with thyme', '45 sausage and apple dressing', '450 pear pomegranate pie', '451 brandied pumpkin and chestnut pie', '452 nutmeg maple cream pie', '453 hashed brussels sprouts with lemon', '454 wilted chard with pickled red onions', '455 fruit and nut stuffing', '456 stuffed acorn squash', '457 oven poached pears with red wine', '458 ricotta cream', '459 monkfish medallions with cranberries', '46 hazelnut cake nussshaumtorte', '460 braised red cabbage with cranberries', '461 cranberry walnut linzer torte', '462 cranberry lime salsa', '463 indian nopales salad', '464 sweet potatoes anna', '465 chinese sausage rice dressing', '466 regina schramblings shaker lemon pie', '467 celery root soup with spiced maple vinegar', '469 apple turnovers', '47 bischofsbrot bishops bread', '470 spiked cranberry relish', '472 spiced sweet potato pudding', '474 seafood lasagna', '475 spinach and artichoke casserole', '476 turkey roulade en cocotte', '477 braised broccoli and rice', '478 green salad with croutons', '48 thanksgiving deviled crab with oysters baked on the half shell', '480 butternut squash and chestnut soup', '481 bourbon roasted pheasant with braised cabbage', '482 roast maine lobster with bourbon and brown butter', '483 corn crusted jumbo sea scallops with bourbon sauce', '484 south coast portuguese fish chowder', '485 acorn squash soup', '486 green chili whipped sweet potatoes', '487 dried corn succotash with fresh vegetables', '488 cranberry squash salsa', '489 red and blue corn sticks', '49 tartar sauce', '490 wild rice risotto with winter squash', '491 gratin of parsley root and parsnips dauphinoise', '492 orange glazed turnips', '493 mashed celeriac and potatoes', '494 tian of pumpkin', '495 armenian pumpkin stew', '496 pan seared duck breast with pumpkin polenta', '497 pumpkin succotash with dried beans tomatoes and spicy shrimp', '498 pumpkin tamale pie', '499 spicy saltfish cakes', '50 hearty duck and wild rice soup', '500 pigeon peas and rice', '501 coconut loaf', '502 sorrel beverage', '503 roast turkey breast', '504 aunt effies custard johnnycake', '505 quails with peppercorns', '506 quails roasted with bacon and foie gras', '507 dried cranberry cherry and tomato relish', '508 warm bread salad', '509 glazed shallots', '51 cooked wild rice', '510 mustard greens salad with roasted cheese pumpkin and goat cheese', '511 jerusalem artichoke and cheese pumpkin soup', '512 roasted jack be little pumpkins with maple panna cotta', '513 fried green tomato crab and ham sandwich', '514 basil sauce', '515 turkey with dressing', '516 apple pecan and raisin pie', '517 turkey soup', '518 turkey and caviar sandwiches', '519 turkey with pasta and broccoli', '52 roast turkey with maple corn sauce', '520 turkey tonnato turkey with tuna sauce', '521 mayonnaise', '522 cranberry ice', '523 james beards pureed parsnips', '524 sauteed kale with garlic and olive oil', '525 roasted vegetables', '526 lasagna with turkey and fresh tomato sauce', '527 mixed green salad', '528 pumpkin soup with ginger croutons', '529 mushroom soup with ginger', '53 long island country samp', '530 cranberry carrot soup with ginger', '531 cranberries and port wine', '532 spiced cranberry orange relish', '533 turkey pilaf in a turban', '534 mexican pizzas', '535 eric riperts turkey two ways', '536 baby stuffed pumpkins', '538 stuffed onions', '539 sweet and sour yams', '54 persimmon and buttermilk pudding', '540 gratin of celery roots and chestnuts', '541 savory baked apples', '542 tamale pie', '543 roast spatchcock turkey', '544 roasted portobello and potato gratin', '545 wild rice and pecan stuffed onions with cranberry orange glaze', '546 spinach and brussels sprouts pie with hazelnut pastry crust', '547 roasted squash with cornbread sage and chestnut stuffing', '548 turducken', '549 galatoires sweet potato cheesecake', '55 oyster stuffing', '550 maple bourbon sweet potato pie', '56 sausage stuffing', '57 fried potatoes greek style', '58 brussels sprouts with garlic and cheese', '59 lemon soy broccoli', '60 cauliflower with cinnamon', '61 gingery pumpkin soup', '62 larrys tarte tatin', '63 smothered chicken', '64 cranberry borscht', '65 rice cream with cranberries', '66 cranberry pecan pie', '67 very rich meat stuffing', '68 potato carrot and celery root stuffing', '682 le delice guy pascal almond meringue cake', '683 marian burross ganache', '684 coffee butter cream', '685 creme chantilly', '686 puffed biscuits', '687 apple onion sage and sour cream dressing', '688 mashed sweet potatoes', '689 leeks baked in cream', '69 corn bread stuffing', '690 swedish turnips', '691 swedish style potatoes au gratin', '692 mashed parsnips', '693 red cabbage with apples', '694 kale and pinkelwurst', '695 suet pudding', '696 hard sauce', '697 turkey piccata', '698 potatoes with zucchini puree', '699 cranberry carrot soup', '70 cranberry walnut crunch', '700 cranberry raisin conserve', '701 cranberry apple crumble pie', '702 squash soup with gingery butternut', '703 striped bass on greens and potatoes', '704 pear almond honey tart', '705 celery root with mushrooms and parmesan', '706 celery root vinaigrette', '707 celery root and potatoes dauphinoise', '708 smoked trout butter', '709 gingered hummus', '71 roast fall vegetables', '710 spaghetti squash with pesto', '711 pasta with parsley sauce', '712 swedish spring chickens', '713 pizzaiuola pesto', '714 chicken thighs with green sauce', '715 fried parsley in bread bouquets', '716 cranberry apple relish', '717 sausage and mushroom stuffing', '718 corn bread and jalapeno stuffing', '719 lettuce wrapped asian turkey salad', '72 roast beets with sage and orange glaze', '720 turkey soup with chinese noodles and ginger', '721 turkey enchiladas with mole sauce', '722 turkey mushroom bread pudding', '723 turkey hash with lemon chili mayonnaise', '724 chestnut and wild rice bisque', '725 butternut squash ratatouille', '726 wild mushroom bread pudding', '727 cranberry trifle with pumpkin chiffon cake', '728 maple pumpkin pie', '729 big apple pie', '73 spinach and acorn squash purees', '730 bourbon pecan pie', '731 golden winter puree', '732 double corn and cheese muffins', '733 warm compote of autumn fruits', '734 butternut squash risotto with sage', '735 fettuccine with sausage and fried sage leaves', '736 southern pecan pie', '737 two crust pumpkin pie', '738 cream of lettuce soup', '739 fricassee of dark meat with brown rice charlie', '74 turkey steaks with prosciutto and mushrooms', '740 scaloppine of white meat with shiitake and cognac sauce', '741 escarole salad with turkey crackling', '742 turkey liver toasts', '743 stuffed and roasted chicken', '744 pease porridge', '745 egg and bacon pie', '746 deerfield inn indian pudding', '747 beets with pine nuts swiss chard and beet greens', '748 celery root and potatoes dauphinoise', '749 cauliflower puree in carrot nest', '75 broccoli rabe with tomatoes', '750 roast young turkey with giblet gravy', '751 country sausage and sage dressing', '752 shell bean succotash', '753 chunky lobster stew with tomalley croutons', '754 pumpkin creme brulee', '755 mushroom white sausage and prosciutto stuffing', '756 celery apple and walnut stuffing', '757 chestnut sausage stuffing', '758 cranberry sauce', '759 cardoon soup with coddled oysters and oyster mushrooms', '76 mussels with saffron sauce', '760 creamy macaroni and cheese', '761 piquant sauce for smoked fish', '762 caramelized baked apples', '763 stuffed artichokes', '764 swiss chard with scallions', '765 spiked cranberry relish', '767 cranberry orange relish', '768 jamaican pumpkin soup', '769 butternut squash soup with sage and parmesan', '77 cornish hens with chinese mushrooms', '770 wild mushroom and cranberry bean soup', '771 biscuit pronounced bees kweet', '772 apple tart', '779 sauteed apple pie', '78 raspberry cream tart', '780 sweet potato puree', '781 pumpkin pots de creme with amaretti ginger crunch', '782 jalapeno corn bread stuffing', '783 jalapeno corn bread', '786 applejack cobbler', '79 pear almond cake', '795 cardoon soup with coddled oysters and oyster mushrooms', '796 natasha and atrinas gingerbread cookies', '797 chicken green olive tajin', '798 tuna steaks with anchovy tomato sauce', '799 veal scallops with chanterelles', '80 wild rice salad with sun dried cherries', '801 anadama bread', '802 cranberry parker house rolls', '803 salami and scallion biscuits', '804 corn and black pepper crackers', '805 braised turkey', '806 cranberry and walnut relish', '808 marinated bay scallops with seaweed', '809 curried bay scallops risotto', '81 cranberry chutney', '810 linguine with bay scallops and pancetta', '811 ginger scallops with rice noodles', '812 scallops with potatoes and white truffle oil', '813 jean andersons scallops algarve style', '814 potato pancakes', '815 carrot potato pancakes', '816 zucchini cheese pancakes', '817 couscous with vegetables and salsa', '818 arugula and vinaigrette', '819 salmon carpaccio with lime and chives', '82 roasted parsnips with fresh thyme', '820 smoked salmon and trout mousse terrine', '821 smoked salmon terrine with spinach', '822 chicken breasts piquant', '823 rice and mushroom ring', '824 lentil soup', '825 croutons with cheese', '826 leek and potato soup', '827 bacon roasted pork with prunes', '828 broccoli rabe salad with roasted garlic vinaigrette', '829 oven dried tomato and bread salad', '83 apple prune and sausage stuffing', '830 stilton rice balls', '831 lobster shepherds pie', '832 rich chocolate cake with creme anglaise', '833 grilled rosemary pork tenderloin', '834 potatoes peppers and onions', '835 pasta with seafood and eggplant', '836 mushroom and avocado salad', '837 duck terrine', '838 venison chili', '839 blackened quail with watercress sauce', '84 sweet potato pecan pie', '840 watercress sauce', '841 sweet potato souffle', '842 warm orzo and black bean salad with smoked turkey', '843 lamb and blue cheese pitas', '844 spinach tangerines and dried cranberries', '845 potato pancakes with pressed caviar and red onion', '846 corn pancakes with creme fraiche and gold and black caviar', '847 cold salmon with caviar and mustard seed sauce', '848 scallops with saffron lobster sauce and caviar', '85 baked stuffed artichokes', '850 shrimp margarita', '851 henri soules poule au pot', '852 four seasons oysters in champagne veloute', '853 bollinger veal with mustard seed', '854 mireille giulianos apple tart', '855 eggplant mushroom lasagna for a crowd', '856 squash soup with goat cheese and chives', '857 roast loin of veal with root vegetables', '858 two potato gratin', '859 frozen maple mousse with sauteed maple apples', '86 beets in orange butter', '860 smoked salmon with mustard vinaigrette and cucumbers', '861 warm salad with crisped spinach and quail', '862 topped with a twist', '863 maida heatters panforte cioccolato', '864 egg pasta', '865 lobster stuffing for ravioli', '866 goat cheese filling for ravioli', '867 tomato sauce', '868 beans and salsa', '87 baked endive', '870 winter vegetable medley', '871 maple mustard salmon with mango', '872 sticky date pudding', '873 baked mackerel in mustard scallion sauce', '874 piccata of mako shark with capers and lemon', '875 steamed mussels with orange', '876 ragu of tuna and thyme', '877 meat patties', '878 chickpea red pepper and celery root soup with cilantro', '879 basic chicken soup', '88 leek mousse', '880 fried chicken and andouille file gumbo', '881 sopa de fideos mexican chicken noodle soup', '882 yunnan steamed chicken soup qiguoji', '883 pickled herring three ways', '884 herring salad', '885 anchovy eye', '886 swedish steak tartare', '887 swedish jellied veal kalvsylta', '888 pickled beets', '889 swedish brown beans', '89 breakfast sausages', '890 swedish meatballs', '891 old mans hash', '892 savory potatoes', '893 herring savory', '894 mock oyster pudding', '895 paris snacks', '896 mazarin cake', '897 breaded oysters with spinach', '898 shrimp and tomato tartlets', '899 lemon vinaigrette', '9 basic reduction sauce', '90 pate de campagne country style pate', '900 tomato compote', '901 poached fillet of beef with winter vegetables', '902 dressing for poached beef', '903 pierre franeys beef broth', '904 fig and orange compote', '905 spinach with pine nuts and raisins', '906 potatoes in red wine with rosemary', '907 white fruitcake', '908 smoked beef tongue with tomato horseradish sauce', '909 red cabbage alsatian style', '91 saucissons a lail french garlic sausages', '910 beef tongue with raisin sauce', '911 chicken dried apricots', '912 roast loin of pork with prunes', '913 james beards compote of dried fruits', '914 veal savarin', '915 festive fish fillets', '916 stuffed peppers', '917 yule log meringue', '918 pistachio ice cream', '919 chocolate ganache', '92 cream of cauliflower raclette', '920 pumpkin cake', '921 roulade', '922 yuletide angel coconut ice cream', '923 croquembouche de noel', '924 mussel and potato salad', '925 mussel and tomato soup', '926 skillet duck', '927 green salad', '93 pamela gurocks gruenkern soup', '94 oat and leek soup', '95 roasted borscht', '96 tomato and quinoa risotto', '97 amana stuffing', '98 amana smoked ham in bread dough', '99 potato dumplings', 'Huevos Rancheros', 'Hungarian Goulash', 'Indonesian Beef Rendang', 'Italian Cassata Cake', 'Italian Panna Cotta', 'Italian Tiramisu', 'Jamaican Jerk Sauce', 'Japanese Dorayaki', 'Japanese Tonkatsu Sauce', 'King Cake', 'Korean BBQ Ribs', 'Korean Bibimbap', 'Korean Doenjang Jjigae', 'Korean Japchae', 'Korean Kimchi', 'Lamb Biryani', 'Lamb Curry', 'Lamb Moussaka', 'Lamb Tagine', 'Lemon and Basil Sorbet', 'Lemon and Lavender Shortbread', 'Lemon Meringue Pie', 'Lentil Soup', 'Lobster Bisque', 'Lobster Ravioli', 'Lobster Roll', 'Lobster Thermidor', 'Macaroni and Cheese', 'Macarons', 'Maltese Rabbit Stew', 'Mango Sticky Rice', 'Maple Bacon Cupcakes', 'Maple Pecan Danish', 'Margherita Pizza', 'Matcha and White Chocolate Cookies', 'Matcha Mochi', 'Matcha Tea Cake', 'Mexican Tamales with Mole Sauce', 'Miso Soup', 'Mole Poblano', 'Moroccan Lamb Tagine', 'Moussaka', 'New York Cheesecake', 'Opera Cake', 'Osso Buco with Gremolata', 'Ossobuco alla Milanese', 'Oysters Rockefeller', 'Pad Thai', 'Paella Valenciana', 'Pancakes', 'Pavlova with Fresh Berries', 'Pear and Almond Tart', 'Peking Duck', 'Peking Duck Pancakes', 'Pesto Pasta', 'Pistachio and Pomegranate Pavlova', 'Pistachio Baklava', 'Pistachio Macarons', 'Polenta with Wild Mushrooms', 'Pork Adobo', 'Pork and Shrimp Shumai', 'Pork Belly Buns', 'Pork Belly with Crackling', 'Pork Dumplings', 'Pork Tacos', 'Portuguese Pastel de Nata', 'Provençal Daube', 'Pulled Pork Sandwich', 'Pumpkin Pie', 'Quail Egg Ravioli', 'Rabbit in Mustard Sauce', 'Rack of Lamb with Herb Crust', 'Ratatouille', 'Red Velvet Cake', 'Red Wine Reduction Sauce', 'Romesco Sauce from Scratch', 'Sacher Torte', 'Salted Caramel Apple Pie', 'Salted Caramel Macarons', 'Sausage Cassoulet', 'Scotch Bonnet Hot Sauce', 'Scottish Shortbread Cookies', 'Seafood Bouillabaisse', 'Seafood Paella', "Shepherd's Pie", 'Shrimp and Grits', 'Shrimp Pad Thai', "Shrimp Po' Boy", 'Shrimp Scampi', 'Singaporean Chili Crab', 'Slow Roasted Pork with Mojo Sauce', 'Smoked Brisket with Homemade BBQ Rub', 'Smoked Salmon Bagel', 'Smoked Trout with Horseradish Cream', 'Soufflé au Chocolat', 'Sourdough Bread', 'Sourdough Pretzels', 'Sourdough Starter from Scratch', 'Spaghetti and Meatballs', 'Spaghetti Bolognese', 'Spaghetti Carbonara', 'Spanish Churros with Chocolate Sauce', 'Spanish Paella', 'Spicy Homemade Harissa Sauce', 'Spinach and Ricotta Cannelloni', 'Sticky Chinese Pork Belly', 'Sticky Toffee Pudding', 'Stuffed Bell Peppers', 'Sure, here are 100 more popular dish titles:', 'Sushi Rolls', 'Swedish Princess Cake', 'Sweet and Sour Pickles', 'Swiss Cheese Fondue', 'Tandoori Masala Spice Mix', 'Tarte Tatin', 'Teppanyaki Style Ginger Sauce', 'Texas BBQ Brisket Rub', 'Texas Style BBQ Sauce', 'Tiramisu', 'Tofu Stir fry', 'Tomato Soup', 'Tournedos Rossini', 'Tres Leches Cake', 'Turducken', 'Turkish Delight', 'Tzatziki Sauce', 'Veal Cordon Bleu', 'Veal Marsala', 'Vegan Banana Bread', 'Vegan Pancakes', 'Vegetable Biryani', 'Vegetable Curry', 'Vegetable Lasagna', 'Vegetable Stir Fry', 'Vegetable Stir Fry', 'Vegetarian Lasagna', 'Veggie Burger', 'Veggie Pizza', 'Veggie Tacos', 'Venison Carpaccio', 'Venison with Blackberry Sauce', 'White Chocolate and Raspberry Roulade', 'Zucchini Bread']


def convert_md(md,dish):

    index = str(food_list.index(dish))
    index2 = index
    hyfdish =  dish.strip()
    link = f"/{hyfdish}  #{index}"

    now = datetime.now()

    dt = now.strftime("%Y-%m-%dT%H:%M:%S%z")

    text = md
    index = text.find("#")  # Find the index of the "#" character

    if index != -1:
        result = text[index:]  # Extract the substring starting from the "#" character
    else:
        result = text  # If "#" is not found, keep the original string
    
    newMD = f"""
---
title: "{dish} Recipe"
date: {dt}
draft: falce
---

{result}
"""



    print(index2)
    return newMD

def run_posts():

    for dish in food_list[238:300]:
        md = chat(dish)
        rcp = convert_md(md,dish)
        hydish = dish.replace(" ", "-")


        # Writing the markdown content to a text document
        with open(f"Cards/posts/{hydish}.md", "w") as file:
    
              file.write(rcp)


run_posts()



#print(markdown_content)


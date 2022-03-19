from flask import Flask

app = Flask(__name__)

html_str = '''

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Fritz Knack" />
    <meta name="description" content="Know your food safety: Food, Acidity, Time, Temperature, Oxygen, Moisture" /><meta name="keywords" content="Food Geek" /><meta name="keywords" content="FAT TOM, ServSafe, HACCP, food safety, biological hazard" /><title>FAT TOM - phrits.com</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <link rel="stylesheet" type="text/css" href="./static/css/phrits.css" />
  </head>
  <body class="bg_frame">

    <div class="container p-1 m-3 bg_frame"> <!-- Everything but the sticky footer. -->
      <div class="container p-1 m-3">
          <h1 class="display-1 bg_frame_title">Your Friend in the Kitchen: FAT TOM</h1>
          <p class="lead">In a restaurant kitchen, or your own, food <i>should</i> be healthful. But it <strong>must</strong> be safe. Food safety includes protection from physical hazards: Think fish pin bones or tiny shards of metal from a can lid, for example. It also includes concern for chemical hazards: Cleaning supplies don&#8217;t belong in the pantry, and we don&#8217;t cook in galvanized&mdash;zinc-plated&mdash;pots and pans. But the concern that gets most of our attention is biological, the things that cause <a href="http://en.wikipedia.org/wiki/Foodborne_illness">foodborne illnesses</a> or &quot;food poisoning&quot;.</p>
          <p class="bg_frame_p">We worry about <span class="phrits_light">viruses</span> such as <a href="http://www.foodborneillness.com/hepatitis_food_poisoning/">Hepatitis A</a> being transmitted from food handlers to eaters, but dangerous bacteria&mdash;pathogens&mdash;are the real bad guys, bringing all sorts of fun games to the party: <a href="http://www.cruisecritic.com/articles.cfm?ID=71">Norovirus</a>, <a href="http://en.wikipedia.org/wiki/Jack_in_the_Box#E._coli_disaster">E. coli</a>, <a href="http://en.wikipedia.org/wiki/Ciguatera">ciguatera</a>, <a href="http://www.about-salmonella.com/">salmonella</a>, and <a href="http://en.wikipedia.org/wiki/Bacillus_cereus"><span class="foreign">bacillus cereus</span></a> are just a few. What can you do? <a href="http://www.ehow.com/how_5137788_wash-hands-food-safety.html">Wash your hands.</a> Avoid <a href="http://www.essortment.com/all/crosscontamina_rubw.htm">cross-contamination</a>. And learn about FAT TOM.<span id="more-929"></span> FAT TOM is a mnemonic to help you remember the critical factors in allowing good food to become dangerous: <strong>F</strong>ood, <strong>A</strong>cidity, <strong>T</strong>emperature, <strong>T</strong>ime, <strong>O</strong>xygen, and <strong>M</strong>oisture.</p>
          <h2 class="display-2 bg_frame_header">Food</h2>
          <p class="bg_frame_p">Restaurant health inspections pay attention, among other things, to how Potentially Hazardous Foods (PHFs) are handled. Generally speaking, PHFs include meat (and fowl, fish, etc.), eggs, a lot of dairy&mdash;notice that these are high-protein foods&mdash;cooked food of all sorts, and many prepared raw foods such as cut fruit.</p>
          <h2 class="display-2 bg_frame_header">Acidity</h2>
          <p class="bg_frame_p">Low acidity foods, that is, foods with a neutral or relatively high <a href="http://en.wikipedia.org/wiki/PH">pH</a> are particularly susceptible to bacteria. High-protein foods are certainly on that list, and so are most cooked foods. Many high-acid foods&mdash;think pickles, <a href="http://www.tabasco.com/main.cfm">Tabasco&reg; Sauce</a>, and sauerkraut or <a href="http://analytical-life.com/blog/recipe-quickle-pickle/">Quickle Pickle</a>&mdash;are largely immune. Mayonnaise-based salads shouldn&#8217;t be left out too long, but because of their relatively high acid content, they&#8217;re <a href="http://www.dressings-sauces.org/Mayonnaise_Dressings.html">not as dangerous</a> as the common wisdom might suggest. And while you&#8217;ll find that many professional recipes use tomatoes for their acid content, beware: Industrial farming practices have reduced the acidity of the average tomato, and cut tomatoes are now considered to be <a href="http://www.fda.gov/Food/FoodSafety/RetailFoodProtection/IndustryandRegulatoryAssistanceandTrainingResources/ucm113843.htm">potentially hazardous</a>.</p>
          <h2 class="display-2 bg_frame_header">Temperature</h2>
          <p class="bg_frame_p">If you keep most foods cold, they will last longer because bacteria grow more slowly or not at all. If you keep them hot enough&mdash;such as on a well-run buffet service&mdash;bacteria die or can&#8217;t grow. PHFs need to be kept below 40&deg;F/4&deg;C or above 140&deg;F/60&deg;C to be safe. The range in between is called the &quot;<a href="http://culinaryarts.about.com/od/safetysanitation/a/dangerzone.htm">temperature danger zone</a>&quot;. For temperatures up to about 120&deg;F/50&deg;C, figure that every 10&deg;F/5&deg;C above 40&deg;F/4&deg;C roughly doubles the reproductive speed of bacteria.</p>
          <p class="bg_frame_p">Incidentally, these temperatures refer to the <a href="http://www.partshelf.com/nsf-certified-products.html">internal temperature</a> of the foods themselves. Storage, cooking, and holding temperatures drive the internal measurement, but it&#8217;s the food the little bugs live in, not the atmosphere around it.</p>
          <h2 class="display-2 bg_frame_header">Time</h2>
          <p class="bg_frame_p">Bacteria are all around us, and it&#8217;s a safe assumption that the food on your table is home to some of them. The bad bugs can&#8217;t hurt us if we keep their population low enough. But the longer you leave a PHF in the temperature danger zone, or the longer you leave it moist or exposed to oxygen, the longer bacteria have to multiply. Food that has been kept in the temperature danger zone for too long has been &quot;time  temperature abused&quot; If a PHF has been so abused&mdash;kept for longer than about 2 hours in the temperature danger zone&mdash;your safest option is to throw it away.</p>
          <h2 class="display-2 bg_frame_header">Oxygen</h2>
          <p class="bg_frame_p">With some exceptions&mdash;<a href="http://en.wikipedia.org/wiki/Clostridium_botulinum">botulism-causing bacteria</a> being perhaps the most familiar&mdash;foodborne pathogens are <a href="http://en.wikipedia.org/wiki/Aerobic_organism">aerobic</a>; i.e., they need oxygen to survive and reproduce. That&#8217;s why covered food lasts longer and why you should squeeze the air out of (or &quot;<a href="http://order.tupperware.com/coe/app/home">burp</a>&quot;) your leftovers&#8217; storage containers. It&#8217;s also why many meats are now shipped and sold in <a href="http://en.wikipedia.org/wiki/Modified_atmosphere">modified atmosphere packaging</a> (MAP), and why <a href="http://www.thespaceshop.com/neopicecream.html">freeze-dried ice cream</a> lasts nearly forever unopened. Oxygen is the culprit when an open bottle of wine starts to taste like vinegar or vegetable oil goes <a href="http://www.cip.ukcentre.com/Rancidity.htm">rancid</a>.</p>
          <h2 class="display-2 bg_frame_header">Moisture</h2>
          <p class="bg_frame_p">Without water, there is no life. Generally speaking, moist foods&mdash;almost everything on your dinner table, for example&mdash;spoil, and dry foods or ingredients (sugar, flour, cornstarch, dried herbs, etc.) do not. Beef jerky is almost entirely protein, but it&#8217;s exceptionally resistant to spoilage because it is dry: The heavy application of salt causes osmosis to draw almost all of the water out of the meat, leaving any pathogens dead or inert. Jams and jellies use sugar for the same effect (<a href="http://www.amazon.com/Food-Cooking-Science-Lore-Kitchen/dp/0684800012/">McGee</a>, &quot;Sugar Preserves&quot;). And dry, aged cheeses such as Parmesan last considerably longer than soft, moist ones such as Brie.</p>
      </div> <!-- class="container" -->
    </div>

    <footer id="board" class="mt-auto py-2">
      <!-- The board image tiles across the bottom. -->
    </footer>
  </body>
</html>

'''

# box-shadow: 14.41px 14.41px 19px #000027, -14.41px -14.41px 19px #00003F;
# box-shadow: 14.41px 14.41px 19px #4D2727, -14.41px -14.41px 19px #7F3F3F;
# background: linear-gradient(145deg, #572B2B, #753B3B);
# background: #663333;
# box-shadow: 14.41px 14.41px 44px #582C2C, -14.41px -14.41px 44px #743A3A;
# box-shadow: 14.41px 14.41px 44px #000055, -14.41px -14.41px 44px #0000FF;


@app.route("/")
def hello_world():
    return html_str

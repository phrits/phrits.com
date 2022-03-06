<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Cream of Anything Soup: Savory (&iquest;Spicy?) Butternut Squash");
    html_meta(array("keywords"      => "Recipe"));
    html_meta(array("keywords"      => "vegetarian, vegan, squash, herbs"));
    html_simple("title", "Savory Butternut Squash Soup - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/recipes/parts/part_savory_butternut_soup.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

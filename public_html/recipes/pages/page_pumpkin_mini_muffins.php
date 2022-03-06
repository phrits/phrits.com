<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Pumpkin mini-muffins recipe");
    html_meta(array("keywords"      => "Recipe"));
    html_meta(array("keywords"      => "vegetarian, dessert, breakfast"));
    html_meta(array("keywords"      => "Fall, Autumn"));
    html_simple("title", "Pumpkin Mini-Muffins - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/recipes/parts/part_pumpkin_mini_muffins.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

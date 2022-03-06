<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Hot mulled cider drink.");
    html_meta(array("keywords"      => "recipe, beverage, Christmas"));
    html_meta(array("keywords"      => "vegetarian, vegan"));
    html_simple("title", "Wassail - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/recipes/parts/part_wassail.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

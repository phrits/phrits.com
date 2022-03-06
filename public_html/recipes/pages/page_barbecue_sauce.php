<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Eastern NC vinegar and red pepper sauce");
    html_meta(array("keywords"      => "Recipe"));
    html_meta(array("keywords"      => "vegetarian, vegan"));
    html_simple("title", "Eastern North Carolina Style Barbecue Sauce - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/recipes/parts/part_eastern_nc_bbq_sauce.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

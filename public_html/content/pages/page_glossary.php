<?php
require("/home/xxxredactedxxx/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Some food terms and their definitions");
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => "cooking, cooking school, glossary, definition, vocabulary"));
    html_meta(array("keywords"      => "mise en place, how to"));
    html_simple("title", "Cooking and Food Terms - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_glossary.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

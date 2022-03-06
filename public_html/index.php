<?php
require("./cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Fritz Knack's Home Page");
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => 'Cook, ServSafe, HACCP'));
    html_meta(array("keywords"      => 'Food, Writing, Blog, Food Science'));
    html_meta(array("keywords"      => 'above board'));
    html_simple("title", "Home - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_splash.php");
    include($www . "/content/parts/part_welcome.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

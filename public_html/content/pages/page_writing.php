<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    description("Food writing, opinion, fiction, etc." );
    html_meta(array("keywords"      => "Food Geek"));
    html_meta(array("keywords"      => "FAT TOM, popcorn, cooking terms"));
    html_simple("title", "Writing - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
/*    include($www . "/content/parts/part_splash.php"); */
    include($www . "/content/parts/part_writing.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>

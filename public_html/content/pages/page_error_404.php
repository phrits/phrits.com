<?php
require("/home/brobip/public_html/cgi-bin/init.php");

doctype();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
<?php
    include($www . "/content/parts/part_head.php");
    html_simple("title", "404 Error: Page Not Found - phrits.com")->output();
?>
    </head>
    <body>

       <div id="above_board"> <!-- Everything but the sticky footer. -->
<?php
    include($www . "/content/parts/part_banner.php");
    include($www . "/content/parts/part_404.php");
    include($www . "/content/parts/part_footer.php");
    include($www . "/content/parts/part_board.php");
?>
    </body>
</html>
